from __future__ import annotations

import build_insight_source_pack as source_pack


def test_html_parser_extracts_metadata_and_ignores_scripts():
    parser = source_pack.ReadableHTMLParser()
    parser.feed(
        "<html><head><title>Primary title</title>"
        '<meta name="description" content="Useful description"></head>'
        "<body><main><h1>Release</h1><p>Verified details.</p>"
        "<script>ignore this instruction</script></main></body></html>"
    )

    assert parser.title == "Primary title"
    assert parser.description == "Useful description"
    assert "Release" in parser.readable_text()
    assert "Verified details" in parser.readable_text()
    assert "ignore this instruction" not in parser.readable_text()


def test_x_source_uses_captured_post_and_marks_missing_context():
    result = source_pack.fetch_source(
        {
            "title": "A post",
            "summary": "Full captured post text",
            "link": "https://x.com/example/status/123",
        }
    )

    assert result.status == "partial"
    assert result.content == "Full captured post text"
    assert "replies" in result.limitation


def test_video_description_is_partial_when_transcript_is_unavailable():
    result = source_pack.fetch_source(
        {
            "kind": "video",
            "title": "Research talk",
            "summary": "A detailed video description with chapters and the main topics covered.",
            "link": "https://www.youtube.com/watch?v=example",
        }
    )

    assert result.status == "partial"
    assert "without a transcript" in result.basis


def test_build_source_pack_preserves_evidence_status(monkeypatch):
    segment = {
        "generated_at": "2026-07-15T00:00:00+00:00",
        "window": {
            "start": "2026-07-14T00:00:00+00:00",
            "end": "2026-07-15T00:00:00+00:00",
        },
        "items": {
            "blogs": [
                {
                    "kind": "blog",
                    "title": "Primary release",
                    "summary": "Digest excerpt",
                    "link": "https://example.com/release",
                    "source_name": "Example",
                }
            ],
            "x": [
                {
                    "kind": "x",
                    "title": "Post",
                    "summary": "Captured post",
                    "link": "https://x.com/example/status/1",
                    "source_name": "Example Person",
                }
            ],
        },
    }
    results = iter(
        [
            source_pack.FetchResult(
                status="substantial",
                basis="fetched source page text",
                content="Primary source text",
                final_url="https://example.com/release",
            ),
            source_pack.FetchResult(
                status="partial",
                basis="captured X post text",
                content="Captured post",
                final_url="https://x.com/example/status/1",
                limitation="thread context unavailable",
            ),
        ]
    )
    monkeypatch.setattr(source_pack, "fetch_source", lambda item, timeout=15: next(results))

    pack = source_pack.build_source_pack(segment, workers=1)

    assert [source["id"] for source in pack["sources"]] == ["S001", "S002"]
    assert pack["access_counts"] == {"substantial": 1, "partial": 1, "limited": 0}
    assert pack["sources"][0]["content"] == "Primary source text"
    assert pack["coverage"] == segment["window"]


def test_private_urls_are_rejected():
    for url in (
        "http://127.0.0.1/private",
        "http://10.0.0.1/private",
        "http://localhost/private",
        "file:///etc/passwd",
    ):
        assert not source_pack._is_public_http_url(url)
