"""Tests for static HTML rendering behavior."""
from __future__ import annotations

import json

import render_html


def test_homepage_links_insight_callout_to_root_without_redirect(tmp_path, monkeypatch):
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

    assert 'hostname === "insight.ai.prov1dence.top"' not in html
    assert "location.replace(" not in html
    assert 'href="https://insight.ai.prov1dence.top/"' in html
    assert "https://insight.ai.prov1dence.top/archive/" not in html
    assert "https://insight.ai.prov1dence.top/ai-briefs/" not in html


def test_insight_link_is_independent_from_hero_title(tmp_path, monkeypatch):
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

    hero_title = html.split("<h1>", 1)[1].split("</h1>", 1)[0]
    assert "insight-link" not in hero_title
    assert '<aside class="sidebar">' in html
    assert '<section class="insight-callout" aria-label="Latest AI insight">' in html
    assert 'class="insight-link"' in html
