"""Tests for publishing interpreted AI brief pages."""
from __future__ import annotations

import publish_ai_brief


def test_publish_injects_language_switch_when_chinese_companion_exists(tmp_path, monkeypatch):
    root = tmp_path
    data_briefs = root / "data" / "ai-briefs"
    dist_briefs = root / "dist" / "ai-briefs"
    data_briefs.mkdir(parents=True)
    dist_briefs.mkdir(parents=True)
    (root / "dist").mkdir(exist_ok=True)

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)
    monkeypatch.setattr(publish_ai_brief, "DATA_BRIEF_DIR", data_briefs)
    monkeypatch.setattr(publish_ai_brief, "DATA_BRIEF_INDEX", data_briefs / "index.json")
    monkeypatch.setattr(publish_ai_brief, "DIST", root / "dist")
    monkeypatch.setattr(publish_ai_brief, "BRIEF_DIR", dist_briefs)

    english_source = root / "firsthand-ai-brief-2026-06-08.html"
    english_source.write_text(
        "<!doctype html><html lang=\"en\"><head><style>body{color:#111}</style></head>"
        "<body><main><h1>English</h1></main></body></html>",
        encoding="utf-8",
    )
    (data_briefs / "2026-06-08-ai-brief-zh.html").write_text(
        "<!doctype html><html lang=\"zh-CN\"><head><style>body{color:#111}</style></head>"
        "<body><main><h1>中文</h1></main></body></html>",
        encoding="utf-8",
    )

    publish_ai_brief.publish(english_source, refresh_homepage=False)

    english = (data_briefs / "2026-06-08-ai-brief.html").read_text(encoding="utf-8")
    chinese = (data_briefs / "2026-06-08-ai-brief-zh.html").read_text(encoding="utf-8")
    dist_english = (dist_briefs / "2026-06-08-ai-brief.html").read_text(encoding="utf-8")
    dist_chinese = (dist_briefs / "2026-06-08-ai-brief-zh.html").read_text(encoding="utf-8")

    assert 'class="lang-switch"' in english
    assert 'href="2026-06-08-ai-brief-zh.html">中文</a>' in english
    assert 'href="2026-06-08-ai-brief.html">EN</a>' in chinese
    assert 'class="active" href="2026-06-08-ai-brief.html">EN</a>' in english
    assert 'class="active" href="2026-06-08-ai-brief-zh.html">中文</a>' in chinese
    assert ".lang-switch" in english
    assert english == dist_english
    assert chinese == dist_chinese
