"""Build an evidence-oriented source pack from a normalized digest segment."""
from __future__ import annotations

import argparse
import concurrent.futures
import ipaddress
import json
import re
import socket
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests


ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "FirsthandAIInsight/1.0 (+https://ai.prov1dence.top/)"
HEAVY_HOSTS = {
    "x.com",
    "twitter.com",
    "www.youtube.com",
    "youtube.com",
    "youtu.be",
    "linkedin.com",
    "www.linkedin.com",
}
MAX_RESPONSE_BYTES = 1_500_000
MAX_CONTENT_CHARS = 12_000
BENCHMARK_PROXY_NETWORKS = (
    ipaddress.ip_network("198.18.0.0/15"),
    ipaddress.ip_network("2001:2::/48"),
)


class ReadableHTMLParser(HTMLParser):
    """Extract useful page text and metadata without third-party HTML parsers."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self._in_title = False
        self._ignored_depth = 0
        self._chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "svg", "noscript"}:
            self._ignored_depth += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            values = {key.lower(): value or "" for key, value in attrs}
            key = values.get("name", "").lower() or values.get("property", "").lower()
            if key in {"description", "og:description", "twitter:description"}:
                self.description = self.description or values.get("content", "")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        if tag in {"script", "style", "svg", "noscript"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if not text or self._ignored_depth:
            return
        if self._in_title:
            self.title = f"{self.title} {text}".strip()
        else:
            self._chunks.append(text)

    def readable_text(self) -> str:
        text = "\n".join(self._chunks)
        text = re.sub(r"(?:\n\s*){3,}", "\n\n", text)
        return text[:MAX_CONTENT_CHARS]


@dataclass(frozen=True)
class FetchResult:
    status: str
    basis: str
    content: str
    fetched_title: str = ""
    description: str = ""
    http_status: int | None = None
    final_url: str = ""
    limitation: str = ""


def _is_public_http_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return False
    hostname = parsed.hostname.lower().rstrip(".")
    if hostname in {"localhost", "localhost.localdomain"} or hostname.endswith(".local"):
        return False
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        return True
    return not (
        address.is_private
        or address.is_loopback
        or address.is_link_local
        or address.is_reserved
        or address.is_multicast
    )


def _resolved_to_public_addresses(url: str) -> bool:
    """Reject obvious private-network targets while allowing DNS failures to fetch normally."""
    hostname = urlparse(url).hostname
    if not hostname:
        return False
    try:
        addresses = {row[4][0] for row in socket.getaddrinfo(hostname, None)}
    except socket.gaierror:
        return True
    for raw in addresses:
        address = ipaddress.ip_address(raw)
        # Some sandboxed/VPN environments proxy public DNS through RFC 2544
        # benchmark ranges. These are non-routable but safe as local egress hops.
        if any(address in network for network in BENCHMARK_PROXY_NETWORKS):
            continue
        if any(
            (
                address.is_private,
                address.is_loopback,
                address.is_link_local,
                address.is_reserved,
                address.is_multicast,
            )
        ):
            return False
    return True


def _request_with_safe_redirects(url: str, *, timeout: float) -> requests.Response:
    session = requests.Session()
    current = url
    for _ in range(6):
        if not _is_public_http_url(current) or not _resolved_to_public_addresses(current):
            raise ValueError("URL resolves to a non-public network address")
        response = session.get(
            current,
            headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"},
            timeout=timeout,
            allow_redirects=False,
            stream=True,
        )
        if response.is_redirect or response.is_permanent_redirect:
            location = response.headers.get("Location")
            response.close()
            if not location:
                return response
            current = urljoin(current, location)
            continue
        return response
    raise requests.TooManyRedirects("more than five redirects")


def _metadata_result(item: dict, limitation: str) -> FetchResult:
    excerpt = str(item.get("summary") or item.get("title") or "").strip()
    kind = str(item.get("kind") or "").lower()
    has_feed_material = kind in {"video", "podcast"} and len(excerpt) >= 40
    return FetchResult(
        status="partial" if has_feed_material else "limited",
        basis=(
            "feed description, chapters, or show notes without a transcript"
            if has_feed_material
            else "digest metadata and captured excerpt"
        ),
        content=excerpt[:MAX_CONTENT_CHARS],
        limitation=limitation,
        final_url=str(item.get("link") or ""),
    )


def fetch_source(item: dict, *, timeout: float = 15.0) -> FetchResult:
    url = str(item.get("link") or "").strip()
    host = (urlparse(url).hostname or "").lower()
    if not _is_public_http_url(url):
        return _metadata_result(item, "missing or unsupported public source URL")
    if host in {"x.com", "twitter.com"}:
        result = _metadata_result(
            item,
            "post text was captured by the digest collector; replies, quoted-post context, and media were not fetched",
        )
        return FetchResult(**{**result.__dict__, "status": "partial", "basis": "captured X post text"})
    if host in HEAVY_HOSTS:
        return _metadata_result(
            item,
            "heavy or anti-bot-prone host; analysis is limited to digest metadata and accessible excerpts",
        )

    try:
        response = _request_with_safe_redirects(url, timeout=timeout)
        status_code = response.status_code
        final_url = response.url or url
        if status_code >= 400:
            response.close()
            result = _metadata_result(item, f"source returned HTTP {status_code}")
            return FetchResult(**{**result.__dict__, "http_status": status_code, "final_url": final_url})
        content_type = response.headers.get("Content-Type", "").lower()
        if "html" not in content_type and "text/" not in content_type:
            response.close()
            result = _metadata_result(item, f"unsupported content type: {content_type or 'unknown'}")
            return FetchResult(**{**result.__dict__, "http_status": status_code, "final_url": final_url})
        chunks: list[bytes] = []
        size = 0
        for chunk in response.iter_content(chunk_size=65_536):
            if not chunk:
                continue
            chunks.append(chunk)
            size += len(chunk)
            if size >= MAX_RESPONSE_BYTES:
                break
        encoding = response.encoding or "utf-8"
        response.close()
        body = b"".join(chunks)[:MAX_RESPONSE_BYTES].decode(encoding, errors="replace")
        parser = ReadableHTMLParser()
        parser.feed(body)
        text = parser.readable_text()
        if len(text) < 200:
            result = _metadata_result(item, "page was reachable but yielded too little readable text")
            return FetchResult(
                **{
                    **result.__dict__,
                    "http_status": status_code,
                    "final_url": final_url,
                    "fetched_title": parser.title,
                    "description": parser.description,
                }
            )
        return FetchResult(
            status="substantial",
            basis="fetched source page text",
            content=text,
            fetched_title=parser.title,
            description=parser.description,
            http_status=status_code,
            final_url=final_url,
        )
    except (requests.RequestException, OSError, ValueError) as exc:
        return _metadata_result(item, f"source fetch failed: {type(exc).__name__}")


def _flatten_items(segment: dict) -> list[dict]:
    items = segment.get("items") or {}
    rows: list[dict] = []
    for kind in ("blogs", "videos", "podcasts", "x"):
        for item in items.get(kind, []):
            row = dict(item)
            row.setdefault("kind", kind.rstrip("s"))
            rows.append(row)
    return rows


def build_source_pack(
    segment: dict,
    *,
    max_sources: int = 120,
    workers: int = 12,
    timeout: float = 15.0,
) -> dict:
    items = _flatten_items(segment)[:max_sources]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        results = list(executor.map(lambda item: fetch_source(item, timeout=timeout), items))

    sources = []
    for index, (item, result) in enumerate(zip(items, results), start=1):
        sources.append(
            {
                "id": f"S{index:03d}",
                "kind": item.get("kind", "unknown"),
                "title": item.get("title") or result.fetched_title or "Untitled source",
                "source_name": item.get("source_name") or item.get("author") or "Unknown source",
                "author": item.get("author") or "",
                "published": item.get("published"),
                "url": item.get("link") or "",
                "digest_excerpt": item.get("summary") or "",
                "access": {
                    "status": result.status,
                    "basis": result.basis,
                    "http_status": result.http_status,
                    "final_url": result.final_url,
                    "limitation": result.limitation,
                },
                "page_title": result.fetched_title,
                "page_description": result.description,
                "content": result.content,
            }
        )

    access_counts = {status: 0 for status in ("substantial", "partial", "limited")}
    for source in sources:
        access_counts[source["access"]["status"]] += 1
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "coverage": segment.get("window") or {},
        "segment_generated_at": segment.get("generated_at"),
        "item_count": len(items),
        "source_count": len(sources),
        "access_counts": access_counts,
        "sources": sources,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--segment", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-sources", type=int, default=120)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args(argv)

    segment = json.loads(args.segment.read_text(encoding="utf-8"))
    pack = build_source_pack(
        segment,
        max_sources=args.max_sources,
        workers=args.workers,
        timeout=args.timeout,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {args.output} with {pack['source_count']} sources: "
        f"{pack['access_counts']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
