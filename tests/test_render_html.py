"""Tests for static HTML rendering behavior."""
from __future__ import annotations

import json

import render_html


def test_homepage_redirects_insight_root_to_latest_brief(tmp_path, monkeypatch):
    brief_index = tmp_path / "index.json"
    brief_index.write_text(
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
    monkeypatch.setattr(render_html, "BRIEF_INDEX", brief_index)

    html = render_html.render(x_items=[], blog_items=[], podcast_items=[], video_items=[])

    assert 'hostname === "insight.ai.prov1dence.top"' in html
    assert 'pathname === "/" || pathname === "/index.html"' in html
    assert 'location.replace("/ai-briefs/2026-06-05-ai-brief.html")' in html
    assert (
        'href="https://insight.ai.prov1dence.top/ai-briefs/2026-06-05-ai-brief.html"'
        in html
    )
