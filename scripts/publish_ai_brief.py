"""Publish generated AI interpretation briefs into the static site."""
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_BRIEF_DIR = ROOT / "data" / "ai-briefs"
DATA_BRIEF_INDEX = DATA_BRIEF_DIR / "index.json"
DIST = ROOT / "dist"
PUBLIC_BRIEF_DIR = "archive"
BRIEF_DIR = DIST / PUBLIC_BRIEF_DIR
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
AI_BRIEFS_START = "<!-- AI_BRIEFS_START -->"
AI_BRIEFS_END = "<!-- AI_BRIEFS_END -->"
AI_BRIEFS_CSS_START = "/* AI_BRIEFS_CSS_START */"
AI_BRIEFS_CSS_END = "/* AI_BRIEFS_CSS_END */"

# AI analysis (the interpreted briefs) are served on a dedicated subdomain
# distinct from the main "Firsthand AI Digest" aggregator.
# Update these two constants + update demos if needed.
#
# Good alternatives (subdomain prefix + card text):
#   insight.ai.prov1dence.top + "Latest AI Insight"  (CURRENT)
#   brief.ai.prov1dence.top  + "Latest AI Brief"     (matches file names *-ai-brief.html)
#   lens.ai.prov1dence.top   + "Latest AI Lens"      (nice metaphor)
#   pulse.ai.prov1dence.top  + "Latest AI Pulse"
#   distill.ai.prov1dence.top + "Latest AI Distill"
#   synth.ai.prov1dence.top  + "Latest AI Synth"
AI_ANALYSIS_DOMAIN = "insight.ai.prov1dence.top"
AI_CARD_LABEL = "Latest AI Insight"

AI_BRIEFS_CSS = f"""
{AI_BRIEFS_CSS_START}
.insight-link {{
  font-size: 0.22em;
  font-weight: 600;
  color: var(--accent);
  text-decoration: none;
  white-space: nowrap;
  background: rgba(0, 113, 227, 0.08);
  padding: 2px 9px;
  border-radius: 999px;
  letter-spacing: 1px;
  transition: background .15s, color .15s;
  line-height: 1;
}}
.insight-link:hover {{
  text-decoration: underline;
  background: rgba(0, 113, 227, 0.15);
}}
@media (max-width: 640px) {{
  .insight-link {{ font-size: 0.2em; padding: 1px 6px; }}
}}
{AI_BRIEFS_CSS_END}
""".strip()

LANG_SWITCH_CSS = (
    ".lang-switch{position:fixed;top:18px;right:18px;z-index:50;display:flex;"
    "gap:4px;background:rgba(255,255,255,.86);border:1px solid var(--line,#dfe5ee);"
    "border-radius:999px;padding:4px;backdrop-filter:blur(18px);"
    "box-shadow:0 4px 18px rgba(30,42,62,.10)}"
    ".lang-switch a{border-radius:999px;padding:6px 10px;font-size:12px;"
    "font-weight:800;color:var(--muted,#647083);text-decoration:none}"
    ".lang-switch a.active{background:var(--blue,var(--green,#2457d6));color:#fff}"
    "@media(max-width:560px){.lang-switch{position:static;margin:14px 20px 0;"
    "display:inline-flex}}"
)
LANG_SWITCH_RE = re.compile(
    r"\s*<nav\b[^>]*class=[\"'][^\"']*\blang-switch\b[^\"']*[\"'][\s\S]*?</nav>",
    re.IGNORECASE,
)
LANG_SWITCH_CSS_RE = re.compile(
    r"\.lang-switch\{[\s\S]*?@media\(max-width:560px\)\{\.lang-switch\{[\s\S]*?\}\}",
    re.IGNORECASE,
)
HTML_LANG_RE = re.compile(r"<html\b([^>]*)\blang=[\"'][^\"']*[\"']([^>]*)>", re.IGNORECASE)
TITLE_RE = re.compile(r"<title>[\s\S]*?</title>", re.IGNORECASE)

LOCALIZED_REWRITES = (
    ("Model access risk becomes the day's operating story", "模型访问风险成为今天最重要的运行议题"),
    ("Firsthand's 24-hour set contained 22 timestamped items.", "Firsthand 24 小时窗口包含 22 个带时间戳条目。"),
    ("Add provider fallback paths.", "为关键工作流添加供应商 fallback 路径。"),
    ("Executive Summary", "执行摘要"),
    ("Source Access", "来源可访问性"),
    ("Cross-Event Trend Judgments", "跨事件趋势判断"),
    ("For Developers", "给开发者"),
    ("For Startups", "给创业公司"),
    ("For Researchers", "给研究者"),
    ("For Enterprise Buyers", "给企业买家"),
    ("24-72 Hour Watchlist", "24-72 小时观察清单"),
    ("Confidence Notes", "置信度说明"),
    ("Source Links", "来源链接"),
    ("Substantial:", "充分："),
    ("Partial:", "部分："),
    ("Limited:", "受限："),
    ("Fact.", "事实。"),
    ("Analysis.", "分析。"),
    ("Inference.", "推断。"),
    ("Implication.", "启示。"),
    ("Uncertainty.", "不确定性。"),
    ("High confidence:", "高置信度："),
    ("Medium confidence:", "中等置信度："),
    ("Low confidence:", "低置信度："),
    ("Execution time:", "执行时间："),
    ("Coverage window:", "覆盖窗口："),
    ("Firsthand AI Insight", "Firsthand AI 解读"),
)


def _brief_date(path: Path, explicit_date: str | None) -> str:
    if explicit_date:
        datetime.strptime(explicit_date, "%Y-%m-%d")
        return explicit_date
    match = DATE_RE.search(path.name)
    if not match:
        raise ValueError(
            f"Could not infer YYYY-MM-DD from {path.name}; pass --date YYYY-MM-DD."
        )
    return match.group(1)


def _load_index() -> dict:
    if not DATA_BRIEF_INDEX.exists():
        return {"schema_version": 1, "briefs": []}
    try:
        payload = json.loads(DATA_BRIEF_INDEX.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {DATA_BRIEF_INDEX}") from exc
    payload.setdefault("schema_version", 1)
    payload.setdefault("briefs", [])
    return payload


def _write_index(payload: dict) -> None:
    DATA_BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    payload["updated_at"] = datetime.now(timezone.utc).isoformat()
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    DATA_BRIEF_INDEX.write_text(text, encoding="utf-8")
    BRIEF_INDEX = BRIEF_DIR / "index.json"
    BRIEF_INDEX.write_text(text, encoding="utf-8")


def _section_html(payload: dict) -> str:
    briefs = payload.get("briefs", [])
    if not isinstance(briefs, list) or not briefs:
        return ""
    latest = briefs[0]
    if not isinstance(latest, dict):
        return ""
    date = str(latest.get("date", "")).strip()
    path = str(latest.get("path", "")).strip()
    if not date or not path:
        return ""
    # Homepage only: link to the Insight root. The standalone site owns its
    # archive routing and renders the latest brief at / without redirects.
    href = f"https://{AI_ANALYSIS_DOMAIN}/"
    return (
        f"{AI_BRIEFS_START}\n"
        f'<a class="insight-link" href="{href}">insight</a>\n'
        f"{AI_BRIEFS_END}"
    )


def _replace_between(text: str, start: str, end: str, replacement: str) -> str | None:
    start_index = text.find(start)
    end_index = text.find(end)
    if start_index == -1 or end_index == -1 or end_index < start_index:
        return None
    end_index += len(end)
    return text[:start_index] + replacement + text[end_index:]


def _language_switch_html(*, date: str, language: str) -> str:
    english = f"{date}-ai-brief.html"
    chinese = f"{date}-ai-brief-zh.html"
    en_class = ' class="active"' if language == "en" else ""
    zh_class = ' class="active"' if language == "zh" else ""
    return (
        '<nav class="lang-switch" aria-label="Language">'
        f'<a{en_class} href="{english}">EN</a>'
        f'<a{zh_class} href="{chinese}">中文</a>'
        "</nav>"
    )


def _inject_language_switch(text: str, *, date: str, language: str) -> str:
    text = LANG_SWITCH_RE.sub("", text, count=1)
    text = LANG_SWITCH_CSS_RE.sub("", text, count=1)
    if "</style>" in text:
        text = text.replace("</style>", f"{LANG_SWITCH_CSS}</style>", 1)
    elif "</head>" in text:
        text = text.replace("</head>", f"<style>{LANG_SWITCH_CSS}</style></head>", 1)
    else:
        text = f"<style>{LANG_SWITCH_CSS}</style>{text}"

    switch = _language_switch_html(date=date, language=language)
    if "<body>" in text:
        return text.replace("<body>", f"<body>\n{switch}", 1)
    body_match = re.search(r"<body\b[^>]*>", text, re.IGNORECASE)
    if body_match:
        return text[: body_match.end()] + "\n" + switch + text[body_match.end() :]
    return switch + "\n" + text


def _generate_chinese_companion(english_html: str, *, date: str) -> str:
    """Create a localized Chinese fallback when the automation omitted zh HTML.

    The daily automation should still produce a polished Chinese rewrite itself.
    This fallback keeps the public site bilingual and preserves links/source
    evidence by localizing the fixed brief frame and common analysis labels.
    """
    text = HTML_LANG_RE.sub(r'<html\1lang="zh-CN"\2>', english_html, count=1)
    if text == english_html:
        text = re.sub(r"<html\b([^>]*)>", r'<html lang="zh-CN"\1>', text, count=1, flags=re.IGNORECASE)
    text = TITLE_RE.sub(f"<title>Firsthand AI 解读 - {date}</title>", text, count=1)

    for source, target in sorted(LOCALIZED_REWRITES, key=lambda pair: len(pair[0]), reverse=True):
        text = text.replace(source, target)

    note = (
        '<p class="note small"><strong>说明：</strong>'
        "本中文版由发布流程自动本地化改写，保留英文版事实、来源链接和不确定性标注；"
        "如同日人工中文稿存在，会优先使用人工稿。</p>"
    )
    if "自动本地化改写" not in text:
        main_match = re.search(r"<main\b[^>]*>", text, re.IGNORECASE)
        if main_match:
            text = text[: main_match.end()] + "\n" + note + text[main_match.end() :]
        elif "<body>" in text:
            text = text.replace("<body>", f"<body>\n{note}", 1)
    return text


def _refresh_homepage(payload: dict) -> None:
    homepage = DIST / "index.html"
    if not homepage.exists():
        return
    text = homepage.read_text(encoding="utf-8")

    css_replacement = AI_BRIEFS_CSS
    css_updated = _replace_between(
        text,
        AI_BRIEFS_CSS_START,
        AI_BRIEFS_CSS_END,
        css_replacement,
    )
    if css_updated is None:
        text = text.replace("</style>", f"{AI_BRIEFS_CSS}\n</style>", 1)
    else:
        text = css_updated

    section = _section_html(payload)
    section_updated = _replace_between(text, AI_BRIEFS_START, AI_BRIEFS_END, section)
    if section_updated is None:
        text = text.replace('<div class="page">', f"{section}\n<div class=\"page\">", 1)
    else:
        text = section_updated
    homepage.write_text(text, encoding="utf-8")


def _upsert_brief(payload: dict, *, date: str, path: str, title: str) -> None:
    briefs = [b for b in payload.get("briefs", []) if b.get("date") != date]
    briefs.append({"date": date, "title": title, "path": path})
    payload["briefs"] = sorted(briefs, key=lambda b: b["date"], reverse=True)


def _normalize_public_paths(payload: dict) -> None:
    normalized = []
    for brief in payload.get("briefs", []):
        if not isinstance(brief, dict):
            continue
        path = str(brief.get("path", "")).strip()
        if path:
            brief = dict(brief)
            brief["path"] = f"{PUBLIC_BRIEF_DIR}/{Path(path).name}"
        normalized.append(brief)
    payload["briefs"] = normalized


def publish(source: Path, *, date: str | None = None, refresh_homepage: bool = True) -> Path:
    source = source.expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(source)
    if source.suffix.lower() != ".html":
        raise ValueError(f"Expected an HTML file, got {source}")

    brief_date = _brief_date(source, date)
    DATA_BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    data_target = DATA_BRIEF_DIR / f"{brief_date}-ai-brief.html"
    target = BRIEF_DIR / data_target.name
    zh_source = DATA_BRIEF_DIR / f"{brief_date}-ai-brief-zh.html"
    english_html = source.read_text(encoding="utf-8")
    if not zh_source.exists():
        zh_source.write_text(
            _generate_chinese_companion(english_html, date=brief_date),
            encoding="utf-8",
        )
    has_chinese_companion = True
    if has_chinese_companion:
        english_html = _inject_language_switch(english_html, date=brief_date, language="en")
    data_target.write_text(english_html, encoding="utf-8")
    shutil.copy2(data_target, target)

    # Also publish companion Chinese version (if exists) so lang switch works from dist/
    if has_chinese_companion:
        zh_data_target = DATA_BRIEF_DIR / zh_source.name  # already is
        zh_dist_target = BRIEF_DIR / zh_source.name
        chinese_html = _inject_language_switch(
            zh_source.read_text(encoding="utf-8"), date=brief_date, language="zh"
        )
        zh_data_target.write_text(chinese_html, encoding="utf-8")
        # ensure zh is also in data (in case source was external) and dist
        if not zh_data_target.exists() or zh_source.resolve() != zh_data_target.resolve():
            shutil.copy2(zh_source, zh_data_target)
        shutil.copy2(zh_data_target, zh_dist_target)

    payload = _load_index()
    _upsert_brief(
        payload,
        date=brief_date,
        title=f"{brief_date} AI 解读",
        path=f"{PUBLIC_BRIEF_DIR}/{target.name}",
    )
    _normalize_public_paths(payload)
    _write_index(payload)

    if refresh_homepage:
        _refresh_homepage(payload)
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Copy a generated AI brief into dist/ and refresh homepage links."
    )
    parser.add_argument("html", type=Path, help="Generated firsthand-ai-brief-YYYY-MM-DD.html")
    parser.add_argument("--date", help="Override date as YYYY-MM-DD")
    parser.add_argument(
        "--no-homepage",
        action="store_true",
        help="Update the brief index without touching dist/index.html.",
    )
    args = parser.parse_args(argv)

    target = publish(args.html, date=args.date, refresh_homepage=not args.no_homepage)
    print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
