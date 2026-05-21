# Modules

A one-page reference for each file under `scripts/` and `tests/`.

## `scripts/run.py`

The pipeline entry point. Reads `config/sources.json`, orchestrates the
four fetchers, applies per-category time windows, dedups across
categories, sorts, and writes `dist/index.html` (plus `CNAME` if present).

CLI flags:

| Flag                  | Default | Meaning                                      |
| --------------------- | ------- | -------------------------------------------- |
| `--config`            | `config/sources.json` | sources file path             |
| `--output`            | `dist/index.html`     | output path                   |
| `--max-per-source`    | 5       | items kept per handle / feed                 |
| `--hours`             | 24      | window for X posts                           |
| `--blog-hours`        | 168     | window for blogs (7 d)                       |
| `--video-hours`       | 168     | window for YouTube (7 d)                     |
| `--podcast-hours`     | 720     | window for podcasts (30 d)                   |
| `--no-podcast-filter` |         | keep all episodes regardless of leader name  |
| `--data-output`       |         | optional normalized JSON output path         |
| `--window-start`      |         | inclusive UTC ISO timestamp for global window |
| `--window-end`        |         | exclusive UTC ISO timestamp for global window |
| `--verbose`           |         | DEBUG logging                                |

## `scripts/segment_window.py`

Computes the latest complete 6-hour Asia/Shanghai segment. In GitHub Actions
it writes `DIGEST_WINDOW_START`, `DIGEST_WINDOW_END`, and
`DIGEST_SEGMENT_PATH` to `$GITHUB_ENV`.

## `scripts/archive_data.py`

Maintains the committed data archive and deployable data bundle.

- merges complete `data/segments/YYYY-MM-DD/*.json` days into
  `data/daily/YYYY-MM-DD.json`
- writes `data/index.json`
- renders `dist/index.html` from the latest 24 hours
- copies `data/` into `dist/data/` for frontend prefetching (atomic swap)

## `scripts/fetch_x.py`

Apify [`kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest`](
https://apify.com/kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest)
actor. Reads `apify_token`, `apify_actor`, `apify_lookback_hours` from
`config/secrets.json`. Never reads system environment variables on
purpose — secrets must live in the file. The CI workflow generates that
file from the `APIFY_TOKEN` repo secret.

The actor is called once per run with batched `searchTerms[]` entries, one
per configured handle, using `from:<handle> since_time:<unix>
until_time:<unix>` so scheduled segments map exactly to their 6-hour window.

`run.py` wraps the call in a try/except so a missing token or upstream
outage degrades gracefully — every other category still publishes.

## `scripts/fetch_rss.py`

Generic RSS / Atom helpers used by blogs, podcasts (delegated), and
YouTube.

- `fetch_feed(url)` — single feed → list of normalized item dicts. Retries
  network errors twice with exponential backoff before giving up.
- `fetch_many(feeds, kind, max_items, role_template)` — fetches every feed
  concurrently (capped at 8 workers) and tags each item with its `kind`.
- `canonical_url(url)` — lowercase host, strip `utm_*`, drop trailing
  slash. Used by `dedup`.
- `dedup(items)` — keep the first occurrence per canonical link.

## `scripts/fetch_podcasts.py`

Thin wrapper around `fetch_rss._fetch_feed` that adds a leader-name
keyword filter (`require_leader_match=True` by default). An episode is
kept if its title / summary / author / keywords mention the full name,
last name, or `@handle` of any configured X leader.

## `scripts/render_html.py`

Pure-Python HTML renderer. Produces a single file with inline CSS and
no external assets. Editorial / magazine layout: serif display headings,
mono-spaced metadata, sticky topbar, sticky section nav, 1-px hairline
grid of cards.

`render(x_items, podcast_items, blog_items, video_items)` returns the
full HTML document. Every item must have at least `source_name`,
`summary`, `link`, `published`, `kind`.

## Tests

| File                                  | Scope                                                           |
| ------------------------------------- | --------------------------------------------------------------- |
| `tests/test_parse_date.py`            | Date parsing helpers                                            |
| `tests/test_fetch_x.py`               | Apify client, mocked HTTP                                       |
| `tests/test_fetch_rss.py`             | Generic RSS / canonical / dedup                                 |
| `tests/test_fetch_podcasts.py`        | Leader-name filter                                              |
| `tests/test_sources_config.py`        | `config/sources.json` shape, no duplicates                      |
| `tests/test_archive_data.py`          | 6-hour segment merge + index                                    |
| `tests/test_run_mock.py`              | Top-level pipeline smoke test (mock data)                       |
| `tests/test_podcast_rss_integration.py` | Live network — every feed reachable (`pytest -m integration`) |

`pytest.ini` skips `integration` by default.
