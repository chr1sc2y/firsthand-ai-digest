"""Tests for publishing the Insight-only static site."""
from __future__ import annotations

import json

import sync_insight_site


def test_sync_insight_site_writes_pages_artifact(tmp_path):
    source = tmp_path / "data" / "ai-briefs"
    source.mkdir(parents=True)
    (source / "2026-06-05-ai-brief.html").write_text(
        '<!doctype html><html><head><title>Latest</title></head><body>'
        '<nav><a href="2026-06-05-ai-brief-zh.html">中文</a></nav>'
        '<h1>Latest Insight</h1></body></html>',
        encoding="utf-8",
    )
    (source / "2026-06-05-ai-brief-zh.html").write_text(
        '<nav><a href="2026-06-05-ai-brief.html">EN</a></nav>',
        encoding="utf-8",
    )
    (source / "index.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "briefs": [
                    {
                        "date": "2026-06-05",
                        "title": "2026-06-05 AI 解读",
                        "path": "ai-briefs/2026-06-05-ai-brief.html",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    target = tmp_path / "insight"

    result = sync_insight_site.sync(source_dir=source, target_dir=target)

    assert result.latest_path == "ai-briefs/2026-06-05-ai-brief.html"
    assert (target / "CNAME").read_text(encoding="utf-8") == "insight.ai.prov1dence.top\n"
    assert (target / "ai-briefs" / "index.json").exists()
    assert (target / "ai-briefs" / "2026-06-05-ai-brief.html").exists()
    assert (target / "ai-briefs" / "2026-06-05-ai-brief-zh.html").exists()
    index = (target / "index.html").read_text(encoding="utf-8")
    assert "<h1>Latest Insight</h1>" in index
    assert '<base href="/ai-briefs/">' in index
    assert 'location.replace(' not in index
    assert 'http-equiv="refresh"' not in index
    workflow = (target / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
    assert "actions/upload-pages-artifact" in workflow
    assert "actions/deploy-pages" in workflow
