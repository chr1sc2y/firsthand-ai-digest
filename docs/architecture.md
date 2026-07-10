# Architecture

## Goal

Produce one static digest window each day at 06:17 Asia/Shanghai that
summarises the preceding 24 hours across X posts, blogs, podcasts, and
YouTube. Serve a zero-server site whose default
view is the latest 24 hours and whose frontend preloads up to 7 days of
committed JSON archive data.

The daily cadence reduces hosted-runner acquisition and Apify actor calls.
The 06:00 cutoff also gives the 08:00 Insight brief a complete recent window.

## Topology

```
                ┌─────────────────────────────────────┐
                │ GitHub Actions (daily, 06:17 BJT)   │
                └────────────────┬────────────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │       scripts/run.py            │
                └─┬─────┬─────┬─────┬─────────────┘
                  │     │     │     │
        ┌─────────┘     │     │     └────────┐
        ▼               ▼     ▼              ▼
  Apify Actor       RSS feeds  RSS         RSS feeds
  (X scraper)        (blogs)  (podc.)      (YouTube)
        │               │     │              │
        └─────┬─────────┴─────┴──────────────┘
              │
              ▼
       24h window-filter → cross-category dedup → sort
              │
              ├──▶ data/segments/YYYY-MM-DD/06.json ───▶ commit to repo
              ├──▶ data/daily/YYYY-MM-DD.json when a day is complete
              ├──▶ data/index.json manifest for the frontend
              │
              ▼
        render latest 24h → dist/index.html + dist/data ───▶ GitHub Pages
```

## Pipeline (run.py)

| # | Stage              | Module                     | Notes                                  |
|---|--------------------|----------------------------|----------------------------------------|
| 1 | Fetch X posts      | `fetch_x.py`               | Batched Apify kaitoeasyapi search terms; failures degrade gracefully |
| 2 | Fetch blogs        | `fetch_rss.py`             | Atom / RSS via `feedparser`, parallel + retry |
| 3 | Fetch YouTube      | `fetch_rss.py`             | `videos.xml?channel_id=…`, parallel + retry |
| 4 | Fetch podcasts     | `fetch_podcasts.py`        | RSS + leader-name keyword filter       |
| 5 | Window-filter      | `run.py`                   | exact 24h `[start, end)` window        |
| 6 | Cross-cat dedup    | `fetch_rss.dedup`          | canonical URL (strip utm, lowercase)   |
| 7 | Sort + clip        | `run.py`                   | newest first, max-per-source           |
| 8 | Window snapshot    | `run.py`                   | `data/segments/YYYY-MM-DD/06.json`     |
| 9 | Archive/index      | `archive_data.py`          | daily merge + `data/index.json`        |
|10 | Render             | `render_html.py`           | latest 24h HTML + 7d client switching  |

## Failure model

- Any single source failure (network, parse error, rate limit) is logged
  and the rest of the pipeline continues. We never abort the whole run for
  one feed. The X fetch in particular is wrapped in try/except so an
  Apify outage does not block blog / video / podcast updates.
- Re-runs are idempotent for a window path: rerunning before the next 06:00
  boundary replaces the same `data/segments/YYYY-MM-DD/06.json`.
- A same-window rerun unions its items with the existing snapshot before an
  atomic replace, so a transient category failure cannot erase prior results.
- Segment and daily JSON files are committed back to the repository and copied
  into the Pages artifact under `dist/data/` via an atomic directory swap.

## Why static + GitHub Pages

- Free hosting, zero servers.
- Custom subdomain via `CNAME` with auto-issued Let's Encrypt cert.
- Public artifacts make the digest archivable / forkable.
- Build runs in CI so secrets never touch the user's machine.

## Future hooks

- LLM summarisation: a `summarize.py` step can be inserted between dedup
  and render. The render layer already accepts a `summary` field per item.
- Optional catch-up/backfill command for missing historical daily windows.
