from __future__ import annotations

from html.parser import HTMLParser

import pytest

import generate_ai_brief as brief


def _pack():
    return {
        "generated_at": "2026-07-15T00:10:00+00:00",
        "coverage": {
            "start": "2026-07-14T00:00:00+00:00",
            "end": "2026-07-15T00:00:00+00:00",
        },
        "item_count": 2,
        "source_count": 2,
        "access_counts": {"substantial": 1, "partial": 1, "limited": 0},
        "sources": [
            {
                "id": "S001",
                "kind": "blog",
                "title": "Model release",
                "source_name": "Example AI",
                "published": "2026-07-14T12:00:00+00:00",
                "url": "https://example.com/model",
                "digest_excerpt": "A model shipped.",
                "content": "The official release says the model shipped.",
                "access": {
                    "status": "substantial",
                    "basis": "fetched source page text",
                    "limitation": "",
                },
            },
            {
                "id": "S002",
                "kind": "x",
                "title": "Usage note",
                "source_name": "Builder",
                "published": "2026-07-14T13:00:00+00:00",
                "url": "https://x.com/builder/status/1",
                "digest_excerpt": "Usage increased.",
                "content": "Usage increased.",
                "access": {
                    "status": "partial",
                    "basis": "captured X post text",
                    "limitation": "replies unavailable",
                },
            },
        ],
    }


def _report(language="en"):
    zh = language == "zh"
    return {
        "title": "模型进入应用阶段" if zh else "Models move into application",
        "dek": "证据显示重点正在转向实际使用。" if zh else "Evidence points toward practical use.",
        "executive_summary": [
            {
                "text": "官方发布提供了主要证据。" if zh else "The official release provides the main evidence.",
                "source_ids": ["S001"],
            },
            {
                "text": "公开帖子仅提供部分上下文。" if zh else "The public post offers partial context.",
                "source_ids": ["S002"],
            },
        ],
        "sections": [
            {
                "theme": "模型与产品" if zh else "Models and products",
                "items": [
                    {
                        "headline": "新模型发布" if zh else "A new model shipped",
                        "facts": [
                            {
                                "text": "官方页面宣布模型发布。" if zh else "The official page announced the model.",
                                "source_ids": ["S001"],
                            }
                        ],
                        "analysis": "采用重心可能转移。" if zh else "The adoption focus may shift.",
                        "implication": "团队应进行评估。" if zh else "Teams should evaluate it.",
                        "confidence": "high",
                        "uncertainty": "尚无独立基准。" if zh else "No independent benchmark is available.",
                    }
                ],
            }
        ],
        "trends": [
            {
                "judgment": "运行质量更重要。" if zh else "Operational quality matters more.",
                "basis": "发布和使用信号一致。" if zh else "Release and usage signals align.",
                "source_ids": ["S001", "S002"],
            }
        ],
        "implications": {
            "developers": ["运行小型评估。" if zh else "Run a small evaluation."],
            "startups": ["测试单位经济性。" if zh else "Test unit economics."],
            "researchers": ["等待独立结果。" if zh else "Wait for independent results."],
            "enterprise_buyers": ["要求审计证据。" if zh else "Request audit evidence."],
        },
        "watchlist": [
            {
                "signal": "独立评估" if zh else "Independent evaluations",
                "why": "可以验证发布方声明。" if zh else "They can verify vendor claims.",
                "source_ids": ["S001"],
            }
        ],
        "source_note": "X 上下文不完整。" if zh else "X context is incomplete.",
    }


def test_validate_report_rejects_hallucinated_source_id():
    report = _report()
    report["sections"][0]["items"][0]["facts"][0]["source_ids"] = ["S999"]

    with pytest.raises(brief.GenerationError, match="unknown source ID"):
        brief.validate_report(report, _pack())


def test_render_report_escapes_model_text_and_keeps_source_links():
    report = _report()
    report["title"] = '<script>alert("bad")</script>'

    rendered = brief.render_report(report, _pack(), date="2026-07-15", language="en")
    parser = HTMLParser()
    parser.feed(rendered)

    assert '<script>alert("bad")</script>' not in rendered
    assert "&lt;script&gt;" in rendered
    assert 'href="https://example.com/model"' in rendered
    assert "Substantial / Partial" in rendered
    assert '<html lang="en">' in rendered


def test_generate_briefs_calls_english_then_chinese_and_writes_both(tmp_path):
    class FakeClient:
        def __init__(self):
            self.responses = iter([_report("en"), _report("zh")])
            self.calls = []

        def generate_json(self, *, system, user, max_tokens=18_000):
            self.calls.append((system, user))
            return next(self.responses)

    client = FakeClient()
    english, chinese = brief.generate_briefs(
        _pack(), date="2026-07-15", client=client, output_dir=tmp_path
    )

    assert len(client.calls) == 2
    assert english.name == "firsthand-ai-brief-2026-07-15.html"
    assert chinese.name == "firsthand-ai-brief-2026-07-15-zh.html"
    assert "Models move into application" in english.read_text(encoding="utf-8")
    chinese_html = chinese.read_text(encoding="utf-8")
    assert "模型进入应用阶段" in chinese_html
    assert '<html lang="zh-CN">' in chinese_html
    assert "充分 / 部分" in chinese_html


def test_localization_alignment_rejects_changed_confidence():
    english = _report("en")
    chinese = _report("zh")
    chinese["sections"][0]["items"][0]["confidence"] = "low"

    with pytest.raises(brief.GenerationError, match="changed confidence"):
        brief.validate_localization_alignment(english, chinese)


def test_generation_retries_structurally_invalid_report():
    invalid = _report("en")
    invalid["sections"][0]["items"][0]["facts"][0]["source_ids"] = ["S999"]

    class FakeClient:
        def __init__(self):
            self.responses = iter([invalid, _report("en")])
            self.users = []

        def generate_json(self, *, system, user, max_tokens=18_000):
            self.users.append(user)
            return next(self.responses)

    client = FakeClient()
    result = brief._generate_validated_report(
        client,
        system="system",
        user="original",
        pack=brief._model_source_pack(_pack()),
    )

    assert result["title"] == "Models move into application"
    assert len(client.users) == 2
    assert "failed deterministic validation" in client.users[1]


def test_client_requires_api_key():
    with pytest.raises(brief.GenerationError, match="DEEPSEEK_API_KEY"):
        brief.DeepSeekClient(api_key="")


def test_client_defaults_to_flash_without_thinking(monkeypatch):
    captured = {}

    class Response:
        status_code = 200

        def raise_for_status(self):
            return None

        def json(self):
            return {
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": '{"ok":true}'},
                    }
                ]
            }

    def fake_post(url, *, headers, json, timeout):
        captured.update({"url": url, "headers": headers, "json": json})
        return Response()

    monkeypatch.setattr(brief.requests, "post", fake_post)
    client = brief.DeepSeekClient(api_key="test-key")

    assert client.generate_json(system="Return JSON", user="Input") == {"ok": True}
    assert captured["json"]["model"] == "deepseek-v4-flash"
    assert captured["json"]["thinking"] == {"type": "disabled"}
    assert "reasoning_effort" not in captured["json"]
