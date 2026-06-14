# Firsthand AI Digest - 当前实现状态总结 (供其他 Agent 执行参考)

**最后更新**: 2026-06-05 (基于最新代码和部署)

## 1. 项目整体架构

- **主站 (Aggregator / 原始信号)**: `https://ai.prov1dence.top/`
  - 展示来自 X、Blogs、Podcasts、Videos 的第一手 (firsthand) 原始内容。
  - 左侧边栏：时间筛选 (Time) + 类型筛选 (Type) —— 两列布局。
  - 顶部 Hero：大标题 `<em>Firsthand</em> AI Digest`，右侧紧贴一个小标签链接 "insight"。
  - 内容区：分类卡片网格 (Blogs / Podcasts / Videos / Posts)，支持时间范围过滤 (3h/6h/.../7d) 和类型过滤。
  - 设计语言：Apple 风格，干净、系统字体、极简色彩、卡片带彩色顶条。

- **AI 分析/解读站 (Insight / 每日 AI 综合)**: `https://insight.ai.prov1dence.top/`
  - 使用**同一个 GitHub Pages 构建产物** (dist/)。
  - 通过 DNS 子域名指向同一份静态文件。
  - 主站上的 "insight" 链接直接跳到 `https://insight.ai.prov1dence.top/ai-briefs/2026-06-05-ai-brief.html` (最新一期英文版)。
  - AI Brief 页面本身支持中英文切换 (EN / 中文)，位于页面右上角固定 lang-switch。
  - 目前 insight 子域名根路径会显示和主站一样的聚合页面（可后续优化为自动跳最新解读或独立 landing）。

- **数据源**:
  - `data/ai-briefs/`：AI 解读 HTML（含最新英文 + 中文版）和 index.json。
  - `data/source-packs/`：Codex 生成 brief 前用的原始素材包（`ai-providence-source-pack-*.md` 等）。
  - `staging/ai-briefs/`：Codex 刚生成的 brief 草稿（gitignored，发布前临时存放）。
  - `data/daily/` + `data/segments/`：原始聚合数据。
  - `data/index.json`：前端加载用的索引。

## 2. 关键代码位置 & 配置（最重要！其他 Agent 改名时只改这里）

### 核心常量（改名只改这两个文件顶部）
- `scripts/render_html.py` (第 28-29 行)
- `scripts/publish_ai_brief.py` (第 33-34 行)

```python
AI_ANALYSIS_DOMAIN = "insight.ai.prov1dence.top"
AI_CARD_LABEL = "Latest AI Insight"
```

注释里列出了备选：
- insight.ai.prov1dence.top + "Latest AI Insight" (当前)
- brief.ai.prov1dence.top + "Latest AI Brief"
- lens.ai.prov1dence.top + "Latest AI Lens"
- pulse.ai.prov1dence.top + "Latest AI Pulse"
- distill.ai.prov1dence.top + "Latest AI Distill"
- synth.ai.prov1dence.top + "Latest AI Synth"

**改名流程**：
1. 只修改上面两个常量的值。
2. 运行 `python scripts/run.py --mock-data --output dist/index.html` 重新生成本地预览（可选）。
3. `git add scripts/ && git commit && git push`
4. GitHub Actions 会自动用 `archive_data.py` 重新构建 `dist/` 并部署。

### 前端布局实现 (render_html.py)
- Hero 标题右侧直接内联 `<a class="insight-link" href="...">insight</a>`
- `.hero h1 { display: flex; align-items: baseline; justify-content: space-between; }`
- 左侧 `.sidebar` 只剩 `.filter-groups` (grid 两列：Time + Type)
- 移除了原来 sidebar 里的完整 AI 卡片（现在入口在标题右边，更空的地方被利用）
- `insight-link` 样式：小 pill 标签、accent 色、hover 效果，响应式（移动端会 wrap）
- AI 链接永远只指向**最新一期英文版**（首页不暴露历史、不显示日期、不显示 EN 标签）

### 其他需要同步更新的地方（如果改名）
- `dist/index.html`（本地预览 / 构建产物，下次部署会覆盖）
- `designs/preview-design-e.html` 和 `designs/design-*.html`（demo 里的文案，JS 硬编码）

## 3. 当前 UI 状态（生产已部署）

- 首页 Hero 标题右边：小标签 "insight"（超链接，无 "EN"、无日期、无 "Latest AI Insight" 前缀）。
- 左侧边栏：干净的两列筛选器（Time 纵向 + Type 纵向）。
- 点击 "insight" 直接跳 `insight.ai.prov1dence.top` 上的最新 AI Brief。
- AI Brief 页面（子域名下）保留原有中英文切换。
- 设计理由（用户问过）：标题右边空间被有效利用；两个产品（Firsthand 聚合 + Insight 解读）在视觉上并列但有主次；sidebar 专注过滤；小标签现代、轻量、不抢标题风头。

## 4. 构建 & 部署流程

- GitHub Actions：
  - `pages.yml`：push main 触发 → `python scripts/archive_data.py --render-hours 24` → 上传 `dist/` 作为 Pages artifact。
  - `daily.yml`：定时抓数据（每 6 小时）。
- 本地构建：`python scripts/run.py --mock-data --output dist/index.html`
- `dist/` 是构建输出（已在 `.gitignore`）。
- 每次部署会复制 root `CNAME`（ai.prov1dence.top）到 `dist/CNAME`。

## 5. DNS & 子域名现状

- 主域名：`ai.prov1dence.top` (CNAME ai → chr1sc2y.github.io)
- AI 子域名：`insight.ai.prov1dence.top` (CNAME insight → chr1sc2y.github.io)
- 用户已手动在 DNS 提供商配置完成（权重 1，TTL 10min）。
- GitHub Pages 同一个站点通过不同域名访问，内容完全一样。
- **重要**：GitHub Pages 自定义域名设置里目前只填了 `ai.prov1dence.top`。子域名 `insight.*` 靠 DNS 指向即可访问，但 HTTPS 证书可能需要：
  - 临时在 GitHub Settings → Pages 把 Custom domain 改成 `insight.ai.prov1dence.top` 等证书颁发，再切回。
  - 或等第一次访问触发。

## 6. 本地测试文件

- `dist/index.html`：当前生产布局的完整可直接双击打开的预览。
- `designs/preview-design-e.html`：早期 design-e 静态 demo（已同步文案）。
- 打开 `dist/index.html` 就能看到最新 "insight" 放在标题右边的效果。

## 7. 已知待办 / 可以让其他 Agent 执行的事项

1. **DNS / HTTPS 收尾**（如果还没生效）：
   - 确认 `dig insight.ai.prov1dence.top` 返回正确。
   - 测试 https 访问子域名下的具体 brief。
   - 如 HTTPS 报错，按上面第 5 节临时切换 custom domain 触发证书。

2. **子域名根路径体验优化**（可选但推荐）：
   - 目前 `insight.ai.prov1dence.top/` 根路径还是显示主站聚合页。
   - 可以让它自动跳转最新 brief，或放一个极简的 "AI Daily Interpretation" landing（只展示最新 Executive Summary + 链接到全文）。
   - 实现方式：在 `archive_data.py` 末尾或新增脚本，根据 `data/ai-briefs/index.json` 复制/生成一个 `dist/index-for-insight.html` 或用重定向。

3. **AI Brief 页面自身优化**（如果需要）：
   - 当前 brief HTML 是外部生成的（`data/ai-briefs/*.html`），标题仍是 "Firsthand AI Brief"。
   - 可在生成 brief 时把 <title> 和 hero 里的文案也带上 "Insight" 品牌，或加返回主站链接。

4. **名字切换支持**：
   - 所有名字相关逻辑已集中到两个常量 + 注释列表。
   - 改完只需推代码，CI 自动更新生产 + 预览。
   - 如果以后想支持运行时切换（极少见），可以把常量移到 config。

5. **文档更新**：
   - `docs/operations.md` 里的 custom domain 章节只写了主域名，可补充子域名说明。
   - `docs/architecture.md` 可加一句 "AI interpretation 走独立子域名 insight.* 以区分品牌"。

6. **测试**：
   - `pytest` 全部通过。
   - 手动验证：时间/类型过滤、insight 链接正确、移动端布局（sidebar 堆叠 + hero 换行）、无日期/EN 出现在首页卡片。

## 8. 快速命令

```bash
# 本地预览最新布局
python scripts/run.py --mock-data --output dist/index.html
open dist/index.html

# 完整构建（会更新 data/ + dist/）
python scripts/archive_data.py --render-hours 24

# 运行测试
pytest

# 查看当前常量
grep -A2 "AI_ANALYSIS_DOMAIN" scripts/render_html.py scripts/publish_ai_brief.py
```

## 9. 给其他 Agent 的执行提示

- **不要** 直接硬编码 "insight" 或域名到 HTML/JS/CSS 里（除了演示文件）。
- 所有生产逻辑必须走 `AI_ANALYSIS_DOMAIN` + `AI_CARD_LABEL` 常量。
- 改动后必须重新生成 `dist/index.html` 给用户本地验证。
- 涉及 DNS 的任务要提醒用户检查 `dig` 和 HTTPS。
- 如果用户说 "换成 xxx"，直接改常量 + 提交 + 说明 DNS 也要对应改（如果 subdomain 变了）。

当前状态：代码已收敛、UI 已按最后需求调整（insight 放标题右边、只显示 "insight" 超链接）、部署已推、生产可访问（DNS 生效后完整可用）。

需要我继续执行哪个具体任务（DNS 验证、子域名根路径优化、文档补全等），直接说。