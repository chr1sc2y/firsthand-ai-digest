# Firsthand AI Digest — Documentation

> Engineering reference for the project. Inspired by Harness's
> Engineering docs: every module, every external service, and every
> failure mode written down once, here.

## Repository layout

| Path | Purpose |
|------|---------|
| `config/` | Source list and secrets template |
| `data/ai-briefs/` | Published daily AI interpretation HTML |
| `data/source-packs/` | Raw source material for brief generation |
| `data/daily/`, `data/segments/` | Committed digest archive |
| `dist/` | Build output served by GitHub Pages (gitignored) |
| `scripts/` | Pipeline entry points |
| `staging/ai-briefs/` | Pre-publish brief drafts from automation (gitignored) |
| `tmp/` | Local scratch files (gitignored) |

Root keeps only project metadata: `README.md`, `requirements.txt`, `pytest.ini`, `CNAME`.

## Table of contents

- [Architecture](architecture.md) — system overview & data flow
- [Modules](modules.md) — what each Python file does and why
- [Data Sources](data-sources.md) — every external feed & API we touch
- [Tech Stack](tech-stack.md) — runtime, libraries, infra
- [Operations](operations.md) — secrets, deploy, custom domain, debugging
