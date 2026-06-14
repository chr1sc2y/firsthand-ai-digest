# Operations

## Local run

```bash
pip install -r requirements.txt
cp config/secrets.example.json config/secrets.json
# edit config/secrets.json and paste your Apify token
python scripts/run.py --verbose
open dist/index.html
```

For a zero-secret smoke test after cloning or moving machines:

```bash
python scripts/run.py --mock-data --verbose
open dist/index.html
```

## Secrets

`config/secrets.json` is gitignored. We never read system environment
variables; the Apify token must be in the file.

```jsonc
{
  "apify_token":              "apify_api_xxx",   // required
  "apify_actor":              "kaitoeasyapi~twitter-x-data-tweet-scraper-pay-per-result-cheapest",
  "apify_lookback_hours":     6,
  "apify_monthly_budget_usd": 4.0                // soft cap; once month-to-date
                                                 // spend hits this, X fetch
                                                 // is skipped for the rest
                                                 // of the cycle.
}
```

## CI / cron

[`.github/workflows/daily.yml`](../.github/workflows/daily.yml) runs every
6 hours on Asia/Shanghai segment boundaries and on manual dispatch. It:

1. Installs `requirements.txt`
2. Runs `pytest` (unit only — `integration` is skipped)
3. Materialises `config/secrets.json` from the repo secret `APIFY_TOKEN`
4. Computes the latest complete 6-hour Asia/Shanghai window
5. Builds `data/segments/YYYY-MM-DD/HH.json`
6. Merges complete days into `data/daily/YYYY-MM-DD.json`
7. Writes `data/index.json`, renders latest 24h, and copies `data/` into `dist/data/`
8. Commits JSON archive changes back to the repository
9. Uploads `dist/` as the Pages artifact and deploys it

The 6-hour cadence (4 runs/day) is sized so that the monthly Apify spend
stays inside the free $5 platform credit.

[`.github/workflows/tests.yml`](../.github/workflows/tests.yml) runs the
unit tests on every push and PR.

[`.github/workflows/pages.yml`](../.github/workflows/pages.yml) deploys the
already-committed `data/` archive to GitHub Pages on every push to `main`.
It does not need `APIFY_TOKEN`; scheduled data fetching still belongs to
`daily.yml`.

## Custom domain

1. Settings → Pages → **Source: GitHub Actions**, **Custom domain:
   `ai.<domain>`**, **Enforce HTTPS**.
2. Create a repo-root `CNAME` file with the same value. `run.py` copies it
   into `dist/` so it survives every deploy.
3. Add a DNS record at your registrar: `CNAME  ai  <username>.github.io`.

The first deploy may take a few minutes for Let's Encrypt to issue the
cert.

### Insight subdomain

The homepage links the latest AI interpretation brief to the standalone
Insight Pages repository:

```text
https://insight.ai.prov1dence.top/
https://insight.ai.prov1dence.top/archive/<brief-file>
```

The main digest repository remains bound to `ai.prov1dence.top`; the separate
[`chr1sc2y/firsthand-ai-insight`](https://github.com/chr1sc2y/firsthand-ai-insight)
repository is bound to `insight.ai.prov1dence.top`.

Build the local Insight repository from committed briefs with:

```bash
python scripts/sync_insight_site.py \
  --target-dir /Users/zintrulcre/repo/firsthand-ai-insight
```

This copies `data/ai-briefs/` into the Insight repo's public `archive/`
directory, writes a root `index.html` that displays the latest English brief,
writes `CNAME`, and installs a minimal GitHub Pages workflow for the Insight
repo.

Daily Insight briefs are expected to be bilingual:

- English: `YYYY-MM-DD-ai-brief.html`
- Chinese: `YYYY-MM-DD-ai-brief-zh.html`
- Both pages must keep the fixed `EN / 中文` language switch.
- The Chinese page should be a localized Chinese rewrite rather than a literal
  line-by-line translation.

If the automation omits the Chinese companion, `scripts/publish_ai_brief.py`
will generate a fallback Chinese page and inject the language switch into both
files before syncing the Insight site.

To let `.github/workflows/daily.yml` sync the Insight repo automatically after
the scheduled digest build, create a main-repo secret named
`INSIGHT_REPO_TOKEN`. It must be a token that can write to
`chr1sc2y/firsthand-ai-insight`; the default `GITHUB_TOKEN` for
`firsthand-ai-digest` cannot write to a different repository.

For the subdomain to work publicly, DNS must publish:

```text
CNAME  insight.ai  chr1sc2y.github.io
```

Check propagation with:

```bash
dig @1.1.1.1 +short insight.ai.prov1dence.top CNAME
dig @8.8.8.8 +short insight.ai.prov1dence.top CNAME
```

Both should return `chr1sc2y.github.io.`. If public DNS is correct but HTTPS
still fails, check the Pages settings in `firsthand-ai-insight` and ensure its
custom domain is `insight.ai.prov1dence.top` with HTTPS enabled.

## Tests

```bash
pytest                 # unit (offline, fast)
pytest -m integration  # live network — every RSS feed must be reachable
```

Mark new tests that hit the network with `@pytest.mark.integration` so
they don't run by default.

## Adding a source

1. Edit [`config/sources.json`](../config/sources.json).
2. Add a unit-test case in `tests/test_sources_config.py` if the change
   introduces a new top-level key.
3. Run `pytest -m integration` locally to verify the feed is alive.
4. Commit. CI will build the next digest.

## Debugging a failing run

- `python scripts/run.py --verbose` prints per-source progress and any
  network errors. Single-source failures are non-fatal.
- `pytest -m integration -k <feed-name>` checks a specific RSS feed.
- GitHub Pages deploy errors: check Actions → most recent run → `deploy`
  step.
- Segment debugging: `python scripts/segment_window.py` prints the latest
  complete 6-hour bucket; `python scripts/archive_data.py` rebuilds
  `data/index.json` and `dist/index.html` from committed JSON.

## Cost

- **Apify** — billed by returned data, with provider-specific minimums per
  actor call. The X fetcher batches all configured handles into one actor run
  per 6-hour segment, then clips the returned tweets per handle locally. At 4
  runs/day the spend stays inside Apify's free $5 monthly platform credit
  (≈ 20k tweets/month). Before each run we also check
  ``GET /v2/users/me/usage/monthly`` and skip the X fetch if the cycle has
  already used more than ``apify_monthly_budget_usd`` (default $4) — a hard
  guarantee that we never overshoot the free tier.
- **GitHub Actions** — free tier covers daily cron easily.
- **GitHub Pages** — free.
- **Domain** — whatever you pay your registrar.
