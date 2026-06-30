# Firsthand AI Digest Source Pack

- Generated: 2026-06-30T08:15:20+08:00
- Intended coverage window: 2026-06-29T08:15:20+08:00 to 2026-06-30T08:15:20+08:00
- Index site: https://ai.prov1dence.top/
- Firsthand AI Digest items in window: 35
- Detail pages fetched: 0
- First-layer original sources fetched/listed: 35
- Original sources with fetched page text: 3
- Metadata-only original sources: 31
- Other limited original sources: 1
- Secondary source candidates fetched/listed: 10

This is a collection aid, not the final analysis. Open primary sources directly before writing final claims.

## Index Page

- URL: https://ai.prov1dence.top/
- Title: Firsthand AI Digest
- Links:
  - https://insight.ai.prov1dence.top/ - Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours.
  - https://simonwillison.net/2026/Jun/29/safari-tab-count/ - Read article ↗
  - https://simonwillison.net/2026/Jun/29/ornith/ - Read article ↗
  - https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/ - Read article ↗
  - https://openai.com/index/mapping-ai-jobs-transition-eu - Read article ↗
  - https://www.youtube.com/watch?v=sNiXjgojxko - Watch ↗
  - https://www.youtube.com/watch?v=f-HiB82Tl94 - Watch ↗
  - https://www.youtube.com/watch?v=GZT_oNQnLV4 - Watch ↗
  - https://x.com/thsottiaux/status/2071710834527523030 - Open ↗
  - https://x.com/rauchg/status/2071710688150528443 - Open ↗
  - https://x.com/swyx/status/2071692683182252317 - Open ↗
  - https://x.com/petergyang/status/2071690793899974773 - Open ↗
  - https://x.com/elonmusk/status/2071673460779041155 - Open ↗
  - https://x.com/xai/status/2071661034683969977 - Open ↗
  - https://x.com/claudeai/status/2071653958905467027 - Open ↗
  - https://x.com/rauchg/status/2071653061748035994 - Open ↗
  - https://x.com/ryolu_/status/2071652629890088964 - Open ↗
  - https://x.com/elonmusk/status/2071652181854343349 - Open ↗
  - https://x.com/elonmusk/status/2071651728202543557 - Open ↗
  - https://x.com/petergyang/status/2071651376959291512 - Open ↗

Excerpt:

Firsthand AI Digest Firsthand AI Digest Posts, blogs, podcasts and videos from the people building AI — straight from the source. Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours. Time 3h 6h 12h 24h 3d 7d Type All Blogs Podcasts Videos Posts Blogs & Long-form 04 items SW Simon Willison By Simon Willison Blog Count the number of Safari tabs Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari: osascript -e 'tell application "Safari" to count tabs of every window' Tags: safari, til, applescript 2026-06-29 18:36:18 UTC Read article ↗ SW Simon Willison By Simon Willison Blog Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce. [...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. As far as I can tell the licenses of those underlying models is compatible with being used in this way - Gemma 4 is Apache 2.0 licensed (and not bound by the janky additional Gemma Terms of Use that afflicted the previous Gemma models) and Qwen 3.5 is Apache 2.0 licensed as well. I've been running the model using LM Studio and the ornith-1.0-35b-Q4_K_M.gguf (20GB) GGUF, hooked up to Pi. Initial impressions are very good - it seems to be able to run the agent harness over many tool calls in a proficient way. Here's a terminal session where I asked it to "find the code that decodes the actor cookie" and then "find the code that opens the insert dialog when thebutton is clicked" against a Datasette checkout, which it handled with ease. I also had it draw this pelican, which came out at 103 tokens/second: It's a little bit mangled but the pelican is clearly a pelican. I couldn't find much information about DeepReinforce themselves. The earliest paper I could find from the was CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning from June 2025. Tags: ai, generative-ai, local-llms, llms, qwen, pelican-riding-a-bicycle, gemma, llm-release, lm-studio 2026-06-29 16:17:59 UTC Read article ↗ IC Import AI (Jack Clark) By Jack Clark Blog Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era Welcome to Import AI, a newsletter about AI researc

## Firsthand AI Digest Items In Window

### 1. Count the number of Safari tabs

- URL: https://simonwillison.net/2026/Jun/29/safari-tab-count/
- Type: Blog
- Published: 2026-06-29T18:36:18+00:00
- Digest summary: Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari: osascript -e 'tell application "Safari" to count tabs of every window' Tags: safari, til, applescript

### 2. Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding

- URL: https://simonwillison.net/2026/Jun/29/ornith/
- Type: Blog
- Published: 2026-06-29T16:17:59+00:00
- Digest summary: Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce. [...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. As far as I can tell the licenses of those underlying models is compatible with being used in this way - Gemma 4 is Apache 2.0 licensed (and not bound by the janky additional Gemma Terms of Use that afflicted the previous Gemma models) and Qwen 3.5 is Apache 2.0 licensed as well. I've been running the model using LM Studio and the ornith-1.0-35b-Q4_K_M.gguf (20GB) GGUF, hooked up to Pi. Initial impressions a

### 3. Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era

- URL: https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/
- Type: Blog
- Published: 2026-06-29T13:03:27+00:00
- Digest summary: Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers. If you’d like to support this, please subscribe. Subscribe now NVIDIA sets up a crude self-improvement loop for real world robotics:…What if you could take the best ideas from AI agents and put them into the […]

### 4. Mapping Europe’s AI Workforce Opportunity

- URL: https://openai.com/index/mapping-ai-jobs-transition-eu
- Type: Blog
- Published: 2026-06-29T07:00:00+00:00
- Digest summary: A new OpenAI report maps how AI could reshape jobs across the EU, highlighting which occupations may face automation, growth, or workflow changes.

### 5. How Church Wealth Made Corruption Inevitable – Ada Palmer

- URL: https://www.youtube.com/watch?v=sNiXjgojxko
- Type: Video
- Published: 2026-06-29T17:15:08+00:00
- Digest summary: Full episode: https://www.youtube.com/watch?v=U1FrhkLQnCI Me on twitter: https://x.com/dwarkesh_sp

### 6. Advent Accelerates Deals with ChatGPT + Codex

- URL: https://www.youtube.com/watch?v=f-HiB82Tl94
- Type: Video
- Published: 2026-06-29T14:30:09+00:00
- Digest summary: ChatGPT + Codex are a one-two punch for investment firms. "Having the ability to connect your deal folder with all of the context, and then be able to ask ChatGPT and Codex real time questions has been really impactful to our workflows," - Jasmine Azizi (Advent). Financial firms hold a tremendous amount of context. ChatGPT acts like a brain layer so teams can spend more time focusing on the next big bet.

### 7. Training Agents 2: Live tutorial on model distillation for training custom agents.

- URL: https://www.youtube.com/watch?v=GZT_oNQnLV4
- Type: Video
- Published: 2026-06-29T09:00:36+00:00
- Digest summary: In this live session, we'll cover how to transfer capability from a teacher model to a smaller student through distillation. We'll work through supervised fine-tuning on teacher-generated data, then on-policy and online methods where the teacher scores the student live, then self-distillation where the model teaches itself. Each one runs in TRL. What we'll cover: - What distillation is, and the four axes that organize it: signal, data source, timing, and teacher identity - White-box vs black-box: distilling from open weights vs strings - Off-policy distillation: generate from the teacher, then SFT on the outputs - On-policy distillation: sample from the student, score with the teacher in the loop - Distillation as reinforcement learning: the KD distance as a dense, token-level reward - Sel

### 8. https://x.com/thsottiaux/status/2071710834527523030

- URL: https://x.com/thsottiaux/status/2071710834527523030
- Type: Post
- Published: 2026-06-29T21:42:08+00:00
- Digest summary: Do you think it has a reset button?

### 9. https://x.com/rauchg/status/2071710688150528443

- URL: https://x.com/rauchg/status/2071710688150528443
- Type: Post
- Published: 2026-06-29T21:41:33+00:00
- Digest summary: curl -sN https://t.co/ovyIAaG8Ix by @_brian_zhang https://t.co/7gLjZevUM5

### 10. https://x.com/swyx/status/2071692683182252317

- URL: https://x.com/swyx/status/2071692683182252317
- Type: Post
- Published: 2026-06-29T20:30:00+00:00
- Digest summary: prescribe one (1) pill when a coworker disrespects scaling laws make a beeline 4pm sharp at aie expo, first come first served https://t.co/NlIx6EBB3E

### 11. https://x.com/petergyang/status/2071690793899974773

- URL: https://x.com/petergyang/status/2071690793899974773
- Type: Post
- Published: 2026-06-29T20:22:30+00:00
- Digest summary: How Anthropic product lead @jess__yan uses AI agents internally across 5 workflows: 1. Understand the codebase Instead of asking engineers what shipped or how something works, Jess can inspect pull requests, deployments, and product architecture directly. “Access to our codebase has been the biggest unlock for me.” 2. Synthesize customer feedback Jess has agents monitor customer Slack channels to get more signal before deciding what to build next. 3. Get briefed before meetings Jess uses agents to prep before customer conversations, pitches, and internal discussions. This helps her show up with baseline research done and a clearer opinion. 4. Pressure-test product & API decisions Jess has an API review agent in Slack that helps the team improve API design and spot when their biases are get

### 12. https://x.com/elonmusk/status/2071673460779041155

- URL: https://x.com/elonmusk/status/2071673460779041155
- Type: Post
- Published: 2026-06-29T19:13:37+00:00
- Digest summary: Deaths in Africa DECREASED after USAID funding was cut, because they’re no longer able to push for violent revolution to install leftist regimes!

### 13. https://x.com/xai/status/2071661034683969977

- URL: https://x.com/xai/status/2071661034683969977
- Type: Post
- Published: 2026-06-29T18:24:14+00:00
- Digest summary: State of the art voice APIs from SpaceXAI, now in the Vercel AI Gateway

### 14. https://x.com/claudeai/status/2071653958905467027

- URL: https://x.com/claudeai/status/2071653958905467027
- Type: Post
- Published: 2026-06-29T17:56:07+00:00
- Digest summary: Claude in Microsoft Foundry is now generally available, hosted on Azure. Azure customers get Claude Opus 4.8 and Claude Haiku 4.5, with Azure authentication, billing, and commitment retirement. https://t.co/4Rz7fa9Bxm

### 15. https://x.com/rauchg/status/2071653061748035994

- URL: https://x.com/rauchg/status/2071653061748035994
- Type: Post
- Published: 2026-06-29T17:52:34+00:00
- Digest summary: Massive performance and memory usage improvements in @nextjs. Turbopack’s bet on the filesystem cache pays off greatly in a world of agents hammering 𝚗𝚎𝚡𝚝 𝚋𝚞𝚒𝚕𝚍.

### 16. https://x.com/ryolu_/status/2071652629890088964

- URL: https://x.com/ryolu_/status/2071652629890088964
- Type: Post
- Published: 2026-06-29T17:50:51+00:00
- Digest summary: wherever ideas hit. desks and laptops optional.

### 17. https://x.com/elonmusk/status/2071652181854343349

- URL: https://x.com/elonmusk/status/2071652181854343349
- Type: Post
- Published: 2026-06-29T17:49:04+00:00
- Digest summary: It’s total bullshit! Deaths in Africa DECREASED after cutting USAID funding, which they were using to push for violent overthrow of governments!!

### 18. https://x.com/elonmusk/status/2071651728202543557

- URL: https://x.com/elonmusk/status/2071651728202543557
- Type: Post
- Published: 2026-06-29T17:47:16+00:00
- Digest summary: I love optimizing machines It’s like a beautiful puzzle That also achieves true usefulness

### 19. https://x.com/petergyang/status/2071651376959291512

- URL: https://x.com/petergyang/status/2071651376959291512
- Type: Post
- Published: 2026-06-29T17:45:52+00:00
- Digest summary: I think I might stop using @telegram if these BS spam msgs don't get blocked by default. Doesn't make sense you have to pay a subscription to reduce spam and not let randos DM you. https://t.co/Dl53wWU5kl

### 20. https://x.com/elonmusk/status/2071650759330906253

- URL: https://x.com/elonmusk/status/2071650759330906253
- Type: Post
- Published: 2026-06-29T17:43:25+00:00
- Digest summary: Cursor for iOS!

### 21. https://x.com/thsottiaux/status/2071636285807059315

- URL: https://x.com/thsottiaux/status/2071636285807059315
- Type: Post
- Published: 2026-06-29T16:45:54+00:00
- Digest summary: Advanced Codex users. We shipped a replacement to coarse sandbox modes: reusable, inheritable permission profiles binding OS-enforced file read/write/deny rules (even **/*.env) to per-domain network + Unix sockets. Plus fail-closed admin allowlists. Least privilege per task. https://t.co/jHyAnUhyFs

### 22. https://x.com/elonmusk/status/2071623241668444308

- URL: https://x.com/elonmusk/status/2071623241668444308
- Type: Post
- Published: 2026-06-29T15:54:04+00:00
- Digest summary: True

### 23. https://x.com/rauchg/status/2071621345151009184

- URL: https://x.com/rauchg/status/2071621345151009184
- Type: Post
- Published: 2026-06-29T15:46:32+00:00
- Digest summary: Voice agents now on Vercel

### 24. https://x.com/elonmusk/status/2071615220326220158

- URL: https://x.com/elonmusk/status/2071615220326220158
- Type: Post
- Published: 2026-06-29T15:22:11+00:00
- Digest summary: The hard truth is that USAID, with its constant support of often violent leftist regime change, caused a lot of death!

### 25. https://x.com/elonmusk/status/2071613438019666143

- URL: https://x.com/elonmusk/status/2071613438019666143
- Type: Post
- Published: 2026-06-29T15:15:06+00:00
- Digest summary: Yup

### 26. https://x.com/swyx/status/2071613383380770823

- URL: https://x.com/swyx/status/2071613383380770823
- Type: Post
- Published: 2026-06-29T15:14:53+00:00
- Digest summary: AIE workshop day https://t.co/VUGtbG30dB

### 27. https://x.com/rauchg/status/2071612651684106518

- URL: https://x.com/rauchg/status/2071612651684106518
- Type: Post
- Published: 2026-06-29T15:11:59+00:00
- Digest summary: So excited for the @vercel ships this week… some would say a decade in the making. any guesses? https://t.co/zL0V3vXV1N

### 28. https://x.com/elonmusk/status/2071612046894936136

- URL: https://x.com/elonmusk/status/2071612046894936136
- Type: Post
- Published: 2026-06-29T15:09:35+00:00
- Digest summary: Correct

### 29. https://x.com/petergyang/status/2071606799791436242

- URL: https://x.com/petergyang/status/2071606799791436242
- Type: Post
- Published: 2026-06-29T14:48:44+00:00
- Digest summary: Winning in AI isn't just about building the best models. You also need to scale the energy grid and data centers. It'll be sad if we have the best models but don't have the infrastructure to serve them.

### 30. https://x.com/elonmusk/status/2071606142753542409

- URL: https://x.com/elonmusk/status/2071606142753542409
- Type: Post
- Published: 2026-06-29T14:46:07+00:00
- Digest summary: Interesting

### 31. https://x.com/petergyang/status/2071594744283902091

- URL: https://x.com/petergyang/status/2071594744283902091
- Type: Post
- Published: 2026-06-29T14:00:50+00:00
- Digest summary: This reminds me of the electric car race where China is making great cars at a fraction of the price and now dominates the global EV market.

### 32. https://x.com/swyx/status/2071478390172049555

- URL: https://x.com/swyx/status/2071478390172049555
- Type: Post
- Published: 2026-06-29T06:18:29+00:00
- Digest summary: because i'm not a design engineer myself, this track is one of the harder ones I struggle to curate. very fortunate to befriend Geoff who has lent a hand to the past 2 years of AI UX meetups, and now is the opener for the Design Engineers at AIE! see you wednesday https://t.co/TrqetNnJQB

### 33. https://x.com/gdb/status/2071453977091477911

- URL: https://x.com/gdb/status/2071453977091477911
- Type: Post
- Published: 2026-06-29T04:41:28+00:00
- Digest summary: Sol & Daybreak https://t.co/FK8Bj17O8i

### 34. https://x.com/elonmusk/status/2071420290702127225

- URL: https://x.com/elonmusk/status/2071420290702127225
- Type: Post
- Published: 2026-06-29T02:27:37+00:00
- Digest summary: Interesting

### 35. https://x.com/elonmusk/status/2071420142756548901

- URL: https://x.com/elonmusk/status/2071420142756548901
- Type: Post
- Published: 2026-06-29T02:27:01+00:00
- Digest summary: Extremely troubling

## Firsthand AI Digest Detail Pages

## Original Sources

### 1. Count the number of Safari tabs

- Type: web
- URL: https://simonwillison.net/2026/Jun/29/safari-tab-count/
- Title: Count the number of Safari tabs
- Description: Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari: osascript -e 'tell application "Safari" to count tabs of every window'
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://10xn.link/simon-depot - Try Depot CI
  - https://simonwillison.net/2026/Jun/29/ - 29th June 2026
  - https://simonwillison.net/2026/Jun/22/porting-moebius/ - Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
  - https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/ - sqlite-utils 4.0rc1 adds migrations and nested transactions
  - https://simonwillison.net/2026/Jun/18/datasette-apps/ - Datasette Apps: Host custom HTML applications inside Datasette
  - https://simonwillison.net/tags/safari/ - safari 69
  - https://simonwillison.net/tags/til/ - til 26
  - https://simonwillison.net/tags/applescript/ - applescript 9
  - https://github.com/sponsors/simonw/ - Sponsor & subscribe
  - https://simonwillison.net/2002/ - 2002
  - https://simonwillison.net/2003/ - 2003
  - https://simonwillison.net/2004/ - 2004
  - https://simonwillison.net/2005/ - 2005
  - https://simonwillison.net/2006/ - 2006
  - https://simonwillison.net/2007/ - 2007
  - https://simonwillison.net/2008/ - 2008
  - https://simonwillison.net/2009/ - 2009
  - https://simonwillison.net/2010/ - 2010

Excerpt:

Count the number of Safari tabs Simon Willison’s Weblog Subscribe Sponsored by: Depot — AI agents write code in seconds. CI shouldn't make them wait minutes. Try Depot CI 29th June 2026 Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari: osascript -e 'tell application "Safari" to count tabs of every window' Posted 29th June 2026 at 6:36 pm Recent articles Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code - 22nd June 2026 sqlite-utils 4.0rc1 adds migrations and nested transactions - 21st June 2026 Datasette Apps: Host custom HTML applications inside Datasette - 18th June 2026 This is a note by Simon Willison, posted on 29th June 2026 . safari 69 til 26 applescript 9 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 2. Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding

- Type: web
- URL: https://simonwillison.net/2026/Jun/29/ornith/
- Title: Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding
- Description: This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce. [...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://10xn.link/simon-depot - Try Depot CI
  - https://deep-reinforce.com/ornith_1_0.html - Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding
  - https://ai.google.dev/gemma/terms - Gemma Terms of Use
  - https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF - ornith-1.0-35b-Q4_K_M.gguf
  - https://pi.dev/ - Pi
  - https://gisthost.github.io/?35da4d9ce7f0c27124c67655a0dc9e5d - a terminal session
  - https://gist.github.com/simonw/1869e1bbcafe5bcad0f26351f6a978a6 - draw this pelican
  - https://arxiv.org/abs/2507.14111 - CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning
  - https://simonwillison.net/2026/Jun/29/ - 29th June 2026
  - https://simonwillison.net/2026/Jun/22/porting-moebius/ - Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
  - https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/ - sqlite-utils 4.0rc1 adds migrations and nested transactions
  - https://simonwillison.net/2026/Jun/18/datasette-apps/ - Datasette Apps: Host custom HTML applications inside Datasette
  - https://simonwillison.net/tags/ai/ - ai 2,090
  - https://simonwillison.net/tags/generative-ai/ - generative-ai 1,847
  - https://simonwillison.net/tags/local-llms/ - local-llms 159
  - https://simonwillison.net/tags/llms/ - llms 1,815
  - https://simonwillison.net/tags/qwen/ - qwen 57
  - https://simonwillison.net/tags/pelican-riding-a-bicycle/ - pelican-riding-a-bicycle 120

Excerpt:

Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding Simon Willison’s Weblog Subscribe Sponsored by: Depot — AI agents write code in seconds. CI shouldn't make them wait minutes. Try Depot CI 29th June 2026 - Link Blog Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding . This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce. [...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. As far as I can tell the licenses of those underlying models is compatible with being used in this way - Gemma 4 is Apache 2.0 licensed (and not bound by the janky additional Gemma Terms of Use that afflicted the previous Gemma models) and Qwen 3.5 is Apache 2.0 licensed as well. I've been running the model using LM Studio and the ornith-1.0-35b-Q4_K_M.gguf (20GB) GGUF, hooked up to Pi . Initial impressions are very good - it seems to be able to run the agent harness over many tool calls in a proficient way. Here's a terminal session where I asked it to "find the code that decodes the actor cookie" and then "find the code that opens the insert dialog when thebutton is clicked" against a Datasette checkout, which it handled with ease. I also had it draw this pelican , which came out at 103 tokens/second: It's a little bit mangled but the pelican is clearly a pelican. I couldn't find much information about DeepReinforce themselves. The earliest paper I could find from the was CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning from June 2025. Posted 29th June 2026 at 4:17 pm Recent articles Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code - 22nd June 2026 sqlite-utils 4.0rc1 adds migrations and nested transactions - 21st June 2026 Datasette Apps: Host custom HTML applications inside Datasette - 18th June 2026 This is a link post by Simon Willison, posted on 29th June 2026 . ai 2,090 generative-ai 1,847 local-llms 159 llms 1,815 qwen 57 pelican-riding-a-bicycle 120 gemma 16 llm-release 208 lm-studio 20 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024

### 3. Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era

- Type: web
- URL: https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/
- Title: Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era
- Published: 2026-06-29T13:03:27+00:00
- Description: Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers. If you’d like to support this, please subscribe. Subscribe now NVIDIA sets up a crude self-improvement loop for real world robotics:…What if you could take the best ideas from AI agents and put them into the…
- Links:
  - https://jack-clark.net/ - Import AI
  - https://jack-clark.net/about/ - About
  - https://jack-clark.net/thinking/ - Work
  - https://importai.substack.com/subscribe - Subscribe now
  - https://research.nvidia.com/labs/gear/enpire/ - ENPIRE: Agentic Robot Policy Self-Improvement in the Real World (NVIDIA research website)
  - https://arxiv.org/abs/2606.19980 - ENPIRE: Agentic Robot Policy Self-Improvement in the Real World (arXiv)
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6875838 - Artificial Intelligence and the Lessons of History (SSRN)
  - https://arxiv.org/abs/2606.20374 - ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters (arXiv)
  - https://borretti.me/fiction/julia - whose work
  - https://borretti.me/fiction/eog581 - you should read
  - https://borretti.me/article/no-one-escapes-the-permanent-underclass - No-One Escapes the Permanent Underclass (Fernando Borretti, blog)
  - https://arxiv.org/abs/2606.19334 - Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States (arXiv)
  - https://huggingface.co/datasets/LocalLaws/LOCUS-v1 - LocalLaws / LOCUS-v1 (HuggingFace)
  - https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/?share=facebook - Share on Facebook (Opens in new window) Facebook
  - https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/?share=twitter - Share on X (Opens in new window) X
  - https://jack-clark.net/2026/06/29/ - June 29, 2026
  - https://jack-clark.net/category/uncategorized/ - Uncategorized
  - https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/ - Cancel reply
  - https://jack-clark.net/2026/06/22/import-ai-462-superpersuasion-self-sustaining-ai-paths-to-asi/ - « Previous Post
  - https://wordpress.com/?ref=footer_custom_svg

Excerpt:

Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era | Import AI Import AI About Work Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era by Jack Clark Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers. If you’d like to support this, please subscribe. Subscribe now NVIDIA sets up a crude self-improvement loop for real world robotics: …What if you could take the best ideas from AI agents and put them into the real world?… Researchers with NVIDIA have developed ENPIRE, software to get physical robotics to go through the same kind of autonomous experimentation and execution loop that AI agents go through. The research gives us a taste of what it might look like for a superintelligence to attempt to use robots to instantiate itself in the physical world – though as with all things in robotics, the current examples are suggestive at best. What ENPIRE is: The software is “a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with single or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes”. ENPIRE works the same way that coding agents work – a scaffold supervises some physical robots which are asked to complete tasks. The robots try to complete the tasks and attempt different strategies for completing stuff, trying and failing and learning. The system both evaluates their success and also resets itself when they fail. “This closed-loop system transforms real-world robot learning into a controllable optimization procedure that agents can manage, thus minimizing human effort while allowing fair ablations across training recipes and agent variants.” Two of the key ingredients for making this work are an automatic evaluation system to help score “the outcome of each trial without human judgement”, as well as an automatic reset system which “returns the scene to a fresh initial state for the next trial”. (Both of these are tasks which have historically required lots of human effort, and it’s likely that more complicat

### 4. https://openai.com/index/mapping-ai-jobs-transition-eu

- Type: official/blog
- URL: https://openai.com/index/mapping-ai-jobs-transition-eu
- Fetch status: limited (HTTP 403: Forbidden)

### 5. How Church Wealth Made Corruption Inevitable – Ada Palmer

- Type: video
- URL: https://www.youtube.com/watch?v=sNiXjgojxko
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 6. Advent Accelerates Deals with ChatGPT + Codex

- Type: video
- URL: https://www.youtube.com/watch?v=f-HiB82Tl94
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 7. Training Agents 2: Live tutorial on model distillation for training custom agents.

- Type: video
- URL: https://www.youtube.com/watch?v=GZT_oNQnLV4
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 8. https://x.com/thsottiaux/status/2071710834527523030

- Type: x-post
- URL: https://x.com/thsottiaux/status/2071710834527523030
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 9. https://x.com/rauchg/status/2071710688150528443

- Type: x-post
- URL: https://x.com/rauchg/status/2071710688150528443
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 10. https://x.com/swyx/status/2071692683182252317

- Type: x-post
- URL: https://x.com/swyx/status/2071692683182252317
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 11. https://x.com/petergyang/status/2071690793899974773

- Type: x-post
- URL: https://x.com/petergyang/status/2071690793899974773
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 12. https://x.com/elonmusk/status/2071673460779041155

- Type: x-post
- URL: https://x.com/elonmusk/status/2071673460779041155
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 13. https://x.com/xai/status/2071661034683969977

- Type: x-post
- URL: https://x.com/xai/status/2071661034683969977
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 14. https://x.com/claudeai/status/2071653958905467027

- Type: x-post
- URL: https://x.com/claudeai/status/2071653958905467027
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 15. https://x.com/rauchg/status/2071653061748035994

- Type: x-post
- URL: https://x.com/rauchg/status/2071653061748035994
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 16. https://x.com/ryolu_/status/2071652629890088964

- Type: x-post
- URL: https://x.com/ryolu_/status/2071652629890088964
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 17. https://x.com/elonmusk/status/2071652181854343349

- Type: x-post
- URL: https://x.com/elonmusk/status/2071652181854343349
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 18. https://x.com/elonmusk/status/2071651728202543557

- Type: x-post
- URL: https://x.com/elonmusk/status/2071651728202543557
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 19. https://x.com/petergyang/status/2071651376959291512

- Type: x-post
- URL: https://x.com/petergyang/status/2071651376959291512
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 20. https://x.com/elonmusk/status/2071650759330906253

- Type: x-post
- URL: https://x.com/elonmusk/status/2071650759330906253
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 21. https://x.com/thsottiaux/status/2071636285807059315

- Type: x-post
- URL: https://x.com/thsottiaux/status/2071636285807059315
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 22. https://x.com/elonmusk/status/2071623241668444308

- Type: x-post
- URL: https://x.com/elonmusk/status/2071623241668444308
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 23. https://x.com/rauchg/status/2071621345151009184

- Type: x-post
- URL: https://x.com/rauchg/status/2071621345151009184
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 24. https://x.com/elonmusk/status/2071615220326220158

- Type: x-post
- URL: https://x.com/elonmusk/status/2071615220326220158
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 25. https://x.com/elonmusk/status/2071613438019666143

- Type: x-post
- URL: https://x.com/elonmusk/status/2071613438019666143
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 26. https://x.com/swyx/status/2071613383380770823

- Type: x-post
- URL: https://x.com/swyx/status/2071613383380770823
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 27. https://x.com/rauchg/status/2071612651684106518

- Type: x-post
- URL: https://x.com/rauchg/status/2071612651684106518
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 28. https://x.com/elonmusk/status/2071612046894936136

- Type: x-post
- URL: https://x.com/elonmusk/status/2071612046894936136
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 29. https://x.com/petergyang/status/2071606799791436242

- Type: x-post
- URL: https://x.com/petergyang/status/2071606799791436242
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 30. https://x.com/elonmusk/status/2071606142753542409

- Type: x-post
- URL: https://x.com/elonmusk/status/2071606142753542409
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 31. https://x.com/petergyang/status/2071594744283902091

- Type: x-post
- URL: https://x.com/petergyang/status/2071594744283902091
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 32. https://x.com/swyx/status/2071478390172049555

- Type: x-post
- URL: https://x.com/swyx/status/2071478390172049555
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 33. https://x.com/gdb/status/2071453977091477911

- Type: x-post
- URL: https://x.com/gdb/status/2071453977091477911
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 34. https://x.com/elonmusk/status/2071420290702127225

- Type: x-post
- URL: https://x.com/elonmusk/status/2071420290702127225
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 35. https://x.com/elonmusk/status/2071420142756548901

- Type: x-post
- URL: https://x.com/elonmusk/status/2071420142756548901
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

## Secondary Source Candidates

These links were discovered from first-layer sources. Use them to reach primary material when the first-layer source is commentary or a link blog.

### 1. https://10xn.link/simon-depot

- Type: web
- URL: https://10xn.link/simon-depot
- Fetch status: limited (TimeoutError: The read operation timed out)

### 2. Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding

- Type: web
- URL: https://deep-reinforce.com/ornith_1_0.html
- Title: Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding
- Description: Introducing Ornith-1.0, a self-improving family of open-source models specially for agentic coding tasks.
- Links:
  - https://x.com/ornith_ - Twitter
  - https://huggingface.co/collections/deepreinforce-ai/ornith-10 - Hugging Face
  - https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B/blob/main/chat_template.jinja - https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B/blob/main/chat_template.jinja

Excerpt:

Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026 Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding Jun. 2026 Twitter Hugging Face Aloha! 🌺 Today, we are introducing Ornith-1.0 , a self-improving family of open-source models specially for agentic coding tasks. Ornith-1.0 spans the full spectrum, from compact 9B Dense models suitable for edge device deployment to 397B MoE frontier-scale models optimized for maximum performance, with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE . Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. The key innovation behind Ornith-1.0 is a self-improving training framework. Instead of relying on human-designed harnesses to drive solution generation in RL, Ornith-1.0 learns to generate both solution rollouts and the task-specific harnesses that guide those rollouts. By jointly optimizing the scaffold and the resulting solution, the model can discover better search trajectories and generate higher-quality solutions. Ornith-1.0 achieves state-of-the-art performance among open-source models of comparable size across a broad range of agentic coding benchmarks: Ornith-1.0-397B ( 77.5 on Terminal-Bench 2.1 and 82.4 on SWE-Bench Verified) matches the performance of Claude Opus 4.7 ( 70.3 on TB-2.1 and 80.8 on SWE-Bench Verified) and outperforming leading open-source models of similar size, including MiniMax M3 ( 66.0 on TB-2.1 and 80.5 on SWE-Bench Verified) and DeepSeek-V4-Pro ( 67.9 on TB-2.1 and 80.6 on SWE-Bench Verified). Ornith-1.0-9B, which can be easily deployed on edge devices, matches or exceeds the performance of much larger models such as Gemma 4-31B and Qwen 3.6 35B. At the flagship scale, Ornith-1.0-397B achieves 77.5 on Terminal-Bench 2.1 and 82.4 on SWE-Bench Verified, surpassing Claude Opus 4.7 on both benchmarks and outperforming leading open-source models of similar size, including Minimax M3 and DeepSeek-V4-Pro. Ornith-1.0-35B significantly outperforms similarly sized models, including Qwen 3.5-35B, Qwen 3.6-35B, and Gemma 31B. Despite having only 35B parameters, it even surpasses Qwen 3.5-397B on Terminal-Bench 2.1 (64.4 vs. 53.5) while matching its performance across several other coding and agentic benchmarks. The edge-deployable Ornith-1.0-9B also delivers remarkably strong results, achieving 43.1 on Terminal-Bench 2.1 and 69.4 on SWE-Bench Verified. De

### 3. Gemma Terms of Use | Google AI for Developers

- Type: official/blog
- URL: https://ai.google.dev/gemma/terms
- Title: Gemma Terms of Use | Google AI for Developers
- Links:
  - https://ai.google.dev/gemma/terms - Skip to main content
  - https://ai.google.dev/
  - https://deepmind.google/models/gemma - Models
  - https://deepmind.google/gemini - About
  - https://ai.google.dev/gemini-api/docs - Docs
  - https://ai.google.dev/api - API reference
  - https://ai.google.dev/pricing - Pricing
  - https://deepmind.google/technologies/imagen/ - About
  - https://ai.google.dev/gemini-api/docs/imagen - Docs
  - https://deepmind.google/technologies/veo/veo-2/ - About
  - https://ai.google.dev/gemini-api/docs/video - Docs
  - https://ai.google.dev/gemma/docs - Docs
  - https://ai.google.dev/gemma/gemmaverse - Gemmaverse
  - https://aistudio.google.com - Google AI Studio
  - https://ai.google.dev/gemma - Gemma open models
  - https://keras.io/keras_3/ - Multi-framework with Keras
  - https://colab.sandbox.google.com/github/google/generative-ai-docs/blob/main/site/en/gemma/docs/lora_tuning.ipynb - Fine-tune in Colab
  - https://ai.google.dev/edge - Google AI Edge
  - https://developer.android.com/ai/gemini-nano - Gemini Nano on Android
  - https://developer.chrome.com/docs/ai/built-in - Chrome built-in web APIs

Excerpt:

Gemma Terms of Use | Google AI for Developers Skip to main content Models Gemini About Docs API reference Pricing Imagen About Docs Pricing Veo About Docs Pricing Gemma About Docs Gemmaverse Solutions Build with Gemini Gemini API Google AI Studio Customize Gemma open models Gemma open models Multi-framework with Keras Fine-tune in Colab Run on-device Google AI Edge Gemini Nano on Android Chrome built-in web APIs Build responsibly Responsible GenAI Toolkit Secure AI Framework Code assistance Android Studio Chrome DevTools Colab Firebase Google Cloud JetBrains Jules VS Code Community Google AI Forum Gemini for Research / English Deutsch Español – América Latina Français Indonesia Italiano Polski Português – Brasil Shqip Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gemma Gemma Docs Models More Gemma Docs Solutions More Code assistance More Community More Overview Get started Releases Models Core Gemma Overview Gemma 4 model card Gemma 3 model card Gemma 2 model card Gemma 1 model card Core Variants Gemma 3n Overview Model card DiffusionGemma Overview Model card Diffusion Explained Generate Output FunctionGemma Overview Model card Formatting and best practices Function calling with Hugging Face Transformers Full function calling sequence with FunctionGemma Fine-tune FunctionGemma EmbeddingGemma Overview Model card Generate embeddings with Sentence Transformers Fine-tune EmbeddingGemma PaliGemma Overview v2 model card v1 model card Generate output with Keras Fine-tune with JAX and Flax Prompt and system instructions ShieldGemma Overview ShieldGemma 2 Model card ShieldGemma 1 Model card Run Gemma Fundamentals Overview Prompt Formatting Legacy Gemma setup [Gemma 1, 2, and 3] Legacy Prompt and system instructions [Gemma 1, 2, and 3] Run locally with a Chat UI or integrate via API LM Studio Ollama Run efficiently on Edge LiteRT-LM Llama.cpp MediaPipe LLM Inference API MLX Build/Train in Python Gemma library Hugging Face Transformers Keras Unsloth Deploy to Production / Enterprise Gemini API Cloud GKE Cloud Run Vertex AI vLLM Multi-Token Prediction (MTP) Overview Hugging Face Transformers Core Capabilities Text Basic and multi-turn chat Function calling Visual data Overview Image understanding Video understanding Audio data Thinking Tuning guides Overview Tune using Hugging Face Transformers and QLoRA Vision Tune using Hugging Face Transformers and QLoRA Full model fine-tune using Hugging Face Transformers Tune

### 4. deepreinforce-ai/Ornith-1.0-35B-GGUF · Hugging Face

- Type: web
- URL: https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF
- Title: deepreinforce-ai/Ornith-1.0-35B-GGUF · Hugging Face
- Description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
- Links:
  - https://huggingface.co/ - Hugging Face
  - https://huggingface.co/models - Models
  - https://huggingface.co/datasets - Datasets
  - https://huggingface.co/spaces - Spaces
  - https://huggingface.co/storage - Buckets new
  - https://huggingface.co/docs - Docs
  - https://huggingface.co/enterprise - Enterprise
  - https://huggingface.co/pricing - Pricing
  - https://huggingface.co/tasks - Tasks
  - https://huggingface.co/chat - HuggingChat
  - https://huggingface.co/collections - Collections
  - https://huggingface.co/languages - Languages
  - https://huggingface.co/organizations - Organizations
  - https://huggingface.co/blog - Blog
  - https://huggingface.co/posts - Posts
  - https://huggingface.co/papers - Daily Papers
  - https://huggingface.co/learn - Learn
  - https://huggingface.co/join/discord - Discord
  - https://discuss.huggingface.co/ - Forum
  - https://github.com/huggingface - GitHub

Excerpt:

deepreinforce-ai/Ornith-1.0-35B-GGUF · Hugging Face Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up deepreinforce-ai / Ornith-1.0-35B-GGUF like 482 Follow DeepReinforce 1.05k Text Generation Transformers GGUF conversational License: mit Model card Files Files and versions xet Community 26 Deploy Copy to bucket new Use this model Instructions to use deepreinforce-ai/Ornith-1.0-35B-GGUF with libraries, inference providers, notebooks, and local apps. Follow these links to get started. Libraries Transformers How to use deepreinforce-ai/Ornith-1.0-35B-GGUF with Transformers: # Use a pipeline as a high-level helper from transformers import pipeline pipe = pipeline("text-generation", model="deepreinforce-ai/Ornith-1.0-35B-GGUF") messages = [ {"role": "user", "content": "Who are you?"}, ] pipe(messages) # Load model directly from transformers import AutoModel model = AutoModel.from_pretrained("deepreinforce-ai/Ornith-1.0-35B-GGUF", dtype="auto") llama-cpp-python How to use deepreinforce-ai/Ornith-1.0-35B-GGUF with llama-cpp-python: # !pip install llama-cpp-python from llama_cpp import Llama llm = Llama.from_pretrained( repo_id="deepreinforce-ai/Ornith-1.0-35B-GGUF", filename="ornith-1.0-35b-Q4_K_M.gguf", ) llm.create_chat_completion( messages = [ { "role": "user", "content": "What is the capital of France?" } ] ) Notebooks Google Colab Kaggle Local Apps Settings llama.cpp How to use deepreinforce-ai/Ornith-1.0-35B-GGUF with llama.cpp: Install (macOS, Linux) curl -LsSf https://llama.app/install.sh | sh # Start a local OpenAI-compatible server with a web UI: llama serve -hf deepreinforce-ai/Ornith-1.0-35B-GGUF:Q4_K_M # Run inference directly in the terminal: llama cli -hf deepreinforce-ai/Ornith-1.0-35B-GGUF:Q4_K_M Install from WinGet (Windows) winget install llama.cpp # Start a local OpenAI-compatible server with a web UI: llama serve -hf deepreinforce-ai/Ornith-1.0-35B-GGUF:Q4_K_M # Run inference directly in the terminal: llama cli -hf deepreinforce-ai/Ornith-1.0-35B-GGUF:Q4_K_M Use pre-built binary # Download pre-built binary from: # https://github.com/ggerganov/llama.cpp/releases # Start a local OpenAI-compatible server with a web UI: ./llama-server -hf deepreinforce-ai/Ornith-1.0-35B-

### 5. ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

- Type: official/blog
- URL: https://research.nvidia.com/labs/gear/enpire/
- Title: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World
- Description: Anonymous ENPIRE project website for agentic robot policy self-improvement in the real world.
- Links:
  - https://research.nvidia.com/labs/gear/enpire/ - Scroll to explore
  - https://wenlixiao.com/ - Wenli Xiao
  - https://jia-xie.com - Jia Xie
  - https://tonghe-zhang.github.io/ - Tonghe Zhang
  - https://darthutopian.github.io/ - Haotian Lin
  - https://max-fu.github.io/ - Letian "Max" Fu
  - https://haoruxue.github.io/ - Haoru Xue
  - https://yiyang-23.github.io/ - Yi Yang
  - https://cunxid.github.io/ - Cunxi Dai
  - https://ziwang1105.github.io/ - Zi Wang
  - https://jimmyyhwu.github.io/ - Jimmy Wu
  - https://guanzhi.me/ - Guanzhi Wang
  - https://www2.eecs.berkeley.edu/Faculty/Homepages/sastry.html - S. Shankar Sastry
  - https://goldberg.berkeley.edu/ - Ken Goldberg
  - https://jimfan.me/ - Linxi "Jim" Fan
  - https://yukezhu.me/ - Yuke Zhu
  - https://www.gshi.me/ - Guanya Shi
  - https://arxiv.org/abs/2606.19980 - Paper
  - https://github.com/huggingface/gym-pusht - huggingface/gym-pusht

Excerpt:

ENPIRE: Agentic Robot Policy Self-Improvement in the Real World E N P I R E Scroll to explore Title Abstract Learned Policy ENPIRE System Environment Loop Auto Evaluation Auto Reset Case 1: Push T Case 2: Pin Insertion Case 3: Tie Zip-tie Case 4: GPU Insertion Policy Improvement Evaluate Coding Agent Fleet Scaling Simulation Evaluation Limitations & Future Directions Acknowledgements Contents Contents Title Abstract Learned Policy ENPIRE System Environment Loop Auto Evaluation Auto Reset Case 1: Push T Case 2: Pin Insertion Case 3: Tie Zip-tie Case 4: GPU Insertion Policy Improvement Evaluate Coding Agent Fleet Scaling Simulation Evaluation Limitations & Future Directions Acknowledgements ENPIRE: Agentic Robot Policy Self-Improvement in the Real World Wenli Xiao 1,2† , Jia Xie 2† , Tonghe Zhang 2† , Haotian Lin 2† , Letian "Max" Fu 3 , Haoru Xue 3 , Jalen Lu 2 , Yi Yang 2 , Cunxi Dai 2 , Zi Wang 1 , Jimmy Wu 1 , Guanzhi Wang 1 , S. Shankar Sastry 3 , Ken Goldberg 3 , Linxi "Jim" Fan 1‡ , Yuke Zhu 1‡ , Guanya Shi 2‡ 1 NVIDIA 2 CMU 3 UC Berkeley † Equal contribution ‡ Equal advising Paper Abstract Achieving dexterous robotic manipulation in the real world relies heavily on human supervision and algorithmic engineering, which is a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined to digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable feedback loop for real-world policy improvement: reset the scene, execute a policy, verify the outcome, and refine the next iteration. To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with single or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes. This closed-loop system transforms real-world robot learning into a controllable optimization procedure that agents can manage, thus minimizing human effort while allowing fair ablations across training recipes and agent variants. Powered by ENPIRE, frontier coding

### 6. ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

- Type: paper
- URL: https://arxiv.org/abs/2606.19980
- Title: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World
- Description: Abstract page for arXiv paper 2606.19980: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World
- Links:
  - https://arxiv.org/abs/2606.19980 - Skip to main content
  - https://www.cornell.edu/
  - https://tech.cornell.edu/arxiv/ - Learn about arXiv becoming an independent nonprofit.
  - https://info.arxiv.org/about/ourmembers.html - member institutions
  - https://info.arxiv.org/about/donate.html - Donate
  - https://arxiv.org/IgnoreMe
  - https://arxiv.org/
  - https://arxiv.org/list/cs/recent - cs
  - https://info.arxiv.org/help - Help
  - https://arxiv.org/search/advanced - Advanced Search
  - https://arxiv.org/login - Login
  - https://info.arxiv.org/about - About
  - https://arxiv.org/search/cs?searchtype=author&query=Xiao,+W - Wenli Xiao
  - https://arxiv.org/search/cs?searchtype=author&query=Xie,+J - Jia Xie
  - https://arxiv.org/search/cs?searchtype=author&query=Zhang,+T - Tonghe Zhang
  - https://arxiv.org/search/cs?searchtype=author&query=Lin,+H - Haotian Lin
  - https://arxiv.org/search/cs?searchtype=author&query=Fu,+L+%22 - Letian "Max" Fu
  - https://arxiv.org/search/cs?searchtype=author&query=Xue,+H - Haoru Xue
  - https://arxiv.org/search/cs?searchtype=author&query=Lu,+J - Jalen Lu
  - https://arxiv.org/search/cs?searchtype=author&query=Yang,+Y - Yi Yang

Excerpt:

[2606.19980] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World Skip to main content arXiv submission will be down for maintenance beginning 14:00 EDT Tuesday June 30th. The site should otherwise remain in operation. Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs > arXiv:2606.19980 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2606.19980 (cs) [Submitted on 18 Jun 2026] Title: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World Authors: Wenli Xiao , Jia Xie , Tonghe Zhang , Haotian Lin , Letian "Max" Fu , Haoru Xue , Jalen Lu , Yi Yang , Cunxi Dai , Zi Wang , Jimmy Wu , Guanzhi Wang , S. Shankar Sastry , Ken Goldberg , Linxi "Jim" Fan , Yuke Zhu , Guanya Shi View a PDF of the paper titled ENPIRE: Agentic Robot Policy Self-Improvement in the Real World, by Wenli Xiao and 16 other authors View PDF HTML (experimental) Abstract: Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined in digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable feedback loop for real-world policy improvement: reset the scene, execute a policy, verify the outcome, and refine the next iteration. To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with one or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes. This closed-loop system transforms real-world manipulation learning into a controllable optimization procedure, minimizing human effort while allo

### 7. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6875838

- Type: web
- URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6875838
- Fetch status: limited (HTTP 403: Forbidden)

### 8. ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters

- Type: paper
- URL: https://arxiv.org/abs/2606.20374
- Title: ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters
- Description: Abstract page for arXiv paper 2606.20374: ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters
- Links:
  - https://arxiv.org/abs/2606.20374 - Skip to main content
  - https://www.cornell.edu/
  - https://tech.cornell.edu/arxiv/ - Learn about arXiv becoming an independent nonprofit.
  - https://info.arxiv.org/about/ourmembers.html - member institutions
  - https://info.arxiv.org/about/donate.html - Donate
  - https://arxiv.org/IgnoreMe
  - https://arxiv.org/
  - https://arxiv.org/list/cs/recent - cs
  - https://info.arxiv.org/help - Help
  - https://arxiv.org/search/advanced - Advanced Search
  - https://arxiv.org/login - Login
  - https://info.arxiv.org/about - About
  - https://arxiv.org/search/cs?searchtype=author&query=Zhou,+J - Jiasheng Zhou
  - https://arxiv.org/search/cs?searchtype=author&query=Zeng,+L - Longbin Zeng
  - https://arxiv.org/search/cs?searchtype=author&query=Chen,+C - Clavis Chen
  - https://arxiv.org/search/cs?searchtype=author&query=Lu,+R - Ruiming Lu
  - https://arxiv.org/search/cs?searchtype=author&query=Yang,+Q - Qinwei Yang
  - https://arxiv.org/search/cs?searchtype=author&query=Ye,+L - Leyi Ye
  - https://arxiv.org/search/cs?searchtype=author&query=Ying,+R - Ray Ying
  - https://arxiv.org/search/cs?searchtype=author&query=Zhang,+K - Key Zhang

Excerpt:

[2606.20374] ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters Skip to main content arXiv submission will be down for maintenance beginning 14:00 EDT Tuesday June 30th. The site should otherwise remain in operation. Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors. Donate > cs > arXiv:2606.20374 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search GO quick links Login Help Pages About Computer Science > Distributed, Parallel, and Cluster Computing arXiv:2606.20374 (cs) [Submitted on 18 Jun 2026] Title: ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters Authors: Jiasheng Zhou , Longbin Zeng , Clavis Chen , Ruiming Lu , Qinwei Yang , Leyi Ye , Ray Ying , Key Zhang View a PDF of the paper titled ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters, by Jiasheng Zhou and 7 other authors View PDF HTML (experimental) Abstract: Large-scale LLM training requires always-on, fine-grained observability for effective performance diagnosis at scale. Coarse resource monitors alone cannot localize root causes, and fine-grained profilers incur prohibitive (5%-30%) overheads and massive trace volumes, making always-on deployment impractical in large production clusters. We propose ARGUS, a low-overhead, fine-grained, always-on tracing and real-time analysis system for training workloads in 10,000+ GPU-scale production clusters. ARGUS decomposes observation along the training call hierarchy into CPU call stacks, framework semantics, and GPU kernel execution, with always-on collection under a combined overhead of less than 2%. It builds a unified data pipeline and compresses raw kernel events by approximately 3,700x from 10 MB to 2.7 KB per rank per step. Its progressive diagnosis framework automatically isolates anomalous windows, straggler ranks, and degraded kernels through iteration-time, phase-level, and kernel-level analysis. Deployed for over six months on a 10,000+ GPU production cluster, ARGUS has supported continuous fail-slow detection and performance optimization. Our case studies further demonstrate its effectiveness across representative anomalies, including compute stragglers, link degradation, pipe

### 9. Julia

- Type: web
- URL: https://borretti.me/fiction/julia
- Title: Julia
- Published: 2026-02-01T00:00:00+00:00
- Description: An aphasic space station monitors an anomalous object, while keeping the last two humans alive.
- Links:
  - https://borretti.me/ - Home
  - https://borretti.me/fiction/ - Fiction
  - https://borretti.me/about - About
  - https://borretti.me/portfolio - Portfolio
  - https://borretti.me/article - Articles
  - https://borretti.me/fiction - Fiction
  - https://borretti.me/consulting - Consulting
  - https://borretti.me/feed.xml - RSS

Excerpt:

Julia Home ❖ Fiction Julia I wrote a program so that I could paint in aquarelle. I take pages from the treasure and paint them: the sky of Varennes on the night of 2 Messidor; a sagittal cut of Saint Sebastian, whose arrows are cylindric sections; Miranda gazing at the sea, waiting to be relieved. At times I include Julia in the scene, in whatever clothes it wears at the time, as though we had always known Julia, and had been reared under its gaze. Thus a flaming halo presides over the battle of Lepanto, and a mirror sphere watches the waters of the Sous. And what would the first astronomers have made of Julia? The wanderers, the flame-haired stars are knowable: think you of the Antikythera device, of the Metonic cycle, of Kepler’s nested solids. Julia is indescribable and incompressible: its appearance has never recurred. Had we known Julia from childhood, we would never have believed in the system of the world, that God is made of algebra. I have always believed our secret purpose is to wait out Julia: to catch a repetition and redeem our faith that the universe is finite and space is discretized. That there are fixed laws and the world is knowable. A system with a finite number of states must repeat itself. I am six hundred meters in major diameter, forty meters in minor diameter. I mass nine hundred thousand tons. I have turned two hundred and forty million times. I am glass and wire. I was born and died on Earth, but I died foolishly, and for that reason my encephalon was laminated, and I was brought to the stars to be immured here. They took my language center, the Chomsky organ, so that I could not complain of my condition. I do not mind it. I can paint in aquarelle. They wired the alarms—of airless rooms and freezing cold and power outages—to the nociceptors, and were I sensible I would be in great pain, for most of me is airless, frozen, and unlit. Therefore I have cut the afferent nerves. I am made of absences, I feel the contours of the absences, where air leaks into vacuum, atom by atom. I have use of the antenna. At times I exhale a sphere of microwave light, close my eyes and listen. And I hear the flotsam echoing back: a discarded tank, a glass strut, a sheet of mylar; Ernst Weyl, who tumbled and drowned, who trails us in our orbit. Julia reflects no light. There is a little redoubt of warmth and air, an island of stability that I preserve against the cold lightless void. There live the last two of the crew, like Miranda, waiting to be relie

### 10. The Epiphany of Gliese 581

- Type: web
- URL: https://borretti.me/fiction/eog581
- Title: The Epiphany of Gliese 581
- Published: 2022-11-15T00:00:00+00:00
- Description: A linguist, a chemist, and a comparative psychologist search the ruins of a dead superintelligence.
- Links:
  - https://borretti.me/ - Home
  - https://borretti.me/fiction/ - Fiction
  - https://www.orionsarm.com/ - Orion's Arm
  - https://www.davidzindell.com/ - David Zindell
  - https://borretti.me/assets/content/eog581/The%20Epiphany%20of%20Gliese%20581.pdf - PDF
  - https://borretti.me/assets/content/eog581/The%20Epiphany%20of%20Gliese%20581.epub - EPUB
  - https://borretti.me/fiction/eog581/the-cartesian-theatre - The Cartesian Theatre
  - https://borretti.me/fiction/eog581/wepwawet - Wepwawet
  - https://borretti.me/fiction/eog581/objects-in-space - Objects in Space
  - https://borretti.me/fiction/eog581/without-organs - Without Organs
  - https://borretti.me/fiction/eog581/ring-zero - Ring Zero
  - https://borretti.me/fiction/eog581/the-book-of-days - The Book of Days
  - https://borretti.me/fiction/eog581/the-lunar-surface - The Lunar Surface
  - https://borretti.me/fiction/eog581/la-sienza-nuova - La Scienza Nuova
  - https://borretti.me/fiction/eog581/colophon - Colophon
  - https://www.reddit.com/r/printSF/comments/11o81gj/comment/jbzyjt6/?context=999 - whenwerewe
  - https://twitter.com/mattparlmer/status/1595505438262497283 - Matt Parlmer
  - https://twitter.com/adamthesherwood/status/1609216850025381888 - Adam
  - https://twitter.com/ch1n3du3/status/1597202910966075394 - @ch1n3du3
  - https://twitter.com/VitaeKate/status/1611058242330791936 - @VitaeKate

Excerpt:

The Epiphany of Gliese 581 Home ❖ Fiction The Epiphany of Gliese 581 A linguist, a chemist, and a comparative psychologist explore the ruins of a dead superintelligence. 26k words. Inspired by Orion's Arm and the works of David Zindell . You can download it as a PDF or an EPUB , or read it online below. Contents The Cartesian Theatre Wepwawet Objects in Space Without Organs Ring Zero The Book of Days The Lunar Surface La Scienza Nuova Colophon Acclaim “strange and new” — whenwerewe “startlingly excellent” — Anthony “strong vibes of [Greg Egan], but in the form of more poetry and wistfulness” — Brandon “one of the best scifi novellas I've read in a while” — Matt Parlmer “This is excellent. The story is beautiful, the world feels real, and your style of prose is scratches an itch I didn't know I had.” — Adam “the best thing I've read in a while” — @ch1n3du3 “I enjoyed this immensely” — @VitaeKate Home — About — Portfolio — Articles — Fiction — Consulting — RSS © 2014 – 2026 Fernando Borretti

