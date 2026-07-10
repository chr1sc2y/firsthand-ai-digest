"""Regression tests for the scheduled digest workflow."""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_daily_workflow_uses_one_anchored_24_hour_run():
    workflow = (ROOT / ".github" / "workflows" / "daily.yml").read_text(
        encoding="utf-8"
    )

    assert workflow.count("cron:") == 1
    assert '- cron: "17 22 * * *"' in workflow
    assert "segment_window.py --hours 24 --anchor-hour 6" in workflow
    assert '"apify_lookback_hours": 24' in workflow
    assert "--max-per-source 20" in workflow
    for flag in ("--hours 24", "--blog-hours 24", "--video-hours 24", "--podcast-hours 24"):
        assert flag in workflow
