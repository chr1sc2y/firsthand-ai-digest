"""Render the collected items into a single self-contained HTML page.

Design language: restrained Apple-style editorial grid with quiet surfaces,
system typography, and minimal chroma.
"""
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSIGHT_INDEX = ROOT / "data" / "insight" / "index.json"

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

CSS = """
:root {
  color-scheme: light dark;
  --bg: #f5f5f7;
  --surface: #ffffff;
  --surface-2: rgba(255,255,255,0.72);
  --ink: #1d1d1f;
  --ink-2: #515154;
  --ink-3: #86868b;
  --border: rgba(0,0,0,0.10);
  --shadow: 0 1px 2px rgba(0,0,0,0.04);
  --shadow-hover: 0 10px 30px rgba(0,0,0,0.08);
  --accent: #0071e3;
  --sans: "SF Pro Display", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  --text: "SF Pro Text", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  --mono: "SF Mono", ui-monospace, Menlo, monospace;
  --radius: 18px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #000000;
    --surface: #1d1d1f;
    --surface-2: rgba(29,29,31,0.78);
    --ink: #f5f5f7;
    --ink-2: #a1a1a6;
    --ink-3: #6e6e73;
    --border: rgba(255,255,255,0.13);
    --shadow: none;
    --shadow-hover: 0 14px 36px rgba(0,0,0,0.42);
    --accent: #2997ff;
  }
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--text);
  font-size: 16px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
a { color: inherit; text-decoration: none; }

/* --- Hero --- */
.hero {
  max-width: 1180px; margin: 0 auto;
  padding: 68px 24px 34px;
}
.hero h1 {
  font-family: var(--sans);
  font-weight: 700;
  font-size: clamp(48px, 7vw, 88px);
  line-height: 1.04;
  letter-spacing: 0;
  margin-bottom: 18px;
  max-width: 920px;
}
.hero h1 em { font-style: normal; color: var(--ink); }
.hero .lede {
  font-family: var(--text);
  font-size: 19px; line-height: 1.45;
  color: var(--ink-2); max-width: 620px; margin: 0;
}

/* --- Divider --- */
.hero-divider {
  max-width: 1180px; margin: 0 auto; padding: 0 24px;
}
.hero-divider hr { border: none; border-top: 1px solid var(--border); margin: 0; }

/* --- New sidebar + main layout for better hierarchy --- */
.content-layout {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px 60px;
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 28px;
  align-items: start;
}
.sidebar {
  position: sticky;
  top: 16px;
  display: grid;
  gap: 18px;
}
.insight-callout {
  border: 1px solid var(--border);
  border-radius: 14px;
  background: var(--surface-2);
  box-shadow: var(--shadow);
  overflow: hidden;
}
.insight-link {
  display: grid;
  gap: 6px;
  padding: 14px;
  text-decoration: none;
  color: var(--accent);
  transition: background .15s, box-shadow .15s, transform .15s;
}
.insight-link:hover {
  background: rgba(0, 113, 227, 0.07);
  box-shadow: var(--shadow-hover);
  transform: translateY(-1px);
}
.insight-kicker {
  font-family: var(--mono);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-3);
}
.insight-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  font-family: var(--sans);
  font-size: 16px;
  font-weight: 700;
  line-height: 1.18;
  color: var(--ink);
}
.insight-arrow {
  flex: 0 0 auto;
  color: var(--accent);
}
.insight-note {
  font-size: 12px;
  line-height: 1.38;
  color: var(--ink-2);
}

.filter-groups {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.filter-group {}
.filter-label {
  font-size: 10px;
  font-weight: 600;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: 0.6px;
  margin-bottom: 5px;
}

/* Make filters vertical + compact in sidebar (two columns side-by-side) */
.sidebar .time-seg,
.sidebar .seg {
  display: flex;
  flex-direction: column;
  background: none;
  border-radius: 0;
  padding: 0;
  gap: 2px;
  border: 0;
}
.sidebar .time-seg button,
.sidebar .seg button {
  appearance: none !important;
  border: none !important;
  background: transparent !important;
  padding: 5px 8px !important;
  border-radius: 6px !important;
  font-size: 12px !important;
  font-weight: 500 !important;
  color: var(--ink-2) !important;
  cursor: pointer !important;
  text-align: left !important;
  transition: all .1s !important;
  width: 100% !important;
  box-shadow: none !important;
}
.sidebar .time-seg button.active,
.sidebar .seg button.active {
  background: var(--surface) !important;
  color: var(--ink) !important;
  box-shadow: 0 1px 2px rgba(0,0,0,.06) !important;
  font-weight: 600 !important;
}

@media (max-width: 860px) {
  .content-layout {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .sidebar {
    position: static;
    order: -1; /* AI + filters on top on mobile */
  }
  .insight-callout {
    max-width: 520px;
  }
  .filter-groups {
    grid-template-columns: 1fr 1fr;
  }
}
.seg {
  display: flex; gap: 0;
  background: rgba(0,0,0,0.05);
  border-radius: 999px; padding: 3px;
  border: 0;
}
.seg button {
  appearance: none; border: none; background: none;
  padding: 6px 18px; border-radius: 999px;
  font-size: 13px; font-weight: 500;
  color: var(--ink-2); cursor: pointer;
  transition: all .15s;
}
.seg button.active { background: var(--surface); color: var(--ink); box-shadow: var(--shadow); }

.time-seg {
  display: flex; gap: 0;
  background: rgba(0,0,0,0.05); border-radius: 999px; padding: 3px;
  border: 0;
}
.time-seg button {
  appearance: none; border: none; background: none;
  padding: 6px 14px; border-radius: 999px;
  font-size: 13px; font-weight: 500;
  color: var(--ink-2); cursor: pointer;
  transition: all .15s;
}
.time-seg button.active { background: var(--surface); color: var(--ink); box-shadow: var(--shadow); }
/* --- Layout --- */
.main-content {
  min-width: 0;
}
.main-content .page {
  max-width: none;
  margin: 0;
  padding: 0;
}
.page { max-width: 1180px; margin: 0 auto; padding: 0 24px 80px; }
.section { margin-bottom: 50px; }
.section-head {
  display: flex; align-items: baseline; justify-content: space-between;
  margin-bottom: 16px; padding-bottom: 10px;
  border-bottom: 1px solid var(--border);
}
.section-head h2 { font-family: var(--sans); font-size: 24px; font-weight: 700; letter-spacing: 0; }
.section-head .count {
  font-family: var(--mono); font-size: 12px; color: var(--ink-3);
  letter-spacing: 0.04em; text-transform: uppercase;
}

/* --- Card grid --- */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 16px;
}
@media (min-width: 1100px) { .grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 780px)  { .grid { grid-template-columns: 1fr 1fr; gap: 14px; } }
@media (max-width: 520px)  { .grid { grid-template-columns: 1fr; } }

/* --- Card --- */
.card {
  background: var(--surface-2);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  display: flex; flex-direction: column;
  transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
  cursor: pointer;
  position: relative; z-index: 1;
  height: 100%;
  overflow: hidden;
  backdrop-filter: blur(18px);
}
.card:hover {
  box-shadow: var(--shadow-hover);
  transform: translateY(-2px);
  z-index: 10;
}

.card-stripe {
  height: 7px; flex-shrink: 0;
  background: var(--border);
}
.stripe-blogs, .stripe-blog { background: #0a84ff; }
.stripe-podcasts, .stripe-podcast { background: #bf5af2; }
.stripe-videos, .stripe-video { background: #ff453a; }
.stripe-x, .stripe-post { background: #34c759; }
@media (prefers-color-scheme: dark) {
  .stripe-blogs, .stripe-blog { background: #2997ff; }
  .stripe-podcasts, .stripe-podcast { background: #bf5af2; }
  .stripe-videos, .stripe-video { background: #ff6961; }
  .stripe-x, .stripe-post { background: #30d158; }
}

.card-body { padding: 20px 20px 16px; flex: 1; display: flex; flex-direction: column; }

/* --- Avatar row --- */
.card-top { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
.avatar {
  width: 36px; height: 36px; border-radius: 50%;
  background: var(--ink); color: var(--surface);
  font-family: var(--mono); font-size: 11px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.card-who { min-width: 0; flex: 1; }
.card-name {
  font-size: 14px; font-weight: 600; line-height: 1.2;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.card-role {
  font-size: 12px; color: var(--ink-3);
  font-family: var(--text); letter-spacing: 0;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}

/* --- Badge --- */
.card-badge {
  font-size: 11px; font-weight: 600; letter-spacing: 0;
  padding: 4px 8px; border-radius: 999px;
  flex-shrink: 0; font-family: var(--text);
  background: rgba(0,0,0,0.05); color: var(--ink-2);
}
.badge-blogs, .badge-podcasts, .badge-videos, .badge-x { background: rgba(0,0,0,0.05); color: var(--ink-2); }
@media (prefers-color-scheme: dark) {
  .seg, .time-seg, .card-badge, .badge-blogs, .badge-podcasts, .badge-videos, .badge-x {
    background: rgba(255,255,255,0.10);
  }
}

/* --- Title (blogs/podcasts/videos only) --- */
.card-title {
  font-family: var(--sans);
  font-size: 18px; font-weight: 650; line-height: 1.24;
  margin-bottom: 10px; letter-spacing: 0;
}

/* --- Summary --- */
.card-summary {
  font-size: 14px; color: var(--ink-2); line-height: 1.5;
  flex: 1;
  word-break: break-word; overflow-wrap: anywhere;
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* --- Foot --- */
.card-foot {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 16px; padding-top: 12px;
  border-top: 1px solid var(--border);
}
.card-time { font-family: var(--mono); font-size: 11px; color: var(--ink-3); }
.card-link {
  font-size: 12px; font-weight: 600; color: var(--accent);
  display: flex; align-items: center; gap: 3px;
  transition: color .12s;
}
.card-link:hover { text-decoration: underline; text-underline-offset: 3px; }
.card-link-podcasts, .card-link-videos, .card-link-x { color: var(--accent); }

/* --- Empty state --- */
.empty {
  grid-column: 1 / -1;
  text-align: center; color: var(--ink-3);
  padding: 48px 24px;
  font-family: var(--text); font-size: 13px;
  letter-spacing: 0;
  background: var(--surface);
  border-radius: var(--radius);
}

/* --- Responsive hero --- */
@media (max-width: 640px) {
  .hero { padding: 36px 20px 28px; }
  .hero-divider { padding: 0 20px; }
  .content-layout { padding: 0 20px 56px; }
  .filter-groups { gap: 10px; }
  .page { padding: 0 20px 64px; }
}

footer.page-foot { display: none; }
"""

CLIENT_JS = r"""
<script>
(function () {
  const ranges = [
    { id: "3h", label: "3h", hours: 3 },
    { id: "6h", label: "6h", hours: 6 },
    { id: "12h", label: "12h", hours: 12 },
    { id: "24h", label: "24h", hours: 24 },
    { id: "3d", label: "3d", hours: 72 },
    { id: "7d", label: "7d", hours: 168 }
  ];
  const kinds = [
    ["blogs",    "Blogs & Long-form", "blogs"],
    ["podcasts",  "Podcasts",         "podcasts"],
    ["videos",    "Videos",           "videos"],
    ["posts",     "Posts",            "x"]
  ];
  let archiveItems = [];
  let latestEnd = null;
  const cacheKey = document.querySelector('meta[name="digest-generated"]')?.content || String(Date.now());

  function withCacheKey(path) {
    const glue = path.includes("?") ? "&" : "?";
    return path + glue + "v=" + encodeURIComponent(cacheKey);
  }

  function text(value) {
    return String(value || "");
  }

  function escapeHtml(value) {
    return text(value).replace(/[&<>"']/g, function (ch) {
      return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[ch];
    });
  }

  function stripHtml(value) {
    const el = document.createElement("div");
    el.innerHTML = text(value);
    return el.textContent || el.innerText || "";
  }

  function initials(name) {
    const parts = text(name).trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return "?";
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
  }

  function fmtTime(value) {
    if (!value) return "";
    const dt = new Date(value);
    if (Number.isNaN(dt.getTime())) return "";
    const pad = (n) => String(n).padStart(2, "0");
    let tz = "";
    try {
      const parts = new Intl.DateTimeFormat(undefined, { timeZoneName: "short" }).formatToParts(dt);
      const part = parts.find((p) => p.type === "timeZoneName");
      if (part && part.value) tz = " " + part.value;
    } catch (err) { /* ignore */ }
    return dt.getFullYear() + "-" + pad(dt.getMonth() + 1) + "-" + pad(dt.getDate()) + " " +
           pad(dt.getHours()) + ":" + pad(dt.getMinutes()) + ":" + pad(dt.getSeconds()) + tz;
  }

  function tag(kind) {
    return {x: "Post", blogs: "Blog", blog: "Blog", podcasts: "Podcast", podcast: "Podcast", videos: "Video", video: "Video"}[kind] || "Item";
  }

  function badgeClass(kind) {
    return "badge-" + ({
      x: "x", blogs: "blogs", blog: "blogs",
      podcasts: "podcasts", podcast: "podcasts",
      videos: "videos", video: "videos"
    }[kind] || "x");
  }

  function stripeClass(kind) {
    return "stripe-" + ({
      x: "x", blogs: "blogs", blog: "blogs",
      podcasts: "podcasts", podcast: "podcasts",
      videos: "videos", video: "videos"
    }[kind] || "x");
  }

  function linkClass(kind) {
    return "card-link-" + ({
      x: "x", blogs: "blogs", blog: "blogs",
      podcasts: "podcasts", podcast: "podcasts",
      videos: "videos", video: "videos"
    }[kind] || "x");
  }

  function card(item) {
    const name = item.source_name || item.author || "Unknown";
    const role = item.kind === "x" && item.source_handle
      ? "@" + item.source_handle + " · " + text(item.source_role)
      : text(item.source_role);
    const title = stripHtml(item.title);
    const summary = stripHtml(item.summary);
    const link = text(item.link);
    const titleBlock = item.kind !== "x" && title
      ? `<div class="card-title">${escapeHtml(title)}</div>`
      : "";
    const label = tag(item.kind);
    const linkLabel = {Blog: "Read article ↗", Podcast: "Listen ↗", Video: "Watch ↗", Post: "Open ↗"}[label] || "Open ↗";
    const openHtml = link
      ? `<a class="card-link ${linkClass(item.kind)}" href="${escapeHtml(link)}" target="_blank" rel="noreferrer noopener">${linkLabel}</a>`
      : "";
    return `<article class="card">
  <div class="card-stripe ${stripeClass(item.kind)}"></div>
  <div class="card-body">
    <div class="card-top">
      <div class="avatar">${escapeHtml(initials(name))}</div>
      <div class="card-who">
        <div class="card-name">${escapeHtml(name)}</div>
        <div class="card-role">${escapeHtml(role)}</div>
      </div>
      <span class="card-badge ${badgeClass(item.kind)}">${escapeHtml(label)}</span>
    </div>
    ${titleBlock}
    <div class="card-summary">${escapeHtml(summary)}</div>
    <div class="card-foot">
      <span class="card-time" data-iso="${escapeHtml(text(item.published))}">${escapeHtml(fmtTime(item.published))}</span>
      ${openHtml}
    </div>
  </div>
</article>`;
  }

  function sortDesc(items) {
    return items.slice().sort((a, b) => new Date(b.published || 0) - new Date(a.published || 0));
  }

  function canonicalLink(value) {
    const raw = text(value).trim();
    if (!raw) return "";
    try {
      const url = new URL(raw, location.href);
      Array.from(url.searchParams.keys()).forEach((key) => {
        if (key.toLowerCase().startsWith("utm_")) url.searchParams.delete(key);
      });
      url.hash = "";
      url.pathname = url.pathname.replace(/\/+$/, "");
      return (url.origin + url.pathname + url.search).toLowerCase();
    } catch (err) {
      return raw.toLowerCase();
    }
  }

  function keyFor(item) {
    const link = canonicalLink(item.link);
    if (link) return link;
    return [item.source_handle || "", item.summary || "", item.published || ""].join("|");
  }

  function filtered(hours) {
    if (!archiveItems.length || !latestEnd) return null;
    const cutoff = latestEnd.getTime() - hours * 60 * 60 * 1000;
    const seen = new Set();
    return sortDesc(archiveItems.filter((item) => {
      const dt = new Date(item.published || 0);
      if (Number.isNaN(dt.getTime()) || dt.getTime() < cutoff || dt.getTime() > latestEnd.getTime()) {
        return false;
      }
      const key = keyFor(item);
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    }));
  }

  function renderRange(rangeId) {
    const range = ranges.find((r) => r.id === rangeId) || ranges[3];
    const items = filtered(range.hours);
    if (!items) return;
    document.querySelectorAll(".time-seg button").forEach((button) => {
      button.classList.toggle("active", button.dataset.range === range.id);
    });
    const byKind = {};
    kinds.forEach(([, , kind]) => { byKind[kind] = []; });
    items.forEach((item) => {
      if (byKind[item.kind]) byKind[item.kind].push(item);
    });
    const sections = kinds.map(([slug, title, kind]) => {
      const rows = byKind[kind] || [];
      if (!rows.length) return "";
      return `<div class="section" id="${slug}"><div class="section-head"><h2>${escapeHtml(title)}</h2><span class="count">${String(rows.length).padStart(2, "0")} items</span></div><div class="grid">${rows.map(card).join("")}</div></div>`;
    }).join("");
    document.querySelector(".page").innerHTML = sections;
    document.querySelectorAll(".seg button").forEach(b => b.classList.remove("active"));
    const allBtn = document.querySelector(".seg button");
    if (allBtn) allBtn.classList.add("active");
  }

  async function loadArchive() {
    try {
      const indexResp = await fetch(withCacheKey("data/index.json"), { cache: "reload" });
      if (!indexResp.ok) throw new Error("missing index");
      const index = await indexResp.json();
      // Only fetch segments whose window_end is within the last 7d (168h).
      // This cuts the initial fetch from ~63 files down to ~28.
      const cutoff = new Date(Date.now() - 168 * 60 * 60 * 1000);
      const recentSegments = (index.segments || []).filter(function (s) {
        var t = new Date(s.window_end || 0);
        return !isNaN(t.getTime()) && t >= cutoff;
      });
      const segmentPaths = recentSegments.map(function (s) { return s.path; });
      const dailyPaths = (index.daily || []).map(function (d) { return d.path; }).slice(-7);
      const archivePaths = Array.from(new Set(dailyPaths.concat(segmentPaths)));
      if (!archivePaths.length) return;
      const payloads = await Promise.all(archivePaths.map(async function (path) {
        var resp = await fetch(withCacheKey(path), { cache: "reload" });
        if (!resp.ok) return null;
        return resp.json();
      }));
      archiveItems = [];
      payloads.filter(Boolean).forEach(function (payload) {
        var items = payload.items || {};
        Object.entries({x: "x", blogs: "blogs", podcasts: "podcasts", videos: "videos"}).forEach(function (entry) {
          var key = entry[0], kind = entry[1];
          (items[key] || []).forEach(function (item) { archiveItems.push(Object.assign({}, item, {kind: kind})); });
        });
      });
      var endValues = recentSegments.map(function (s) { return new Date(s.window_end || 0); }).filter(function (dt) { return !isNaN(dt.getTime()); });
      var itemValues = archiveItems.map(function (item) { return new Date(item.published || 0); }).filter(function (dt) { return !isNaN(dt.getTime()); });
      latestEnd = endValues.length
        ? new Date(Math.max.apply(null, endValues))
        : (itemValues.length ? new Date(Math.max.apply(null, itemValues)) : new Date());
      renderRange("24h");
    } catch (err) {
      // archive unavailable — showing server-rendered content only
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".time-seg button").forEach((button) => {
      button.addEventListener("click", () => renderRange(button.dataset.range));
    });
    document.querySelectorAll(".seg button").forEach((button) => {
      button.addEventListener("click", function () {
        document.querySelectorAll(".seg button").forEach(b => b.classList.remove("active"));
        this.classList.add("active");
        const kindLabel = this.textContent.trim();
        const mapping = {"Blogs": "blogs", "Podcasts": "podcasts", "Videos": "videos", "Posts": "posts"};
        const target = mapping[kindLabel];
        document.querySelectorAll(".section").forEach(s => {
          s.style.display = (!target || s.id === target) ? "" : "none";
        });
      });
    });
    loadArchive();
  });
})();
</script>
"""


def _initials(name: str) -> str:
    parts = [p for p in re.split(r"\s+", name.strip()) if p]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def _strip_html(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return text.strip()


def _coerce_utc(dt) -> datetime | None:
    if not dt:
        return None
    if isinstance(dt, str):
        text = dt.strip()
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(text)
        except ValueError:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _fmt_time(dt) -> str:
    coerced = _coerce_utc(dt)
    if not coerced:
        return ""
    return coerced.strftime("%Y-%m-%d %H:%M:%S UTC")


def _iso_time(dt) -> str:
    coerced = _coerce_utc(dt)
    if not coerced:
        return ""
    return coerced.isoformat()


def _card(item: dict) -> str:
    name = item.get("source_name") or item.get("author") or "Unknown"
    role = item.get("source_role", "")
    title = _strip_html(item.get("title", ""))
    summary = _strip_html(item.get("summary", ""))
    link = item.get("link", "")
    published = item.get("published")
    when = _fmt_time(published)
    iso = _iso_time(published)
    kind = item.get("kind", "")
    tag_label = {
        "x": "Post",
        "podcasts": "Podcast",
        "blogs": "Blog",
        "videos": "Video",
    }.get(kind, kind.title() or "Item")

    if kind == "x" and item.get("source_handle"):
        role_text = f'@{html.escape(item["source_handle"])} · {html.escape(role)}'
    else:
        role_text = html.escape(role)

    link_label = {
        "Blog": "Read article ↗",
        "Podcast": "Listen ↗",
        "Video": "Watch ↗",
        "Post": "Open ↗",
    }.get(tag_label, "Open ↗")

    open_link = (
        f'<a class="card-link card-link-{html.escape(kind)}" href="{html.escape(link)}" target="_blank" rel="noreferrer noopener">{link_label}</a>'
        if link else ""
    )

    title_block = (
        f'<div class="card-title">{html.escape(title)}</div>'
        if kind != "x" and title
        else ""
    )

    return f"""
<article class="card">
  <div class="card-stripe stripe-{html.escape(kind)}"></div>
  <div class="card-body">
    <div class="card-top">
      <div class="avatar">{html.escape(_initials(name))}</div>
      <div class="card-who">
        <div class="card-name">{html.escape(name)}</div>
        <div class="card-role">{role_text}</div>
      </div>
      <span class="card-badge badge-{html.escape(kind)}">{tag_label}</span>
    </div>
    {title_block}
    <div class="card-summary">{html.escape(summary)}</div>
    <div class="card-foot">
      <span class="card-time" data-iso="{html.escape(iso)}">{html.escape(when)}</span>
      {open_link}
    </div>
  </div>
</article>
""".strip()


def _latest_ai_brief_path() -> str:
    if not INSIGHT_INDEX.exists():
        return ""
    try:
        payload = json.loads(INSIGHT_INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""
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
    return "/" + path.lstrip("/")


def _ai_brief_links() -> str:
    path = _latest_ai_brief_path()
    if not path:
        return ""
    # Homepage: link to Insight root only. The standalone Insight site renders
    # the latest brief at / and keeps archived briefs under /archive/.
    # AI analysis pages are served from a dedicated subdomain and presented
    # as a separate homepage callout, not part of the title lockup.
    href = f"https://{AI_ANALYSIS_DOMAIN}/"
    return (
        '<!-- AI_BRIEFS_START -->'
        '<section class="insight-callout" aria-label="Latest AI insight">'
        f'<a class="insight-link" href="{html.escape(href)}" '
        'aria-label="Latest AI Insight, daily interpreted brief from the last 24 hours">'
        '<span class="insight-kicker">Analysis</span>'
        f'<span class="insight-title">{html.escape(AI_CARD_LABEL)}'
        '<span class="insight-arrow" aria-hidden="true">-&gt;</span></span>'
        '<span class="insight-note">Daily interpreted brief from the last 24 hours.</span>'
        '</a>'
        '</section>'
        '<!-- AI_BRIEFS_END -->'
    )


def render(
    x_items: list[dict],
    podcast_items: list[dict],
    blog_items: list[dict] | None = None,
    video_items: list[dict] | None = None,
    site: dict | None = None,
    interactive: bool = False,
) -> str:
    blog_items = blog_items or []
    video_items = video_items or []
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")  # used in meta tag

    sections_meta = [
        ("blogs",    "Blogs & Long-form", blog_items),
        ("podcasts", "Podcasts",          podcast_items),
        ("videos",   "Videos",             video_items),
        ("posts",    "Posts",              x_items),
    ]

    def _section(slug: str, title: str, items: list[dict]) -> str:
        if not items:
            return ""
        body = '<div class="grid">' + "\n".join(_card(i) for i in items) + "</div>"
        return (
            f'<div class="section" id="{slug}">'
            f'<div class="section-head"><h2>{html.escape(title)}</h2>'
            f'<span class="count">{len(items):02d} items</span></div>'
            f"{body}</div>"
        )

    sections = "".join(_section(s, t, items) for s, t, items in sections_meta)
    ai_brief_links = _ai_brief_links()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="digest-generated" content="{html.escape(generated)}" />
<title>Firsthand AI Digest</title>
<style>{CSS}</style>
</head>
<body>
<header class="hero">
  <h1><em>Firsthand</em> AI Digest</h1>
  <p class="lede">Posts, blogs, podcasts and videos from the people building AI &mdash; straight from the source.</p>
</header>
<div class="hero-divider"><hr /></div>
<div class="content-layout">
  <aside class="sidebar">
    {ai_brief_links}
    <div class="filter-groups">
      <div class="filter-group">
        <div class="filter-label">Time</div>
        <div class="time-seg" aria-label="Time range">
          <button type="button" data-range="3h">3h</button>
          <button type="button" data-range="6h">6h</button>
          <button type="button" data-range="12h">12h</button>
          <button class="active" type="button" data-range="24h">24h</button>
          <button type="button" data-range="3d">3d</button>
          <button type="button" data-range="7d">7d</button>
        </div>
      </div>
      <div class="filter-group">
        <div class="filter-label">Type</div>
        <div class="seg" aria-label="Content type">
          <button type="button" class="active">All</button>
          <button type="button">Blogs</button>
          <button type="button">Podcasts</button>
          <button type="button">Videos</button>
          <button type="button">Posts</button>
        </div>
      </div>
    </div>
  </aside>
  <div class="main-content">
    <div class="page">
      {sections}
    </div>
  </div>
</div>
<footer class="page-foot"></footer>
<script>
(function () {{
  function fmtLocal(iso) {{
    if (!iso) return "";
    var dt = new Date(iso);
    if (isNaN(dt.getTime())) return "";
    var pad = function (n) {{ return String(n).padStart(2, "0"); }};
    var tz = "";
    try {{
      var parts = new Intl.DateTimeFormat(undefined, {{ timeZoneName: "short" }}).formatToParts(dt);
      var part = parts.find(function (p) {{ return p.type === "timeZoneName"; }});
      if (part && part.value) tz = " " + part.value;
    }} catch (e) {{ /* ignore */ }}
    return dt.getFullYear() + "-" + pad(dt.getMonth() + 1) + "-" + pad(dt.getDate()) + " " +
           pad(dt.getHours()) + ":" + pad(dt.getMinutes()) + ":" + pad(dt.getSeconds()) + tz;
  }}
  function apply(root) {{
    (root || document).querySelectorAll(".card-time[data-iso]").forEach(function (el) {{
      var out = fmtLocal(el.getAttribute("data-iso"));
      if (out) el.textContent = out;
    }});
  }}
  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", function () {{ apply(); }});
  }} else {{
    apply();
  }}
  window.__applyLocalTime = apply;
}})();
</script>
{CLIENT_JS if interactive else ''}
</body>
</html>
"""
