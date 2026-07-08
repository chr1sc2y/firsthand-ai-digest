# Firsthand AI Digest Source Pack

- Generated: 2026-07-08T08:02:07+08:00
- Intended coverage window: 2026-07-07T08:02:07+08:00 to 2026-07-08T08:02:07+08:00
- Index site: https://ai.prov1dence.top/
- Firsthand AI Digest items in window: 43
- Detail pages fetched: 0
- First-layer original sources fetched/listed: 43
- Original sources with fetched page text: 4
- Metadata-only original sources: 39
- Other limited original sources: 0
- Secondary source candidates fetched/listed: 10

This is a collection aid, not the final analysis. Open primary sources directly before writing final claims.

## Index Page

- URL: https://ai.prov1dence.top/
- Title: Firsthand AI Digest
- Links:
  - https://insight.ai.prov1dence.top/ - Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours.
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - Read article ↗
  - https://simonwillison.net/2026/Jul/7/sqlite-migrate/ - Read article ↗
  - https://simonwillison.net/2026/Jul/7/github-code-component/ - Read article ↗
  - https://daily.juya.uk/issues/2026-07-07/ - Read article ↗
  - https://simonwillison.net/2026/Jul/6/hy3/ - Read article ↗
  - https://www.youtube.com/shorts/mC8nKdQbbO4 - Watch ↗
  - https://www.youtube.com/watch?v=SRXJevuTnNI - Watch ↗
  - https://www.youtube.com/watch?v=1yBU41auQhw - Watch ↗
  - https://www.youtube.com/watch?v=9waIAoyM7Aw - Watch ↗
  - https://www.youtube.com/watch?v=sLYXRA5Ay9g - Watch ↗
  - https://www.youtube.com/watch?v=0x4KRxmRGz4 - Watch ↗
  - https://x.com/petergyang/status/2074579727365591297 - Open ↗
  - https://x.com/steipete/status/2074572085163381195 - Open ↗
  - https://x.com/steipete/status/2074563725043150967 - Open ↗
  - https://x.com/petergyang/status/2074555759904579838 - Open ↗
  - https://x.com/rauchg/status/2074555608578281920 - Open ↗
  - https://x.com/petergyang/status/2074553363035996239 - Open ↗
  - https://x.com/petergyang/status/2074551032240312778 - Open ↗
  - https://x.com/claudeai/status/2074548242386178258 - Open ↗

Excerpt:

Firsthand AI Digest Firsthand AI Digest Posts, blogs, podcasts and videos from the people building AI — straight from the source. Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours. Time 3h 6h 12h 24h 3d 7d Type All Blogs Podcasts Videos Posts Blogs & Long-form 05 items SW Simon Willison By Simon Willison Blog sqlite-utils 4.0, now with database schema migrations This morning I released sqlite-utils 4.0, the 124th release of that project and the first major version bump since 3.0 in November 2020. In addition to some small but significant breaking changes (described in this upgrade guide), this version introduces three major features: database migrations, nested transactions (via a new db.atomic() method), and support for compound foreign keys. Database schema migrations using sqlite-utils Schema migrations define a sequence of changes to be made to a SQLite database, plus a mechanism for tracking which migrations have been applied and applying any that are found to be pending. Migrations are defined in Python files using the sqlite-utils Python library, which includes a powerful table.transform() method providing enhanced alter table capabilities that are not supported by SQLite's ALTER TABLE statement. (table.transform() implements the pattern recommended by the SQLite documentation - create a new temporary table with the new schema, copy across the data, then drop the old table and rename the temporary one in its place.) Here's an example migration file which creates a table called creatures, adds an additional column to it in a second step, then changes the types of two of the columns in a third: from sqlite_utils import Migrations migrations = Migrations("creatures") @migrations() def create_table(db): db["creatures"].create( {"id": int, "name": str, "species": str}, pk="id", ) @migrations() def add_weight(db): db["creatures"].add_column("weight", float) @migrations() def change_column_types(db): db["creatures"].transform(types={"species": int, "weight": str}) Save that as migrations.py and run it against a fresh database like this: uvx sqlite-utils migrate data.db migrations.py Then if you check the schema of that database: uvx sqlite-utils schema data.db You'll see this SQL: CREATE TABLE "_sqlite_migrations" ( "id" INTEGER PRIMARY KEY, "migration_set" TEXT, "name" TEXT, "applied_at" TEXT ); CREATE UNIQUE INDEX "idx__sqlite_migrations_migration_set_name" ON "_sqlite_migrations" ("migration_set", "name"); CREATE TABLE "creatu

## Firsthand AI Digest Items In Window

### 1. sqlite-utils 4.0, now with database schema migrations

- URL: https://simonwillison.net/2026/Jul/7/sqlite-utils-4/
- Type: Blog
- Published: 2026-07-07T19:32:57+00:00
- Digest summary: This morning I released sqlite-utils 4.0, the 124th release of that project and the first major version bump since 3.0 in November 2020. In addition to some small but significant breaking changes (described in this upgrade guide), this version introduces three major features: database migrations, nested transactions (via a new db.atomic() method), and support for compound foreign keys. Database schema migrations using sqlite-utils Schema migrations define a sequence of changes to be made to a SQLite database, plus a mechanism for tracking which migrations have been applied and applying any that are found to be pending. Migrations are defined in Python files using the sqlite-utils Python library, which includes a powerful table.transform() method providing enhanced alter table capabilities 

### 2. sqlite-migrate 0.2

- URL: https://simonwillison.net/2026/Jul/7/sqlite-migrate/
- Type: Blog
- Published: 2026-07-07T16:33:55+00:00
- Digest summary: Release: sqlite-migrate 0.2 The version that retires the library, instead implementing a compatibility shim against the new sqlite-utils 4.0 dependency. Tags: sqlite-utils

### 3. github-code Web Component

- URL: https://simonwillison.net/2026/Jul/7/github-code-component/
- Type: Blog
- Published: 2026-07-07T16:18:16+00:00
- Digest summary: Tool: github-code Web Component An experimental Web Component built using GPT-5.5 and the following prompt: let's build a Web Component for embedding code from GitHub <github-code href="https://github.com/simonw/sqlite-ast/blob/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py#L9-L18"></github-code> It takes URLs like that, converts them to https://raw.githubusercontent.com/simonw/sqlite-ast/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py, then uses fetch() to fetch them and displays the specified range of lines - with line numbers, no syntax highlighting though Show me a preview web browser so I can see your work Here's what it looks like embedded on this page: Tags: github, web-components, gpt

### 4. 2026-07-07

- URL: https://daily.juya.uk/issues/2026-07-07/
- Type: Blog
- Published: 2026-07-07T03:14:39+00:00
- Digest summary: AI 早报 2026 07 07 视频版 ：哔哩哔哩 ｜ YouTube 概览 要闻 腾讯混元发布并开源 Hy3 模型 ↗ 1 模型发布 阿里升级语音模型Fun ASR Realtime ↗ 2 蚂蚁灵波科技发布LingBot Vision视觉基础模型及深度补全2.0 ↗ 3 OpenAI 发布 GPT Realtime 2.1 与 2.1 mini 语音模型 ↗ 4 产品应用 ChatGPT for PowerPoint 正式上线，面向全球所有用户 ↗ 5 技术与洞察 Anthropic 发现 Claude 内部存在全局工作空间 J space ↗ 6 行业动态 Cursor 推出 CFO Council 探讨 AI 经济学框架 ↗ 7 xAI正式更名为SpaceXAI，官方账号同步启用 ↗ 8 日本计划到…

### 5. How TPG Is Accelerating Investment Research with ChatGPT

- URL: https://www.youtube.com/shorts/mC8nKdQbbO4
- Type: Video
- Published: 2026-07-07T17:33:50+00:00
- Digest summary: For investment firms, getting smart faster is a competitive advantage. “My team uses ChatGPT on a daily basis… for market studies and desktop information scrapes… It enables us to get smart on industries really, really quickly.” -David Bessel, TPG See how TPG is putting ChatGPT to work across research and diligence.

### 6. How TPG Is Accelerating Investment Research with ChatGPT

- URL: https://www.youtube.com/watch?v=SRXJevuTnNI
- Type: Video
- Published: 2026-07-07T17:15:23+00:00
- Digest summary: For investment firms, getting smart faster is a competitive advantage. “My team uses ChatGPT on a daily basis… for market studies and desktop information scrapes… It enables us to get smart on industries really, really quickly.” -David Bessel, TPG See how TPG is putting ChatGPT to work across research and diligence.

### 7. DeepSeek's New AI Speed Hack Is Amazing

- URL: https://www.youtube.com/watch?v=1yBU41auQhw
- Type: Video
- Published: 2026-07-07T16:33:29+00:00
- Digest summary: ❤️ Check out Lambda here and sign up for their GPU Cloud: https://lambda.ai/papers 📝 The DeepSeek paper is available here: https://arxiv.org/abs/2607.05147v1 🙏 We would like to thank our generous Patreon supporters who make Two Minute Papers possible: Adam Bridges, Benji Rabhan, B Shang, Cameron Navor, Charles Ian Norman Venn, Christian Ahlin, Eric T, Fred R, Gordon Child, Juan Benet, Michael Tedder, Owen Skarpness, Richard Sundvall, Ryan Stankye, Shawn Becker, Steef, Taras Bobrovytsky, Tazaur Sagenclaw, Tybie Fitzhugh, Ueli Gallizzi

### 8. The Math Problem That Fooled Terry Tao – Grant Sanderson (@3blue1brown )

- URL: https://www.youtube.com/watch?v=9waIAoyM7Aw
- Type: Video
- Published: 2026-07-07T10:30:20+00:00
- Digest summary: Full episode: https://www.youtube.com/watch?v=TfyPshgMbug Me on twitter: https://x.com/dwarkesh_sp

### 9. Réinventer l'expérience beauté grâce à l'IA

- URL: https://www.youtube.com/watch?v=sLYXRA5Ay9g
- Type: Video
- Published: 2026-07-07T09:01:40+00:00
- Digest summary: Découvrez comment Sephora réinvente l'expérience beauté grâce à l'intelligence artificielle. Lors de cette session enregistrée à l'occasion de l'événement OpenAI France en juin 2026, Géraldine Servouze, Global VP Data, AI & Insights chez Sephora, présente la stratégie IA de l'entreprise et la manière dont elle s'appuie sur les modèles d'OpenAI pour proposer des expériences toujours plus personnalisées à ses clients, tout en accompagnant ses équipes et ses partenaires. Géraldine revient notamment sur le développement du Shopping Assistant de Sephora et sur l'intégration de l'application dans ChatGPT. Elle partage les enseignements tirés de ces projets, de l'importance d'une expérience utilisateur guidée, à la transparence des recommandations et à une approche continue de test and learn pour

### 10. What does an AI-native future look like for one of the world's largest automotive marketplaces?

- URL: https://www.youtube.com/watch?v=0x4KRxmRGz4
- Type: Video
- Published: 2026-07-07T08:23:39+00:00
- Digest summary: In this customer story, Justin Re, Global Chief Product Officer at AutoScout24 Group, shares how the company is using Codex across the organization to accelerate software development, automate workflows, and explore new ways of working. Hear how AutoScout24 is working toward a future of "hands off coding," built an AI-powered agent in just 48 hours, and is already saving approximately one million working hours annually through a single workflow. Read the full AutoScout24 story: https://openai.com/index/autoscout24/

### 11. https://x.com/petergyang/status/2074579727365591297

- URL: https://x.com/petergyang/status/2074579727365591297
- Type: Post
- Published: 2026-07-07T19:42:05+00:00
- Digest summary: Me if Anthropic extends Fable rate limits (sound on) 😅 https://t.co/m6Nl6W7ZCa

### 12. https://x.com/steipete/status/2074572085163381195

- URL: https://x.com/steipete/status/2074572085163381195
- Type: Post
- Published: 2026-07-07T19:11:43+00:00
- Digest summary: "When intelligence is plentiful, volition is valuable. The people who are going to make a difference are not the ones who seek relaxation and passively use AI to work less. They are the ones who will seek improvement and actively wrestle with AI to develop their own mental capabilities and accomplish more." https://t.co/gDEy4aABwo

### 13. https://x.com/steipete/status/2074563725043150967

- URL: https://x.com/steipete/status/2074563725043150967
- Type: Post
- Published: 2026-07-07T18:38:30+00:00
- Digest summary: This should ship EOD! We been cookin’

### 14. https://x.com/petergyang/status/2074555759904579838

- URL: https://x.com/petergyang/status/2074555759904579838
- Type: Post
- Published: 2026-07-07T18:06:51+00:00
- Digest summary: Every Argentina match is a banger

### 15. https://x.com/rauchg/status/2074555608578281920

- URL: https://x.com/rauchg/status/2074555608578281920
- Type: Post
- Published: 2026-07-07T18:06:15+00:00
- Digest summary: Heavenly victory 🇦🇷

### 16. https://x.com/petergyang/status/2074553363035996239

- URL: https://x.com/petergyang/status/2074553363035996239
- Type: Post
- Published: 2026-07-07T17:57:19+00:00
- Digest summary: LOLLLL best match ever

### 17. https://x.com/petergyang/status/2074551032240312778

- URL: https://x.com/petergyang/status/2074551032240312778
- Type: Post
- Published: 2026-07-07T17:48:04+00:00
- Digest summary: YES!!!!! Vamos Messi!

### 18. https://x.com/claudeai/status/2074548242386178258

- URL: https://x.com/claudeai/status/2074548242386178258
- Type: Post
- Published: 2026-07-07T17:36:58+00:00
- Digest summary: We're extending access to Claude Fable 5 on all paid plans through July 12.

### 19. https://x.com/petergyang/status/2074544797814321410

- URL: https://x.com/petergyang/status/2074544797814321410
- Type: Post
- Published: 2026-07-07T17:23:17+00:00
- Digest summary: I cannot watch anymore this is terrible

### 20. https://x.com/levie/status/2074528241990394178

- URL: https://x.com/levie/status/2074528241990394178
- Type: Post
- Published: 2026-07-07T16:17:30+00:00
- Digest summary: A small percentage of useful data is on the open web available to all models for training or for agents to operate with. Most of it lives inside of organizations and often is in legacy systems, in people’s heads, or is fragmented across the enterprise. It’s the marketing plans, product roadmaps, development practices, contracts, financial data, strategies, and general corporate knowledge that every company operates off of. Whether it’s for training a model or used as context for agents, this data will increasingly be more valuable over time. The ability to get the right data to agents to operate on, securely, will be a defining characteristic of how companies operate and compete in the future. Effective use of AI will in the economy will largely come down to the companies that are able to 

### 21. https://x.com/claudeai/status/2074525815820169320

- URL: https://x.com/claudeai/status/2074525815820169320
- Type: Post
- Published: 2026-07-07T16:07:51+00:00
- Digest summary: Claude Cowork is coming to mobile and web. Hand Claude a task at your desk and pick up the finished work from your phone. Close the laptop and Claude keeps going. Beta is rolling out over the next several weeks starting with the Max plan, with more plans to follow. https://t.co/W4WrgN9TrG

### 22. https://x.com/elonmusk/status/2074523879075115285

- URL: https://x.com/elonmusk/status/2074523879075115285
- Type: Post
- Published: 2026-07-07T16:00:10+00:00
- Digest summary: Great point

### 23. https://x.com/rauchg/status/2074523653488947338

- URL: https://x.com/rauchg/status/2074523653488947338
- Type: Post
- Published: 2026-07-07T15:59:16+00:00
- Digest summary: Welcome @bekacru to Vercel. It's a privilege to join forces with Bereket and Better Auth to further our Open SDK vision. Developers deserve better auth, to serve humans and agents, built in the open and with taste. That's what Bereket has accomplished. Congrats! 🇪🇹🇺🇸

### 24. https://x.com/elonmusk/status/2074523573142573321

- URL: https://x.com/elonmusk/status/2074523573142573321
- Type: Post
- Published: 2026-07-07T15:58:57+00:00
- Digest summary: Yes

### 25. https://x.com/rauchg/status/2074522238175633482

- URL: https://x.com/rauchg/status/2074522238175633482
- Type: Post
- Published: 2026-07-07T15:53:38+00:00
- Digest summary: Making the dev world a better place

### 26. https://x.com/elonmusk/status/2074521679179526572

- URL: https://x.com/elonmusk/status/2074521679179526572
- Type: Post
- Published: 2026-07-07T15:51:25+00:00
- Digest summary: https://t.co/V31k59VkTQ

### 27. https://x.com/elonmusk/status/2074521451474895265

- URL: https://x.com/elonmusk/status/2074521451474895265
- Type: Post
- Published: 2026-07-07T15:50:31+00:00
- Digest summary: Why did the media push this lie so hard?

### 28. https://x.com/elonmusk/status/2074520690326196556

- URL: https://x.com/elonmusk/status/2074520690326196556
- Type: Post
- Published: 2026-07-07T15:47:29+00:00
- Digest summary: We’re gonna need a bigger rocket! (Starship)

### 29. https://x.com/elonmusk/status/2074519858381799592

- URL: https://x.com/elonmusk/status/2074519858381799592
- Type: Post
- Published: 2026-07-07T15:44:11+00:00
- Digest summary: Falcon delivers 81 satellites to orbit

### 30. https://x.com/GoogleDeepMind/status/2074513661750546762

- URL: https://x.com/GoogleDeepMind/status/2074513661750546762
- Type: Post
- Published: 2026-07-07T15:19:34+00:00
- Digest summary: 🏛️ We’re unveiling a new way to converse with the ancient world. By grounding Gemini directly in our expert models Aeneas and Ithaca, our Predicting the Past Skill in Google @antigravity lets historians study Greek and Latin texts using plain English. 🧵 https://t.co/WQbUEyw8av

### 31. https://x.com/adityaag/status/2074512219434602995

- URL: https://x.com/adityaag/status/2074512219434602995
- Type: Post
- Published: 2026-07-07T15:13:50+00:00
- Digest summary: More important to wear the colors proudly the day after a loss. Proud of USMNT. We were outclasses yesterday Down but not out. We will be back. https://t.co/N1TTwo5mD5

### 32. https://x.com/steipete/status/2074389082017550720

- URL: https://x.com/steipete/status/2074389082017550720
- Type: Post
- Published: 2026-07-07T07:04:32+00:00
- Digest summary: You don't wanna miss this. Signup closes this week. Will be there and share some claws and tokens 🦞

### 33. https://x.com/steipete/status/2074380549318443311

- URL: https://x.com/steipete/status/2074380549318443311
- Type: Post
- Published: 2026-07-07T06:30:37+00:00
- Digest summary: How do folks run AI-assisted engineering interviews these days?

### 34. https://x.com/elonmusk/status/2074378653501128833

- URL: https://x.com/elonmusk/status/2074378653501128833
- Type: Post
- Published: 2026-07-07T06:23:05+00:00
- Digest summary: Grok Imagine update

### 35. https://x.com/elonmusk/status/2074355329517629776

- URL: https://x.com/elonmusk/status/2074355329517629776
- Type: Post
- Published: 2026-07-07T04:50:24+00:00
- Digest summary: https://t.co/7BfdeIH3rU

### 36. https://x.com/amasad/status/2074353874996211831

- URL: https://x.com/amasad/status/2074353874996211831
- Type: Post
- Published: 2026-07-07T04:44:38+00:00
- Digest summary: Major inflection point around the time of the brief bear market fall of last year.

### 37. https://x.com/swyx/status/2074344727202463832

- URL: https://x.com/swyx/status/2074344727202463832
- Type: Post
- Published: 2026-07-07T04:08:17+00:00
- Digest summary: imo this is the most impt part of anthropic's J-space paper today. it's a two-parter: 1) ant proved that they can do "brain surgery" interventions into reasoning to change topics midstream* 2) THE MODEL IS ABLE TO DETECT WHAT INTERVENTION WAS DONE - close cousin to eval awareness** *control > correlation - this convincingly demonstrates understanding **this was prompted awareness... surely @mlpowered's team also tried to eval unprompted awareness but i didn't see evidence of that

### 38. https://x.com/elonmusk/status/2074339319779569908

- URL: https://x.com/elonmusk/status/2074339319779569908
- Type: Post
- Published: 2026-07-07T03:46:47+00:00
- Digest summary: AI+Optimus will enable universal excellent healthcare that is better than anyone receives today

### 39. https://x.com/elonmusk/status/2074338887367786977

- URL: https://x.com/elonmusk/status/2074338887367786977
- Type: Post
- Published: 2026-07-07T03:45:04+00:00
- Digest summary: True

### 40. https://x.com/rauchg/status/2074313180554412076

- URL: https://x.com/rauchg/status/2074313180554412076
- Type: Post
- Published: 2026-07-07T02:02:55+00:00
- Digest summary: Update: 🇪🇸 ESP - 🇦🇷 ARG final. The legendary Spanish team will avenge team USA with a decisive defeat of 🇧🇪.

### 41. https://x.com/elonmusk/status/2074305337373462852

- URL: https://x.com/elonmusk/status/2074305337373462852
- Type: Post
- Published: 2026-07-07T01:31:45+00:00
- Digest summary: https://t.co/szhJMG4dlr

### 42. https://x.com/petergyang/status/2074295408902479910

- URL: https://x.com/petergyang/status/2074295408902479910
- Type: Post
- Published: 2026-07-07T00:52:18+00:00
- Digest summary: Go USA!!!

### 43. https://x.com/rauchg/status/2074287795028512773

- URL: https://x.com/rauchg/status/2074287795028512773
- Type: Post
- Published: 2026-07-07T00:22:03+00:00
- Digest summary: 🆒 eve evals itself with 𝚎𝚟𝚎 𝚎𝚟𝚊𝚕. Web frameworks made testing an ecosystem choice. e.g.: React didn’t ship with a built-in testing solution. For agents, evals are essential… thus we ship 𝚎𝚟𝚎 𝚎𝚟𝚊𝚕 out of the box. For your agents and eve’s own evolution.

## Firsthand AI Digest Detail Pages

## Original Sources

### 1. sqlite-utils 4.0, now with database schema migrations

- Type: web
- URL: https://simonwillison.net/2026/Jul/7/sqlite-utils-4/
- Title: sqlite-utils 4.0, now with database schema migrations
- Description: This morning I released sqlite-utils 4.0, the 124th release of that project and the first major version bump since 3.0 in November 2020. In addition to some small but significant …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/3STP9vD - Get the report
  - https://sqlite-utils.datasette.io/en/stable/changelog.html - sqlite-utils 4.0
  - https://sqlite-utils.datasette.io/en/stable/upgrading.html - this upgrade guide
  - https://sqlite-utils.datasette.io/en/stable/python-api.html - sqlite-utils Python library
  - https://www.sqlite.org/lang_altertable.html - recommended by the SQLite documentation
  - https://sqlite-utils.datasette.io/en/stable/migrations.html - from Python code
  - https://llm.datasette.io/ - LLM tool
  - https://github.com/simonw/llm/blob/0.31/llm/embeddings_migrations.py - llm/embeddings_migrations.py
  - https://docs.djangoproject.com/en/6.0/topics/migrations/ - Django’s Migrations
  - https://github.com/andrewgodwin/south - South
  - https://www.youtube.com/watch?v=VSq8m00p1FM - Schema Evolution panel
  - https://simonwillison.net/2008/Sep/3/dmigrations/ - dmigrations
  - https://github.com/simonw/sqlite-migrate - sqlite-migrate
  - https://github.com/simonw/sqlite-migrate/releases/tag/0.2 - one last release
  - https://github.com/simonw/sqlite-utils/issues/752 - #752
  - https://github.com/simonw/sqlite-utils/issues/755 - #755
  - https://sqlite.org/lang_savepoint.html - Savepoints
  - https://github.com/simonw/sqlite-utils/issues/594 - #594

Excerpt:

sqlite-utils 4.0, now with database schema migrations Simon Willison’s Weblog Subscribe Sponsored by: Sonar — Gartner just named Sonar a Leader in the 2026 Magic Quadrant™ for Technical Debt Management Tools. Read the report and learn how to measure and remediate technical debt across your codebase. Get the report sqlite-utils 4.0, now with database schema migrations 7th July 2026 This morning I released sqlite-utils 4.0 , the 124th release of that project and the first major version bump since 3.0 in November 2020. In addition to some small but significant breaking changes (described in this upgrade guide ), this version introduces three major features: database migrations , nested transactions (via a new db.atomic() method), and support for compound foreign keys . Database schema migrations using sqlite-utils Schema migrations define a sequence of changes to be made to a SQLite database, plus a mechanism for tracking which migrations have been applied and applying any that are found to be pending. Migrations are defined in Python files using the sqlite-utils Python library , which includes a powerful table.transform() method providing enhanced alter table capabilities that are not supported by SQLite’s ALTER TABLE statement. ( table.transform() implements the pattern recommended by the SQLite documentation —create a new temporary table with the new schema, copy across the data, then drop the old table and rename the temporary one in its place.) Here’s an example migration file which creates a table called creatures , adds an additional column to it in a second step, then changes the types of two of the columns in a third: from sqlite_utils import Migrations migrations = Migrations ( "creatures" ) @ migrations () def create_table ( db ): db [ "creatures" ]. create ( { "id" : int , "name" : str , "species" : str }, pk = "id" , ) @ migrations () def add_weight ( db ): db [ "creatures" ]. add_column ( "weight" , float ) @ migrations () def change_column_types ( db ): db [ "creatures" ]. transform ( types = { "species" : int , "weight" : str }) Save that as migrations.py and run it against a fresh database like this: uvx sqlite-utils migrate data.db migrations.py Then if you check the schema of that database: uvx sqlite-utils schema data.db You’ll see this SQL: CREATE TABLE " _sqlite_migrations " ( " id " INTEGER PRIMARY KEY , " migration_set " TEXT , " name " TEXT , " applied_at " TEXT ); CREATE UNIQUE INDEX " idx__sqlite_migrations_migration_set_name " ON "

### 2. Release: sqlite-migrate 0.2

- Type: web
- URL: https://simonwillison.net/2026/Jul/7/sqlite-migrate/
- Title: Release: sqlite-migrate 0.2
- Description: A simple database migration system for SQLite, based on sqlite-utils
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/3STP9vD - Get the report
  - https://simonwillison.net/elsewhere/release/ - Release
  - https://github.com/simonw/sqlite-migrate/releases/tag/0.2 - sqlite-migrate 0.2
  - https://simonwillison.net/2026/Jul/7/ - 7th July 2026
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - sqlite-utils 4.0, now with database schema migrations
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/ - sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
  - https://simonwillison.net/2026/Jun/30/shot-scraper-video/ - Have your agent record video demos of its work with shot-scraper video
  - https://simonwillison.net/tags/sqlite-utils/ - sqlite-utils 231
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

Release: sqlite-migrate 0.2 Simon Willison’s Weblog Subscribe Sponsored by: Sonar — Gartner just named Sonar a Leader in the 2026 Magic Quadrant™ for Technical Debt Management Tools. Read the report and learn how to measure and remediate technical debt across your codebase. Get the report 7th July 2026 Release sqlite-migrate 0.2 — A simple database migration system for SQLite, based on sqlite-utils The version that retires the library, instead implementing a compatibility shim against the new sqlite-utils 4.0 dependency. Posted 7th July 2026 at 4:33 pm Recent articles sqlite-utils 4.0, now with database schema migrations - 7th July 2026 sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25) - 5th July 2026 Have your agent record video demos of its work with shot-scraper video - 30th June 2026 This is a beat by Simon Willison, posted on 7th July 2026 . sqlite-utils 231 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 3. Tool: github-code Web Component

- Type: web
- URL: https://simonwillison.net/2026/Jul/7/github-code-component/
- Title: Tool: github-code Web Component
- Description: github-code Web Component
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://fandf.co/3STP9vD - Get the report
  - https://simonwillison.net/elsewhere/tool/ - Tool
  - https://tools.simonwillison.net/github-code-component - github-code Web Component
  - https://gist.github.com/simonw/0e3db21947b5ae7e29e8a4f69a0b0617 - the following prompt
  - https://simonwillison.net/2026/Jul/7/ - 7th July 2026
  - https://simonwillison.net/2026/Jul/7/sqlite-utils-4/ - sqlite-utils 4.0, now with database schema migrations
  - https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/ - sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
  - https://simonwillison.net/2026/Jun/30/shot-scraper-video/ - Have your agent record video demos of its work with shot-scraper video
  - https://simonwillison.net/tags/github/ - github 189
  - https://simonwillison.net/tags/web-components/ - web-components 26
  - https://simonwillison.net/tags/gpt/ - gpt 128
  - https://github.com/sponsors/simonw/ - Sponsor & subscribe
  - https://simonwillison.net/2002/ - 2002
  - https://simonwillison.net/2003/ - 2003
  - https://simonwillison.net/2004/ - 2004
  - https://simonwillison.net/2005/ - 2005
  - https://simonwillison.net/2006/ - 2006
  - https://simonwillison.net/2007/ - 2007

Excerpt:

Tool: github-code Web Component Simon Willison’s Weblog Subscribe Sponsored by: Sonar — Gartner just named Sonar a Leader in the 2026 Magic Quadrant™ for Technical Debt Management Tools. Read the report and learn how to measure and remediate technical debt across your codebase. Get the report 7th July 2026 Tool github-code Web Component An experimental Web Component built using GPT-5.5 and the following prompt : let's build a Web Component for embedding code from GitHub <github-code href="https://github.com/simonw/sqlite-ast/blob/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py#L9-L18"></github-code> It takes URLs like that, converts them to https://raw.githubusercontent.com/simonw/sqlite-ast/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py, then uses fetch() to fetch them and displays the specified range of lines - with line numbers, no syntax highlighting though Show me a preview web browser so I can see your work Here's what it looks like embedded on this page: Posted 7th July 2026 at 4:18 pm Recent articles sqlite-utils 4.0, now with database schema migrations - 7th July 2026 sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25) - 5th July 2026 Have your agent record video demos of its work with shot-scraper video - 30th June 2026 This is a beat by Simon Willison, posted on 7th July 2026 . github 189 web-components 26 gpt 128 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 4. AI 早报 2026-07-07

- Type: web
- URL: https://daily.juya.uk/issues/2026-07-07/
- Title: AI 早报 2026-07-07
- Links:
  - https://daily.juya.uk/ - 首页
  - https://daily.juya.uk/archive/ - 归档
  - https://daily.juya.uk/rss.xml - RSS
  - https://daily.juya.uk/markdown/2026-07-07.md - Markdown
  - https://www.bilibili.com/video/BV1BMM46cEBo - 哔哩哔哩
  - https://www.youtube.com/watch?v=tEn1n4p0aFY - YouTube
  - https://hy.tencent.com/research/hy3 - ↗
  - https://mp.weixin.qq.com/s/Uq03C7koDBwmYtxoR8kSvA - ↗
  - https://technology.robbyant.com/lingbot-vision - ↗
  - https://developers.openai.com/api/docs/models/gpt-realtime-2.1 - ↗
  - https://x.com/ChatGPTapp/status/2057560276384563560 - ↗
  - https://www.anthropic.com/research/global-workspace - ↗
  - https://cursor.com/blog/cfo-council - ↗
  - https://x.com/SpaceXAI/status/2074214064746832060 - ↗
  - https://www3.nhk.or.jp/nhkworld/en/news/20260630_21/ - ↗
  - https://mp.weixin.qq.com/s/tMzJ2t4HGlClshcMtvuzQQ - ↗
  - https://github.com/Tencent-Hunyuan/Hy3 - https://github.com/Tencent-Hunyuan/Hy3
  - https://huggingface.co/tencent/Hy3 - https://huggingface.co/tencent/Hy3
  - https://github.com/Robbyant/lingbot-vision - https://github.com/Robbyant/lingbot-vision
  - https://huggingface.co/collections/robbyant/lingbot-vision - https://huggingface.co/collections/robbyant/lingbot-vision

Excerpt:

AI 早报 2026-07-07 首页 归档 RSS 2026-07-07 · Markdown AI 早报 2026-07-07 视频版 ： 哔哩哔哩 ｜ YouTube 概览 要闻 腾讯混元发布并开源 Hy3 模型 ↗ #1 模型发布 阿里升级语音模型Fun-ASR-Realtime ↗ #2 蚂蚁灵波科技发布LingBot-Vision视觉基础模型及深度补全2.0 ↗ #3 OpenAI 发布 GPT-Realtime-2.1 与 2.1-mini 语音模型 ↗ #4 产品应用 ChatGPT for PowerPoint 正式上线，面向全球所有用户 ↗ #5 技术与洞察 Anthropic 发现 Claude 内部存在全局工作空间 J-space ↗ #6 行业动态 Cursor 推出 CFO Council 探讨 AI 经济学框架 ↗ #7 xAI正式更名为SpaceXAI，官方账号同步启用 ↗ #8 日本计划到2040年部署约1000万个AI机器人 ↗ #9 前瞻与传闻 秘塔AI研发医学+AI应用，开放内测群招募 ↗ #10 要闻 腾讯混元发布并开源 Hy3 模型 #1 腾讯混元发布并开源了 {Hy3|"混元3"} 大模型正式版，该模型总参数295B，激活参数{21B|"21B"}，支持 256K 上下文。官方称其性能比肩参数规模大{2-5|二至五}倍的旗舰模型，幻觉率较预览版大幅降低，已在{腾讯云API|"腾讯云API"}、{元宝|"元宝"}等上线。同时在 OpenRouter、Nous Portal和CodeBuddy等多平台提供两周限时免费体验。 腾讯混元团队正式发布 Hy3 大模型，该模型为 MoE 架构，总参数 295B、激活参数 21B，支持 256K 上下文窗口，并已以 Apache 2.0 协议开源。官方称，Hy3 在后训练数据质量与 RL 算力规模上显著提升，Agent 能力、推理与长上下文表现可比肩参数规模为其 2-5 倍的更大尺寸旗舰模型；在内部 270 位专家盲测中得分 2.67/4，优于 GLM5.1，且工具调用稳定性、抗幻觉及多轮意图保持等体验指标大幅改善，幻觉率从 12.5% 降至 5.4%。目前，元宝已接入 Hy3 并免费向用户提供文件生成、数据分析与网页制作等功能；腾讯云 API 价格为每百万 tokens 输入 1 元，输出 4元；同时在 OpenRouter、Nous Portal和CodeBuddy等多平台提供两周限时免费体验。 相关链接： https://hy.tencent.com/research/hy3 https://github.com/Tencent-Hunyuan/Hy3 https://huggingface.co/tencent/Hy3 模型发布 阿里升级语音模型Fun-ASR-Realtime #2 阿里宣布正式升级实时语音识别模型Fun-ASR-Realtime，其首字延迟百毫秒、准确率接近离线、支持16种方言和30种语言，已用于影视飓风直播并上线阿里云百炼。 阿里近日正式升级实时语音识别大模型Fun-ASR-Realtime，该模型首字延迟控制在百毫秒级别，识别准确率接近其离线模型，并具备基于上下文的自我纠错能力。据官方测试，它支持16种方言和30种语言，方言识别字符准确率平均88.62%，在12类方言上领先竞品，工业中文和英文场景准确率分别达88.42%和91.58%，泰语等东南亚语言亦获专项优化。其离线版本Fun-ASR-Flash在Artificial Analysis平台上以1.7%字错率位居全球第一。该模型已支撑影视飓风“重返荒岛”100小时直播生成132万字字幕，目前已在阿里云百炼平台开放体验。 相关链接： https://mp.weixin.qq.com/s/Uq03C7koDBwmYtxoR8kSvA 蚂蚁灵波科技发布LingBot-Vision视觉基础模型及深度补全2.0 #3 蚂蚁灵波科技发布自监督视觉模型LingBot-Vision和深度补全模型LingBot-Depth 2.0，采用掩码边界建模实现密集空间感知，在深度估计等任务中超越更大参数模型，现已开源并发布预训练权重。 蚂蚁灵波科技Robbyant正式发布LingBot-Vision系列自监督视觉基础模型，采用掩码边界建模，无需人工标注即可在线学习亚像素边界并引导密集视觉令牌学习；同期推出的LingBot-Depth 2.0则将深度补全建模为掩码深度建模，并改用LingBot-Vision作为编码器初始化。LingBot-Vision以ViT-g/16为教师模型，蒸馏出L、B、S三个学生模型，在NYUv2深度估计上达到0.296 RMSE，优于7B参数的DINOv3，小规模模型同样保持领先；深度补全2.0在透明和反射表面场景重建稳定连续表面，块掩码DIODE-Indoor RMSE较前代减半。所有模型权重已通过HuggingFace开源，代码在GitHub以Apache 2.0许可发布，提供pip安装、Python接口及PCA可视化演示。 相关链接： https://technology.robbyant.com/lingbot-vision https://github.com/Robbyant/lingbot-vision https://huggingface.co/collections/robbyant/lingbot-vision OpenAI 发布 GPT-Realtime-2.1 与 2.1-mini 语音模型 #4 OpenAI 发布 GPT-Realtime-{2.1|two point one} 及 GPT-Realtime-2.1-mini 两款实时音频模型。GPT-Realtime-{2.1|two point one}显著改善了字母数字信息的处理，GPT-Realtime-2.1-mini 首次在mini系列引入推理与工具调

### 5. How TPG Is Accelerating Investment Research with ChatGPT

- Type: video
- URL: https://www.youtube.com/shorts/mC8nKdQbbO4
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 6. How TPG Is Accelerating Investment Research with ChatGPT

- Type: video
- URL: https://www.youtube.com/watch?v=SRXJevuTnNI
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 7. DeepSeek's New AI Speed Hack Is Amazing

- Type: video
- URL: https://www.youtube.com/watch?v=1yBU41auQhw
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 8. The Math Problem That Fooled Terry Tao – Grant Sanderson (@3blue1brown )

- Type: video
- URL: https://www.youtube.com/watch?v=9waIAoyM7Aw
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 9. Réinventer l'expérience beauté grâce à l'IA

- Type: video
- URL: https://www.youtube.com/watch?v=sLYXRA5Ay9g
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 10. What does an AI-native future look like for one of the world's largest automotive marketplaces?

- Type: video
- URL: https://www.youtube.com/watch?v=0x4KRxmRGz4
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 11. https://x.com/petergyang/status/2074579727365591297

- Type: x-post
- URL: https://x.com/petergyang/status/2074579727365591297
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 12. https://x.com/steipete/status/2074572085163381195

- Type: x-post
- URL: https://x.com/steipete/status/2074572085163381195
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 13. https://x.com/steipete/status/2074563725043150967

- Type: x-post
- URL: https://x.com/steipete/status/2074563725043150967
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 14. https://x.com/petergyang/status/2074555759904579838

- Type: x-post
- URL: https://x.com/petergyang/status/2074555759904579838
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 15. https://x.com/rauchg/status/2074555608578281920

- Type: x-post
- URL: https://x.com/rauchg/status/2074555608578281920
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 16. https://x.com/petergyang/status/2074553363035996239

- Type: x-post
- URL: https://x.com/petergyang/status/2074553363035996239
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 17. https://x.com/petergyang/status/2074551032240312778

- Type: x-post
- URL: https://x.com/petergyang/status/2074551032240312778
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 18. https://x.com/claudeai/status/2074548242386178258

- Type: x-post
- URL: https://x.com/claudeai/status/2074548242386178258
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 19. https://x.com/petergyang/status/2074544797814321410

- Type: x-post
- URL: https://x.com/petergyang/status/2074544797814321410
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 20. https://x.com/levie/status/2074528241990394178

- Type: x-post
- URL: https://x.com/levie/status/2074528241990394178
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 21. https://x.com/claudeai/status/2074525815820169320

- Type: x-post
- URL: https://x.com/claudeai/status/2074525815820169320
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 22. https://x.com/elonmusk/status/2074523879075115285

- Type: x-post
- URL: https://x.com/elonmusk/status/2074523879075115285
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 23. https://x.com/rauchg/status/2074523653488947338

- Type: x-post
- URL: https://x.com/rauchg/status/2074523653488947338
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 24. https://x.com/elonmusk/status/2074523573142573321

- Type: x-post
- URL: https://x.com/elonmusk/status/2074523573142573321
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 25. https://x.com/rauchg/status/2074522238175633482

- Type: x-post
- URL: https://x.com/rauchg/status/2074522238175633482
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 26. https://x.com/elonmusk/status/2074521679179526572

- Type: x-post
- URL: https://x.com/elonmusk/status/2074521679179526572
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 27. https://x.com/elonmusk/status/2074521451474895265

- Type: x-post
- URL: https://x.com/elonmusk/status/2074521451474895265
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 28. https://x.com/elonmusk/status/2074520690326196556

- Type: x-post
- URL: https://x.com/elonmusk/status/2074520690326196556
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 29. https://x.com/elonmusk/status/2074519858381799592

- Type: x-post
- URL: https://x.com/elonmusk/status/2074519858381799592
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 30. https://x.com/GoogleDeepMind/status/2074513661750546762

- Type: x-post
- URL: https://x.com/GoogleDeepMind/status/2074513661750546762
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 31. https://x.com/adityaag/status/2074512219434602995

- Type: x-post
- URL: https://x.com/adityaag/status/2074512219434602995
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 32. https://x.com/steipete/status/2074389082017550720

- Type: x-post
- URL: https://x.com/steipete/status/2074389082017550720
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 33. https://x.com/steipete/status/2074380549318443311

- Type: x-post
- URL: https://x.com/steipete/status/2074380549318443311
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 34. https://x.com/elonmusk/status/2074378653501128833

- Type: x-post
- URL: https://x.com/elonmusk/status/2074378653501128833
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 35. https://x.com/elonmusk/status/2074355329517629776

- Type: x-post
- URL: https://x.com/elonmusk/status/2074355329517629776
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 36. https://x.com/amasad/status/2074353874996211831

- Type: x-post
- URL: https://x.com/amasad/status/2074353874996211831
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 37. https://x.com/swyx/status/2074344727202463832

- Type: x-post
- URL: https://x.com/swyx/status/2074344727202463832
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 38. https://x.com/elonmusk/status/2074339319779569908

- Type: x-post
- URL: https://x.com/elonmusk/status/2074339319779569908
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 39. https://x.com/elonmusk/status/2074338887367786977

- Type: x-post
- URL: https://x.com/elonmusk/status/2074338887367786977
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 40. https://x.com/rauchg/status/2074313180554412076

- Type: x-post
- URL: https://x.com/rauchg/status/2074313180554412076
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 41. https://x.com/elonmusk/status/2074305337373462852

- Type: x-post
- URL: https://x.com/elonmusk/status/2074305337373462852
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 42. https://x.com/petergyang/status/2074295408902479910

- Type: x-post
- URL: https://x.com/petergyang/status/2074295408902479910
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 43. https://x.com/rauchg/status/2074287795028512773

- Type: x-post
- URL: https://x.com/rauchg/status/2074287795028512773
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

## Secondary Source Candidates

These links were discovered from first-layer sources. Use them to reach primary material when the first-layer source is commentary or a link blog.

### 1. Changelog - sqlite-utils

- Type: web
- URL: https://sqlite-utils.datasette.io/en/stable/changelog.html
- Title: Changelog - sqlite-utils
- Links:
  - https://sqlite-utils.datasette.io/en/stable/changelog.html - Skip to content
  - https://sqlite-utils.datasette.io/en/stable/index.html - sqlite-utils
  - https://sqlite-utils.datasette.io/en/stable/installation.html - Installation
  - https://sqlite-utils.datasette.io/en/stable/cli.html - sqlite-utils command-line tool
  - https://sqlite-utils.datasette.io/en/stable/python-api.html - sqlite_utils Python library
  - https://sqlite-utils.datasette.io/en/stable/migrations.html - Database migrations
  - https://sqlite-utils.datasette.io/en/stable/plugins.html - Plugins
  - https://sqlite-utils.datasette.io/en/stable/reference.html - API reference
  - https://sqlite-utils.datasette.io/en/stable/cli-reference.html - CLI reference
  - https://sqlite-utils.datasette.io/en/stable/upgrading.html - Upgrading
  - https://sqlite-utils.datasette.io/en/stable/contributing.html - Contributing
  - https://sqlite-utils.datasette.io/en/stable/_sources/changelog.rst.txt - View this page
  - https://github.com/simonw/sqlite-utils/issues/752 - #752
  - https://github.com/simonw/sqlite-utils/issues/755 - #755
  - https://github.com/simonw/sqlite-utils/issues/594 - #594
  - https://github.com/simonw/sqlite-utils/issues/652 - #652
  - https://github.com/simonw/sqlite-utils/issues/679 - #679
  - https://github.com/simonw/sqlite-utils/issues/530 - #530
  - https://github.com/simonw/sqlite-utils/issues/760 - #760
  - https://github.com/simonw/sqlite-utils/issues/625 - #625

Excerpt:

Changelog - sqlite-utils Skip to content sqlite-utils sqlite-utils Installation sqlite-utils command-line tool sqlite_utils Python library Database migrations Plugins API reference CLI reference Upgrading Contributing Changelog Back to top View this page Changelog ¶ 4.0 (2026-07-07) ¶ The 4.0 release includes some minor backwards-incompatible fixes (hence the major version number bump) and introduces three major new features: Database migrations , providing a structured mechanism for evolving a project’s schema over time. ( #752 ) Nested transaction support via db.atomic() , plus numerous improvements to how transactions work across the library. ( #755 ) Support for compound foreign keys , including creation, transformation and introspection through table.foreign_keys . ( #594 ) Other notable changes include: Upserts now use SQLite’s INSERT ... ON CONFLICT ... DO UPDATE SET syntax, detect existing table primary keys automatically and reject records that are missing required primary key values. ( #652 ) db.query() now executes immediately and rejects statements that do not return rows; use db.execute() for writes and DDL. CSV and TSV imports now detect column types by default, while inserts into existing tables preserve those tables’ column types. ( #679 ) Foreign key handling now preserves ON DELETE / ON UPDATE actions during transforms and resolves referenced primary keys more accurately. ( #530 ) Column names passed to Python API methods are now matched case-insensitively, mirroring SQLite’s own identifier behavior. ( #760 ) The command-line tool now emits UTF-8 JSON output by default, with --ascii available to restore escaped output. ( #625 ) table.extract() and extracts= no longer create lookup table records for all- null values. ( #186 ) See Upgrading from 3.x to 4.0 for details on backwards-incompatible changes. The detailed release notes for the features and fixes shipped during the 4.0 pre-release cycle are available in 4.0a0 , 4.0a1 , 4.0rc1 , 4.0rc2 , 4.0rc3 and 4.0rc4 . Bug fixes since 4.0rc4 ¶ Fixed 4.0 regressions in insert / upsert against tables that use SQLite’s implicit rowid primary key. Passing pk="rowid" , pk="_rowid_" or pk="oid" now works again for rowid tables, and last_pk is set correctly. ( #781 ) Fixed insert(..., ignore=True) and insert_all(..., ignore=True) so an ignored insert that conflicts with an existing primary key row now reports that existing row in last_rowid and last_pk where possible. This also works for compound prim

### 2. Upgrading - sqlite-utils

- Type: web
- URL: https://sqlite-utils.datasette.io/en/stable/upgrading.html
- Title: Upgrading - sqlite-utils
- Links:
  - https://sqlite-utils.datasette.io/en/stable/upgrading.html - Skip to content
  - https://sqlite-utils.datasette.io/en/stable/index.html - sqlite-utils
  - https://sqlite-utils.datasette.io/en/stable/installation.html - Installation
  - https://sqlite-utils.datasette.io/en/stable/cli.html - sqlite-utils command-line tool
  - https://sqlite-utils.datasette.io/en/stable/python-api.html - sqlite_utils Python library
  - https://sqlite-utils.datasette.io/en/stable/migrations.html - Database migrations
  - https://sqlite-utils.datasette.io/en/stable/plugins.html - Plugins
  - https://sqlite-utils.datasette.io/en/stable/reference.html - API reference
  - https://sqlite-utils.datasette.io/en/stable/cli-reference.html - CLI reference
  - https://sqlite-utils.datasette.io/en/stable/contributing.html - Contributing
  - https://sqlite-utils.datasette.io/en/stable/changelog.html - Changelog
  - https://sqlite-utils.datasette.io/en/stable/_sources/upgrading.rst.txt - View this page
  - https://github.com/simonw/sqlite-utils-tui - sqlite-utils-tui
  - https://www.sphinx-doc.org/ - Sphinx
  - https://pradyunsg.me - @pradyunsg
  - https://github.com/pradyunsg/furo - Furo

Excerpt:

Upgrading - sqlite-utils Skip to content sqlite-utils sqlite-utils Installation sqlite-utils command-line tool sqlite_utils Python library Database migrations Plugins API reference CLI reference Upgrading Contributing Changelog Back to top View this page Upgrading ¶ This page describes the changes you may need to make to your own code or scripts when upgrading between major versions of sqlite-utils . For the full list of changes in every release see the Changelog . Upgrading from 3.x to 4.0 ¶ Requirements ¶ Python 3.10 or higher is required. The click dependency must be version 8.3.1 or later. Command-line changes ¶ Type detection is now the default for CSV and TSV imports. sqlite-utils insert and sqlite-utils upsert now detect column types when importing CSV or TSV data - previously every column was created as TEXT unless you passed --detect-types . To restore the old behavior pass the new --no-detect-types flag: sqlite-utils insert data.db rows data.csv --csv --no-detect-types Two related things have been removed: The SQLITE_UTILS_DETECT_TYPES environment variable. The old -d/--detect-types flag itself. Since detection is now the default the flag did nothing - remove it from any scripts that used it. The convert command no longer skips falsey values. sqlite-utils convert previously skipped values that evaluated to False (empty strings, 0 ) unless you passed --no-skip-false . All values are now converted and the --no-skip-false flag has been removed. drop-table and drop-view check the object type. sqlite-utils drop-table now refuses to drop a view, and drop-view refuses to drop a table. Previously each would silently drop the wrong type of object if the name matched. If you relied on that (unlikely), use the matching command instead. sqlite-utils tui has moved to a plugin. The optional terminal interface is now provided by the sqlite-utils-tui plugin: sqlite-utils install sqlite-utils-tui Python API changes ¶ db.query() now rejects SQL that does not return rows. This is likely the most common change you will need to make to existing code. db.query() used to accept any SQL statement - passing one that returns no rows, such as an INSERT or UPDATE without a RETURNING clause or a CREATE TABLE , did nothing at all, silently. Those statements now raise a ValueError , and are rolled back so they have no effect on the database. Transaction control statements ( BEGIN , COMMIT , END , ROLLBACK , SAVEPOINT , RELEASE ) plus VACUUM , ATTACH and DETACH are also rejecte

### 3. sqlite_utils Python library - sqlite-utils

- Type: web
- URL: https://sqlite-utils.datasette.io/en/stable/python-api.html
- Title: sqlite_utils Python library - sqlite-utils
- Links:
  - https://sqlite-utils.datasette.io/en/stable/python-api.html - Skip to content
  - https://sqlite-utils.datasette.io/en/stable/index.html - sqlite-utils
  - https://sqlite-utils.datasette.io/en/stable/installation.html - Installation
  - https://sqlite-utils.datasette.io/en/stable/cli.html - sqlite-utils command-line tool
  - https://sqlite-utils.datasette.io/en/stable/migrations.html - Database migrations
  - https://sqlite-utils.datasette.io/en/stable/plugins.html - Plugins
  - https://sqlite-utils.datasette.io/en/stable/reference.html - API reference
  - https://sqlite-utils.datasette.io/en/stable/cli-reference.html - CLI reference
  - https://sqlite-utils.datasette.io/en/stable/upgrading.html - Upgrading
  - https://sqlite-utils.datasette.io/en/stable/contributing.html - Contributing
  - https://sqlite-utils.datasette.io/en/stable/changelog.html - Changelog
  - https://sqlite-utils.datasette.io/en/stable/_sources/python-api.rst.txt - View this page
  - https://www.sqlite.org/pragma.html - recursive triggers
  - https://www.sqlite.org/stricttables.html - SQLite STRICT mode
  - https://docs.python.org/3/library/sqlite3.html - sqlite3.Cursor
  - https://datasette.io/ - Datasette
  - https://github.com/simonw/sqlite-utils/issues/66 - issue #66
  - https://github.com/simonw/sqlite-utils-fast-fks - sqlite-utils-fast-fks
  - https://www.sqlite.org/lang_altertable.html - described in the SQLite documentation
  - https://www.sqlite.org/json1.html - excellent JSON support

Excerpt:

sqlite_utils Python library - sqlite-utils Skip to content sqlite-utils sqlite-utils Installation sqlite-utils command-line tool sqlite_utils Python library Database migrations Plugins API reference CLI reference Upgrading Contributing Changelog Back to top View this page sqlite_utils Python library ¶ Getting started Connecting to or creating a database Closing a database Attaching additional databases Tracing queries Executing queries db.query(sql, params) db.execute(sql, params) Passing parameters Transactions and saving your changes Grouping changes with db.atomic() Raw SQL writes with db.execute() Managing transactions yourself Supported connection modes Accessing tables Accessing views Listing tables Listing views Listing rows Counting rows Listing rows with their primary keys Retrieving a specific record Showing the schema Creating tables Custom column order and column types Explicitly creating a table Compound primary keys Specifying foreign keys Compound foreign keys Table configuration options Setting defaults and not null constraints Renaming a table Duplicating tables Bulk inserts Inserting data from a list or tuple iterator Insert-replacing data Updating a specific record Deleting a specific record Deleting multiple records Upserting data Alternative upserts using INSERT OR IGNORE Converting data in columns Working with lookup tables Creating lookup tables explicitly Populating lookup tables automatically during insert/upsert Working with many-to-many relationships Using m2m and lookup tables together Analyzing a column Adding columns Adding columns automatically on insert/update Adding foreign key constraints Adding multiple foreign key constraints at once Adding indexes for all foreign keys Dropping a table or view Transforming a table Altering column types Renaming columns Dropping columns Changing primary keys Changing not null status Altering column defaults Changing column order Adding foreign key constraints Replacing foreign key constraints Dropping foreign key constraints Custom transformations with .transform_sql() Extracting columns into a separate table Setting an ID based on the hash of the row contents Creating views Storing JSON Converting column values using SQL functions Checking the SQLite version Dumping the database to SQL Introspecting tables and views .exists() .count .columns .columns_dict .default_values .pks .use_rowid .foreign_keys .schema .strict .indexes .xindexes .triggers .triggers_dict .detect_fts() .virtual_table

### 4. ALTER TABLE

- Type: web
- URL: https://www.sqlite.org/lang_altertable.html
- Title: ALTER TABLE
- Links:
  - https://www.sqlite.org/index.html
  - https://www.sqlite.org/about.html - About
  - https://www.sqlite.org/docs.html - Documentation
  - https://www.sqlite.org/download.html - Download
  - https://www.sqlite.org/copyright.html - License
  - https://www.sqlite.org/support.html - Support
  - https://www.sqlite.org/prosupport.html - Purchase
  - https://www.sqlite.org/lang_altertable.html - 1. Overview
  - https://www.sqlite.org/syntax/alter-table-stmt.html - alter-table-stmt:
  - https://www.sqlite.org/syntax/column-def.html - column-def:
  - https://www.sqlite.org/syntax/column-constraint.html - column-constraint:
  - https://www.sqlite.org/syntax/foreign-key-clause.html - foreign-key-clause:
  - https://www.sqlite.org/syntax/literal-value.html - literal-value:
  - https://www.sqlite.org/syntax/signed-number.html - signed-number:
  - https://www.sqlite.org/syntax/type-name.html - type-name:
  - https://www.sqlite.org/syntax/conflict-clause.html - conflict-clause:
  - https://www.sqlite.org/syntax/expr.html - expr:
  - https://www.sqlite.org/syntax/filter-clause.html - filter-clause:
  - https://www.sqlite.org/syntax/function-arguments.html - function-arguments:
  - https://www.sqlite.org/syntax/ordering-term.html - ordering-term:

Excerpt:

ALTER TABLE Small. Fast. Reliable. Choose any three. Home Menu About Documentation Download License Support Purchase Search About Documentation Download Support Purchase Search Documentation Search Changelog ALTER TABLE Table Of Contents 1. Overview 2. ALTER TABLE RENAME 3. ALTER TABLE RENAME COLUMN 4. ALTER TABLE ADD COLUMN 5. ALTER TABLE DROP COLUMN 5.1. How It Works 6. ALTER TABLE ALTER COLUMN 7. Disable Error Checking Using PRAGMA writable_schema=ON 8. Making Other Kinds Of Table Schema Changes 9. Why ALTER TABLE is such a problem for SQLite 1. Overview alter-table-stmt: hide column-def: show column-constraint: show foreign-key-clause: show literal-value: show signed-number: show type-name: show signed-number: show conflict-clause: show expr: show filter-clause: show function-arguments: show ordering-term: show literal-value: show over-clause: show frame-spec: show ordering-term: show raise-function: show select-stmt: show common-table-expression: show compound-operator: show join-clause: show join-constraint: show join-operator: show ordering-term: show result-column: show table-or-subquery: show window-defn: show frame-spec: show type-name: show signed-number: show SQLite supports a limited subset of ALTER TABLE. The ALTER TABLE command in SQLite allows these alterations of an existing table: it can be renamed; a column can be renamed; a column can be added to it; or a column can be dropped from it. 2. ALTER TABLE RENAME The RENAME TO syntax changes the name of table-name to new-table-name . This command cannot be used to move a table between attached databases, only to rename a table within the same database. If the table being renamed has triggers or indices, then these remain attached to the table after it has been renamed. Compatibility Note: The behavior of ALTER TABLE when renaming a table was enhanced in versions 3.25.0 (2018-09-15) and 3.26.0 (2018-12-01) in order to carry the rename operation forward into triggers and views that reference the renamed table. This is considered an improvement. Applications that depend on the older (and arguably buggy) behavior can use the PRAGMA legacy_alter_table=ON statement or the SQLITE_DBCONFIG_LEGACY_ALTER_TABLE configuration parameter on sqlite3_db_config() interface to make ALTER TABLE RENAME behave as it did prior to version 3.25.0. Beginning with release 3.25.0 (2018-09-15), references to the table within trigger bodies and view definitions are also renamed. Prior to version 3.26.0 (2018-12-01), FORE

### 5. Database migrations - sqlite-utils

- Type: web
- URL: https://sqlite-utils.datasette.io/en/stable/migrations.html
- Title: Database migrations - sqlite-utils
- Links:
  - https://sqlite-utils.datasette.io/en/stable/migrations.html - Skip to content
  - https://sqlite-utils.datasette.io/en/stable/index.html - sqlite-utils
  - https://sqlite-utils.datasette.io/en/stable/installation.html - Installation
  - https://sqlite-utils.datasette.io/en/stable/cli.html - sqlite-utils command-line tool
  - https://sqlite-utils.datasette.io/en/stable/python-api.html - sqlite_utils Python library
  - https://sqlite-utils.datasette.io/en/stable/plugins.html - Plugins
  - https://sqlite-utils.datasette.io/en/stable/reference.html - API reference
  - https://sqlite-utils.datasette.io/en/stable/cli-reference.html - CLI reference
  - https://sqlite-utils.datasette.io/en/stable/upgrading.html - Upgrading
  - https://sqlite-utils.datasette.io/en/stable/contributing.html - Contributing
  - https://sqlite-utils.datasette.io/en/stable/changelog.html - Changelog
  - https://sqlite-utils.datasette.io/en/stable/_sources/migrations.rst.txt - View this page
  - https://github.com/simonw/sqlite-migrate - sqlite-migrate
  - https://www.sphinx-doc.org/ - Sphinx
  - https://pradyunsg.me - @pradyunsg
  - https://github.com/pradyunsg/furo - Furo

Excerpt:

Database migrations - sqlite-utils Skip to content sqlite-utils sqlite-utils Installation sqlite-utils command-line tool sqlite_utils Python library Database migrations Plugins API reference CLI reference Upgrading Contributing Changelog Back to top View this page Database migrations ¶ sqlite-utils includes a migration system for applying repeatable changes to SQLite database files. A migration is a Python function that receives a sqlite_utils.Database instance and then executes Python code to modify that database - creating or transforming tables, adding indexes, inserting rows, or any other operation supported by SQLite. Migrations are grouped into named sets using the sqlite_utils.Migrations class, and each applied migration is recorded in the _sqlite_migrations table in that database. This means you can run the migrate operation multiple times and it will only apply migrations that have not previously been recorded. Defining migrations ¶ Ordered migration sets are defined by first creating a sqlite_utils.Migrations object. Individual migrations are Python functions that are then registered with that migration set. Each migration function is passed a single argument that is a sqlite_utils.Database instance. The name passed to Migrations("creatures") identifies that set of migrations. Use a name that is unique for your project, since multiple migration sets can be applied to the same database. Here is a simple example of a migrations.py file which creates a table, then adds an extra column to that table in a second migration: from sqlite_utils import Database , Migrations migrations = Migrations ( "creatures" ) @migrations () def create_table ( db ): db [ "creatures" ] . create ( { "id" : int , "name" : str , "species" : str }, pk = "id" , ) @migrations () def add_weight ( db ): db [ "creatures" ] . add_column ( "weight" , float ) Applying migrations in Python ¶ Once you have a Migrations(name) collection with one or more migrations registered to it, you can execute them in Python code like this: db = Database ( "creatures.db" ) migrations . apply ( db ) Running migrations.apply(db) repeatedly is safe. Migrations that already have a matching migration_set and name row in _sqlite_migrations will be skipped. Migration functions are applied in the order that they were registered. The function name is used as the migration name unless you pass one explicitly: @migrations ( name = "001_create_table" ) def create_table ( db ): db [ "creatures" ] . create ({ "i

### 6. Migrations | Django documentation

- Type: web
- URL: https://docs.djangoproject.com/en/6.0/topics/migrations/
- Title: Migrations | Django documentation
- Description: The web framework for perfectionists with deadlines.
- Links:
  - https://docs.djangoproject.com/en/6.0/topics/migrations/ - Skip to main content
  - https://www.djangoproject.com/ - Django
  - https://www.djangoproject.com/start/overview/ - Overview
  - https://www.djangoproject.com/download/ - Download
  - https://docs.djangoproject.com/ - Documentation
  - https://www.djangoproject.com/weblog/ - News
  - https://github.com/django/django - Code
  - https://code.djangoproject.com/ - Issues
  - https://www.djangoproject.com/community/ - Community
  - https://www.djangoproject.com/foundation/ - Foundation
  - https://www.djangoproject.com/fundraising/ - ♥ Donate
  - https://docs.djangoproject.com/en/6.0/ - Documentation
  - https://www.djangoproject.com/weblog/2026/may/12/2026-django-developers-survey/ - Read more on the Django blog
  - https://surveys.jetbrains.com/s3/wb-django-developers-survey-2026 - Take the survey ✨
  - https://docs.djangoproject.com/en/6.0/faq/help/ - Getting Help
  - https://docs.djangoproject.com/zh-hans/6.0/topics/migrations/ - zh-hans
  - https://docs.djangoproject.com/sv/6.0/topics/migrations/ - sv
  - https://docs.djangoproject.com/pt-br/6.0/topics/migrations/ - pt-br
  - https://docs.djangoproject.com/pl/6.0/topics/migrations/ - pl
  - https://docs.djangoproject.com/ko/6.0/topics/migrations/ - ko

Excerpt:

Migrations | Django documentation | Django Skip to main content Django The web framework for perfectionists with deadlines. Menu Main navigation Overview Download Documentation News Code Issues Community Foundation ♥ Donate Search Submit Toggle theme (current theme: auto) Toggle theme (current theme: light) Toggle theme (current theme: dark) Toggle Light / Dark / Auto color theme Documentation Django Developer Survey The Django Software Foundation is once again partnering with JetBrains to run the 2026 Django Developer Survey 📊 Help us better understand how Django is being used around the world and guide future technical and community decisions. Read more on the Django blog . Take the survey ✨ Getting Help Language: en zh-hans sv pt-br pl ko ja it id fr es el Documentation version: 6.0 dev 6.1 5.2 5.1 5.0 4.2 4.1 4.0 3.2 3.1 3.0 2.2 2.1 2.0 1.11 1.10 1.9 1.8 Migrations ¶ Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into. The Commands ¶ There are several commands which you will use to interact with migrations and Django’s handling of database schema: migrate , which is responsible for applying and unapplying migrations. makemigrations , which is responsible for creating new migrations based on the changes you have made to your models. sqlmigrate , which displays the SQL statements for a migration. showmigrations , which lists a project’s migrations and their status. You should think of migrations as a version control system for your database schema. makemigrations is responsible for packaging up your model changes into individual migration files - analogous to commits - and migrate is responsible for applying those to your database. The migration files for each app live in a “migrations” directory inside of that app, and are designed to be committed to, and distributed as part of, its codebase. You should be making them once on your development machine and then running the same migrations on your colleagues’ machines, your staging machines, and eventually your production machines. Note It is possible to override the name of the package which contains the migrations on a per-app basis by modifying the MIGRATION_MODULES setting. Migrations will run the same way on the same dataset and produce consistent results, meaning

### 7. https://www.youtube.com/watch?v=VSq8m00p1FM

- Type: video
- URL: https://www.youtube.com/watch?v=VSq8m00p1FM
- Fetch status: limited (metadata-only host; skipped raw HTML fetch)

### 8. Savepoints

- Type: web
- URL: https://sqlite.org/lang_savepoint.html
- Title: Savepoints
- Links:
  - https://sqlite.org/index.html
  - https://sqlite.org/about.html - About
  - https://sqlite.org/docs.html - Documentation
  - https://sqlite.org/download.html - Download
  - https://sqlite.org/copyright.html - License
  - https://sqlite.org/support.html - Support
  - https://sqlite.org/prosupport.html - Purchase
  - https://sqlite.org/syntax/savepoint-stmt.html - savepoint-stmt:
  - https://sqlite.org/syntax/release-stmt.html - release-stmt:
  - https://sqlite.org/syntax/rollback-stmt.html - rollback-stmt:
  - https://sqlite.org/lang_transaction.html - BEGIN

Excerpt:

Savepoints Small. Fast. Reliable. Choose any three. Home Menu About Documentation Download License Support Purchase Search About Documentation Download Support Purchase Search Documentation Search Changelog Savepoints 1. Syntax savepoint-stmt: hide release-stmt: hide rollback-stmt: hide 2. Savepoints SAVEPOINTs are a method of creating transactions, similar to BEGIN and COMMIT , except that the SAVEPOINT and RELEASE commands are named and may be nested. The SAVEPOINT command starts a new transaction with a name. The transaction names need not be unique. A SAVEPOINT can be started either within or outside of a BEGIN ... COMMIT . When a SAVEPOINT is the outer-most savepoint and it is not within a BEGIN ... COMMIT then the behavior is the same as BEGIN DEFERRED TRANSACTION. The ROLLBACK TO command reverts the state of the database back to what it was just after the corresponding SAVEPOINT. Note that unlike that plain ROLLBACK command (without the TO keyword) the ROLLBACK TO command does not cancel the transaction. Instead of cancelling the transaction, the ROLLBACK TO command restarts the transaction again at the beginning. All intervening SAVEPOINTs are canceled, however. The RELEASE command is like a COMMIT for a SAVEPOINT. The RELEASE command causes all savepoints back to and including the most recent savepoint with a matching name to be removed from the transaction stack. The RELEASE of an inner transaction does not cause any changes to be written to the database file; it merely removes savepoints from the transaction stack such that it is no longer possible to ROLLBACK TO those savepoints. If a RELEASE command releases the outermost savepoint, so that the transaction stack becomes empty, then RELEASE is the same as COMMIT . The COMMIT command may be used to release all savepoints and commit the transaction even if the transaction was originally started by a SAVEPOINT command instead of a BEGIN command. If the savepoint-name in a RELEASE command does not match any savepoint currently in the transaction stack, then no savepoints are released, the database is unchanged, and the RELEASE command returns an error. Note that an inner transaction might commit (using the RELEASE command) but then later have its work undone by a ROLLBACK in an outer transaction. A power failure or program crash or OS crash will cause the outer-most transaction to rollback, undoing all changes that have occurred within that outer transaction, even changes that have supposedly been 

### 9. https://gist.githubusercontent.com/simonw/95800bf584f8e437f1cf0d48d9ef81e6/raw/c43918b36a129bba1d2f2a129117aa11c85146c0/12_bug_repros.py

- Type: web
- URL: https://gist.githubusercontent.com/simonw/95800bf584f8e437f1cf0d48d9ef81e6/raw/c43918b36a129bba1d2f2a129117aa11c85146c0/12_bug_repros.py

Excerpt:

# Reproductions of bugs found while reviewing 4.0 before release. # Each check prints BUG when the problem reproduces - these are expected # to print BUG until fixed. Run: uv run python scratch-v4/12_bug_repros.py import pathlib import sqlite3 import sqlite_utils here = pathlib.Path(__file__).parent def fresh(name): p = here / name p.unlink(missing_ok=True) return p print("=== 1. Failed db.execute() write leaves an implicit transaction open ===") # The auto-commit in execute() only happens on the success path. After a # failed write the sqlite3 driver's implicit BEGIN stays open, so every # subsequent write joins a phantom transaction that nothing commits - # work is silently lost when the connection closes. p = fresh("bug1.db") db = sqlite_utils.Database(p) db.execute("create table t (id integer primary key)") db.execute("insert into t values (1)") try: db.execute("insert into t values (1)") # IntegrityError except sqlite3.IntegrityError: pass print(f" in_transaction after failed write: {db.conn.in_transaction}") db["other"].insert({"id": 1}) # visible on this connection... db.close() db2 = sqlite_utils.Database(p) if not db2["other"].exists(): print(" BUG: table 'other' silently lost when connection closed") else: print(" ok: table 'other' survived") db2.close() print() print("=== 2. Leading ';' bypasses the query() first-token scanner ===") # sqlite3 accepts '; COMMIT' but _first_keyword() stops at the ';' and # returns '', so the transaction-statement rejection is skipped. The COMMIT # executes, commits the user's open transaction and destroys the guard # savepoint, raising OperationalError instead of ValueError. p = fresh("bug2.db") db = sqlite_utils.Database(p) db.execute("create table t (id integer primary key)") db.begin() db.execute("insert into t values (99)") try: db.query("; COMMIT") except ValueError: print(" ok: rejected with ValueError") except Exception as ex: print(f" BUG: raised {type(ex).__name__}: {ex}") try: db.rollback() except Exception as ex: print(f" rollback also broken: {type(ex).__name__}: {ex}") db.close() db2 = sqlite_utils.Database(p) n = db2.execute("select count(*) from t").fetchone()[0] if n: print(f" BUG: row persisted despite rollback (count={n})") else: print(" ok: rollback worked") db2.close() print() print("=== 3. Rejected write PRAGMA via query() still takes effect ===") # query() promises rejected statements are rolled back and have no effect, # but the PRAGMA path executes before the returns-rows check and outside 

### 10. Simon Willison (@simon@simonwillison.net)

- Type: web
- URL: https://fedi.simonwillison.net/@simon
- Title: Simon Willison (@simon@simonwillison.net)
- Description: 9.31K Posts, 2.07K Following, 27.6K Followers · Open source developer building tools to help journalists, archivists, librarians and others analyze, explore and publish their data. https://datasette.io and many other #projects.
- Links:
  - https://joinmastodon.org/apps

Excerpt:

Simon Willison (@simon@simonwillison.net) - Mastodon

