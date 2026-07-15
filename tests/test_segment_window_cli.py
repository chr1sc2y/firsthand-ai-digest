from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

import segment_window


def test_insight_date_uses_window_end_date():
    start, end = segment_window.latest_complete_window(
        datetime(2026, 7, 15, 8, 0, tzinfo=ZoneInfo("Asia/Shanghai")),
        hours=24,
        anchor_hour=6,
    )

    assert start.isoformat() == "2026-07-14T06:00:00+08:00"
    assert end.isoformat() == "2026-07-15T06:00:00+08:00"
    assert end.date().isoformat() == "2026-07-15"
