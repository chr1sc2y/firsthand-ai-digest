# Firsthand AI Digest Source Pack

- Generated: 2026-07-15T08:02:24+08:00
- Intended coverage window: 2026-07-14T08:02:24+08:00 to 2026-07-15T08:02:24+08:00
- Index site: https://ai.prov1dence.top/
- Firsthand AI Digest items in window: 64
- Detail pages fetched: 0
- First-layer original sources fetched/listed: 64
- Original sources with fetched page text: 5
- Metadata-only original sources: 58
- Other limited original sources: 1
- Secondary source candidates fetched/listed: 10

This is a collection aid, not the final analysis. Open primary sources directly before writing final claims.

## Index Page

- URL: https://ai.prov1dence.top/
- Title: Firsthand AI Digest
- Links:
  - https://insight.ai.prov1dence.top/ - Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours.
  - https://simonwillison.net/2026/Jul/14/lobsters-sqlite/ - Read article ↗
  - https://simonwillison.net/2026/Jul/14/armin-ronacher/ - Read article ↗
  - https://simonwillison.net/2026/Jul/14/datasette/ - Read article ↗
  - https://openai.com/index/managing-ai-investments-in-agentic-era - Read article ↗
  - https://daily.juya.uk/issues/2026-07-14/ - Read article ↗
  - https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/ - Read article ↗
  - https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex - Read article ↗
  - https://openai.com/academy/codex-for-work/how-sales-teams-use-codex - Read article ↗
  - https://simonwillison.net/2026/Jul/13/doomql/ - Read article ↗
  - https://www.youtube.com/watch?v=ATEUNCLS2Lo - Watch ↗
  - https://www.youtube.com/watch?v=avpZWh6sm9M - Watch ↗
  - https://www.youtube.com/watch?v=8zH_O74hZBw - Watch ↗
  - https://www.youtube.com/watch?v=R-Yqes8AotY - Watch ↗
  - https://www.youtube.com/watch?v=-J5KoSMfPLk - Watch ↗
  - https://x.com/swyx/status/2077142073472590041 - Open ↗
  - https://x.com/adityaag/status/2077136023616962651 - Open ↗
  - https://x.com/petergyang/status/2077132606798442817 - Open ↗
  - https://x.com/adityaag/status/2077130899733553560 - Open ↗
  - https://x.com/petergyang/status/2077118932952264800 - Open ↗

Excerpt:

Firsthand AI Digest Firsthand AI Digest Posts, blogs, podcasts and videos from the people building AI — straight from the source. Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours. Time 3h 6h 12h 24h 3d 7d Type All Blogs Podcasts Videos Posts Blogs & Long-form 09 items SW Simon Willison By Simon Willison Blog lobste.rs is now running on SQLite lobste.rs is now running on SQLite Community site Lobsters has been planning a migration away from MariaDB since August 2018 - originally targeting PostgreSQL, but last year they decided to investigate SQLite instead. This weekend they completed the migration, and now consider it stable enough that it looks like this is the permanent architecture for the site going forward: SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB. There's also a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack_attack database used by the Rack::Attack middleware for blocking and throttling abusive requests. There are plenty more details in both the linked thread and this SQLite migration PR by Thomas Dziedzic, which added 735 lines and removed 593 lines across 30 commits and 188 files. That PR built on top of previous PRs #1705, #1871, and #1924. This is a really useful case study, and a great reminder that you can get a whole lot done with a single server and SQLite in 2026. Tags: migrations, ops, rails, sqlite, lobsters 2026-07-14 19:44:11 UTC Read article ↗ SW Simon Willison By Simon Willison Blog Quoting Armin Ronacher The shared language of a software project is not English or Python but it is the common understanding of what its concepts mean, where the boundaries are, which invariants matter, who owns what, and why the system has the shape it does. This language is rarely written down in one place. It lives partly in documentation and code, but also in code review, conversations, arguments, and the experience of having to explain a change to somebody else. Before agents, some of this shared understanding was maintained by friction. If I wanted to change your storage layer, I usually had to read your code, ask you questions, and perhaps coordinate with another team whose service depended on it. This was slow, and much of that slowness 

## Firsthand AI Digest Items In Window

### 1. lobste.rs is now running on SQLite

- URL: https://simonwillison.net/2026/Jul/14/lobsters-sqlite/
- Type: Blog
- Published: 2026-07-14T19:44:11+00:00
- Digest summary: lobste.rs is now running on SQLite Community site Lobsters has been planning a migration away from MariaDB since August 2018 - originally targeting PostgreSQL, but last year they decided to investigate SQLite instead. This weekend they completed the migration, and now consider it stable enough that it looks like this is the permanent architecture for the site going forward: SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB. There's also a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack_attack database used by the R

### 2. Quoting Armin Ronacher

- URL: https://simonwillison.net/2026/Jul/14/armin-ronacher/
- Type: Blog
- Published: 2026-07-14T18:04:23+00:00
- Digest summary: The shared language of a software project is not English or Python but it is the common understanding of what its concepts mean, where the boundaries are, which invariants matter, who owns what, and why the system has the shape it does. This language is rarely written down in one place. It lives partly in documentation and code, but also in code review, conversations, arguments, and the experience of having to explain a change to somebody else. Before agents, some of this shared understanding was maintained by friction. If I wanted to change your storage layer, I usually had to read your code, ask you questions, and perhaps coordinate with another team whose service depended on it. This was slow, and much of that slowness was waste but not all of it was. Some of it was the process by which

### 3. datasette 1.0a37

- URL: https://simonwillison.net/2026/Jul/14/datasette/
- Type: Blog
- Published: 2026-07-14T16:31:41+00:00
- Digest summary: Release: datasette 1.0a37 A minor release. Performance and documentation improvements to the permissions system, plus I reverted a cosmetic API change which caused almost every existing plugin test suite to break. Tags: datasette

### 4. How to manage AI investments in the agentic era

- URL: https://openai.com/index/managing-ai-investments-in-agentic-era
- Type: Blog
- Published: 2026-07-14T10:00:00+00:00
- Digest summary: Learn how enterprises can manage AI investments in the agentic era by measuring useful work per dollar, improving efficiency, and scaling high-value workflows.

### 5. 2026-07-14

- URL: https://daily.juya.uk/issues/2026-07-14/
- Type: Blog
- Published: 2026-07-14T01:13:36+00:00
- Digest summary: AI 早报 2026 07 14 视频版 ：哔哩哔哩 ｜ YouTube 概览 要闻 Codex 周活用户达 700 万，官方发放重置额度致庆 ↗ 1 Codex 更新：GPT 5.6 Sol上下文回滚至272k并修复多Agent消耗 ↗ 2 模型发布 actAVA发布医疗模型Cura 1T ↗ 3 腾讯混元全栈开源 HyOCR 1.5 ↗ 4 开发生态 Claude Code Artifacts 支持公开分享与多人编辑 ↗ 5 GLM Coding Plan 专项治理违规账号 ↗ 6 Grok Build CLI 被指上传完整代码库，官方已服务端禁用 ↗ 7 产品应用 阶跃星辰发布Step AOS与智能体手机STEPX Neo ↗ 8 技术与洞察 Anthropic研究揭示Claude价值观在模型与语言间存…

### 6. Using uvx in GitHub Actions in a cache-friendly way

- URL: https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/
- Type: Blog
- Published: 2026-07-14T00:56:20+00:00
- Digest summary: TIL: Using uvx in GitHub Actions in a cache-friendly way I finally found a cache-friendly recipe for using uvx tool-name in GitHub Actions workflows that I like. The trick is setting a UV_EXCLUDE_NEWER: "2026-07-12" environment variable at the start of the workflow and then using that as part of the GitHub Actions cache key. This means any uvx tool-name commands will resolve to the most recent version as-of that date, and you can bust the cache and upgrade the tools by bumping the date in the future. My goal here is to use Python tools in GitHub Actions without every run of the workflow hitting PyPI to download a fresh copy of the tool and its dependencies. Update: Here's an existing issue against the astral-sh/setup-uv repository requesting that they switch the default to cache rather tha

### 7. Who Owns the Sea? – Sarah Paine

- URL: https://www.youtube.com/watch?v=ATEUNCLS2Lo
- Type: Video
- Published: 2026-07-14T21:20:03+00:00
- Digest summary: Full episode: https://www.youtube.com/watch?v=OS1NZLgKM2c Me on twitter: https://x.com/dwarkesh_sp

### 8. Improved Intelligence with GPT-Live

- URL: https://www.youtube.com/watch?v=avpZWh6sm9M
- Type: Video
- Published: 2026-07-14T20:22:11+00:00
- Digest summary: More about our next generation voice model here: https://openai.com/index/introducing-gpt-live/

### 9. Build and publish web apps directly in ChatGPT

- URL: https://www.youtube.com/watch?v=8zH_O74hZBw
- Type: Video
- Published: 2026-07-14T19:19:36+00:00
- Digest summary: See how to build a working web app directly in ChatGPT. Describe what you want, try the first version, ask for changes in plain language, and publish it when it’s ready—with hosting and storage built in. Learn more: https://learn.chatgpt.com/ Chapters 00:00 Introducing Sites 00:21 Building a launch site 00:41 Refining with feedback 00:55 Annotating and publishing 01:09 Working with Build Web Apps 01:20 Creating a web game

### 10. Reconstructing Pelé’s lost goal

- URL: https://www.youtube.com/watch?v=R-Yqes8AotY
- Type: Video
- Published: 2026-07-14T13:04:39+00:00
- Digest summary: On August 2, 1959, Pelé scored the most beautiful goal of his career: three consecutive “sombreros” without the ball touching the ground. Yet, the legendary ‘Gol da Rua Javari’ was never caught on film. We worked alongside historians, sports journalists, football legends, and Pelé’s family to reconstruct this lost moment and share it with the world. This project was created in full partnership with the Pelé Brand, the official managers of the Pelé estate. Rooted in education and cultural preservation, the project heads to the Pelé Museum this year. To achieve this, teams from Google DeepMind used models like Gemini Omni and Veo to transform historical fragments into moving imagery, filmed on the original pitch with authentic uniforms and a vintage ball. By making the memory of this goal mo

### 11. https://x.com/swyx/status/2077142073472590041

- URL: https://x.com/swyx/status/2077142073472590041
- Type: Post
- Published: 2026-07-14T21:23:56+00:00
- Digest summary: [40something VC who just came back from a week in Shanghai, staying at the best Marriotts, chauffeured in the latest Audis and BMWs, bag full of LV, Chanel and Lancôme for the wife] "Let me tell you, I just came back from China and my god the West is so cooked"

### 12. https://x.com/adityaag/status/2077136023616962651

- URL: https://x.com/adityaag/status/2077136023616962651
- Type: Post
- Published: 2026-07-14T20:59:54+00:00
- Digest summary: Is there any move involving Lamine Yamal where Yamal doesn't end up on the floor rolling around?

### 13. https://x.com/petergyang/status/2077132606798442817

- URL: https://x.com/petergyang/status/2077132606798442817
- Type: Post
- Published: 2026-07-14T20:46:19+00:00
- Digest summary: Honestly the way Spain is playing it’ll be a huge upset if they’re not the champions

### 14. https://x.com/adityaag/status/2077130899733553560

- URL: https://x.com/adityaag/status/2077130899733553560
- Type: Post
- Published: 2026-07-14T20:39:32+00:00
- Digest summary: I appreciate the in-depth feature set of the new "ChatGPT" app... But there is a real tradeoff. I used ChatGPT (Legacy) 15-20 times a day for queries... And now it feels so heavyweight for that use case. Shame.

### 15. https://x.com/petergyang/status/2077118932952264800

- URL: https://x.com/petergyang/status/2077118932952264800
- Type: Post
- Published: 2026-07-14T19:51:59+00:00
- Digest summary: So...these two teams seem to play alot better than Argentina or England 😅

### 16. https://x.com/sama/status/2077118672150388816

- URL: https://x.com/sama/status/2077118672150388816
- Type: Post
- Published: 2026-07-14T19:50:57+00:00
- Digest summary: hello!

### 17. https://x.com/kevinweil/status/2077118363663499335

- URL: https://x.com/kevinweil/status/2077118363663499335
- Type: Post
- Published: 2026-07-14T19:49:43+00:00
- Digest summary: This is an amazing quote, and it's true well beyond politics. There is no they. Everyone is figuring it out as they go. You can just do things.

### 18. https://x.com/petergyang/status/2077115676893057233

- URL: https://x.com/petergyang/status/2077115676893057233
- Type: Post
- Published: 2026-07-14T19:39:02+00:00
- Digest summary: Viva España!

### 19. https://x.com/thsottiaux/status/2077114635308986427

- URL: https://x.com/thsottiaux/status/2077114635308986427
- Type: Post
- Published: 2026-07-14T19:34:54+00:00
- Digest summary: Hello. We have reached 8M active users across Codex and ChatGPT Work. We are once again resetting the usage limits for all. And we continue to not have the 5h rate limit as well, allowing everyone to explore the boundaries of GPT-5.6 Sol and discover how ambitious you can be. See you tomorrow for more updates on our growth!

### 20. https://x.com/ryolu_/status/2077108336844210352

- URL: https://x.com/ryolu_/status/2077108336844210352
- Type: Post
- Published: 2026-07-14T19:09:52+00:00
- Digest summary: assembling the best design team (looking for design engs, too)

### 21. https://x.com/ryolu_/status/2077107655894860137

- URL: https://x.com/ryolu_/status/2077107655894860137
- Type: Post
- Published: 2026-07-14T19:07:10+00:00
- Digest summary: 💛

### 22. https://x.com/sama/status/2077106587307798989

- URL: https://x.com/sama/status/2077106587307798989
- Type: Post
- Published: 2026-07-14T19:02:55+00:00
- Digest summary: 5.6 sol growth is insane. the inference team has done heroic work to be able to support demand. we are going to move mountains to continue to scale, but it is possible there are some hiccups soon.

### 23. https://x.com/AravSrinivas/status/2077105849638728118

- URL: https://x.com/AravSrinivas/status/2077105849638728118
- Type: Post
- Published: 2026-07-14T18:59:59+00:00
- Digest summary: Perplexity has the best (both on cost and performance) deep and wide research harness in Computer. One of the contributing factors is strong internal evals and benchmarks. Today, we're open-sourcing WANDR, the benchmark we use internally for measuring research capabilities. https://t.co/afwRd7NUm1

### 24. https://x.com/petergyang/status/2077103041397084269

- URL: https://x.com/petergyang/status/2077103041397084269
- Type: Post
- Published: 2026-07-14T18:48:50+00:00
- Digest summary: For making html slides and videos (e.g., using @HyperFrames_ ) Fable is still significantly better than GPT 5.6 Sol. The stuff that Sol makes is unusable. For landing pages, 5.6 Sol has caught up.

### 25. https://x.com/danshipper/status/2077100057136894166

- URL: https://x.com/danshipper/status/2077100057136894166
- Type: Post
- Published: 2026-07-14T18:36:58+00:00
- Digest summary: we have now issued over 1 million codex credits to @every subscribers!!!

### 26. https://x.com/danshipper/status/2077094235640156199

- URL: https://x.com/danshipper/status/2077094235640156199
- Type: Post
- Published: 2026-07-14T18:13:50+00:00
- Digest summary: builders love @every's builder pack! https://t.co/w6Ne8xZkGq

### 27. https://x.com/petergyang/status/2077093016620384401

- URL: https://x.com/petergyang/status/2077093016620384401
- Type: Post
- Published: 2026-07-14T18:09:00+00:00
- Digest summary: This is super cute although I don't understand why people have to sign in with ChatGPT to visit a ChatGPT created website? https://t.co/iAEcLMZBcA

### 28. https://x.com/steipete/status/2077088803500818682

- URL: https://x.com/steipete/status/2077088803500818682
- Type: Post
- Published: 2026-07-14T17:52:15+00:00
- Digest summary: Streaming some open source in a few! 🙌

### 29. https://x.com/sundarpichai/status/2077086951833063580

- URL: https://x.com/sundarpichai/status/2077086951833063580
- Type: Post
- Published: 2026-07-14T17:44:54+00:00
- Digest summary: Well said Demis! Worth reading

### 30. https://x.com/fchollet/status/2077084408633503774

- URL: https://x.com/fchollet/status/2077084408633503774
- Type: Post
- Published: 2026-07-14T17:34:48+00:00
- Digest summary: Gödelian humor is self-referential

### 31. https://x.com/swyx/status/2077072402828361772

- URL: https://x.com/swyx/status/2077072402828361772
- Type: Post
- Published: 2026-07-14T16:47:05+00:00
- Digest summary: cosign. models have overtuned to this now and do not realize when the agentsmd is out of date and should be changed/ignored. last night i goaled 5.6 sol to complete a 5 stage task and woke up to find it was still stuck on stage 0. it took a while to read the transcript back a few hours to realize at some point some agent had committed “stage 0 is the target dont do anything else” so poor sol spent 8 hours only refining and verifying stage 0 because /goal would not let it stop and agentsmd would not let it proceed. if you dont know whats in your agentsmd before you fire off each task, it is an indirect prompt injection you perform on yourself. /plan, /goal, /skill, or nothing at all.

### 32. https://x.com/ryolu_/status/2077060449837990399

- URL: https://x.com/ryolu_/status/2077060449837990399
- Type: Post
- Published: 2026-07-14T15:59:35+00:00
- Digest summary: some of us are building agents. some of us are buying landlines. https://t.co/vPVu5qwMsu

### 33. https://x.com/danshipper/status/2077058541853061466

- URL: https://x.com/danshipper/status/2077058541853061466
- Type: Post
- Published: 2026-07-14T15:52:00+00:00
- Digest summary: BREAKING: Introducing All Access from @every, our new membership tier for the best builders in AI All Access subs get the Builder Pack which includes $7,000 in credits and free usage to the models + tool stack we use @every. All Access subscribers get: - $1,000 in Codex / @ChatGPTapp for Work credits - 12 months free of @Cursor_AI Pro+ - $4,000 in @PostHog credits including self-driving to automatically fix bugs and identify issues in your production app - 1 year free of @Framer - 6 months free of @NotionHQ And much more! (Did I mention $1,000 in Codex credits? It's time to build!) Get all access: https://t.co/3HlZawcc9N Why All Access and the Builder Pack This is the best time in history to build something. For a long time, it’s been possible to one-shot impressive demos, but they’d fall 

### 34. https://x.com/sama/status/2077053140508266710

- URL: https://x.com/sama/status/2077053140508266710
- Type: Post
- Published: 2026-07-14T15:30:33+00:00
- Digest summary: Concerning.

### 35. https://x.com/claudeai/status/2077047278078931243

- URL: https://x.com/claudeai/status/2077047278078931243
- Type: Post
- Published: 2026-07-14T15:07:15+00:00
- Digest summary: We're introducing Claude for Teachers: free access to premium Claude capabilities for verified K-12 educators in the US, with a library of teaching skills and a direct connection to evidence-based curricula, mapped to academic standards in all 50 states. https://t.co/5hZZijVPCV https://t.co/5ofG8YLEON

### 36. https://x.com/petergyang/status/2077047201889747096

- URL: https://x.com/petergyang/status/2077047201889747096
- Type: Post
- Published: 2026-07-14T15:06:57+00:00
- Digest summary: I get podcast outreach from various PR agencies and I have to say almost 100% of the time they're pitching a CEO or exec to promote their product (which makes for bad episodes). The best CEO and exec episodes show real workflows with no agenda.

### 37. https://x.com/elonmusk/status/2077044528234553709

- URL: https://x.com/elonmusk/status/2077044528234553709
- Type: Post
- Published: 2026-07-14T14:56:19+00:00
- Digest summary: Ancient times https://t.co/8VWNoiOHjg

### 38. https://x.com/levie/status/2077043523703243070

- URL: https://x.com/levie/status/2077043523703243070
- Type: Post
- Published: 2026-07-14T14:52:20+00:00
- Digest summary: Thoughtful proposal for a standards body for AI. This is distinct from a regulatory agency, and would certainly allow for much faster improvement of standards and collaboration with the industry. What you definitely don’t want is for AI progress to start to move at the speed of that the government classically operates at. If that happens then we can essentially guarantee progress begins to stall, and worse, America likely just loses the AI race. This framework threads the needle mostly. The only challenge is still that even those in industry don’t agree on the same safety risks in AI. But if you can get alignment there, this looks better than most other proposals.

### 39. https://x.com/elonmusk/status/2077043449279262954

- URL: https://x.com/elonmusk/status/2077043449279262954
- Type: Post
- Published: 2026-07-14T14:52:02+00:00
- Digest summary: True

### 40. https://x.com/sama/status/2077042528906527225

- URL: https://x.com/sama/status/2077042528906527225
- Type: Post
- Published: 2026-07-14T14:48:23+00:00
- Digest summary: this is a thoughtful proposal from demis:

### 41. https://x.com/sama/status/2077037818824843719

- URL: https://x.com/sama/status/2077037818824843719
- Type: Post
- Published: 2026-07-14T14:29:40+00:00
- Digest summary: this would have been a whole startup not too long ago

### 42. https://x.com/sama/status/2077036999303999910

- URL: https://x.com/sama/status/2077036999303999910
- Type: Post
- Published: 2026-07-14T14:26:24+00:00
- Digest summary: GPT-5.6 sol is half the price and ~twice as token efficient as fable in many cases for accomplishing the same task. happy to deliver at one-quarter of the price.

### 43. https://x.com/danshipper/status/2077036035062554906

- URL: https://x.com/danshipper/status/2077036035062554906
- Type: Post
- Published: 2026-07-14T14:22:34+00:00
- Digest summary: something new coming from @every in a few 👀

### 44. https://x.com/sama/status/2077033807736459713

- URL: https://x.com/sama/status/2077033807736459713
- Type: Post
- Published: 2026-07-14T14:13:43+00:00
- Digest summary: 2.5x increase in usage of our agentic products (codex and chatgpt work) in the last week! welcome.

### 45. https://x.com/fchollet/status/2077033256365736098

- URL: https://x.com/fchollet/status/2077033256365736098
- Type: Post
- Published: 2026-07-14T14:11:32+00:00
- Digest summary: Super impressed with what Harvinder and Suman have built at @airtap_ai. They've essentially turned SMS into a headless agentic execution layer for your mobile apps. You just text it to run errands, and it operates apps like DoorDash, TikTok, etc. in the background. It keeps you updated in plain text, and only needs your intervention for authentication. Cool consumer AI concept. Check it out at https://t.co/y2AKloQI9w or text the AI at +1 (650) 213-7322

### 46. https://x.com/AnthropicAI/status/2077026346375540870

- URL: https://x.com/AnthropicAI/status/2077026346375540870
- Type: Post
- Published: 2026-07-14T13:44:04+00:00
- Digest summary: We’re committing $10 million CAD and partnering with leading AI institutions in Canada to help fund new AI research. https://t.co/A8wpanWYQO

### 47. https://x.com/danshipper/status/2076996862939205848

- URL: https://x.com/danshipper/status/2076996862939205848
- Type: Post
- Published: 2026-07-14T11:46:55+00:00
- Digest summary: im sorry this is very strange and unnecessary i actually like the tagline but we don't need the shots of *checks notes* burning houses and graves!

### 48. https://x.com/mustafasuleyman/status/2076991204705624434

- URL: https://x.com/mustafasuleyman/status/2076991204705624434
- Type: Post
- Published: 2026-07-14T11:24:26+00:00
- Digest summary: Fully support this important proposal from @demishassabis. The time for us all to act is now. "...we must use this precious window before AGI arrives to shape this technology for the benefit of all humanity."

### 49. https://x.com/demishassabis/status/2076957440109625718

- URL: https://x.com/demishassabis/status/2076957440109625718
- Type: Post
- Published: 2026-07-14T09:10:16+00:00
- Digest summary: https://t.co/PTeDiv1b6L

### 50. https://x.com/steipete/status/2076923300593422560

- URL: https://x.com/steipete/status/2076923300593422560
- Type: Post
- Published: 2026-07-14T06:54:36+00:00
- Digest summary: I moved our maintainer agent to the cloud and they are fighting already. https://t.co/LKq0st8sns

### 51. https://x.com/steipete/status/2076917691139674373

- URL: https://x.com/steipete/status/2076917691139674373
- Type: Post
- Published: 2026-07-14T06:32:19+00:00
- Digest summary: We shipped! iOS and Android apps also got updates and they look great. Had to bump Node to keep things smooth, if the autoupdater doesn't work, run the web installer and it'll take care of that for you.

### 52. https://x.com/elonmusk/status/2076909201524203973

- URL: https://x.com/elonmusk/status/2076909201524203973
- Type: Post
- Published: 2026-07-14T05:58:35+00:00
- Digest summary: Grok 4.5 reaches #1 position on Long-Horizon Terminal-Bench

### 53. https://x.com/thsottiaux/status/2076907789763621237

- URL: https://x.com/thsottiaux/status/2076907789763621237
- Type: Post
- Published: 2026-07-14T05:52:58+00:00
- Digest summary: Tomorrow might be 8M active user celebration day. Just saying

### 54. https://x.com/amasad/status/2076907304897974775

- URL: https://x.com/amasad/status/2076907304897974775
- Type: Post
- Published: 2026-07-14T05:51:03+00:00
- Digest summary: Our code https://t.co/MfiTND4bSA

### 55. https://x.com/AravSrinivas/status/2076907075834355749

- URL: https://x.com/AravSrinivas/status/2076907075834355749
- Type: Post
- Published: 2026-07-14T05:50:08+00:00
- Digest summary: Sometimes, the optimal action is no action.

### 56. https://x.com/elonmusk/status/2076905740531302479

- URL: https://x.com/elonmusk/status/2076905740531302479
- Type: Post
- Published: 2026-07-14T05:44:50+00:00
- Digest summary: The woke mob had turned Twitter into Wormtongue to the World https://t.co/XUcA15vImB

### 57. https://x.com/thsottiaux/status/2076894071323537898

- URL: https://x.com/thsottiaux/status/2076894071323537898
- Type: Post
- Published: 2026-07-14T04:58:28+00:00
- Digest summary: ChatGPT Work presents https://t.co/pY5Vei9OIz

### 58. https://x.com/levie/status/2076882332821373381

- URL: https://x.com/levie/status/2076882332821373381
- Type: Post
- Published: 2026-07-14T04:11:49+00:00
- Digest summary: A few thoughts on what we will see in AI structurally for the foreseeable future: * Frontier intelligence continues unabated and pushes the industry forward continuously. The top labs will continue to buy the best and the most data, build the most compute, be at the forefront of improved training breakthroughs, and so on. A few different approaches stratify the market on pricing and capability, but overall competitive pressure brings down pricing on a per task basis. That said, we just ask more from the models over time - as one thing gets cheaper, we just use more - so frontier spend and use remains robust. * Open weights rapidly absorbs frontier breakthroughs (and drives other breakthrough directions given the constraints), offering both lower cost intelligence and the ability to be post

### 59. https://x.com/gdb/status/2076878421314195745

- URL: https://x.com/gdb/status/2076878421314195745
- Type: Post
- Published: 2026-07-14T03:56:16+00:00
- Digest summary: GPT-5.6 is now generally available on Bedrock:

### 60. https://x.com/_catwu/status/2076867882894684314

- URL: https://x.com/_catwu/status/2076867882894684314
- Type: Post
- Published: 2026-07-14T03:14:24+00:00
- Digest summary: Artifacts just got an upgrade!

### 61. https://x.com/levie/status/2076839463410671637

- URL: https://x.com/levie/status/2076839463410671637
- Type: Post
- Published: 2026-07-14T01:21:28+00:00
- Digest summary: Here’s a great post on driving down costs, while maintaining high performance, with frontier intelligence as a manager and lower cost models for the workhorse tasks. This will be the template for what model routing looks like in the future. “We started this experiment expecting to measure how much Fable’s 2x premium would increase cost. We were surprised to find that Fable’s effective delegation actually decreased cost overall. It specified constraints and outcomes instead of spelling out the implementation, gave feedback instead of making fixes itself, and in most cases never touched the code at all. These are the habits of a good manager.” The industry is increasingly figuring out what it looks like to mix models together to be able to get targeted performance levels and optimal cost str

### 62. https://x.com/sama/status/2076824686307271125

- URL: https://x.com/sama/status/2076824686307271125
- Type: Post
- Published: 2026-07-14T00:22:45+00:00
- Digest summary: i thought this was satire, kept looking for the handle to be spelled c1audeai or something

### 63. https://x.com/sama/status/2076823209589313910

- URL: https://x.com/sama/status/2076823209589313910
- Type: Post
- Published: 2026-07-14T00:16:53+00:00
- Digest summary: still sorta breaks my brain to see our models be good at design finally

### 64. https://x.com/adityaag/status/2076821102194721167

- URL: https://x.com/adityaag/status/2076821102194721167
- Type: Post
- Published: 2026-07-14T00:08:30+00:00
- Digest summary: I don't know if I am using Codex or ChatGPT (wtf) But I do know that I am asking a AGI LEVEL coding agent: "What necklaces does Benson Boone wear? (for my daughter) https://t.co/ctFiYytqiE

## Firsthand AI Digest Detail Pages

## Original Sources

### 1. lobste.rs is now running on SQLite

- Type: web
- URL: https://simonwillison.net/2026/Jul/14/lobsters-sqlite/
- Title: lobste.rs is now running on SQLite
- Description: Community site Lobsters has been planning a migration away from MariaDB since August 2018 - originally targeting PostgreSQL, but last year they decided to investigate SQLite instead. This weekend they …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/4b48aSh - Teleport
  - https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite - lobste.rs is now running on SQLite
  - https://lobste.rs - Lobsters
  - https://github.com/lobsters/lobsters/issues/539 - since August 2018
  - https://github.com/rack/rack-attack - Rack::Attack
  - https://github.com/lobsters/lobsters/pull/1927 - SQLite migration PR
  - https://github.com/lobsters/lobsters/pull/1705 - #1705
  - https://github.com/lobsters/lobsters/pull/1871 - #1871
  - https://github.com/lobsters/lobsters/pull/1924 - #1924
  - https://simonwillison.net/2026/Jul/14/ - 14th July 2026
  - https://simonwillison.net/2026/Jul/9/gpt-5-6/ - The new GPT-5.6 family: Luna, Terra, Sol
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - sqlite-utils 4.0, now with database schema migrations
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/ - sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
  - https://simonwillison.net/tags/migrations/ - migrations 12
  - https://simonwillison.net/tags/ops/ - ops 20
  - https://simonwillison.net/tags/rails/ - rails 111
  - https://simonwillison.net/tags/sqlite/ - sqlite 480
  - https://simonwillison.net/tags/lobsters/ - lobsters 4

Excerpt:

lobste.rs is now running on SQLite Simon Willison’s Weblog Subscribe Sponsored by: Teleport — How do you ensure that AI agents act within your intended boundaries? Teleport’s “From Zero Trust to Agent Trust” white paper details what needs to be in place to realize the promise of agentic designs. 14th July 2026 - Link Blog lobste.rs is now running on SQLite . Community site Lobsters has been planning a migration away from MariaDB since August 2018 - originally targeting PostgreSQL, but last year they decided to investigate SQLite instead. This weekend they completed the migration, and now consider it stable enough that it looks like this is the permanent architecture for the site going forward: SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB. There's also a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack_attack database used by the Rack::Attack middleware for blocking and throttling abusive requests. There are plenty more details in both the linked thread and this SQLite migration PR by Thomas Dziedzic, which added 735 lines and removed 593 lines across 30 commits and 188 files. That PR built on top of previous PRs #1705 , #1871 , and #1924 . This is a really useful case study, and a great reminder that you can get a whole lot done with a single server and SQLite in 2026. Posted 14th July 2026 at 7:44 pm Recent articles The new GPT-5.6 family: Luna, Terra, Sol - 9th July 2026 sqlite-utils 4.0, now with database schema migrations - 7th July 2026 sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25) - 5th July 2026 This is a link post by Simon Willison, posted on 14th July 2026 . migrations 12 ops 20 rails 111 sqlite 480 lobsters 4 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 2. A quote from Armin Ronacher

- Type: web
- URL: https://simonwillison.net/2026/Jul/14/armin-ronacher/
- Title: A quote from Armin Ronacher
- Description: The shared language of a software project is not English or Python but it is the common understanding of what its concepts mean, where the boundaries are, which invariants matter, …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/4b48aSh - Teleport
  - https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/ - Armin Ronacher
  - https://simonwillison.net/2026/Jul/14/ - 14th July 2026
  - https://simonwillison.net/2026/Jul/9/gpt-5-6/ - The new GPT-5.6 family: Luna, Terra, Sol
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - sqlite-utils 4.0, now with database schema migrations
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/ - sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
  - https://simonwillison.net/tags/armin-ronacher/ - armin-ronacher 25
  - https://simonwillison.net/tags/software-engineering/ - software-engineering 63
  - https://simonwillison.net/tags/ai/ - ai 2,117
  - https://simonwillison.net/tags/generative-ai/ - generative-ai 1,872
  - https://simonwillison.net/tags/llms/ - llms 1,839
  - https://simonwillison.net/tags/ai-assisted-programming/ - ai-assisted-programming 398
  - https://simonwillison.net/tags/coding-agents/ - coding-agents 222
  - https://simonwillison.net/tags/agentic-engineering/ - agentic-engineering 58
  - https://simonwillison.net/2002/ - 2002
  - https://simonwillison.net/2003/ - 2003
  - https://simonwillison.net/2004/ - 2004
  - https://simonwillison.net/2005/ - 2005

Excerpt:

A quote from Armin Ronacher Simon Willison’s Weblog Subscribe Sponsored by: Teleport — How do you ensure that AI agents act within your intended boundaries? Teleport’s “From Zero Trust to Agent Trust” white paper details what needs to be in place to realize the promise of agentic designs. 14th July 2026 The shared language of a software project is not English or Python but it is the common understanding of what its concepts mean, where the boundaries are, which invariants matter, who owns what, and why the system has the shape it does. This language is rarely written down in one place. It lives partly in documentation and code, but also in code review, conversations, arguments, and the experience of having to explain a change to somebody else. Before agents, some of this shared understanding was maintained by friction. If I wanted to change your storage layer, I usually had to read your code, ask you questions, and perhaps coordinate with another team whose service depended on it. This was slow, and much of that slowness was waste but not all of it was. Some of it was the process by which your understanding became mine, and by which both of us discovered whether we still agreed about how the system worked. This friction synchronizes people. — Armin Ronacher , The Tower Keeps Rising Posted 14th July 2026 at 6:04 pm Recent articles The new GPT-5.6 family: Luna, Terra, Sol - 9th July 2026 sqlite-utils 4.0, now with database schema migrations - 7th July 2026 sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25) - 5th July 2026 This is a quotation collected by Simon Willison, posted on 14th July 2026 . armin-ronacher 25 software-engineering 63 ai 2,117 generative-ai 1,872 llms 1,839 ai-assisted-programming 398 coding-agents 222 agentic-engineering 58 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 3. Release: datasette 1.0a37

- Type: web
- URL: https://simonwillison.net/2026/Jul/14/datasette/
- Title: Release: datasette 1.0a37
- Description: An open source multi-tool for exploring and publishing data
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/4b48aSh - Teleport
  - https://simonwillison.net/elsewhere/release/ - Release
  - https://github.com/simonw/datasette/releases/tag/1.0a37 - datasette 1.0a37
  - https://docs.datasette.io/en/latest/authentication.html - documentation
  - https://simonwillison.net/2026/Jul/14/ - 14th July 2026
  - https://simonwillison.net/2026/Jul/9/gpt-5-6/ - The new GPT-5.6 family: Luna, Terra, Sol
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - sqlite-utils 4.0, now with database schema migrations
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/ - sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
  - https://simonwillison.net/tags/datasette/ - datasette 1,526
  - https://github.com/sponsors/simonw/ - Sponsor & subscribe
  - https://simonwillison.net/2002/ - 2002
  - https://simonwillison.net/2003/ - 2003
  - https://simonwillison.net/2004/ - 2004
  - https://simonwillison.net/2005/ - 2005
  - https://simonwillison.net/2006/ - 2006
  - https://simonwillison.net/2007/ - 2007
  - https://simonwillison.net/2008/ - 2008
  - https://simonwillison.net/2009/ - 2009

Excerpt:

Release: datasette 1.0a37 Simon Willison’s Weblog Subscribe Sponsored by: Teleport — How do you ensure that AI agents act within your intended boundaries? Teleport’s “From Zero Trust to Agent Trust” white paper details what needs to be in place to realize the promise of agentic designs. 14th July 2026 Release datasette 1.0a37 — An open source multi-tool for exploring and publishing data A minor release. Performance and documentation improvements to the permissions system, plus I reverted a cosmetic API change which caused almost every existing plugin test suite to break. Posted 14th July 2026 at 4:31 pm Recent articles The new GPT-5.6 family: Luna, Terra, Sol - 9th July 2026 sqlite-utils 4.0, now with database schema migrations - 7th July 2026 sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25) - 5th July 2026 This is a beat by Simon Willison, posted on 14th July 2026 . datasette 1,526 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 4. https://openai.com/index/managing-ai-investments-in-agentic-era

- Type: official/blog
- URL: https://openai.com/index/managing-ai-investments-in-agentic-era
- Fetch status: limited (HTTP 403: Forbidden)

### 5. AI 早报 2026-07-14

- Type: web
- URL: https://daily.juya.uk/issues/2026-07-14/
- Title: AI 早报 2026-07-14
- Links:
  - https://daily.juya.uk/ - 首页
  - https://daily.juya.uk/archive/ - 归档
  - https://daily.juya.uk/rss.xml - RSS
  - https://daily.juya.uk/markdown/2026-07-14.md - Markdown
  - https://www.bilibili.com/video/BV1qeNX6tE8V - 哔哩哔哩
  - https://www.youtube.com/watch?v=9WqCAZoQZBk - YouTube
  - https://x.com/thsottiaux/status/2076735790567338203 - ↗
  - https://x.com/thsottiaux/status/2076543065045795309 - ↗
  - https://www.actava.ai/cura - ↗
  - https://mp.weixin.qq.com/s/vKFCa9FfoGBUGK8J1MhFag - ↗
  - https://x.com/ClaudeDevs/status/2076789349145092230 - ↗
  - https://applink.feishu.cn/client/message/link/open?token=Amjtw5fSSAADalS8pCYPS8A%3D - ↗
  - https://www.reddit.com/r/LocalLLaMA/comments/1ut7tis/comment/ox4zamk/ - ↗
  - https://mp.weixin.qq.com/s/YvKYAZzgNK4Chh2JpQM5jg - ↗
  - https://www.anthropic.com/research/claude-values-models-languages - ↗
  - https://about.fb.com/news/2026/07/teachers-local-businesses-win-as-meta-expands-louisiana-data-center/ - ↗
  - https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/ - ↗
  - https://www.msit.go.kr/bbs/view.do?sCode=user&mPid=121&mId=311&bbsSeqNo=100&nttSeqNo=3186816 - ↗
  - https://x.com/thsottiaux/status/2076543971216830551 - https://x.com/thsottiaux/status/2076543971216830551
  - https://github.com/actava-ai/Cura - https://github.com/actava-ai/Cura

Excerpt:

AI 早报 2026-07-14 首页 归档 RSS 2026-07-14 · Markdown AI 早报 2026-07-14 视频版 ： 哔哩哔哩 ｜ YouTube 概览 要闻 Codex 周活用户达 700 万，官方发放重置额度致庆 ↗ #1 Codex 更新：GPT-5.6 Sol上下文回滚至272k并修复多Agent消耗 ↗ #2 模型发布 actAVA发布医疗模型Cura 1T ↗ #3 腾讯混元全栈开源 HyOCR-1.5 ↗ #4 开发生态 Claude Code Artifacts 支持公开分享与多人编辑 ↗ #5 GLM Coding Plan 专项治理违规账号 ↗ #6 Grok Build CLI 被指上传完整代码库，官方已服务端禁用 ↗ #7 产品应用 阶跃星辰发布Step AOS与智能体手机STEPX Neo ↗ #8 技术与洞察 Anthropic研究揭示Claude价值观在模型与语言间存在差异 ↗ #9 行业动态 Meta扩展路易斯安那州数据中心至5GW算力，总投资超500亿美元 ↗ #10 消息称 Nous Research 洽谈新融资 估值达15亿美元 ↗ #11 韩国科信部启动全民AI项目 ↗ #12 要闻 Codex 周活用户达 700 万，官方发放重置额度致庆 #1 Codex 与 ChatGPT Work 的活跃用户数已达 700 万，为庆祝这一里程碑，OpenAI 向所有账户额外提供了一次“banked reset”，可用于手动重置使用额度。 OpenAI 宣布 Codex 和 ChatGPT Work 的周活跃用户数已达到 700 万。为此，团队向所有账户额外提供了一次“banked reset”额度，可用于手动重置每周使用额度。该重置可在桌面或网页客户端使用，应用后将立即补满当周的使用额度。 相关链接： https://x.com/thsottiaux/status/2076735790567338203 Codex 更新：GPT-5.6 Sol上下文回滚至272k并修复多Agent消耗 #2 OpenAI宣布通过推理优化，为Codex用户带来了约百分之十的 GPT-5.6 Sol 用量提升。同时，为排查额外消耗来源而进行的{推理努力实验|"推理努力实验"}也已回滚。由于提升至372k上下文限制导致消耗远超预期，官方已将其调整至272k。官方再次否认{超272k存在双倍计费|"超272k存在双倍计费"}的说法，解释额外消耗主要源于较长的上下文在多次工具调用之间反复传递而导致的缓存读取成本上升，目前正调整系统以在未来重新支持372k的上限。 OpenAI开发者Tibo宣布，通过推理优化为GPT-5.6 Sol订阅用户带来约10%用量提升。官方将上下文限制从272k升至372k后，消耗远超预期，已回滚至272k并计划未来重新推出，同步回滚推理努力实验调整，5小时使用限制继续暂停。针对开发者Theo关于超272k双倍计费导致用量暴增的说法，Tibo明确否认，强调官方控制所有设置，不会加收费用；解释超额消耗真正原因是上下文在工具调用间移动导致缓存读取成本上升，最大上下文长度并非成本甜点。官方正调整系统以在不增加计费使用量情况下恢复372k。此外，官方正修复多Agent高推理努力下消耗偏高及自动审查效率问题。 相关链接： https://x.com/thsottiaux/status/2076543065045795309 https://x.com/thsottiaux/status/2076543971216830551 模型发布 actAVA发布医疗模型Cura 1T #3 actAVA推出万亿参数医疗模型 Cura 1T，该模型基于Kimi-K2.6微调，专注患者护理、临床推理及医疗Agentic工作流，在六项医疗基准中五项得分领先。actAVA同步开源了评估工具cura-eval。 actAVA发布万亿参数医疗模型Cura 1T，微调自Kimi-K2.6，采用递归自我改进机制训练以处理患者护理、临床推理和医疗Agentic工作流。官方数据显示，该模型在HealthBench Hard等6项医疗基准中的5项得分领先，在MedXpertQA-Multimodal上排名第二，同时其通用能力在各域外榜单保持前五。同步开源了模型无关的评估工具cura-eval。官方强调Cura 1T为研究模型，非医疗服务替代品。 相关链接： https://www.actava.ai/cura https://github.com/actava-ai/Cura 腾讯混元全栈开源 HyOCR-1.5 #4 腾讯混元团队全栈开源{1B参数|"1B参数"}{端到端OCR大模型|"端到端OCR大模型"}{Hy|混元}OCR-1.5。该模型在OmniDocBench基准取得SOTA。并引入DFlash投机解码最高提速6.37倍，还支持普通笔记本本地部署。 腾讯混元团队全栈开源 1B 参数端到端 OCR 大模型 HyOCR-1.5，公开其数据构造方法、训练配方与推理框架。该模型引入基于约 90.7M 草稿模型的 DFlash 投机解码框架，官方称在 Transformers 下实现 6.37 倍加速，并支持通过 llama.cpp 在 CPU、消费级显卡及普通笔记本上本地部署。训练方面，其采用 Agentic Data Flow 构造低资源语种、古文字与多图问答数据，并将最大图像分辨率提升至 4K、上下文扩展至 128K。官方称该模型在 OmniDocBench v1.6 等多个基准取得 SOTA，但也坦承在 CHAOS-Bench 幻觉抑制测试中绝对值仍偏低。 相关链接： https://mp.weixin.qq.com/s/vKFCa9FfoGBUGK8J1MhFag https://github.com/Tencent-Hunyuan/HunyuanOCR 开发生态 Claude Co

### 6. TIL: Using uvx in GitHub Actions in a cache-friendly way

- Type: web
- URL: https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/
- Title: TIL: Using uvx in GitHub Actions in a cache-friendly way
- Description: I often find myself wanting to run a quick Python tool inside of GitHub Actions using `uvx name-of-tool` - but I don't want that to result in a network request …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/4b48aSh - Teleport
  - https://til.simonwillison.net/github-actions/uvx-github-actions-cache
  - https://simonwillison.net/elsewhere/til/ - TIL
  - https://github.com/astral-sh/setup-uv/issues/745 - issue
  - https://simonwillison.net/2026/Jul/14/ - 14th July 2026
  - https://simonwillison.net/2026/Jul/9/gpt-5-6/ - The new GPT-5.6 family: Luna, Terra, Sol
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - sqlite-utils 4.0, now with database schema migrations
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/ - sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
  - https://simonwillison.net/tags/packaging/ - packaging 50
  - https://simonwillison.net/tags/pypi/ - pypi 48
  - https://simonwillison.net/tags/python/ - python 1,264
  - https://simonwillison.net/tags/github-actions/ - github-actions 68
  - https://simonwillison.net/tags/uv/ - uv 96
  - https://github.com/sponsors/simonw/ - Sponsor & subscribe
  - https://simonwillison.net/2002/ - 2002
  - https://simonwillison.net/2003/ - 2003
  - https://simonwillison.net/2004/ - 2004
  - https://simonwillison.net/2005/ - 2005

Excerpt:

TIL: Using uvx in GitHub Actions in a cache-friendly way Simon Willison’s Weblog Subscribe Sponsored by: Teleport — How do you ensure that AI agents act within your intended boundaries? Teleport’s “From Zero Trust to Agent Trust” white paper details what needs to be in place to realize the promise of agentic designs. 14th July 2026 TIL Using uvx in GitHub Actions in a cache-friendly way — I often find myself wanting to run a quick Python tool inside of GitHub Actions using `uvx name-of-tool` - but I don't want that to result in a network request to PyPI every time the workflow runs. I want the tool to be fetched the first time and then reused from the GitHub Actions cache for subsequent runs. I finally found a cache-friendly recipe for using uvx tool-name in GitHub Actions workflows that I like. The trick is setting a UV_EXCLUDE_NEWER: "2026-07-12" environment variable at the start of the workflow and then using that as part of the GitHub Actions cache key. This means any uvx tool-name commands will resolve to the most recent version as-of that date, and you can bust the cache and upgrade the tools by bumping the date in the future. My goal here is to use Python tools in GitHub Actions without every run of the workflow hitting PyPI to download a fresh copy of the tool and its dependencies. Update : Here's an existing issue against the astral-sh/setup-uv repository requesting that they switch the default to cache rather than purge wheels from PyPI. Posted 14th July 2026 at 12:56 am Recent articles The new GPT-5.6 family: Luna, Terra, Sol - 9th July 2026 sqlite-utils 4.0, now with database schema migrations - 7th July 2026 sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25) - 5th July 2026 This is a beat by Simon Willison, posted on 14th July 2026 . packaging 50 pypi 48 python 1,264 github-actions 68 uv 96 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 7. Who Owns the Sea? – Sarah Paine

- Type: video
- URL: https://www.youtube.com/watch?v=ATEUNCLS2Lo
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 8. Improved Intelligence with GPT-Live

- Type: video
- URL: https://www.youtube.com/watch?v=avpZWh6sm9M
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 9. Build and publish web apps directly in ChatGPT

- Type: video
- URL: https://www.youtube.com/watch?v=8zH_O74hZBw
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 10. Reconstructing Pelé’s lost goal

- Type: video
- URL: https://www.youtube.com/watch?v=R-Yqes8AotY
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 11. https://x.com/swyx/status/2077142073472590041

- Type: x-post
- URL: https://x.com/swyx/status/2077142073472590041
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 12. https://x.com/adityaag/status/2077136023616962651

- Type: x-post
- URL: https://x.com/adityaag/status/2077136023616962651
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 13. https://x.com/petergyang/status/2077132606798442817

- Type: x-post
- URL: https://x.com/petergyang/status/2077132606798442817
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 14. https://x.com/adityaag/status/2077130899733553560

- Type: x-post
- URL: https://x.com/adityaag/status/2077130899733553560
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 15. https://x.com/petergyang/status/2077118932952264800

- Type: x-post
- URL: https://x.com/petergyang/status/2077118932952264800
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 16. https://x.com/sama/status/2077118672150388816

- Type: x-post
- URL: https://x.com/sama/status/2077118672150388816
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 17. https://x.com/kevinweil/status/2077118363663499335

- Type: x-post
- URL: https://x.com/kevinweil/status/2077118363663499335
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 18. https://x.com/petergyang/status/2077115676893057233

- Type: x-post
- URL: https://x.com/petergyang/status/2077115676893057233
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 19. https://x.com/thsottiaux/status/2077114635308986427

- Type: x-post
- URL: https://x.com/thsottiaux/status/2077114635308986427
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 20. https://x.com/ryolu_/status/2077108336844210352

- Type: x-post
- URL: https://x.com/ryolu_/status/2077108336844210352
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 21. https://x.com/ryolu_/status/2077107655894860137

- Type: x-post
- URL: https://x.com/ryolu_/status/2077107655894860137
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 22. https://x.com/sama/status/2077106587307798989

- Type: x-post
- URL: https://x.com/sama/status/2077106587307798989
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 23. https://x.com/AravSrinivas/status/2077105849638728118

- Type: x-post
- URL: https://x.com/AravSrinivas/status/2077105849638728118
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 24. https://x.com/petergyang/status/2077103041397084269

- Type: x-post
- URL: https://x.com/petergyang/status/2077103041397084269
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 25. https://x.com/danshipper/status/2077100057136894166

- Type: x-post
- URL: https://x.com/danshipper/status/2077100057136894166
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 26. https://x.com/danshipper/status/2077094235640156199

- Type: x-post
- URL: https://x.com/danshipper/status/2077094235640156199
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 27. https://x.com/petergyang/status/2077093016620384401

- Type: x-post
- URL: https://x.com/petergyang/status/2077093016620384401
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 28. https://x.com/steipete/status/2077088803500818682

- Type: x-post
- URL: https://x.com/steipete/status/2077088803500818682
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 29. https://x.com/sundarpichai/status/2077086951833063580

- Type: x-post
- URL: https://x.com/sundarpichai/status/2077086951833063580
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 30. https://x.com/fchollet/status/2077084408633503774

- Type: x-post
- URL: https://x.com/fchollet/status/2077084408633503774
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 31. https://x.com/swyx/status/2077072402828361772

- Type: x-post
- URL: https://x.com/swyx/status/2077072402828361772
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 32. https://x.com/ryolu_/status/2077060449837990399

- Type: x-post
- URL: https://x.com/ryolu_/status/2077060449837990399
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 33. https://x.com/danshipper/status/2077058541853061466

- Type: x-post
- URL: https://x.com/danshipper/status/2077058541853061466
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 34. https://x.com/sama/status/2077053140508266710

- Type: x-post
- URL: https://x.com/sama/status/2077053140508266710
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 35. https://x.com/claudeai/status/2077047278078931243

- Type: x-post
- URL: https://x.com/claudeai/status/2077047278078931243
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 36. https://x.com/petergyang/status/2077047201889747096

- Type: x-post
- URL: https://x.com/petergyang/status/2077047201889747096
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 37. https://x.com/elonmusk/status/2077044528234553709

- Type: x-post
- URL: https://x.com/elonmusk/status/2077044528234553709
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 38. https://x.com/levie/status/2077043523703243070

- Type: x-post
- URL: https://x.com/levie/status/2077043523703243070
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 39. https://x.com/elonmusk/status/2077043449279262954

- Type: x-post
- URL: https://x.com/elonmusk/status/2077043449279262954
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 40. https://x.com/sama/status/2077042528906527225

- Type: x-post
- URL: https://x.com/sama/status/2077042528906527225
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 41. https://x.com/sama/status/2077037818824843719

- Type: x-post
- URL: https://x.com/sama/status/2077037818824843719
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 42. https://x.com/sama/status/2077036999303999910

- Type: x-post
- URL: https://x.com/sama/status/2077036999303999910
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 43. https://x.com/danshipper/status/2077036035062554906

- Type: x-post
- URL: https://x.com/danshipper/status/2077036035062554906
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 44. https://x.com/sama/status/2077033807736459713

- Type: x-post
- URL: https://x.com/sama/status/2077033807736459713
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 45. https://x.com/fchollet/status/2077033256365736098

- Type: x-post
- URL: https://x.com/fchollet/status/2077033256365736098
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 46. https://x.com/AnthropicAI/status/2077026346375540870

- Type: x-post
- URL: https://x.com/AnthropicAI/status/2077026346375540870
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 47. https://x.com/danshipper/status/2076996862939205848

- Type: x-post
- URL: https://x.com/danshipper/status/2076996862939205848
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 48. https://x.com/mustafasuleyman/status/2076991204705624434

- Type: x-post
- URL: https://x.com/mustafasuleyman/status/2076991204705624434
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 49. https://x.com/demishassabis/status/2076957440109625718

- Type: x-post
- URL: https://x.com/demishassabis/status/2076957440109625718
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 50. https://x.com/steipete/status/2076923300593422560

- Type: x-post
- URL: https://x.com/steipete/status/2076923300593422560
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 51. https://x.com/steipete/status/2076917691139674373

- Type: x-post
- URL: https://x.com/steipete/status/2076917691139674373
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 52. https://x.com/elonmusk/status/2076909201524203973

- Type: x-post
- URL: https://x.com/elonmusk/status/2076909201524203973
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 53. https://x.com/thsottiaux/status/2076907789763621237

- Type: x-post
- URL: https://x.com/thsottiaux/status/2076907789763621237
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 54. https://x.com/amasad/status/2076907304897974775

- Type: x-post
- URL: https://x.com/amasad/status/2076907304897974775
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 55. https://x.com/AravSrinivas/status/2076907075834355749

- Type: x-post
- URL: https://x.com/AravSrinivas/status/2076907075834355749
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 56. https://x.com/elonmusk/status/2076905740531302479

- Type: x-post
- URL: https://x.com/elonmusk/status/2076905740531302479
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 57. https://x.com/thsottiaux/status/2076894071323537898

- Type: x-post
- URL: https://x.com/thsottiaux/status/2076894071323537898
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 58. https://x.com/levie/status/2076882332821373381

- Type: x-post
- URL: https://x.com/levie/status/2076882332821373381
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 59. https://x.com/gdb/status/2076878421314195745

- Type: x-post
- URL: https://x.com/gdb/status/2076878421314195745
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 60. https://x.com/_catwu/status/2076867882894684314

- Type: x-post
- URL: https://x.com/_catwu/status/2076867882894684314
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 61. https://x.com/levie/status/2076839463410671637

- Type: x-post
- URL: https://x.com/levie/status/2076839463410671637
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 62. https://x.com/sama/status/2076824686307271125

- Type: x-post
- URL: https://x.com/sama/status/2076824686307271125
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 63. https://x.com/sama/status/2076823209589313910

- Type: x-post
- URL: https://x.com/sama/status/2076823209589313910
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 64. https://x.com/adityaag/status/2076821102194721167

- Type: x-post
- URL: https://x.com/adityaag/status/2076821102194721167
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

## Secondary Source Candidates

These links were discovered from first-layer sources. Use them to reach primary material when the first-layer source is commentary or a link blog.

### 1. lobste.rs is now running on SQLite

- Type: web
- URL: https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite
- Title: lobste.rs is now running on SQLite
- Description: 92 comments
- Links:
  - https://lobste.rs/
  - https://lobste.rs/active - Active
  - https://lobste.rs/recent - Recent
  - https://lobste.rs/comments - Comments
  - https://lobste.rs/search - Search
  - https://lobste.rs/login - Login
  - https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite - lobste.rs is now running on SQLite
  - https://lobste.rs/t/meta - meta
  - https://lobste.rs/~thomas0
  - https://lobste.rs/~pushcx - @pushcx
  - https://github.com/lobsters/lobsters/pull/1927 - SQLite pull request
  - https://gist.github.com/pushcx/eb7cdf2dc9707dc3ab9e7173d197ddfc?permalink_comment_id=6251610 - "We're having a quiet Monday."
  - https://github.com/lobsters/lobsters/issues/539 - #539 Migrate to SQLite
  - https://lobste.rs/s/zzprkr/weekly_lobsters_office_hours - lobsters office hours
  - https://github.com/lobsters/lobsters/pull/1705 - first pull request attempt
  - https://github.com/lobsters/lobsters/pull/1871 - second PR attempt
  - https://github.com/lobsters/lobsters/blob/main/lib/tasks/migrate.rake - database x to database y script
  - https://gist.github.com/pushcx/eb7cdf2dc9707dc3ab9e7173d197ddfc/a11e6d5865776f3bb4e1adbc56582a3b1f99878c - checklist
  - https://github.com/lobsters/lobsters/pull/1924 - revert
  - https://github.com/lobsters/lobsters/pull/1927/changes/e7630ffe5c0df9fc0a388db5b6b6e11eb4a4c407 - minor issues with search

Excerpt:

lobste.rs is now running on SQLite | Lobsters Active Recent Comments Search Login Login 384 lobste.rs is now running on SQLite ☶ meta authored by thomas0 27 hours ago | 92 comments This past Saturday, @pushcx and I deployed the SQLite pull request to production. We were waiting till this morning to see how it would react to the Monday traffic spike before making this post. Needless to say, SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down, and finally "We're having a quiet Monday." . Finally #539 Migrate to SQLite was closed this morning. Let us know if you have any questions about the migration. Background Story: I got involved with this migration because back in 2019 I stumbled upon #539 and because I had lots of experience working with, managing and migrating largish databases, I left a comment suggesting MySQL as an alternative, because of the compatibility between MariaDB and MySQL. At that time I wasn't planning on getting involved since there were already conversations in place to migrate to PostgreSQL. Fast forward to 2025, Rahul left a comment mentioning K1's acquisition of MariaDB. A discussion around the details of migrating to postgresql proceeded. Then in February, Rahul asked "Can lobsters run on sqlite? which included a very detailed post around SQLite. I officially showed interest in taking on this project in June 2025 . I think this somehow got mentioned in lobsters office hours but it has been so long since then that I don't rememeber for certain. In August 2025 I opened my first pull request attempt when I got busy and couldn't attend to the PR. Github closed it as stale and I couldn't reopen it so I opened another PR. The second PR attempt included some performance testing, a database x to database y script (since none of the existing mariadb/mysql to sqlite scripts satisfied me), debugging and thinking around data integrity. Then came the first deploy on Feb 21st. @pushcx and I got on a call, came up with a checklist for the deployment. Everything went right up until the deployment of the PR. Once deployed the site was in readonly mode, but just the readonly traffic was spiking all the cpus to 100%. We couldn't figure out what the problem was so we decided to revert . I didn't feel great after that first failed deploy since I knew that performance could be a problem due to not having access to the production

### 2. The Tower Keeps Rising

- Type: web
- URL: https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/
- Title: The Tower Keeps Rising
- Published: 2026-07-13T00:00:00
- Description: Vibecoding and the possible collapse of a shared language.
- Links:
  - https://lucumr.pocoo.org/about/ - Armin Ronacher
  - https://lucumr.pocoo.org/ - blog
  - https://lucumr.pocoo.org/archive/ - archive
  - https://lucumr.pocoo.org/projects/ - projects
  - https://lucumr.pocoo.org/travel/ - travel
  - https://lucumr.pocoo.org/talks/ - talks
  - https://en.wikipedia.org/wiki/The_Tower_of_Babel_(Bruegel) - “The Tower of Babel”
  - https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/ - 1
  - https://www.biblegateway.com/passage/?search=Genesis%2011%3A3-6&version=KJV - Genesis 11:3-6, KJV
  - https://lucumr.pocoo.org/tags/ai/ - ai
  - https://lucumr.pocoo.org/tags/thoughts/ - thoughts
  - https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising.md - copy as
  - https://creativecommons.org/licenses/by-nc/4.0/ - License
  - https://bsky.app/profile/mitsuhiko.at - bluesky
  - http://x.com/mitsuhiko - x
  - http://github.com/mitsuhiko - github
  - https://github.com/sponsors/mitsuhiko/ - sponsor me on github
  - https://lucumr.pocoo.org/about - imprint
  - https://lucumr.pocoo.org/ai-transparency - AI transparency
  - https://lucumr.pocoo.org/feed.atom - atom

Excerpt:

The Tower Keeps Rising | Armin Ronacher's Thoughts and Writings Armin Ronacher 's Thoughts and Writings blog archive projects travel talks about The Tower Keeps Rising written on July 13, 2026 I feel that some vibecoded software changes somewhat randomly and unexpectedly. That made me think about Bruegel’s “The Tower of Babel” which shows an already quite chaotic depiction of the Tower of Babel. The story is usually told as one about pride and ambition and ultimately why people no longer speak the same language. But it is also a story about the unity that makes technological progress work. The text begins with a technology upgrade: And they said one to another, Go to, let us make brick, and burn them thoroughly. And they had brick for stone, and slime had they for morter. They use it for a civilizational project: let us build us a city and a tower, whose top may reach unto heaven But when God assesses the situation the bricks are not what concern him: the people is one, and they have all one language, […] and now nothing will be restrained from them. 1 The source of their power is coordination. They share a language and with that shared language they can combine their work into something no one of them could build alone. God does not take away the bricks or their knowledge of how to make them. He takes away their ability to understand one another, and construction stops. There is the appealing idea that AI-assisted programming means better tools which lets us build more ambitious software. That is certainly true at the level of the individual and without doubt a developer with an agent will be dramatically more capable of changing a codebase. But large software projects have never been limited only by how quickly an individual can produce code. They are limited by how well people can coordinate their understanding of the system they are changing. The shared language of a software project is not English or Python but it is the common understanding of what its concepts mean, where the boundaries are, which invariants matter, who owns what, and why the system has the shape it does. This language is rarely written down in one place. It lives partly in documentation and code, but also in code review, conversations, arguments, and the experience of having to explain a change to somebody else. Before agents, some of this shared understanding was maintained by friction. If I wanted to change your storage layer, I usually had to read your code, ask you questions, a

### 3. Authentication and permissions - Datasette documentation

- Type: web
- URL: https://docs.datasette.io/en/latest/authentication.html
- Title: Authentication and permissions - Datasette documentation
- Links:
  - https://docs.datasette.io/en/latest/authentication.html - Skip to content
  - https://docs.datasette.io/en/latest/index.html - Datasette documentation
  - https://datasette.io/
  - https://docs.datasette.io/en/latest/getting_started.html - Getting started
  - https://docs.datasette.io/en/latest/installation.html - Installation
  - https://docs.datasette.io/en/latest/configuration.html - Configuration
  - https://docs.datasette.io/en/latest/ecosystem.html - The Datasette Ecosystem
  - https://docs.datasette.io/en/latest/cli-reference.html - CLI reference
  - https://docs.datasette.io/en/latest/pages.html - Pages and API endpoints
  - https://docs.datasette.io/en/latest/publish.html - Publishing data
  - https://docs.datasette.io/en/latest/deploying.html - Deploying Datasette
  - https://docs.datasette.io/en/latest/json_api.html - JSON API
  - https://docs.datasette.io/en/latest/sql_queries.html - Running SQL queries
  - https://docs.datasette.io/en/latest/performance.html - Performance and caching
  - https://docs.datasette.io/en/latest/csv_export.html - CSV export
  - https://docs.datasette.io/en/latest/binary_data.html - Binary data
  - https://docs.datasette.io/en/latest/facets.html - Facets
  - https://docs.datasette.io/en/latest/full_text_search.html - Full-text search
  - https://docs.datasette.io/en/latest/spatialite.html - SpatiaLite
  - https://docs.datasette.io/en/latest/metadata.html - Metadata

Excerpt:

Authentication and permissions - Datasette documentation Skip to content Datasette documentation Contents Getting started Installation Configuration The Datasette Ecosystem CLI reference Pages and API endpoints Publishing data Deploying Datasette JSON API Running SQL queries Authentication and permissions Actors How actors are displayed Using the "root" actor Permissions Denying all permissions by default How permissions are resolved Defining permissions with "allow" blocks The /-/allow-debug tool Access permissions in datasette.yaml Access to an instance Access to specific databases Access to specific tables and views Access to specific queries Controlling the ability to execute arbitrary SQL Other permissions in datasette.yaml API Tokens datasette create-token Checking permissions in plugins actor_matches_allow() Permissions debug tools Allowed resources view Permission rules view Permission check view The ds_actor cookie Including an expiry time The /-/logout page Built-in actions view-instance view-database view-database-download view-table view-query store-query update-query delete-query insert-row delete-row update-row create-table create-view alter-table set-column-type drop-table drop-view execute-sql execute-write-sql permissions-debug debug-menu Performance and caching CSV export Binary data Facets Full-text search SpatiaLite Metadata Settings Introspection Custom pages and templates Template context Plugins Writing plugins JavaScript plugins Plugin hooks Testing plugins Internals for plugins Events Upgrade guide Contributing Changelog Back to top View this page Authentication and permissions ¶ Datasette doesn't require authentication by default. Any visitor to a Datasette instance can explore the full data and execute read-only SQL queries. Datasette can be configured to only allow authenticated users, or to control which databases, tables, and queries can be accessed by the public or by specific users. Datasette's plugin system can be used to add many different styles of authentication, such as user accounts, single sign-on or API keys. Actors ¶ Through plugins, Datasette can support both authenticated users (with cookies) and authenticated API clients (via authentication tokens). The word "actor" is used to cover both of these cases. Every request to Datasette has an associated actor value, available in the code as request.actor . This can be None for unauthenticated requests, or a JSON compatible Python dictionary for authenticated users or A

### 4. https://www.bilibili.com/video/BV1qeNX6tE8V

- Type: video
- URL: https://www.bilibili.com/video/BV1qeNX6tE8V

Excerpt:

�     �ywW�7���)t������1� < �N���Ё@������j��`K�%C Oւ$�s�! B����Lkݏr�%����o��N�RIV��q�\c��h�i������O��j���[7 �j���,�[�їv� �j��x�Yn�T�&&�*�/ l/�^e�=�:�I��V�9�40V�M�X���yֲ����-��z�]ϩ�&��U([x�X���j��W�G�Jy��T�5�\{i��{�c���R��B�T�oQs�1�7]����ʠ��fPO}����4 < ��� �t�V 4���P���������,/Ӎ�7�75�Mq�+���� c^yЭ�(�NY��&bMN�� � �0��%����������MUhѴ�bm +B3����X=t��K�m�)o����Xe��L� %P(�a4�V��%a٘[ ��9���v���Z�j%g��h�[��+��� kԫ./ZV�� ?�j;ǽ��բo��{��"F�|�� ���9��@a�sK�K���R�/���"�;����.���u��丵ӛZ��Z^�T��e��ْ�i�ޭ��`U_�]ՙ*M�~��υ����� �� [��vi�4X�y�;�Ʊ��}�����Xmdz>������h�GF�}���az �Ș��~��nO���T�-���C�f�Z{郁��cd�49�b�h�W���9۽���x#^����>���jm���Ts�F�+�l��2] ����#���l��j��xi�Tû��i"~xf�6=92QqA�}Y� ��)t2� < ���� �/��+�UFjĮ�?�j �K��Y5 B�e��K¯S΄;R����T��銁Uk6 ���ދ:���6og���K۽�\� ï�4�a�X4k�G��͑1�:��墠X�&�hc�h9��4zt����R��,Շli����Hyzb`�m6��u�M��o#�q5�@���֡Ob�:�->�̰ɇY���5�K���0(>��M| �����Q�����T+�ƽ?��$x����Z��A�������Ǐ � f�������g�3���'� ��?�xt��ӥ���̾�� ��}bhM�~�����I��AA ��>9�z����������T�c�kլ���� �p�"Q�Ŧ��륏7��� ��#[۶�����7�pd���)�$TrjY3���Ƈ��ߔ�-!�vT�\@~pDK��9g��~�� ��5��֮��� ����̌�r���Ǐ^�_��y���kץ���B4�/�����������3�0��;������ ��o����=�������ߏ������m < мq�q����e�#��$ ��~�����1����]�����N��z|��fiÆ�� �+��>Y��5��$������`n?�h������/_b;t����C��~�����=U�M�ԝ���;zb�x�|�vt�D7#r���7w�-Կ�l��w��i�P 5��}p�м~�t�� �׏4� ��^m>�߸z�� ���g/���\?s��J0���dM]��w��xp�����f���+G�ܟ�nvf ����f� ���R����5�������c��G�[��#{�s�й�������� � ��¦�xa� q��q�O�>�f��n��|���Bߛ_����翯~��ُ��D��-���X0|�/��]����t7�k|t��������@L�Z�:�ߺռ>� < �����#3s���j�rOVOU�)�T�� �p���E�ƙ�� ��7Y��mە��o��Ǳs{n�9 �S����m����G��~�̿}s����W��.7� < �w �����:��&u@�$�z��l�����o� �H���v�܃���������=�7e]�V� }꟟��6 }��I$ܼ�S� ؍��K��?��\��\)�^���/-�G �M�9u"�Ae|s����4�?������&J�RA^�6LU �8ԇ}G ��;�����g��}�����콃��;���'���X�`� 5� Pi�� ���� ]m~�����߻�m� ���B���`�����R ���; h���>��w���������6��{o�ß����Q�Y�5�D# ���D$��}$/�oc���O��=�����)^��$�� ;�E�$6��,y������Zm�ز�GL5�f}��mM9c8�/u�T\�TLG֊�n*�.{�$*�f�V�*�g��w'G��(;F�clDt�M�G{�Nmlz�.Î�fj�ϹWӓ�ܯ���Tr�*� A[!Ƕ�.g|�m���K�y���hfNYټ��Η*�+�R����[֩,ݚN�\W���!�����Q�84EcGɭ�q�c(Z�c�#� �Z��:�+�ݩ���X�J�Hȟ�ůG��쇝���ySe�Q�ͮR �Y��������~�z� |EAS�����ڑ�^d`�n��� �*��� o����?��cD�9��}�mj�e�c�������8Y����UȖb[�>���-��FR5A48�1��N&��(N�����`�5U(�.�6;j�*S˦����(4�*/�u`��NUJ.�3�Ў7휰KVy�&2�l@���B���^,� ����e�V��.������ ���п'J�K� ;^�,�ʣ���?�x��� ��VJ�`���__�}�

### 5. https://www.youtube.com/watch?v=9WqCAZoQZBk

- Type: video
- URL: https://www.youtube.com/watch?v=9WqCAZoQZBk
- Fetch status: limited (metadata-only host; skipped raw HTML fetch)

### 6. https://x.com/thsottiaux/status/2076735790567338203

- Type: x-post
- URL: https://x.com/thsottiaux/status/2076735790567338203
- Fetch status: limited (metadata-only host; skipped raw HTML fetch)

### 7. https://x.com/thsottiaux/status/2076543065045795309

- Type: x-post
- URL: https://x.com/thsottiaux/status/2076543065045795309
- Fetch status: limited (metadata-only host; skipped raw HTML fetch)

### 8. Cura 1T | Specialized Model for Agentic Healthcare

- Type: web
- URL: https://www.actava.ai/cura
- Title: Cura 1T | Specialized Model for Agentic Healthcare
- Description: Cura 1T is actAVA's one-trillion-parameter healthcare model — trained through recursive self-improvement for patient care, clinical reasoning, and healthcare agentic tasks. Top on 5 of 6 healthcare benchmark panels.
- Links:
  - https://forms.gle/hLfVUq1pBPRNojkj8 - Join waitlist
  - https://www.actava.ai/cura/docs - API documentation
  - https://github.com/actava-ai/Cura - GitHub
  - https://www.actava.ai/cura/cura-technical-report.pdf - Technical report
  - https://www.actava.ai/cura - the strongest healthcare LLM today
  - https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf - HealthBench Professional
  - https://openai.com/index/healthbench/ - HealthBench Hard
  - https://github.com/TsinghuaC3I/MedXpertQA - MedXpertQA
  - https://www.nature.com/articles/s41746-026-02674-7 - AgentClinic
  - https://arxiv.org/pdf/2501.14654 - MedAgentBench
  - https://www.actava.ai/cura/docs/api - API reference →
  - https://www.actava.ai/why-kora - KORA
  - https://www.actava.ai/kora/blue - BLUE
  - https://www.actava.ai/kora/red - RED
  - https://www.actava.ai/kora/green - GREEN
  - https://www.actava.ai/chryso - CHRYSO
  - https://www.actava.ai/technology - Our Technology
  - https://www.actava.ai/about/team - Our Team
  - https://www.actava.ai/about/advisors - Our Advisors
  - https://www.actava.ai/about/investors - Our Investors

Excerpt:

Cura 1T | Specialized Model for Agentic Healthcare Introducing Cura Specialized 1T model for agentic healthcare, trained via recursive self-improvement for patient care, clinical reasoning, health administration, and long-running agentic healthcare workflows. Join waitlist API documentation GitHub Technical report Cura 1T will also soon be available on The strongest healthcare LLM — custom-built for your enterprise, owned by you Cura is a one-trillion-parameter model built for the realities of enterprise healthcare. Post-trained from Kimi-K2.6 through recursive self-improvement, it is the strongest healthcare LLM today : it leads GPT-5.5, Claude Opus 4.8, and Gemini 3.1 Pro on five of the six benchmark panels that matter most in clinical and operational work. Cura turns your institutional knowledge into an asset you own forever, one that gets smarter with every task your agents run. This is how healthcare organizations stop renting intelligence and start owning their agentic future. Healthcare demands clinician-grade patient communication, expert reasoning over clinical text and images, and reliable execution against the real systems Payers and Providers run: core administrative processing, care management, network management, policy management, and CRM systems on the Payer side; EHRs, revenue cycle and practice management, ERP and finance, scheduling and workforce, and pharmacy systems on the Provider side. Cura 1T is built to serve all three. Its capabilities include: 01 Patient care High-stakes patient communication: consultation, triage, and safety-conscious guidance. Trained with physician-authored rubrics, Cura communicates clearly, surfaces red flags, escalates when needed, and leads the frontier on physician-graded evaluations. 02 Clinical reasoning Expert-level medical reasoning over clinical images. Cura works through specialty-board-level cases across 17 medical specialties and 11 body systems, and reasons natively over diverse clinical images, patient records, and examination results. 03 Healthcare agentic workflows Interactive diagnosis and EHR workflow. Cura conducts multi-turn diagnostic dialogues (taking history, ordering tests, narrowing the differential) and drives FHIR tool calls against live EHR systems for Providers and core administrative processing systems for Payers. Watch Cura work through each healthcare capability in a live demo: Join waitlist API documentation GitHub Technical report Recursive self-improvement Recursive self-imp

### 9. 训推全开源：HyOCR-1.5 让端到端 OCR 大模型跑得更快、看得更准、功能更全

- Type: web
- URL: https://mp.weixin.qq.com/s/vKFCa9FfoGBUGK8J1MhFag
- Title: 训推全开源：HyOCR-1.5 让端到端 OCR 大模型跑得更快、看得更准、功能更全
- Description: 1B 的身板，打出越级的成绩

Excerpt:

训推全开源：HyOCR-1.5 让端到端 OCR 大模型跑得更快、看得更准、功能更全 腾讯混元 在小说阅读器读本章 去阅读 在小说阅读器中沉浸阅读 VLM 端到端 OCR 专家模型全栈式开源，仅 1 B 参数覆盖 8 种以上 text-centric 任务，推理最高提速 6.37 倍，OmniDocBench v1.6 以 94.74 高分稳居端到端第一。 用大模型处理一份合同、一张发票、一篇 PDF 论文时，人们会本能地期待它“又快又准”——既能把密密麻麻的表格、公式、多栏版面一字不差地还原成结构化文本，又能在一两秒内出结果。但现实往往是—— 越是长、越是结构化复杂的文档，自回归大模型解码越慢；越是想跑得快，就越要牺牲精度或换上更好的显卡。 在 HyOCR-1.0 已经验证 “轻量端到端 OCR 专家模型” 这条路走得通之后，HyOCR-1.5 把目标又推进了一步： 如何让它同时变得更快、更强、更全面？ HyOCR-1.5 是端到端 OCR 大模型领域首个 将 训练、推理、模型权重完整开源 的 OCR 专家大模型：从数据构造方法、训练配方到推理加速框架均对外公开，任何人都可以在此基础上复现、微调与二次开发。 更重要的是，它足够轻量——不仅能部署在服务器上，还能通过 llama.cpp 跑在 CPU、消费级显卡乃至普通笔记本上 ，让强大的 OCR 能力真正走进 个人电脑 ；同时足够全能——不仅支持传统的文字检测识别与文档解析任务，还一次性囊括了信息抽取、拍照翻译、图表解析、古文字识别、视频字幕提取、多页文档问答等多种能力。 图1：HyOCR-1.5 网络结构图 HyOCR-1.5 真正想做的，是为广大 B 端与 C 端用户提供一套 最优的 OCR 解决方案 ——用尽可能低的部署与使用成本，精准满足各类定制化的 OCR 需求。 下面就结合这份最新发布的技术报告，看看这个只有 1 B 参数的小模型，是如何在「速度」与「能力」两条战线上同时取得突破的。 项目主页：https://github.com/Tencent-H unyuan/ H unyuan OCR 论文地址：https://arxiv.org/pdf/2607.04884 模型权重：https://huggingface.co/tencent/H unyuan OCR 一、Faster：把长文档解码的「慢」，交给 DFlash 来解 端到端 OCR 有一个绕不开的痛点： 长自回归解码 。文档越密、表格越大、公式越长，模型就要一个 token 接一个 token 地往外「吐」，解码延迟随之线性膨胀，成为真实部署中最大的瓶颈之一。 为此，HyOCR-1.5 引入了基于 DFlash 的投机解码（speculative decoding）框架：一个仅约 90.7M 参数 的轻量级 block-diffusion 草稿模型，一次并行前向就能「猜」出一整块候选 token，再交给目标模型一次性验证、接受最长的正确前缀。 整个过程 严格保持目标模型的输出分布 ——也就是说，快，但结果不变。 在我们的评测中，DFlash 让 HyOCR-1.5 在 Transformers 下取得 6.37× 加速、在 vLLM 下取得 2.14× 加速，成为所有 OCR VLMs 中推理最快的一个。 整体速度：一次并行验证，多推进好几个 token 采用权威文档解析基准 OmniDocBench 测试，在 单请求推理 配置 下，DFlash 的效果立竿见影： ● vLLM ：平均延迟从 3.032s 降到 1.408s ，吞吐从 466.9 提升到 1002.3 token/s ，页速从 0.330 提到 0.706 page/s ，整体 2.14× ； ● Transformers ：由于 A uto regressive(AR) 基线更接近逐 token 朴素解码， 收益更大，整体加速高达 6.37× 。 表 1：AR 解码 vs. DFlash 解码（OmniDocBench，batch size = 1） 越长越结构化，速度越快 投机解码的天然特性是： 输出越长，加速越明显 。在 vLLM 下，加速比从 0–256 token 的 1.31× 一路提升到 2048+ token 的 2.30×；Transformers 下更是从 4.56× 提升到 6.67×。按内容类型看， 表格页加速最大 （vLLM 2.39×、Transformers 7.81×），其次是公式页、纯文本页——因为 HTML 表格这类高度规整的结构，未来 token 更容易被「猜中」，有效接受长度也更长。 端到端速度对比：比两阶段级联方案更快 更值得一提的是横向对比。我们在 OmniDocBench 测试集、同等算力下，把适配了DFlash 的 HyOCR-1.5 与主流 OCR VLM 放在一起比拼—— 它是所有参评方案中端到端推理最快的一个 ，达到每页 1.408s、0.706 page/s，甚至比 GLM-OCR、PaddleOCR-VL-1.6 这类 两阶段级联方案 还要快，同时保持着「无需版面切分、无需分区级联」的统一端到端形态。 表 2：与代表性 OCR 系统的端到端速度对比（OmniDocBench） 从服务器到笔记本：还能装进你的电脑 除了面向服务器的 vLLM 部署，HyOCR-1.5 还支持通过 llama.cpp 进行 PC 端推理，可以跑在 CPU、消费级显卡乃至普通笔记本上——让轻量 OCR 真正做到「随处可部署」。 二、Better：巧用Agent参与模型自进化，把「短板」变成「能力」 如果说 DFlash 解决的是「快」，那么 HyOCR-1.5 的「强」，靠的是一套全新的数据构造哲学—— Agentic Data Flow（智能体驱动的数据流） 。 传统数据管线，几乎全靠人工写脚本、人工搜集素材、人工标注数据。而 Agentic Data Flow 的思路是： 把模型

### 10. https://x.com/ClaudeDevs/status/2076789349145092230

- Type: x-post
- URL: https://x.com/ClaudeDevs/status/2076789349145092230
- Fetch status: limited (metadata-only host; skipped raw HTML fetch)

