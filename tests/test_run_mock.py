"""Smoke tests for the top-level pipeline using built-in mock data."""
from __future__ import annotations

import json

import run


def test_run_with_mock_data_writes_html(tmp_path):
    output = tmp_path / "index.html"

    status = run.main(["--mock-data", "--output", output.as_posix()])

    html = output.read_text(encoding="utf-8")
    assert status == 0
    assert "Firsthand AI Digest" in html
    assert "Sam Altman" in html
    assert "OpenAI Blog" in html
    assert "Latent Space" in html
    assert "Google DeepMind" in html


def test_run_with_mock_data_copies_root_cname(tmp_path):
    output = tmp_path / "index.html"
    output_cname = tmp_path / "CNAME"
    output_cname.write_text("old.example.com\n", encoding="utf-8")

    status = run.main(["--mock-data", "--output", output.as_posix()])

    assert status == 0
    assert output_cname.read_text(encoding="utf-8") == "ai.prov1dence.top\n"


def test_run_with_mock_data_allows_output_next_to_root_cname(tmp_path, monkeypatch):
    monkeypatch.setattr(run, "ROOT", tmp_path)
    (tmp_path / "CNAME").write_text("ai.prov1dence.top\n", encoding="utf-8")
    output = tmp_path / "preview-index.html"

    status = run.main(["--mock-data", "--output", output.as_posix()])

    assert status == 0
    assert output.exists()
    assert (tmp_path / "CNAME").read_text(encoding="utf-8") == "ai.prov1dence.top\n"


def test_run_with_mock_data_writes_normalized_json(tmp_path):
    output = tmp_path / "index.html"
    data_output = tmp_path / "data" / "2026-05-21.json"

    status = run.main(
        [
            "--mock-data",
            "--output",
            output.as_posix(),
            "--data-output",
            data_output.as_posix(),
        ]
    )

    payload = json.loads(data_output.read_text(encoding="utf-8"))
    assert status == 0
    assert payload["schema_version"] == 1
    assert payload["counts"] == {
        "x": 2,
        "blogs": 2,
        "podcasts": 1,
        "videos": 1,
    }
    assert payload["items"]["x"][0]["source_name"] == "Sam Altman"
    assert payload["items"]["x"][0]["published"].endswith("+00:00")


def test_run_with_mock_data_writes_window_metadata(tmp_path):
    output = tmp_path / "index.html"
    data_output = tmp_path / "segment.json"

    status = run.main(
        [
            "--mock-data",
            "--output",
            output.as_posix(),
            "--data-output",
            data_output.as_posix(),
            "--window-start",
            "2026-05-21T09:00:00Z",
            "--window-end",
            "2026-05-21T12:00:00Z",
        ]
    )

    payload = json.loads(data_output.read_text(encoding="utf-8"))
    assert status == 0
    assert payload["window"] == {
        "start": "2026-05-21T09:00:00+00:00",
        "end": "2026-05-21T12:00:00+00:00",
    }


def test_run_skip_empty_segment_does_not_write_when_all_categories_empty(tmp_path):
    output = tmp_path / "index.html"
    data_output = tmp_path / "segment.json"

    # A window in the distant past — the mock data is generated relative
    # to "now", so every item gets filtered out and all four counts hit 0.
    status = run.main(
        [
            "--mock-data",
            "--output",
            output.as_posix(),
            "--data-output",
            data_output.as_posix(),
            "--skip-empty-segment",
            "--window-start",
            "2000-01-01T00:00:00Z",
            "--window-end",
            "2000-01-01T06:00:00Z",
        ]
    )

    assert status == 0
    assert not data_output.exists(), "empty segment should not have been written"
    # The HTML is still produced (so the site never goes blank).
    assert output.exists()
