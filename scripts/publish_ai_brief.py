"""Publish generated AI interpretation briefs into the static site."""
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_BRIEF_DIR = ROOT / "data" / "ai-briefs"
DATA_BRIEF_INDEX = DATA_BRIEF_DIR / "index.json"
DIST = ROOT / "dist"
BRIEF_DIR = DIST / "ai-briefs"
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
AI_BRIEFS_START = "<!-- AI_BRIEFS_START -->"
AI_BRIEFS_END = "<!-- AI_BRIEFS_END -->"
AI_BRIEFS_CSS_START = "/* AI_BRIEFS_CSS_START */"
AI_BRIEFS_CSS_END = "/* AI_BRIEFS_CSS_END */"

AI_BRIEFS_CSS = f"""
{AI_BRIEFS_CSS_START}
.ai-briefs {{
  max-width: 1180px; margin: 0 auto;
  padding: 4px 24px 28px;
}}
.ai-briefs h2 {{
  font-size: 13px; font-weight: 600;
  color: var(--ink-2);
  margin-bottom: 11px;
}}
.ai-brief-list {{
  display: flex; flex-wrap: wrap; gap: 8px;
}}
.ai-brief-link {{
  display: inline-flex; align-items: center;
  min-height: 34px; padding: 7px 13px;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: var(--surface-2);
  color: var(--accent);
  font-size: 13px; font-weight: 600;
  backdrop-filter: blur(18px);
  box-shadow: var(--shadow);
}}
.ai-brief-link:hover {{ text-decoration: underline; text-underline-offset: 3px; }}
@media (max-width: 640px) {{
  .ai-briefs {{ padding: 6px 20px 22px; }}
}}
{AI_BRIEFS_CSS_END}
""".strip()


def _brief_date(path: Path, explicit_date: str | None) -> str:
    if explicit_date:
        datetime.strptime(explicit_date, "%Y-%m-%d")
        return explicit_date
    match = DATE_RE.search(path.name)
    if not match:
        raise ValueError(
            f"Could not infer YYYY-MM-DD from {path.name}; pass --date YYYY-MM-DD."
        )
    return match.group(1)


def _load_index() -> dict:
    if not DATA_BRIEF_INDEX.exists():
        return {"schema_version": 1, "briefs": []}
    try:
        payload = json.loads(DATA_BRIEF_INDEX.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {DATA_BRIEF_INDEX}") from exc
    payload.setdefault("schema_version", 1)
    payload.setdefault("briefs", [])
    return payload


def _write_index(payload: dict) -> None:
    DATA_BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    payload["updated_at"] = datetime.now(timezone.utc).isoformat()
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    DATA_BRIEF_INDEX.write_text(text, encoding="utf-8")
    BRIEF_INDEX = BRIEF_DIR / "index.json"
    BRIEF_INDEX.write_text(text, encoding="utf-8")


def _section_html(payload: dict, limit: int = 14) -> str:
    rows = []
    for brief in payload.get("briefs", [])[:limit]:
        date = str(brief.get("date", "")).strip()
        path = str(brief.get("path", "")).strip()
        if not date or not path:
            continue
        rows.append(
            f'<a class="ai-brief-link" href="{path}">{date} AI 解读</a>'
        )
    if not rows:
        return ""
    return (
        f"{AI_BRIEFS_START}\n"
        '<section class="ai-briefs" aria-label="Daily AI interpretations">\n'
        "  <h2>AI 解读</h2>\n"
        f'  <div class="ai-brief-list">{"".join(rows)}</div>\n'
        "</section>\n"
        f"{AI_BRIEFS_END}"
    )


def _replace_between(text: str, start: str, end: str, replacement: str) -> str | None:
    start_index = text.find(start)
    end_index = text.find(end)
    if start_index == -1 or end_index == -1 or end_index < start_index:
        return None
    end_index += len(end)
    return text[:start_index] + replacement + text[end_index:]


def _refresh_homepage(payload: dict) -> None:
    homepage = DIST / "index.html"
    if not homepage.exists():
        return
    text = homepage.read_text(encoding="utf-8")

    css_replacement = AI_BRIEFS_CSS
    css_updated = _replace_between(
        text,
        AI_BRIEFS_CSS_START,
        AI_BRIEFS_CSS_END,
        css_replacement,
    )
    if css_updated is None:
        text = text.replace("</style>", f"{AI_BRIEFS_CSS}\n</style>", 1)
    else:
        text = css_updated

    section = _section_html(payload)
    section_updated = _replace_between(text, AI_BRIEFS_START, AI_BRIEFS_END, section)
    if section_updated is None:
        text = text.replace('<div class="page">', f"{section}\n<div class=\"page\">", 1)
    else:
        text = section_updated
    homepage.write_text(text, encoding="utf-8")


def _upsert_brief(payload: dict, *, date: str, path: str, title: str) -> None:
    briefs = [b for b in payload.get("briefs", []) if b.get("date") != date]
    briefs.append({"date": date, "title": title, "path": path})
    payload["briefs"] = sorted(briefs, key=lambda b: b["date"], reverse=True)


def publish(source: Path, *, date: str | None = None, refresh_homepage: bool = True) -> Path:
    source = source.expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(source)
    if source.suffix.lower() != ".html":
        raise ValueError(f"Expected an HTML file, got {source}")

    brief_date = _brief_date(source, date)
    DATA_BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    data_target = DATA_BRIEF_DIR / f"{brief_date}-ai-brief.html"
    target = BRIEF_DIR / data_target.name
    shutil.copy2(source, data_target)
    shutil.copy2(data_target, target)

    payload = _load_index()
    _upsert_brief(
        payload,
        date=brief_date,
        title=f"{brief_date} AI 解读",
        path=f"ai-briefs/{target.name}",
    )
    _write_index(payload)

    if refresh_homepage:
        _refresh_homepage(payload)
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Copy a generated AI brief into dist/ and refresh homepage links."
    )
    parser.add_argument("html", type=Path, help="Generated firsthand-ai-brief-YYYY-MM-DD.html")
    parser.add_argument("--date", help="Override date as YYYY-MM-DD")
    parser.add_argument(
        "--no-homepage",
        action="store_true",
        help="Update the brief index without touching dist/index.html.",
    )
    args = parser.parse_args(argv)

    target = publish(args.html, date=args.date, refresh_homepage=not args.no_homepage)
    print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
