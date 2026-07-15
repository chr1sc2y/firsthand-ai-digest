"""Tests for publishing interpreted AI brief pages."""
from __future__ import annotations

import json

import publish_ai_brief


def _write_staged_brief(root, name: str, html: str):
    target = root / "staging" / "drafts" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    return target


def test_resolve_brief_source_prefers_staging_directory(tmp_path, monkeypatch):
    root = tmp_path
    staging = root / "staging" / "drafts"
    staging.mkdir(parents=True)
    staged = staging / "firsthand-ai-brief-2026-06-08.html"
    staged.write_text("<html></html>", encoding="utf-8")

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)

    resolved = publish_ai_brief.resolve_brief_source(
        publish_ai_brief.Path("firsthand-ai-brief-2026-06-08.html")
    )
    assert resolved == staged.resolve()


def test_publish_injects_language_switch_when_chinese_companion_exists(tmp_path, monkeypatch):
    root = tmp_path
    data_insight = root / "data" / "insight"
    dist_archive = root / "dist" / "archive"
    data_insight.mkdir(parents=True)
    dist_archive.mkdir(parents=True)
    (root / "dist").mkdir(exist_ok=True)

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_DIR", data_insight)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_INDEX", data_insight / "index.json")
    monkeypatch.setattr(publish_ai_brief, "DIST", root / "dist")
    monkeypatch.setattr(publish_ai_brief, "BRIEF_DIR", dist_archive)

    english_source = _write_staged_brief(
        root,
        "firsthand-ai-brief-2026-06-08.html",
        "<!doctype html><html lang=\"en\"><head><style>body{color:#111}</style></head>"
        "<body><main><h1>English</h1></main></body></html>",
    )
    (data_insight / "2026-06-08-ai-brief-zh.html").write_text(
        "<!doctype html><html lang=\"zh-CN\"><head><style>body{color:#111}</style></head>"
        "<body><main><h1>中文</h1></main></body></html>",
        encoding="utf-8",
    )

    publish_ai_brief.publish(english_source, refresh_homepage=False)

    assert not english_source.exists()
    english = (data_insight / "2026-06-08-ai-brief.html").read_text(encoding="utf-8")
    chinese = (data_insight / "2026-06-08-ai-brief-zh.html").read_text(encoding="utf-8")
    dist_english = (dist_archive / "2026-06-08-ai-brief.html").read_text(encoding="utf-8")
    dist_chinese = (dist_archive / "2026-06-08-ai-brief-zh.html").read_text(encoding="utf-8")

    assert 'class="lang-switch"' in english
    assert 'href="2026-06-08-ai-brief-zh.html">中文</a>' in english
    assert 'href="2026-06-08-ai-brief.html">EN</a>' in chinese
    assert 'class="active" href="2026-06-08-ai-brief.html">EN</a>' in english
    assert 'class="active" href="2026-06-08-ai-brief-zh.html">中文</a>' in chinese
    assert ".lang-switch" in english
    assert english == dist_english
    assert chinese == dist_chinese


def test_publish_auto_generates_chinese_companion_when_missing(tmp_path, monkeypatch):
    root = tmp_path
    data_insight = root / "data" / "insight"
    dist_archive = root / "dist" / "archive"
    data_insight.mkdir(parents=True)
    dist_archive.mkdir(parents=True)

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_DIR", data_insight)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_INDEX", data_insight / "index.json")
    monkeypatch.setattr(publish_ai_brief, "DIST", root / "dist")
    monkeypatch.setattr(publish_ai_brief, "BRIEF_DIR", dist_archive)

    english_source = _write_staged_brief(
        root,
        "firsthand-ai-brief-2026-06-14.html",
        '<!doctype html><html lang="en"><head><title>Firsthand AI Insight - June 14, 2026</title>'
        "<style>body{color:#111}</style></head><body><main><h1>"
        "Model access risk becomes the day's operating story"
        "</h1><h2>Executive Summary</h2><p><strong>Fact.</strong> "
        "Firsthand's 24-hour set contained 22 timestamped items."
        "</p><h2>For Developers</h2><ul><li>Add provider fallback paths.</li></ul>"
        "</main></body></html>",
    )

    publish_ai_brief.publish(english_source, refresh_homepage=False)

    english = (data_insight / "2026-06-14-ai-brief.html").read_text(encoding="utf-8")
    chinese = (data_insight / "2026-06-14-ai-brief-zh.html").read_text(encoding="utf-8")
    dist_chinese = (dist_archive / "2026-06-14-ai-brief-zh.html").read_text(encoding="utf-8")

    assert '<html lang="zh-CN">' in chinese
    assert "模型访问风险成为今天最重要的运行议题" in chinese
    assert "<h2>执行摘要</h2>" in chinese
    assert "<h2>给开发者</h2>" in chinese
    assert "事实。" in chinese
    assert "自动本地化改写" in chinese
    assert 'class="active" href="2026-06-14-ai-brief.html">EN</a>' in english
    assert 'href="2026-06-14-ai-brief-zh.html">中文</a>' in english
    assert 'href="2026-06-14-ai-brief.html">EN</a>' in chinese
    assert 'class="active" href="2026-06-14-ai-brief-zh.html">中文</a>' in chinese
    assert chinese == dist_chinese


def test_publish_prefers_staged_chinese_companion_over_fallback(tmp_path, monkeypatch):
    root = tmp_path
    data_insight = root / "data" / "insight"
    dist_archive = root / "dist" / "archive"
    data_insight.mkdir(parents=True)
    dist_archive.mkdir(parents=True)

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_DIR", data_insight)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_INDEX", data_insight / "index.json")
    monkeypatch.setattr(publish_ai_brief, "DIST", root / "dist")
    monkeypatch.setattr(publish_ai_brief, "BRIEF_DIR", dist_archive)

    english_source = _write_staged_brief(
        root,
        "firsthand-ai-brief-2026-07-04.html",
        '<!doctype html><html lang="en"><head><style>body{color:#111}</style></head>'
        "<body><main><h1>English</h1></main></body></html>",
    )
    _write_staged_brief(
        root,
        "firsthand-ai-brief-2026-07-04-zh.html",
        '<!doctype html><html lang="zh-CN"><head><style>body{color:#111}</style></head>'
        "<body><main><h1>人工中文稿</h1></main></body></html>",
    )

    publish_ai_brief.publish(english_source, refresh_homepage=False)

    chinese = (data_insight / "2026-07-04-ai-brief-zh.html").read_text(encoding="utf-8")
    dist_chinese = (dist_archive / "2026-07-04-ai-brief-zh.html").read_text(encoding="utf-8")
    assert "人工中文稿" in chinese
    assert "自动本地化改写" not in chinese
    assert 'class="active" href="2026-07-04-ai-brief-zh.html">中文</a>' in chinese
    assert chinese == dist_chinese


def test_publish_records_public_archive_path(tmp_path, monkeypatch):
    root = tmp_path
    data_insight = root / "data" / "insight"
    dist_archive = root / "dist" / "archive"
    data_insight.mkdir(parents=True)
    dist_archive.mkdir(parents=True)

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_DIR", data_insight)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_INDEX", data_insight / "index.json")
    monkeypatch.setattr(publish_ai_brief, "DIST", root / "dist")
    monkeypatch.setattr(publish_ai_brief, "BRIEF_DIR", dist_archive)

    english_source = _write_staged_brief(
        root,
        "firsthand-ai-brief-2026-06-08.html",
        "<!doctype html><html><head></head><body><h1>English</h1></body></html>",
    )

    publish_ai_brief.publish(english_source, refresh_homepage=False)

    index = json.loads((data_insight / "index.json").read_text(encoding="utf-8"))
    assert index["briefs"][0]["path"] == "archive/2026-06-08-ai-brief.html"
    assert (dist_archive / "2026-06-08-ai-brief.html").exists()


def test_publish_normalizes_existing_brief_paths_to_archive(tmp_path, monkeypatch):
    root = tmp_path
    data_insight = root / "data" / "insight"
    dist_archive = root / "dist" / "archive"
    data_insight.mkdir(parents=True)
    dist_archive.mkdir(parents=True)
    (data_insight / "index.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "briefs": [
                    {
                        "date": "2026-06-07",
                        "title": "2026-06-07 AI 解读",
                        "path": "ai-briefs/2026-06-07-ai-brief.html",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(publish_ai_brief, "ROOT", root)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_DIR", data_insight)
    monkeypatch.setattr(publish_ai_brief, "DATA_INSIGHT_INDEX", data_insight / "index.json")
    monkeypatch.setattr(publish_ai_brief, "DIST", root / "dist")
    monkeypatch.setattr(publish_ai_brief, "BRIEF_DIR", dist_archive)

    english_source = _write_staged_brief(
        root,
        "firsthand-ai-brief-2026-06-08.html",
        "<!doctype html><html><head></head><body><h1>English</h1></body></html>",
    )

    publish_ai_brief.publish(english_source, refresh_homepage=False)

    index = json.loads((data_insight / "index.json").read_text(encoding="utf-8"))
    assert [brief["path"] for brief in index["briefs"]] == [
        "archive/2026-06-08-ai-brief.html",
        "archive/2026-06-07-ai-brief.html",
    ]
