# Firsthand AI Digest

**Every day, the sharpest AI voices in one place.**

A self-hosted digest that automatically aggregates what AI's leading researchers, founders, and builders are saying — across X posts, long-form blogs, podcasts, and YouTube — then publishes it as a clean, interactive site on GitHub Pages.

No login. No algorithm. No noise.

---

## What it tracks

| Source | What you get |
|--------|-------------|
| **X / Twitter** | Real-time posts from 50+ AI leaders |
| **Blogs** | Long-form writing from OpenAI, Anthropic, DeepMind, and independent researchers |
| **Podcasts** | Episodes featuring leaders you follow, filtered by name |
| **YouTube** | Recent uploads from AI research channels |

---

## How it works

GitHub Actions fetches every source once daily at 06:17 Beijing time and commits a normalized 24-hour window to this repo. GitHub Pages serves the static site — no backend, no database, no cost.

The daily cadence reduces hosted-runner and [Apify](https://apify.com/) actor invocations while the 06:00 cutoff keeps the 08:00 Insight brief current.

Flip between time windows (3h · 6h · 12h · 24h · 3d · 7d) to see what's fresh or catch up on the week.

## Daily AI interpretations

The daily GitHub Actions workflow deepens the normalized source window, calls
DeepSeek for an evidence-linked English analysis and Chinese localized rewrite,
then publishes both Insight briefs into `data/insight/`. Public builds expose
the briefs under `archive/`, with a fixed `EN / 中文` switch on both versions.
See [operations](docs/operations.md) for the required repository secrets.

---

## Quick start

```bash
pip install -r requirements.txt
python scripts/run.py --mock-data --output dist/index.html
open dist/index.html
```

To deploy your own instance, see **[docs/operations.md](docs/operations.md)**.

---

## Docs

Full engineering reference: **[docs/](docs/README.md)**

---

## License

MIT · Inspired by [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders)
