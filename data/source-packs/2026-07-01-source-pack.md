# Firsthand AI Digest Source Pack

- Generated: 2026-07-01T08:13:01+08:00
- Intended coverage window: 2026-06-30T08:13:01+08:00 to 2026-07-01T08:13:01+08:00
- Index site: https://ai.prov1dence.top/
- Firsthand AI Digest items in window: 56
- Detail pages fetched: 0
- First-layer original sources fetched/listed: 56
- Original sources with fetched page text: 5
- Metadata-only original sources: 51
- Other limited original sources: 0
- Secondary source candidates fetched/listed: 10

This is a collection aid, not the final analysis. Open primary sources directly before writing final claims.

## Index Page

- URL: https://ai.prov1dence.top/
- Title: Firsthand AI Digest
- Links:
  - https://insight.ai.prov1dence.top/ - Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours.
  - https://simonwillison.net/2026/Jun/30/claude-sonnet-5/ - Read article ↗
  - https://simonwillison.net/2026/Jun/30/the-ai-compass/ - Read article ↗
  - https://simonwillison.net/2026/Jun/30/shot-scraper-video/ - Read article ↗
  - https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/ - Read article ↗
  - https://simonwillison.net/2026/Jun/30/shot-scraper/ - Read article ↗
  - https://simonwillison.net/2026/Jun/29/html-table-extractor/ - Read article ↗
  - https://www.youtube.com/watch?v=pv1TUJSEM2k - Watch ↗
  - https://www.youtube.com/watch?v=88IxTQT8PBM - Watch ↗
  - https://www.youtube.com/shorts/HfjF__xhSdk - Watch ↗
  - https://x.com/steipete/status/2072061089177539003 - Open ↗
  - https://x.com/petergyang/status/2072051258882666620 - Open ↗
  - https://x.com/miramurati/status/2072050039317578236 - Open ↗
  - https://x.com/swyx/status/2072048730581405800 - Open ↗
  - https://x.com/levie/status/2072046374045249671 - Open ↗
  - https://x.com/rauchg/status/2072044844965400589 - Open ↗
  - https://x.com/steipete/status/2072037247122284825 - Open ↗
  - https://x.com/elonmusk/status/2072034905299563005 - Open ↗
  - https://x.com/AravSrinivas/status/2072031649693675810 - Open ↗
  - https://x.com/danshipper/status/2072025187751731334 - Open ↗

Excerpt:

Firsthand AI Digest Firsthand AI Digest Posts, blogs, podcasts and videos from the people building AI — straight from the source. Analysis Latest AI Insight -> Daily interpreted brief from the last 24 hours. Time 3h 6h 12h 24h 3d 7d Type All Blogs Podcasts Videos Posts Blogs & Long-form 06 items SW Simon Willison By Simon Willison Blog What's new in Claude Sonnet 5 What's new in Claude Sonnet 5 Claude Sonnet 5 came out this morning. I always head straight for the "what's new" developer docs because they tend to have more actionable information than the official announcement post. Anthropic say of Sonnet 5 that "its performance is close to that of Opus 4.8, but at lower prices". The system card helps explain how they were able to release the model without being blocked by the US government: Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models that are more capable than Sonnet 5 but much less capable than Mythos 5). Of note from the "what's new" API changes: Sampling parameters temperature, top_p, top_k are no longer supported. It has a 1 million token context window and 128,000 maximum output tokens. It features "the same set of tools and platform features as Claude Sonnet 4.6" Adaptive thinking is on by default, unless you specify "thinking": {type: "disabled"}. The pricing is the same as Sonnet 4.6: $3/million input, $15/million input, with an introductory discount to $2/$10 until 31st August. But... The model has a new tokenizer, where "The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6." - effectively a 30% price increase. I used my Claude Token Counter tool to try out the new tokenizer. Here are my results for several larger documents: Document Sonnet 4.6 Opus 4.7 Sonnet 5 Universal Declaration of Human Rights (English) 2,356 3,347 1.42x 3,341 1.42x Universal Declaration of Human Rights (Spanish) 3,572 4,753 1.33x 4,747 1.33x Universal Declaration of Human Rights (Chinese, Mandarin Simplified) 3,334 3,366 1.01x 3,360 1.01x sqlite_utils/db.py (4,279 lines of Python) 44,014 56,118 1.28x 56,113 1.27x So the new token is roughly 1.4x times more expensive for English, 1.33x for Spanish, 1.28x for Python code and effectively the same cost for Simplified Mandarin. Here's the pelican. It's nothing to write home about. Sonnet 5 thinks it looks like a goose. Via Hacker News Tags: ai, generative-ai, llms, anthropic, claude, llm-pric

## Firsthand AI Digest Items In Window

### 1. What's new in Claude Sonnet 5

- URL: https://simonwillison.net/2026/Jun/30/claude-sonnet-5/
- Type: Blog
- Published: 2026-06-30T21:23:02+00:00
- Digest summary: What's new in Claude Sonnet 5 Claude Sonnet 5 came out this morning. I always head straight for the "what's new" developer docs because they tend to have more actionable information than the official announcement post. Anthropic say of Sonnet 5 that "its performance is close to that of Opus 4.8, but at lower prices". The system card helps explain how they were able to release the model without being blocked by the US government: Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models that are more capable than Sonnet 5 but much less capable than Mythos 5). Of note from the "what's new" API changes: Sampling parameters temperature, top_p, top_k are no longer supported. It has a 1 million token co

### 2. The AI Compass

- URL: https://simonwillison.net/2026/Jun/30/the-ai-compass/
- Type: Blog
- Published: 2026-06-30T17:39:23+00:00
- Digest summary: The AI Compass This political compass style quiz by bambamramfan is pretty neat - answer 29 questions about AI and AI ethics to see which of the 30 archetypes you best fit. I'm impressed that my answers on my first time through the quiz categorized me as "The Garage Tinkerer", patron saint myself! It's implemented as a single page React app using the <script type="text/babel"> trick to avoid the necessary build step. Here's the code. Via @erisianrite.com Tags: ai, generative-ai, llms, ai-ethics

### 3. Have your agent record video demos of its work with shot-scraper video

- URL: https://simonwillison.net/2026/Jun/30/shot-scraper-video/
- Type: Blog
- Published: 2026-06-30T16:54:26+00:00
- Digest summary: shot-scraper video is a new command introduced in today's shot-scraper 1.10 release which accepts a storyboard.yml file defining a routine to run against a web application and uses Playwright to record a video of that routine. I've written before about the importance of having coding agents produce demos of their work; this is my latest attempt at enabling them to do that. Here's an example video created using shot-scraper video, exercising a still in development feature adding the ability to create new tables in Datasette from pasted CSV, TSV or JSON data: That video was created by running this command: shot-scraper video datasette-bulk-insert-storyboard.yml \ --auth datasette-demo-auth.json --mp4 (That --auth JSON file contains a cookie, as described here in the documentation.) Here's th

### 4. Start building with Nano Banana 2 Lite and Gemini Omni Flash

- URL: https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/
- Type: Blog
- Published: 2026-06-30T16:02:40+00:00

### 5. shot-scraper 1.10

- URL: https://simonwillison.net/2026/Jun/30/shot-scraper/
- Type: Blog
- Published: 2026-06-30T15:10:14+00:00
- Digest summary: Release: shot-scraper 1.10 The big new feature is shot-scraper video storyboard.yml, described in detail in Have your agent record video demos of its work with shot-scraper video. Tags: shot-scraper

### 6. Anthony Kaldellis: Roman Empire, Byzantine Empire, Rise & Fall of Empires | Lex Fridman Podcast #498

- URL: https://www.youtube.com/watch?v=pv1TUJSEM2k
- Type: Video
- Published: 2026-06-30T21:16:13+00:00
- Digest summary: Anthony Kaldellis is a historian of the Roman Empire and author of "The New Roman Empire", a comprehensive history of the Byzantine Empire (Eastern Roman Empire). Thank you for listening ❤ Check out our sponsors: https://lexfridman.com/sponsors/ep498-sb See below for timestamps, transcript, and to give feedback, submit questions, contact Lex, etc. *Transcript:* https://lexfridman.com/anthony-kaldellis-transcript *CONTACT LEX:* *Feedback* - give feedback to Lex: https://lexfridman.com/survey *AMA* - submit questions, videos or call-in: https://lexfridman.com/ama *Hiring* - join our team: https://lexfridman.com/hiring *Other* - other ways to get in touch: https://lexfridman.com/contact *EPISODE LINKS:* Anthony's Books: https://amzn.to/49AX7Q1 Anthony's Publications: https://kaldellispublicat

### 7. Machiavelli was NOT Machiavellian – Ada Palmer

- URL: https://www.youtube.com/watch?v=88IxTQT8PBM
- Type: Video
- Published: 2026-06-30T16:30:10+00:00
- Digest summary: Full episode: https://www.youtube.com/watch?v=U1FrhkLQnCI Me on twitter: https://x.com/dwarkesh_sp

### 8. How LLMs Actually Generate Text

- URL: https://www.youtube.com/shorts/HfjF__xhSdk
- Type: Video
- Published: 2026-06-30T06:34:41+00:00
- Digest summary: Text generation looks like one function call. Underneath, it's a loop: infer, pick a token, append it, repeat. Watch how Transformers.js runs an LLM step by step.. and understand what's actually happening every time you chat with one.

### 9. https://x.com/steipete/status/2072061089177539003

- URL: https://x.com/steipete/status/2072061089177539003
- Type: Post
- Published: 2026-06-30T20:53:55+00:00
- Digest summary: Folks I found the reset button. @thsottiaux https://t.co/kqWkXvevd1

### 10. https://x.com/petergyang/status/2072051258882666620

- URL: https://x.com/petergyang/status/2072051258882666620
- Type: Post
- Published: 2026-06-30T20:14:51+00:00
- Digest summary: I think @charlieholtz is right - the term "software factory" implies assembly line style tasks. That can't be the future of work with AI. We should be collaborating with agents like a conductor working with an orchestra or a film director working with a crew or a chef leading a kitchen. Work needs to be creative.

### 11. https://x.com/miramurati/status/2072050039317578236

- URL: https://x.com/miramurati/status/2072050039317578236
- Type: Post
- Published: 2026-06-30T20:10:00+00:00
- Digest summary: Bridgewater used their unique financial knowledge and partnered with us on @tinkerapi to fine-tune a model that helps their analysts focus on what's important. Experts improving AI that empowers experts. https://t.co/6RJITMG2BJ

### 12. https://x.com/swyx/status/2072048730581405800

- URL: https://x.com/swyx/status/2072048730581405800
- Type: Post
- Published: 2026-06-30T20:04:48+00:00
- Digest summary: very successful first poster sessions day at AIEWF, thanks to @heathercmiller and @ACM_President for the support!! tomorrow: Poaster sessions! submit your hottest tweets to @vibhuuuus for printing! spotted: left shark https://t.co/nv2I2l00Oe

### 13. https://x.com/levie/status/2072046374045249671

- URL: https://x.com/levie/status/2072046374045249671
- Type: Post
- Published: 2026-06-30T19:55:26+00:00
- Digest summary: We've been running Anthropic's Claude Sonnet 5 through the Box AI Complex Work Eval, our agentic benchmark that puts models through real enterprise document work end-to-end. Sonnet 5 holds frontier-class quality on complex multi-step work and pulls ahead of Sonnet 4.6 in several core enterprise domains like Energy (+4.7pp), Retail (+4.4pp), and Professional Services (+2.6pp), and other spaces where unstructured data is heavily complex. Here are a few examples of wins compared to Sonnet 4.6 to get a sense of some of the more advanced reasoning capabilities in Sonnet 5: * Financing due diligence: It computed the company's liquidity and leverage ratios from the raw balance sheet, and caught that the source report's own stated debt-to-equity figure understated the leverage, flagging all three 

### 14. https://x.com/rauchg/status/2072044844965400589

- URL: https://x.com/rauchg/status/2072044844965400589
- Type: Post
- Published: 2026-06-30T19:49:22+00:00
- Digest summary: So great to get to work with @tobi and the wonderful @shopify team. Excited to push the agentic web forward.

### 15. https://x.com/steipete/status/2072037247122284825

- URL: https://x.com/steipete/status/2072037247122284825
- Type: Post
- Published: 2026-06-30T19:19:10+00:00
- Digest summary: Honored to be part of @aiDotEngineer’s keynote today!

### 16. https://x.com/elonmusk/status/2072034905299563005

- URL: https://x.com/elonmusk/status/2072034905299563005
- Type: Post
- Published: 2026-06-30T19:09:52+00:00
- Digest summary: Neuralink has solved through-dura electrode implantation! This is a very big deal, as it greatly improves the safety and ease of interfacing with the brain.

### 17. https://x.com/AravSrinivas/status/2072031649693675810

- URL: https://x.com/AravSrinivas/status/2072031649693675810
- Type: Post
- Published: 2026-06-30T18:56:56+00:00
- Digest summary: New orchestrator model for Computer users (Pro and Max): Sonnet 5.

### 18. https://x.com/danshipper/status/2072025187751731334

- URL: https://x.com/danshipper/status/2072025187751731334
- Type: Post
- Published: 2026-06-30T18:31:15+00:00
- Digest summary: yo — it's the Every growth team. Dan's in Cabo, so we're taking over for some live reactions to Sonnet 5. before our official vibe check drops, we asked the new model to search our systems and guess what Dan's up to on vacation right now 👇 1. checking Slack from the beach 10 minutes after telling ops he's "on PTO" 2. running his own one-man vibe check before ours is even live 3. locking in so deep with Codex vibe coding he doesn't even know Sonnet 5 dropped 4. texting Dario unsolicited hot takes 5. giving out free copies of Annie Dillard to everyone at his hotel follow along for more updates from the big dog's account while our team runs their benchmarks

### 19. https://x.com/claudeai/status/2072017450611142835

- URL: https://x.com/claudeai/status/2072017450611142835
- Type: Post
- Published: 2026-06-30T18:00:31+00:00
- Digest summary: Introducing Claude Sonnet 5, our most agentic Sonnet yet. It makes plans, uses tools like browsers and terminals, and runs autonomously at a level that just a few months ago required larger and more expensive models. https://t.co/UKK8G7ww5h

### 20. https://x.com/elonmusk/status/2072015711635914948

- URL: https://x.com/elonmusk/status/2072015711635914948
- Type: Post
- Published: 2026-06-30T17:53:36+00:00
- Digest summary: Half price Starlink for people in the Memphis region

### 21. https://x.com/OpenAI/status/2072004836674167294

- URL: https://x.com/OpenAI/status/2072004836674167294
- Type: Post
- Published: 2026-06-30T17:10:23+00:00
- Digest summary: We’re introducing GeneBench-Pro, a research-level benchmark for a harder kind of AI progress: how well agents can navigate messy biological data, choose the right analysis path, and make judgment calls that real computational research depends on. https://t.co/AsilnnSxnE

### 22. https://x.com/petergyang/status/2072004576442802487

- URL: https://x.com/petergyang/status/2072004576442802487
- Type: Post
- Published: 2026-06-30T17:09:21+00:00
- Digest summary: GLM's new harness - should it be just called Z Codex https://t.co/8yqB7ooOtz

### 23. https://x.com/DrJimFan/status/2072004190856212902

- URL: https://x.com/DrJimFan/status/2072004190856212902
- Type: Post
- Published: 2026-06-30T17:07:49+00:00
- Digest summary: Today, we give robots a /skills library that self-evolves and compounds indefinitely! Introducing ASPIRE: a robot solving its 100th task is no longer as clueless as solving its first. Coding agents observe multimodal sensory traces from simulation and real robots, launch an evolutionary search over control programs, and distill the best know-how into an ever-expanding library. ASPIRE is a new type of continual learning: "training" is skill refinement instead of gradient descent. "Trained model" is a repo of sensorimotor skills instead of floating weights. “Distributed training” is a panel of agents each practicing a different skill instead of sharded minibatches. Here's the beauty: ASPIRE gives the tired terms "sim2real transfer" and "cross-embodiment transfer" a whole new meaning. Bridgin

### 24. https://x.com/claudeai/status/2072002740830842899

- URL: https://x.com/claudeai/status/2072002740830842899
- Type: Post
- Published: 2026-06-30T17:02:04+00:00
- Digest summary: Introducing Claude Science, a new app designed with every stage of research in mind. Artifacts traced to their code, environments managed on demand, and 60+ optional scientific databases that you can connect. Available now in beta. https://t.co/HKhLknxLJO

### 25. https://x.com/elonmusk/status/2072000588112343388

- URL: https://x.com/elonmusk/status/2072000588112343388
- Type: Post
- Published: 2026-06-30T16:53:30+00:00
- Digest summary: SpaceXAI

### 26. https://x.com/elonmusk/status/2072000185769586922

- URL: https://x.com/elonmusk/status/2072000185769586922
- Type: Post
- Published: 2026-06-30T16:51:54+00:00
- Digest summary: And that’s just the tip of the iceberg

### 27. https://x.com/elonmusk/status/2071994061624426582

- URL: https://x.com/elonmusk/status/2071994061624426582
- Type: Post
- Published: 2026-06-30T16:27:34+00:00
- Digest summary: https://t.co/VgpWIg2BFI

### 28. https://x.com/levie/status/2071992799109824562

- URL: https://x.com/levie/status/2071992799109824562
- Type: Post
- Published: 2026-06-30T16:22:33+00:00
- Digest summary: More data is showing the opposite of what many people expected with AI adoption and jobs. Ramp found that the more AI adoption a company has the more their headcount grows. At Box, we recently did a survey of 1,600+ mid and large sized companies, and the findings were similar. 58% of respondents expected headcount to rise over the next three years. Interestingly, that figure climbs to 79% among the most mature adopters of AI. The more advanced AI adopters expected to grow their headcount at a greater rate in the future than others. Of course it's true that the companies that can afford to adopt AI the most are also the ones that likely are seeing growth in their business, leading to more headcount. So the point of the story isn't necessarily that by adopting AI you will inherently grow. *B

### 29. https://x.com/amasad/status/2071992670394765407

- URL: https://x.com/amasad/status/2071992670394765407
- Type: Post
- Published: 2026-06-30T16:22:03+00:00
- Digest summary: World’s first subway hackathon!

### 30. https://x.com/amasad/status/2071992110132117740

- URL: https://x.com/amasad/status/2071992110132117740
- Type: Post
- Published: 2026-06-30T16:19:49+00:00
- Digest summary: AI is expensive to run partly because most workloads today run on generic hardware designed pre-LLMs. Etched is the first system designed from the ground up for modern inference.

### 31. https://x.com/AndrewYNg/status/2071988145667928442

- URL: https://x.com/AndrewYNg/status/2071988145667928442
- Type: Post
- Published: 2026-06-30T16:04:04+00:00
- Digest summary: “Loop engineering” is a hot buzzphrase after mentions of it by Boris Cherny (Claude Code’s creator) and Peter Steinberger (OpenClaw's creator) went viral on social media. Loops are now a key part of how we get AI agents to iterate at length to build software. In this letter, I’d like to share my 3 key loops, shown in the image below, for building 0-to-1 products. These loops guide not just how I build software, but also how I decide what software to build. Agentic coding loop: Given a product specification and optionally a set of evals (that is, a dataset against which to measure performance), we can have an AI agent write code, test its work, and keep iterating until the code is bug-free and meets its specification. This idea of closing the loop took off around the end of last year, and i

### 32. https://x.com/GoogleDeepMind/status/2071988044878516466

- URL: https://x.com/GoogleDeepMind/status/2071988044878516466
- Type: Post
- Published: 2026-06-30T16:03:40+00:00
- Digest summary: We’re shipping 2 major releases: 🔘 Nano Banana 2 Lite: our fastest and cheapest Gemini Image model 🔘 Gemini Omni Flash: now available via the Gemini API and in @GoogleAIStudio to help developers generate and edit high-quality videos.

### 33. https://x.com/petergyang/status/2071985410809700863

- URL: https://x.com/petergyang/status/2071985410809700863
- Type: Post
- Published: 2026-06-30T15:53:12+00:00
- Digest summary: Been using @riversidedotfm for 2 years now to produce my podcast and will continue to be a loyal customer. Great to see them expand to end to end content production. You can get 1 month free with "peteryang" at checkout: https://t.co/KbfkRqU2cR

### 34. https://x.com/elonmusk/status/2071984597311557807

- URL: https://x.com/elonmusk/status/2071984597311557807
- Type: Post
- Published: 2026-06-30T15:49:58+00:00
- Digest summary: I will take that as a compliment https://t.co/kTZqkuPqMf

### 35. https://x.com/adityaag/status/2071983952894837062

- URL: https://x.com/adityaag/status/2071983952894837062
- Type: Post
- Published: 2026-06-30T15:47:24+00:00
- Digest summary: It is a very strange state of the world where the models powering innovation in the USA are Chinese open source models.

### 36. https://x.com/AravSrinivas/status/2071982392554983440

- URL: https://x.com/AravSrinivas/status/2071982392554983440
- Type: Post
- Published: 2026-06-30T15:41:12+00:00
- Digest summary: Private market data from Forge Global now in Perplexity Computer

### 37. https://x.com/elonmusk/status/2071978911919923676

- URL: https://x.com/elonmusk/status/2071978911919923676
- Type: Post
- Published: 2026-06-30T15:27:22+00:00
- Digest summary: 🎯

### 38. https://x.com/swyx/status/2071977886991679715

- URL: https://x.com/swyx/status/2071977886991679715
- Type: Post
- Published: 2026-06-30T15:23:18+00:00
- Digest summary: we are talking loops today ✅ https://t.co/aorwoqPHZy

### 39. https://x.com/steipete/status/2071972449277898924

- URL: https://x.com/steipete/status/2071972449277898924
- Type: Post
- Published: 2026-06-30T15:01:41+00:00
- Digest summary: Good morning @aiDotEngineer ! Are we talking loops today?

### 40. https://x.com/steipete/status/2071972239734616146

- URL: https://x.com/steipete/status/2071972239734616146
- Type: Post
- Published: 2026-06-30T15:00:51+00:00
- Digest summary: Was thinking if I should highlight this tweet or not, but it’s a masterclass in the amount of vitriol people face when working on open source. Is the app great yet? No. It’s a start. It was built by the community. Getting the iOS and Android apps working with secure pairing and push notifications - and getting both through App Review -took a surprising amount of work. OpenClaw wasn’t acquired by OpenAI and isn’t an OpenAI product. It’s an open, independent project under the OpenClaw Foundation. OpenAI sponsors the project’s token usage; I work there. Cristian, your tweet was just one of ~30 I woke up to today. I’d genuinely love your help making it great. Attention is still the scarcest resource. I’d rather spend mine encouraging people who build.

### 41. https://x.com/elonmusk/status/2071968172647858409

- URL: https://x.com/elonmusk/status/2071968172647858409
- Type: Post
- Published: 2026-06-30T14:44:42+00:00
- Digest summary: https://t.co/05z7mrhVYu

### 42. https://x.com/rauchg/status/2071966055308607765

- URL: https://x.com/rauchg/status/2071966055308607765
- Type: Post
- Published: 2026-06-30T14:36:17+00:00
- Digest summary: Vercel Services You can now collocate e.g.: a Python backend API, an ExpressJS server, and a React SPA in one Vercel project. tl:dr; ▪️ You can run all locally with 𝚟𝚌 𝚍𝚎𝚟 ▪️ Deploy and rollback all at once ▪️ Observe, monitor, debug together ▪️ Internal networking

### 43. https://x.com/elonmusk/status/2071965448120180964

- URL: https://x.com/elonmusk/status/2071965448120180964
- Type: Post
- Published: 2026-06-30T14:33:52+00:00
- Digest summary: https://t.co/6IvSYzq851

### 44. https://x.com/petergyang/status/2071960766434140644

- URL: https://x.com/petergyang/status/2071960766434140644
- Type: Post
- Published: 2026-06-30T14:15:16+00:00
- Digest summary: How companies should think about driving AI adoption from @jess__yan (Anthropic product lead): “Alot of enterprises immediately jump to: How could I automate this crazy twenty-team workflow that would have required a lot of cross-cutting coordination? But there is something really valuable about: how do we unlock the individual? How do we make any individual on any team feel exponentially more powerful? There is a huge amount of value that’s unlocked simply by making every employee feel like they have their own power to develop products as a one-person startup.” 📌 Watch the full episode: https://t.co/oYU3ZV4wPL

### 45. https://x.com/rauchg/status/2071951861112840501

- URL: https://x.com/rauchg/status/2071951861112840501
- Type: Post
- Published: 2026-06-30T13:39:53+00:00
- Digest summary: The time is now

### 46. https://x.com/elonmusk/status/2071836426316984797

- URL: https://x.com/elonmusk/status/2071836426316984797
- Type: Post
- Published: 2026-06-30T06:01:11+00:00
- Digest summary: The AOC puppet is just flat-out lying

### 47. https://x.com/elonmusk/status/2071813050978480423

- URL: https://x.com/elonmusk/status/2071813050978480423
- Type: Post
- Published: 2026-06-30T04:28:18+00:00
- Digest summary: Cybercab with no steering wheel or pedals driving around Austin https://t.co/Oo7uPoOjhp

### 48. https://x.com/elonmusk/status/2071809876490063928

- URL: https://x.com/elonmusk/status/2071809876490063928
- Type: Post
- Published: 2026-06-30T04:15:41+00:00
- Digest summary: Yup

### 49. https://x.com/elonmusk/status/2071794940930068983

- URL: https://x.com/elonmusk/status/2071794940930068983
- Type: Post
- Published: 2026-06-30T03:16:20+00:00
- Digest summary: https://t.co/DOKd8F3EGI

### 50. https://x.com/elonmusk/status/2071792015205966208

- URL: https://x.com/elonmusk/status/2071792015205966208
- Type: Post
- Published: 2026-06-30T03:04:43+00:00
- Digest summary: Exactly

### 51. https://x.com/elonmusk/status/2071789793902534993

- URL: https://x.com/elonmusk/status/2071789793902534993
- Type: Post
- Published: 2026-06-30T02:55:53+00:00
- Digest summary: They are such liars!

### 52. https://x.com/elonmusk/status/2071786841439642060

- URL: https://x.com/elonmusk/status/2071786841439642060
- Type: Post
- Published: 2026-06-30T02:44:09+00:00
- Digest summary: Bingo

### 53. https://x.com/elonmusk/status/2071785727860342961

- URL: https://x.com/elonmusk/status/2071785727860342961
- Type: Post
- Published: 2026-06-30T02:39:44+00:00
- Digest summary: Exactly

### 54. https://x.com/levie/status/2071775583072375214

- URL: https://x.com/levie/status/2071775583072375214
- Type: Post
- Published: 2026-06-30T01:59:25+00:00
- Digest summary: This gets to the core of one of the central debates in AI. If a closed stack is always perpetually at the frontier by a wide margin, then being vertically integrated, and gate keeping in the US can work. Because you always have control over who gets access to the best technology, and it will be in high enough demand that it always favors you. If, however, open weights AI can remain a close second to frontier intelligence, then the equation reverses. With a highly regulated approach, you’ll own the frontier market still, but the vast majority of tokens used will go to an alternative stack. That stack will include the model and the underlying hardware that runs it, in the limit. And that stack will be controlled and monetized by someone else. Depending on your belief on how close to the fron

### 55. https://x.com/steipete/status/2071770560875671831

- URL: https://x.com/steipete/status/2071770560875671831
- Type: Post
- Published: 2026-06-30T01:39:28+00:00
- Digest summary: was this vibed https://t.co/keLhgWSKH5

### 56. https://x.com/steipete/status/2071769993151398074

- URL: https://x.com/steipete/status/2071769993151398074
- Type: Post
- Published: 2026-06-30T01:37:12+00:00
- Digest summary: This would have been amazing a few years ago, but in the age of AI, what’s the point?

## Firsthand AI Digest Detail Pages

## Original Sources

### 1. What’s new in Claude Sonnet 5

- Type: web
- URL: https://simonwillison.net/2026/Jun/30/claude-sonnet-5/
- Title: What’s new in Claude Sonnet 5
- Description: Claude Sonnet 5 came out this morning. I always head straight for the "what's new" developer docs because they tend to have more actionable information than the official announcement post. …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://10xn.link/simon-depot - Try Depot CI
  - https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5 - What's new in Claude Sonnet 5
  - https://news.ycombinator.com/item?id=48736605 - via
  - https://www.anthropic.com/news/claude-sonnet-5 - this morning
  - https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf - system card
  - https://tools.simonwillison.net/claude-token-counter - Claude Token Counter
  - https://github.com/simonw/udhr-markdown/blob/main/declarations/eng.md - Universal Declaration of Human Rights (English)
  - https://github.com/simonw/udhr-markdown/blob/main/declarations/spa.md - Universal Declaration of Human Rights (Spanish)
  - https://github.com/simonw/udhr-markdown/blob/main/declarations/cmn_hans.md - Universal Declaration of Human Rights (Chinese, Mandarin Simplified)
  - https://github.com/simonw/sqlite-utils/blob/79117b9d110d72f46dab5fe2cda412ff4789ab55/sqlite_utils/db.py - sqlite_utils/db.py
  - https://gist.github.com/simonw/a89e756b621a31e8ffc210e3428efa77 - the pelican
  - https://simonwillison.net/2026/Jun/30/ - 30th June 2026
  - https://simonwillison.net/2026/Jun/30/shot-scraper-video/ - Have your agent record video demos of its work with shot-scraper video
  - https://simonwillison.net/2026/Jun/22/porting-moebius/ - Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
  - https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/ - sqlite-utils 4.0rc1 adds migrations and nested transactions
  - https://simonwillison.net/tags/ai/ - ai 2,094
  - https://simonwillison.net/tags/generative-ai/ - generative-ai 1,851
  - https://simonwillison.net/tags/llms/ - llms 1,819

Excerpt:

What's new in Claude Sonnet 5 Simon Willison’s Weblog Subscribe Sponsored by: Depot — AI agents write code in seconds. CI shouldn't make them wait minutes. Try Depot CI 30th June 2026 - Link Blog What's new in Claude Sonnet 5 ( via ) Claude Sonnet 5 came out this morning . I always head straight for the "what's new" developer docs because they tend to have more actionable information than the official announcement post. Anthropic say of Sonnet 5 that "its performance is close to that of Opus 4.8, but at lower prices". The system card helps explain how they were able to release the model without being blocked by the US government: Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models that are more capable than Sonnet 5 but much less capable than Mythos 5). Of note from the "what's new" API changes: Sampling parameters temperature , top_p , top_k are no longer supported. It has a 1 million token context window and 128,000 maximum output tokens. It features "the same set of tools and platform features as Claude Sonnet 4.6" Adaptive thinking is on by default, unless you specify "thinking": {type: "disabled"} . The pricing is the same as Sonnet 4.6: $3/million input, $15/million input, with an introductory discount to $2/$10 until 31st August. But... The model has a new tokenizer, where "The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6." - effectively a 30% price increase. I used my Claude Token Counter tool to try out the new tokenizer. Here are my results for several larger documents: Document Sonnet 4.6 Opus 4.7 Sonnet 5 Universal Declaration of Human Rights (English) 2,356 3,347 1.42x 3,341 1.42x Universal Declaration of Human Rights (Spanish) 3,572 4,753 1.33x 4,747 1.33x Universal Declaration of Human Rights (Chinese, Mandarin Simplified) 3,334 3,366 1.01x 3,360 1.01x sqlite_utils/db.py (4,279 lines of Python) 44,014 56,118 1.28x 56,113 1.27x So the new token is roughly 1.4x times more expensive for English, 1.33x for Spanish, 1.28x for Python code and effectively the same cost for Simplified Mandarin. Here's the pelican . It's nothing to write home about. Sonnet 5 thinks it looks like a goose. Posted 30th June 2026 at 9:23 pm Recent articles Have your agent record video demos of its work with shot-scraper video - 30th June 2026 Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code - 22nd Ju

### 2. The AI Compass

- Type: web
- URL: https://simonwillison.net/2026/Jun/30/the-ai-compass/
- Title: The AI Compass
- Description: This political compass style quiz by bambamramfan is pretty neat - answer 29 questions about AI and AI ethics to see which of the 30 archetypes you best fit. I'm …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://10xn.link/simon-depot - Try Depot CI
  - https://bambamramfan.github.io/ai-compass/ - The AI Compass
  - https://bsky.app/profile/erisianrite.com/post/3mphwpqgd4c2y - via
  - https://bambamramfan.tumblr.com/post/820505178072580096/the-ai-compass - by bambamramfan
  - https://github.com/bambamramfan/ai-compass/blob/main/index.html - Here's the code
  - https://simonwillison.net/2026/Jun/30/ - 30th June 2026
  - https://simonwillison.net/2026/Jun/30/shot-scraper-video/ - Have your agent record video demos of its work with shot-scraper video
  - https://simonwillison.net/2026/Jun/22/porting-moebius/ - Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
  - https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/ - sqlite-utils 4.0rc1 adds migrations and nested transactions
  - https://simonwillison.net/tags/ai/ - ai 2,094
  - https://simonwillison.net/tags/generative-ai/ - generative-ai 1,851
  - https://simonwillison.net/tags/llms/ - llms 1,819
  - https://simonwillison.net/tags/ai-ethics/ - ai-ethics 320
  - https://github.com/sponsors/simonw/ - Sponsor & subscribe
  - https://simonwillison.net/2002/ - 2002
  - https://simonwillison.net/2003/ - 2003
  - https://simonwillison.net/2004/ - 2004
  - https://simonwillison.net/2005/ - 2005

Excerpt:

The AI Compass Simon Willison’s Weblog Subscribe Sponsored by: Depot — AI agents write code in seconds. CI shouldn't make them wait minutes. Try Depot CI 30th June 2026 - Link Blog The AI Compass ( via ) This political compass style quiz by bambamramfan is pretty neat - answer 29 questions about AI and AI ethics to see which of the 30 archetypes you best fit. I'm impressed that my answers on my first time through the quiz categorized me as "The Garage Tinkerer", patron saint myself! It's implemented as a single page React app using the <script type="text/babel"> trick to avoid the necessary build step. Here's the code . Posted 30th June 2026 at 5:39 pm Recent articles Have your agent record video demos of its work with shot-scraper video - 30th June 2026 Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code - 22nd June 2026 sqlite-utils 4.0rc1 adds migrations and nested transactions - 21st June 2026 This is a link post by Simon Willison, posted on 30th June 2026 . ai 2,094 generative-ai 1,851 llms 1,819 ai-ethics 320 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 3. Have your agent record video demos of its work with shot-scraper video

- Type: web
- URL: https://simonwillison.net/2026/Jun/30/shot-scraper-video/
- Title: Have your agent record video demos of its work with shot-scraper video
- Description: shot-scraper video is a new command introduced in today’s shot-scraper 1.10 release which accepts a storyboard.yml file defining a routine to run against a web application and uses Playwright to …
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://10xn.link/simon-depot - Try Depot CI
  - https://shot-scraper.datasette.io/en/stable/video.html - shot-scraper video
  - https://github.com/simonw/shot-scraper/releases/tag/1.10 - shot-scraper 1.10
  - https://simonwillison.net/2026/Feb/10/showboat-and-rodney/ - having coding agents produce demos
  - https://github.com/simonw/datasette/pull/2813 - still in development
  - https://gist.github.com/simonw/287b26aff53fcb72942b19f5b69d7e5c - contains a cookie
  - https://shot-scraper.datasette.io/en/stable/authentication.html - described here
  - https://github.com/simonw/datasette/commits/b759ea548606bc9bf9a4bf0e33e2d57ead7e0ab8/ - this branch
  - https://playwright.dev/ - Playwright
  - https://github.com/simonw/shot-scraper/pull/194/changes/c2f3b3a52ba84f2adcf3ad6da4d39c2570328584 - a few white frames at the start of the videos
  - https://playwright.dev/python/docs/api/class-screencast - screencast mechanism
  - https://github.com/microsoft/playwright/pull/41183 - landed PR fixing that
  - https://github.com/microsoft/playwright-python/releases/tag/v1.61.0 - playwright-python 1.61.0
  - https://github.com/simonw/shot-scraper/blob/1.10/shot_scraper/video.py - use Pydantic
  - https://github.com/simonw/shot-scraper/issues/142 - original issue
  - https://simonwillison.net/2026/Jun/30/ - 30th June 2026
  - https://fedi.simonwillison.net/@simon - Mastodon
  - https://bsky.app/profile/simonwillison.net - Bluesky

Excerpt:

Have your agent record video demos of its work with shot-scraper video Simon Willison’s Weblog Subscribe Sponsored by: Depot — AI agents write code in seconds. CI shouldn't make them wait minutes. Try Depot CI Have your agent record video demos of its work with shot-scraper video 30th June 2026 shot-scraper video is a new command introduced in today’s shot-scraper 1.10 release which accepts a storyboard.yml file defining a routine to run against a web application and uses Playwright to record a video of that routine. I’ve written before about the importance of having coding agents produce demos of their work; this is my latest attempt at enabling them to do that. Here’s an example video created using shot-scraper video , exercising a still in development feature adding the ability to create new tables in Datasette from pasted CSV, TSV or JSON data: That video was created by running this command : shot-scraper video datasette-bulk-insert-storyboard.yml \ --auth datasette-demo-auth.json --mp4 (That --auth JSON file contains a cookie , as described here in the documentation.) Here’s the datasette-bulk-insert-storyboard.yml file: output : /tmp/datasette-bulk-insert-demo.webm server : - uv - --directory - /Users/simon/Dropbox/dev/datasette - run - datasette - -p - 6419 - --root - --secret - " 1 " - /tmp/demo.db url : http://127.0.0.1:6419/demo/tasks viewport : width : 1280 height : 720 cursor : true wait_for : ' button[data-table-action="insert-row"] ' javascript : | (() => { let clipboardText = ""; Object.defineProperty(navigator, "clipboard", { configurable: true, get: () => ({ writeText: async (text) => { clipboardText = String(text); }, readText: async () => clipboardText, }), }); })(); scenes : - name : Bulk insert existing table rows do : - pause : 0.8 - click : ' button[data-table-action="insert-row"] ' - wait_for : " #row-edit-dialog[open] " - pause : 0.5 - click : " .row-edit-bulk-insert " - wait_for : " .row-edit-bulk-textarea " - pause : 0.5 - click : " .row-edit-copy-template " - wait_for : " text=Copied " - pause : 0.8 - fill : into : " .row-edit-bulk-textarea " text : | title,owner,status,priority,notes Prepare release video,Ana,doing,1,Recorded with shot-scraper Check pasted CSV import,Ben,review,3,Previewed before inserting Share the branch demo,Chen,queued,2,Bulk insert creates three rows - pause : 0.8 - click : " .row-edit-save " - wait_for : " text=Previewing 3 rows. " - pause : 1.2 - click : " .row-edit-save " - wait_for : " text=3 rows inse

### 4. Start building with Nano Banana 2 Lite and Gemini Omni Flash

- Type: official/blog
- URL: https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/
- Title: Start building with Nano Banana 2 Lite and Gemini Omni Flash
- Published: 2026-06-30
- Description: Scale your ideas with Nano Banana 2 Lite, our fastest, most cost-efficient Gemini Image model, and Gemini Omni Flash for high-quality video and conversational editing.
- Links:
  - https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/ - Skip to main content
  - https://deepmind.google/ - The Keyword
  - https://twitter.com/intent/tweet?text=Start%20building%20with%20Nano%20Banana%202%20Lite%20and%20Gemini%20Omni%20Flash%20%40google&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/ - x.com
  - https://www.facebook.com/sharer/sharer.php?caption=Start%20building%20with%20Nano%20Banana%202%20Lite%20and%20Gemini%20Omni%20Flash&u=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/ - Facebook
  - https://www.linkedin.com/shareArticle?mini=true&url=https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/&title=Start%20building%20with%20Nano%20Banana%202%20Lite%20and%20Gemini%20Omni%20Flash - LinkedIn
  - https://deepmind.google/innovation-and-ai/models-and-research/google-deepmind/ - Google DeepMind
  - https://deepmind.google/innovation-and-ai/models-and-research/google-research/ - Google Research
  - https://deepmind.google/innovation-and-ai/models-and-research/google-labs/ - Google Labs
  - https://deepmind.google/innovation-and-ai/models-and-research/gemini-models/ - Gemini models
  - https://deepmind.google/innovation-and-ai/models-and-research/quantum-computing/ - Quantum computing
  - https://deepmind.google/innovation-and-ai/models-and-research/ - See all
  - https://deepmind.google/innovation-and-ai/technology/developers-tools/ - Developer tools
  - https://deepmind.google/innovation-and-ai/products/gemini-app/ - Gemini app
  - https://deepmind.google/innovation-and-ai/products/notebooklm/ - NotebookLM
  - https://deepmind.google/innovation-and-ai/products/ - See all
  - https://deepmind.google/innovation-and-ai/infrastructure-and-cloud/global-network/ - Global network
  - https://deepmind.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ - Google Cloud
  - https://deepmind.google/innovation-and-ai/infrastructure-and-cloud/ - See all
  - https://deepmind.google/innovation-and-ai/technology/safety-security/ - Safety & Security
  - https://deepmind.google/innovation-and-ai/technology/health/ - Health

Excerpt:

Start building with Nano Banana 2 Lite and Gemini Omni Flash Skip to main content The Keyword Start building with Nano Banana 2 Lite and Gemini Omni Flash Share x.com Facebook LinkedIn Mail Copy link Home Innovation & AI Innovation & AI Models & Research Google DeepMind Google Research Google Labs Gemini models Quantum computing See all Products Developer tools Gemini app NotebookLM See all Infrastructure & cloud Global network Google Cloud See all Technology Safety & Security Health See all Learn more: Google DeepMind blog Google Research blog Google Developers blog Google Cloud blog See all AI updates Models & Research Google DeepMind Google Research Google Labs Gemini models Quantum computing See all Products Developer tools Gemini app NotebookLM See all Infrastructure & cloud Global network Google Cloud See all Technology Safety & Security Health See all Learn more: Google DeepMind blog Google Research blog Google Developers blog Google Cloud blog See all AI updates Products & platforms Products & platforms Products Search Maps Chrome Google Health Google Workspace Learning & Education Shopping See all Platforms Android Google Play Wear OS See all Devices Pixel Google Nest Fitbit Chromebooks See all Learn more: Google Ads & Commerce blog Waze blog See all product updates Products Search Maps Chrome Google Health Google Workspace Learning & Education Shopping See all Platforms Android Google Play Wear OS See all Devices Pixel Google Nest Fitbit Chromebooks See all Learn more: Google Ads & Commerce blog Waze blog See all product updates Company news Company news Outreach & initiatives Creating opportunity Safety & security Google.org Public policy Sustainability Health See all Leadership Sundar Pichai, CEO More authors See all Inside Google Around the globe Life at Google See all Learn more: Google Security blog Outreach & initiatives Creating opportunity Safety & security Google.org Public policy Sustainability Health See all Leadership Sundar Pichai, CEO More authors See all Inside Google Around the globe Life at Google See all Learn more: Google Security blog Feed Subscribe Global (English) Africa (English) Australia (English) Brasil (Português) Canada (English) Canada (Français) Česko (Čeština) Deutschland (Deutsch) España (Español) France (Français) Greece (Ελληνικά) India (English) Indonesia (Bahasa Indonesia) Ireland (English) Italia (Italiano) 日本 (日本語) 대한민국 (한국어) Latinoamérica (Español) الشرق الأوسط وشمال أفريقيا (اللغة العربية) MENA (English) Ne

### 5. Release: shot-scraper 1.10

- Type: web
- URL: https://simonwillison.net/2026/Jun/30/shot-scraper/
- Title: Release: shot-scraper 1.10
- Description: A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript
- Links:
  - https://simonwillison.net/ - Simon Willison’s Weblog
  - https://simonwillison.net/about/ - Subscribe
  - https://10xn.link/simon-depot - Try Depot CI
  - https://simonwillison.net/elsewhere/release/ - Release
  - https://github.com/simonw/shot-scraper/releases/tag/1.10 - shot-scraper 1.10
  - https://simonwillison.net/2026/Jun/30/shot-scraper-video/ - Have your agent record video demos of its work with shot-scraper video
  - https://simonwillison.net/2026/Jun/30/ - 30th June 2026
  - https://simonwillison.net/2026/Jun/22/porting-moebius/ - Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
  - https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/ - sqlite-utils 4.0rc1 adds migrations and nested transactions
  - https://simonwillison.net/tags/shot-scraper/ - shot-scraper 69
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

Release: shot-scraper 1.10 Simon Willison’s Weblog Subscribe Sponsored by: Depot — AI agents write code in seconds. CI shouldn't make them wait minutes. Try Depot CI 30th June 2026 Release shot-scraper 1.10 — A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript The big new feature is shot-scraper video storyboard.yml , described in detail in Have your agent record video demos of its work with shot-scraper video . Posted 30th June 2026 at 3:10 pm Recent articles Have your agent record video demos of its work with shot-scraper video - 30th June 2026 Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code - 22nd June 2026 sqlite-utils 4.0rc1 adds migrations and nested transactions - 21st June 2026 This is a beat by Simon Willison, posted on 30th June 2026 . shot-scraper 69 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026

### 6. Anthony Kaldellis: Roman Empire, Byzantine Empire, Rise & Fall of Empires | Lex Fridman Podcast #498

- Type: video
- URL: https://www.youtube.com/watch?v=pv1TUJSEM2k
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 7. Machiavelli was NOT Machiavellian – Ada Palmer

- Type: video
- URL: https://www.youtube.com/watch?v=88IxTQT8PBM
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 8. How LLMs Actually Generate Text

- Type: video
- URL: https://www.youtube.com/shorts/HfjF__xhSdk
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 9. https://x.com/steipete/status/2072061089177539003

- Type: x-post
- URL: https://x.com/steipete/status/2072061089177539003
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 10. https://x.com/petergyang/status/2072051258882666620

- Type: x-post
- URL: https://x.com/petergyang/status/2072051258882666620
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 11. https://x.com/miramurati/status/2072050039317578236

- Type: x-post
- URL: https://x.com/miramurati/status/2072050039317578236
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 12. https://x.com/swyx/status/2072048730581405800

- Type: x-post
- URL: https://x.com/swyx/status/2072048730581405800
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 13. https://x.com/levie/status/2072046374045249671

- Type: x-post
- URL: https://x.com/levie/status/2072046374045249671
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 14. https://x.com/rauchg/status/2072044844965400589

- Type: x-post
- URL: https://x.com/rauchg/status/2072044844965400589
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 15. https://x.com/steipete/status/2072037247122284825

- Type: x-post
- URL: https://x.com/steipete/status/2072037247122284825
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 16. https://x.com/elonmusk/status/2072034905299563005

- Type: x-post
- URL: https://x.com/elonmusk/status/2072034905299563005
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 17. https://x.com/AravSrinivas/status/2072031649693675810

- Type: x-post
- URL: https://x.com/AravSrinivas/status/2072031649693675810
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 18. https://x.com/danshipper/status/2072025187751731334

- Type: x-post
- URL: https://x.com/danshipper/status/2072025187751731334
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 19. https://x.com/claudeai/status/2072017450611142835

- Type: x-post
- URL: https://x.com/claudeai/status/2072017450611142835
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 20. https://x.com/elonmusk/status/2072015711635914948

- Type: x-post
- URL: https://x.com/elonmusk/status/2072015711635914948
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 21. https://x.com/OpenAI/status/2072004836674167294

- Type: x-post
- URL: https://x.com/OpenAI/status/2072004836674167294
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 22. https://x.com/petergyang/status/2072004576442802487

- Type: x-post
- URL: https://x.com/petergyang/status/2072004576442802487
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 23. https://x.com/DrJimFan/status/2072004190856212902

- Type: x-post
- URL: https://x.com/DrJimFan/status/2072004190856212902
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 24. https://x.com/claudeai/status/2072002740830842899

- Type: x-post
- URL: https://x.com/claudeai/status/2072002740830842899
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 25. https://x.com/elonmusk/status/2072000588112343388

- Type: x-post
- URL: https://x.com/elonmusk/status/2072000588112343388
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 26. https://x.com/elonmusk/status/2072000185769586922

- Type: x-post
- URL: https://x.com/elonmusk/status/2072000185769586922
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 27. https://x.com/elonmusk/status/2071994061624426582

- Type: x-post
- URL: https://x.com/elonmusk/status/2071994061624426582
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 28. https://x.com/levie/status/2071992799109824562

- Type: x-post
- URL: https://x.com/levie/status/2071992799109824562
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 29. https://x.com/amasad/status/2071992670394765407

- Type: x-post
- URL: https://x.com/amasad/status/2071992670394765407
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 30. https://x.com/amasad/status/2071992110132117740

- Type: x-post
- URL: https://x.com/amasad/status/2071992110132117740
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 31. https://x.com/AndrewYNg/status/2071988145667928442

- Type: x-post
- URL: https://x.com/AndrewYNg/status/2071988145667928442
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 32. https://x.com/GoogleDeepMind/status/2071988044878516466

- Type: x-post
- URL: https://x.com/GoogleDeepMind/status/2071988044878516466
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 33. https://x.com/petergyang/status/2071985410809700863

- Type: x-post
- URL: https://x.com/petergyang/status/2071985410809700863
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 34. https://x.com/elonmusk/status/2071984597311557807

- Type: x-post
- URL: https://x.com/elonmusk/status/2071984597311557807
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 35. https://x.com/adityaag/status/2071983952894837062

- Type: x-post
- URL: https://x.com/adityaag/status/2071983952894837062
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 36. https://x.com/AravSrinivas/status/2071982392554983440

- Type: x-post
- URL: https://x.com/AravSrinivas/status/2071982392554983440
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 37. https://x.com/elonmusk/status/2071978911919923676

- Type: x-post
- URL: https://x.com/elonmusk/status/2071978911919923676
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 38. https://x.com/swyx/status/2071977886991679715

- Type: x-post
- URL: https://x.com/swyx/status/2071977886991679715
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 39. https://x.com/steipete/status/2071972449277898924

- Type: x-post
- URL: https://x.com/steipete/status/2071972449277898924
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 40. https://x.com/steipete/status/2071972239734616146

- Type: x-post
- URL: https://x.com/steipete/status/2071972239734616146
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 41. https://x.com/elonmusk/status/2071968172647858409

- Type: x-post
- URL: https://x.com/elonmusk/status/2071968172647858409
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 42. https://x.com/rauchg/status/2071966055308607765

- Type: x-post
- URL: https://x.com/rauchg/status/2071966055308607765
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 43. https://x.com/elonmusk/status/2071965448120180964

- Type: x-post
- URL: https://x.com/elonmusk/status/2071965448120180964
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 44. https://x.com/petergyang/status/2071960766434140644

- Type: x-post
- URL: https://x.com/petergyang/status/2071960766434140644
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 45. https://x.com/rauchg/status/2071951861112840501

- Type: x-post
- URL: https://x.com/rauchg/status/2071951861112840501
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 46. https://x.com/elonmusk/status/2071836426316984797

- Type: x-post
- URL: https://x.com/elonmusk/status/2071836426316984797
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 47. https://x.com/elonmusk/status/2071813050978480423

- Type: x-post
- URL: https://x.com/elonmusk/status/2071813050978480423
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 48. https://x.com/elonmusk/status/2071809876490063928

- Type: x-post
- URL: https://x.com/elonmusk/status/2071809876490063928
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 49. https://x.com/elonmusk/status/2071794940930068983

- Type: x-post
- URL: https://x.com/elonmusk/status/2071794940930068983
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 50. https://x.com/elonmusk/status/2071792015205966208

- Type: x-post
- URL: https://x.com/elonmusk/status/2071792015205966208
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 51. https://x.com/elonmusk/status/2071789793902534993

- Type: x-post
- URL: https://x.com/elonmusk/status/2071789793902534993
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 52. https://x.com/elonmusk/status/2071786841439642060

- Type: x-post
- URL: https://x.com/elonmusk/status/2071786841439642060
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 53. https://x.com/elonmusk/status/2071785727860342961

- Type: x-post
- URL: https://x.com/elonmusk/status/2071785727860342961
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 54. https://x.com/levie/status/2071775583072375214

- Type: x-post
- URL: https://x.com/levie/status/2071775583072375214
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 55. https://x.com/steipete/status/2071770560875671831

- Type: x-post
- URL: https://x.com/steipete/status/2071770560875671831
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

### 56. https://x.com/steipete/status/2071769993151398074

- Type: x-post
- URL: https://x.com/steipete/status/2071769993151398074
- Fetch status: limited (metadata-only host; use browser/platform-specific access for full content)

## Secondary Source Candidates

These links were discovered from first-layer sources. Use them to reach primary material when the first-layer source is commentary or a link blog.

### 1. Sign up

- Type: web
- URL: https://10xn.link/simon-depot
- Title: Sign up
- Links:
  - https://10xn.link/api/login?provider=GoogleOAuth&state=eyJyZXR1cm5QYXRobmFtZSI6Ii9vcmdzIn0%3D&redirect_uri=https%3A%2F%2Fdepot.dev%2Fsign-in%2Fsso&client_id=client_01FKVF2C49KQ0BY8XR0K98JVVE&source=signup&authorization_session_id=01KWDGB2K4S4C6VDT3CQQPRXN5 - Continue with Google
  - https://10xn.link/api/login?provider=MicrosoftOAuth&state=eyJyZXR1cm5QYXRobmFtZSI6Ii9vcmdzIn0%3D&redirect_uri=https%3A%2F%2Fdepot.dev%2Fsign-in%2Fsso&client_id=client_01FKVF2C49KQ0BY8XR0K98JVVE&source=signup&authorization_session_id=01KWDGB2K4S4C6VDT3CQQPRXN5 - Continue with Microsoft
  - https://10xn.link/?state=eyJyZXR1cm5QYXRobmFtZSI6Ii9vcmdzIn0%3D&redirect_uri=https%3A%2F%2Fdepot.dev%2Fsign-in%2Fsso&authorization_session_id=01KWDGB2K4S4C6VDT3CQQPRXN5 - Sign in
  - https://depot.dev/terms-of-service - Terms of Service
  - https://depot.dev/privacy-policy - Privacy Policy

Excerpt:

Sign up Sign up First name Last name Email Continue OR Continue with Google Continue with Microsoft Already have an account? Sign in By creating an account, you agree to the Terms of Service and Privacy Policy Live Benchmarks Unrivaled Performance PostHog/posthog 16x faster With Depot 5m 11s Without Depot 84m 42s mastodon/mastodon 8.7x faster With Depot 2m 46s Without Depot 24m 7s grpc/grpc 6.1x faster With Depot 4m 7s Without Depot 25m 5s apache/kafka 2.2x faster With Depot 5m 48s Without Depot 12m 32s

### 2. What's new in Claude Sonnet 5

- Type: web
- URL: https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5
- Title: What's new in Claude Sonnet 5
- Description: Overview of new features and behavior changes in Claude Sonnet 5.
- Links:
  - https://platform.claude.com/docs/en/home - Claude Platform Docs
  - https://platform.claude.com/docs/en/intro - Messages
  - https://platform.claude.com/docs/en/managed-agents/overview - Managed Agents
  - https://platform.claude.com/docs/en/manage-claude/admin-api - Admin
  - https://platform.claude.com/docs/en/api/overview -  API reference
  - https://platform.claude.com/ -  Console
  - https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fabout-claude%2Fmodels%2Fwhats-new-sonnet-5 - Log in
  - https://platform.claude.com/docs/en/about-claude/models/overview - Models overview
  - https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions - Model IDs and versioning
  - https://platform.claude.com/docs/en/about-claude/models/choosing-a-model - Choosing a model
  - https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 - Introducing Claude Fable 5 and Claude Mythos 5
  - https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8 - What's new in Claude Opus 4.8
  - https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5 - What's new in Claude Sonnet 5
  - https://platform.claude.com/docs/en/about-claude/models/migration-guide - Upgrade between model versions
  - https://platform.claude.com/docs/en/about-claude/model-deprecations - Model deprecations
  - https://platform.claude.com/docs/en/resources/overview - Model cards
  - https://platform.claude.com/docs/en/release-notes/system-prompts - System prompts
  - https://platform.claude.com/docs/en/about-claude/pricing - Pricing
  - https://platform.claude.com/login -  Log in
  - https://platform.claude.com/docs - Claude Platform Docs

Excerpt:

What's new in Claude Sonnet 5 - Claude Platform Docs Claude Platform Docs Messages Managed Agents Admin Resources   API reference English   Console Log in    Search... ⌘K Models Models overview Model IDs and versioning Choosing a model Introducing Claude Fable 5 and Claude Mythos 5 What's new in Claude Opus 4.8 What's new in Claude Sonnet 5 Upgrade between model versions Model deprecations Model cards System prompts Pricing  Log in  Models & pricing  What's new in Claude Sonnet 5 Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Loading... Claude Platform Docs Solutions AI agents Code modernization Coding Customer support Education Financial services Government Life sciences Partners Claude on AWS Claude on Google Cloud Learn Blog Courses Use cases Connectors Customer stories Engineering at Anthropic Events Powered by Claude Service partners Startups program Company Anthropic Careers Economic Futures Research News Responsible Scaling Policy Security and compliance Transparency Learn Blog Courses Use cases Connectors Customer stories Engineering at Anthropic Events Powered by Claude Service partners Startups program Help and security Availability Status Support Discord Terms and policies Privacy policy Responsible disclosure policy Terms of service: Commercial Terms of service: Consumer Usage policy Models & pricing / Models What's new in Claude Sonnet 5 Copy page  Overview of new features and behavior changes in Claude Sonnet 5. Copy page  Claude Sonnet 5 is the next generation of Anthropic's Sonnet model family. It is a drop-in upgrade for Claude Sonnet 4.6 with three behavior changes: adaptive thinking is on by default, manual extended thinking now returns a 400 error (it was deprecated on Claude Sonnet 4.6), and setting sampling parameters ( temperature , top_p , top_k ) to non-default values returns a 400 error. This page summarizes everything new at launch, including a new tokenizer.  New model Model API model ID Description Claude Sonnet 5 claude-sonnet-5 The best combination of speed and intelligence Claude Sonnet 5 supports the 1M token context window by default (1M tokens is both the default and the maximum; there is no smaller context variant), 128k max output tokens, adaptive thinking , and the same set of tools and platform features as Claude Sonnet 4.6, except Priority Tier , which is not available on Claude Sonnet 5.

### 3. Introducing Claude Sonnet 5

- Type: official/blog
- URL: https://www.anthropic.com/news/claude-sonnet-5
- Title: Introducing Claude Sonnet 5
- Description: Our most agentic Sonnet yet, with top-tier intelligence for coding and everyday professional work.
- Links:
  - https://www.anthropic.com/news/claude-sonnet-5 - Skip to main content
  - https://www.anthropic.com/
  - https://www.anthropic.com/research - Research
  - https://www.anthropic.com/policy - Policy
  - https://www.anthropic.com/news - News
  - https://claude.ai/ - Try Claude
  - https://www.anthropic.com/claude-sonnet-5-system-card - Claude Sonnet 5 System Card
  - https://platform.claude.com/docs/en/about-claude/models/overview - Claude API
  - https://platform.claude.com/docs/en/build-with-claude/effort - effort
  - https://arxiv.org/abs/2504.12516 - BrowseComp
  - https://xlang.ai/blog/osworld-verified - OSWorld-Verified
  - https://www.anthropic.com/news/mozilla-firefox-security - in collaboration with Mozilla
  - https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude - safeguards
  - https://platform.claude.com/cookbook/evals-agentic-search-reproduce-agentic-search-benchmarks - standard methodology
  - https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf - Sonnet 5 system card
  - https://platform.claude.com/settings/limits - Claude Console
  - https://platform.claude.com/docs/en/api/rate-limits - documentation
  - https://www.anthropic.com/news/claude-sonnet-4-6 - Sonnet 4.6 launch blog
  - https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/claude-sonnet-5
  - https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/claude-sonnet-5

Excerpt:

Introducing Claude Sonnet 5 \ Anthropic Skip to main content Skip to footer Research Policy Commitments Learn News Try Claude Product Introducing Claude Sonnet 5 Jun 30, 2026 Claude Sonnet 5 is built to be the most agentic Sonnet model yet. It can make plans, use tools like browsers and terminals, and run autonomously at a level that, just a few months ago, required larger and more expensive models. For many developers, the agentic AI era began with Sonnet-class models: Claude Sonnet 3.5, 3.6, and 3.7 were the first models that showed impressive skills in coding and tool use. More recently, though, the clearest gains in agentic capabilities have been in our Opus-class models. Sonnet 5 narrows the gap: its performance is close to that of Opus 4.8, but at lower prices. It’s a substantial improvement over its predecessor, Sonnet 4.6, on important aspects of agentic performance like reasoning, tool use, coding, and knowledge work: Scores for Sonnet 5 on a variety of evaluations compared to those of Sonnet 4.6 and Opus 4.8 (a more generally capable model, for reference). The Claude Sonnet 5 System Card reports a broader set of evaluations in detail. Our safety assessments found that Sonnet 5 shows an overall lower rate of undesirable behaviors than Sonnet 4.6, and is generally safer to use in agentic contexts. Evaluations also show that it has a much lower ability to perform cybersecurity tasks than our current Opus models. From today, Claude Sonnet 5 is available across all plans: it is the default model for Free and Pro plans, and is available to Max, Team, and Enterprise users. It’s also available in Claude Code and on the Claude Platform, where it launches with introductory pricing of $2 per million input tokens and $10 per million output tokens through August 31, 2026, after which it will be priced at $3 per million input tokens and $15 per million output tokens. Developers can use claude-sonnet-5 via the Claude API . Working with Claude Sonnet 5 The charts below compare the performance of Sonnet 5 with Sonnet 4.6 and Opus 4.8 at different effort levels on the agentic search evaluation BrowseComp and the computer use evaluation OSWorld-Verified . Sonnet 5 (orange line) is a strict improvement over Sonnet 4.6 (gray line) and covers a much wider range of cost-performance options than Opus 4.8 (yellow line). It provides substantially improved cost efficiency at medium effort; its higher-effort performance can match Opus 4.8 on some tasks. Between Sonnet 5 and

### 4. https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf

- Type: paper
- URL: https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf

Excerpt:

%PDF-1.4 %���� 1 0 obj < > endobj 3 0 obj < > endobj 8 0 obj < > endobj 10 0 obj < > stream x����J�`��Ԃ(�� 28�h��mRpi#�V!�S�� �IHS�tspu+.ހ�e(��%���| �:t����� �� � @V�� G�zM�� < ���$*�xÐ�!��K�����c��z�G��� ��>�&|)�4c�Ƃ��� � �ٛbw��0�o�Π?�һY���M�֩УO� > stream x���r�8���'��1eWYU$ %�9go�>���U�A�Ҹ菲)��H�'Vt���� .  �         0cL]���gk�mß��L����?�P�����m�6�dYVU��ߪ����ʲ���   2��� ^p/�zu�4�=������� t���_��_�����$          #��(˲�����l#8���_BqM�,Kc�pN�,���G�   ��_����������h�}��e�ߞ�˟� �es < ���Z͌*��$�=߾}[4(ɢ���7Mc������� v43➓%# ��mY Dι�i��S�@ 0��u�kۖ:� I����*�������jI��3��Xk�sJ� < �����q���1/X*��]�8:1�Gź��|��*��,�b��΋�i�~��W�$M�ǣfIY�ZWH�b��A�QJ��ݡU|L���}��`̢���� �a�a��P '��=��ƶ-�qXk�u�ᐌ�˭#����a��x�����h��9��Eq.,�ǲ��.�� � ����{��ݗ4��z׸��z��*�k^�D)�#H ~C�צ�@�Mk���s6:�Ȧ �� u� [5����:Nk���Y�8�N��bM ������ _��Ɉ�1f�٬v(���� _ ����J���m���u������;��e ��'�( �F�������~�g��  ��su\�E����ZD�kѪ/�9�1�����X{_�m�u��v^�U�T�I�Z�e�}; >�y ��]zb:�������r~!����߷]�Q���柿�����I�N���'�h����_׋n&��?c��n �斲ء{|1x����'��� < \�e[i�� v�>�Zk�� �}�4M�F��Jy_ų0(�2;����F�L�eΕa7�0���5�pw*u�ߐ1(��"��|��xy��{��� �J 8�"M�/�}�J��؛�Թ��� �T`��?��N*J����O ����w|� ��{熊�D-�����fs> R������3�������9�қ͆ᨅZ�+!ަ�ϥ�ye�= �� �-% #�E����焝�K�ְ� ��� ���䝴$����' ��J�;>��'cq��v������ڬ�Ź��ϲM��ӱ3�n�Y��d�����xGv��ZF���t����[�ŗVN\7[�=yc[^6 #���s&A�����|BÜ�:Z��:�_S���:fL������J�����%� �J����6��%�L��,�)Tk����eK7`[�4��'��xn�]�zu��v������� �汑G�6��8�S'��1�� �Z�{ǐ�[C��I'�q6� ������F������ ����I��\Fܤ �i���� ��� �������:��ՁbI���Tjh�_ܸ�G�f�[��7���IX���>��2@�%�qS=y;�J�4�D��D]CCF�x ����}S������ ����I�K�֡4�M}O�0^�������uc?�}�K��OZƘ��B1��L���Bikv#�1��ux�\οkۖa3c��\��6Ǌ� ���Y wi��˴�Ą��M����' ����?��WB��Y"0쓳�ph��W���6 0��(���f�9������fUUE��W���гM�Veo�\���F֤��8��� C��f�򙐐���u�4ԑN�� Ɩ������MI��v(�{&� �������C3F�9���~�ǖ�幻�˲�(�P� � �P�Şƿ �_V/��SŞsq`v1�n�ԱS�m�J���Ֆ�����/ ��H�55M� ��X�a�'��f�p��$���� �$����' ��J�;>t��4� nV]k�,f�ز8K����S���/��1�c��ޭe��*���N �5b){�+J�����/(�M��x N����_���Ӊ2v�!O�d��M��c����R������ ��+!��Ѝ"��k:� ��r��O[[&��N�v`���x��3G��KU,~R�e��+��*;��{�eul�gy������� n�@9 J�f����t:����H�'�����u�?��^Y �������9 ��ĝu���ڶ����s�� &FƘp5�O�>z �Ѫ� < ������y��0n���p��snE�Jk�4��#��Z�{���$�]��x�Vu~�*D��?��.)I����O ����$��"�Ç��}ms��� ���% ��m�v����{�_����\ɍg��� c�s�p8���Q/���}߶-�$��G>^!|#ܰm$-|B^����(VA�����W>'�> ��x < < ==����]��u���`�p/������+��=�

### 5. Token Counter

- Type: web
- URL: https://tools.simonwillison.net/claude-token-counter
- Title: Token Counter
- Links:
  - https://platform.claude.com/docs/en/build-with-claude/token-counting - Anthropic's token counting API

Excerpt:

Token Counter Claude Token Counter This tool uses your Anthropic API key to count tokens in text and images using Anthropic's token counting API . System prompt: User message: Drag and drop files here or click to select Models to compare: Count Tokens

### 6. The AI Compass

- Type: web
- URL: https://bambamramfan.github.io/ai-compass/
- Title: The AI Compass
- Description: 29 questions. Two axes. Which of 30 AI archetypes are you?

Excerpt:

The AI Compass Loading the compass...

### 7. The AI Compass

- Type: web
- URL: https://bambamramfan.tumblr.com/post/820505178072580096/the-ai-compass
- Title: The AI Compass
- Published: 2026-06-26T17:25:14+00:00
- Description: The AI Compass I made an AI Political compass. It doesn’t store any info, so tell me what you get in replies or tags.
- Links:
  - https://bambamramfan.tumblr.com/
  - https://bambamramfan.tumblr.com/following - Following
  - https://bambamramfan.tumblr.com/ask - Ask me anything
  - https://bambamramfan.tumblr.com/about - Effortposts and Masks
  - https://bambamramfan.tumblr.com/archive - Archive
  - https://bambamramfan.github.io/ai-compass/ - The AI Compass 14 questions. Two axes. Where do you actually land on AI? bambamramfan.github.io
  - https://bambamramfan.tumblr.com/post/820505178072580096/the-ai-compass - 728 notes
  - https://facebook.com/sharer.php?u=https%3A%2F%2Fbambamramfan.tumblr.com%2Fpost%2F820505178072580096%2Fthe-ai-compass&t= - Facebook
  - https://twitter.com/intent/tweet?text=The%20AI%20Compass%20I%20made%20an%20AI%20Political%20compass.%20It%20doesn%E2%80%99t%20store%20any%20info%2C%20so%20tell%20me%20what%20you%20get%20in%20replies%20or%20tags.%20https%3A%2F%2Ftmblr.co%2FZn5WpfjZ1HoxOe00 - Tweet
  - https://reddit.com/submit?url=https%3A%2F%2Fbambamramfan.tumblr.com%2Fpost%2F820505178072580096%2Fthe-ai-compass - Reddit
  - https://bambamramfan.tumblr.com/post/820505178072580096/embed - Embed
  - https://www.tumblr.com/reblog/bambamramfan/820505178072580096/1o3Dr5LO
  - https://chooseyourgods.tumblr.com/
  - https://cenylie.tumblr.com/
  - https://cenylie.tumblr.com/post/820871490448801792 - cenylie
  - https://rhapsodyxvi.tumblr.com/ - rhapsodyxvi
  - https://zenvangogh.tumblr.com/
  - https://zenvangogh.tumblr.com/post/820866589213835264 - zenvangogh
  - https://grkuvus.tumblr.com/ - grkuvus
  - https://ips-n-caliban.tumblr.com/

Excerpt:

three masks — The AI Compass three masks — The AI Compass 1.5M ratings 277k ratings See, that’s what the app is perfect for. Sounds perfect Wahhhh, I don’t wanna three masks Posts Following Ask me anything Effortposts and Masks Archive The AI Compass 14 questions. Two axes. Where do you actually land on AI? bambamramfan.github.io I made an AI Political compass. It doesn’t store any info, so tell me what you get in replies or tags. 728 notes 728 notes Jun 26th, 2026 Open in app Facebook Tweet Reddit Mail Embed Permalink chooseyourgods liked this cenylie reblogged this from rhapsodyxvi zenvangogh reblogged this from grkuvus ips-n-caliban liked this nycroshears liked this zenvangogh liked this caelanthe liked this yoikami reblogged this from genderascendant yoikami liked this genderascendant reblogged this from watcherscrown leatherbookmark reblogged this from nototherwisespecified homochondriac reblogged this from watcherscrown mla-citation reblogged this from bambamramfan mla-citation liked this daro-shivani liked this vworpreally reblogged this from watcherscrown watcherscrown reblogged this from fluorescentnova grkuvus reblogged this from fluorescentnova fluorescentnova reblogged this from deep-space-netwerk fluorescentnova liked this sereminar reblogged this from filenesdebasement kc-corduroy liked this hilltop-dolmen reblogged this from drumlincountry sundring liked this v0idspeak liked this bambamramfan said: @native-to-entropy There are at least 2 questions with surveillance and governance directly addressed, and several others that are indicatory in that direction. bluesuedeclogs liked this scottmcstark liked this jealousofthetea liked this tijuanabiblestudies reblogged this from filenesdebasement tijuanabiblestudies liked this tomato-greens liked this deermouth liked this filenesdebasement reblogged this from tomato-greens behappybeusefulbekind reblogged this from ferrousferrule behappybeusefulbekind liked this warthymesinger liked this superduperdokapokapoligysmo reblogged this from matricejacobine intearsaboutrobots liked this matricejacobine reblogged this from aksemmi and added: well, fuck you too! foyet-of-hyrule reblogged this from liesmyth foyet-of-hyrule liked this steadyangelrunaway reblogged this from thisrobothasnosoul and added: Can we ensure AI systems do what we actually want them to do?...is it not fine if we... steadyangelrunaway liked this thelilbittt liked this boogiepoeta liked this ohhgingersnaps liked this thebrightness reblogge

### 8. Recording videos - shot-scraper

- Type: web
- URL: https://shot-scraper.datasette.io/en/stable/video.html
- Title: Recording videos - shot-scraper
- Links:
  - https://shot-scraper.datasette.io/en/stable/index.html - shot-scraper
  - https://shot-scraper.datasette.io/en/stable/installation.html - Installation
  - https://shot-scraper.datasette.io/en/stable/screenshots.html - Taking a screenshot
  - https://shot-scraper.datasette.io/en/stable/authentication.html - Websites that need authentication
  - https://shot-scraper.datasette.io/en/stable/multi.html - Taking multiple screenshots
  - https://shot-scraper.datasette.io/en/stable/javascript.html - Scraping pages using JavaScript
  - https://shot-scraper.datasette.io/en/stable/video.html - Recording videos
  - https://shot-scraper.datasette.io/en/stable/pdf.html - Saving a web page to PDF
  - https://shot-scraper.datasette.io/en/stable/html.html - Dumping the HTML of a page
  - https://shot-scraper.datasette.io/en/stable/har.html - Saving a web page to an HTTP Archive
  - https://shot-scraper.datasette.io/en/stable/accessibility.html - Dumping out an accessibility tree
  - https://shot-scraper.datasette.io/en/stable/github-actions.html - Using shot-scraper with GitHub Actions
  - https://shot-scraper.datasette.io/en/stable/contributing.html - Contributing
  - https://playwright.dev/docs/locators - Playwright locator syntax
  - https://www.sphinx-doc.org/ - Sphinx
  - https://pradyunsg.me - @pradyunsg
  - https://github.com/pradyunsg/furo - Furo

Excerpt:

Recording videos - shot-scraper Hide navigation sidebar Hide table of contents sidebar Toggle site navigation sidebar shot-scraper Toggle Light / Dark / Auto color theme Toggle table of contents sidebar shot-scraper Installation Taking a screenshot Websites that need authentication Taking multiple screenshots Scraping pages using JavaScript Recording videos Saving a web page to PDF Dumping the HTML of a page Saving a web page to an HTTP Archive Dumping out an accessibility tree Using shot-scraper with GitHub Actions Contributing Back to top Toggle Light / Dark / Auto color theme Toggle table of contents sidebar Recording videos ¶ The shot-scraper video command records a WebM video from a YAML storyboard. Storyboards describe the video as a sequence of scenes. Each scene can open a page, wait for content, perform actions and pause between steps. Create a file called storyboard.yml like this: output : demo.webm url : https://shot-scraper.datasette.io/en/stable/ viewport : width : 1280 height : 720 cursor : true wait_for : "text=Quick start" scenes : - name : Documentation home do : - pause : 1 - name : Open installation docs do : - click : ".sidebar-tree a[href='installation.html']" - wait_for : 'h1:has-text("Installation")' - screenshot : installation.png - pause : 1 - name : Search the docs do : - click : "input.sidebar-search" - type : into : "input.sidebar-search" text : "authentication" delay_ms : 25 - press : selector : "input.sidebar-search" key : Enter - wait_for : "text=Search Results" - pause : 2 Then run: shot-scraper video storyboard.yml This opens the starting URL, records the scenes and writes the video to demo.webm . Use -o or --output to override the output filename: shot-scraper video storyboard.yml -o alternate.webm Use --mp4 to also convert the recorded WebM video to MP4 using ffmpeg . The WebM is still written first, then the MP4 is written using the same filename with the extension replaced by .mp4 : shot-scraper video storyboard.yml --mp4 If ffmpeg is not installed, the WebM file is still created but the command exits with a non-zero status and an error explaining that the MP4 was not created. Storyboard structure ¶ A storyboard file is a YAML mapping with these keys: output Filename for the recorded WebM video. This can be omitted if -o is used. output : demo.webm url Starting URL for the video. This can be an http:// or https:// URL, a bare domain or a path to a local HTML file. url : https://shot-scraper.datasette.io/en/stable/ sh Op

### 9. Websites that need authentication - shot-scraper

- Type: web
- URL: https://shot-scraper.datasette.io/en/stable/authentication.html
- Title: Websites that need authentication - shot-scraper
- Links:
  - https://shot-scraper.datasette.io/en/stable/index.html - shot-scraper
  - https://shot-scraper.datasette.io/en/stable/installation.html - Installation
  - https://shot-scraper.datasette.io/en/stable/screenshots.html - Taking a screenshot
  - https://shot-scraper.datasette.io/en/stable/authentication.html - Websites that need authentication
  - https://shot-scraper.datasette.io/en/stable/multi.html - Taking multiple screenshots
  - https://shot-scraper.datasette.io/en/stable/javascript.html - Scraping pages using JavaScript
  - https://shot-scraper.datasette.io/en/stable/video.html - Recording videos
  - https://shot-scraper.datasette.io/en/stable/pdf.html - Saving a web page to PDF
  - https://shot-scraper.datasette.io/en/stable/html.html - Dumping the HTML of a page
  - https://shot-scraper.datasette.io/en/stable/har.html - Saving a web page to an HTTP Archive
  - https://shot-scraper.datasette.io/en/stable/accessibility.html - Dumping out an accessibility tree
  - https://shot-scraper.datasette.io/en/stable/github-actions.html - Using shot-scraper with GitHub Actions
  - https://shot-scraper.datasette.io/en/stable/contributing.html - Contributing
  - https://www.sphinx-doc.org/ - Sphinx
  - https://pradyunsg.me - @pradyunsg
  - https://github.com/pradyunsg/furo - Furo

Excerpt:

Websites that need authentication - shot-scraper Hide navigation sidebar Hide table of contents sidebar Toggle site navigation sidebar shot-scraper Toggle Light / Dark / Auto color theme Toggle table of contents sidebar shot-scraper Installation Taking a screenshot Websites that need authentication Taking multiple screenshots Scraping pages using JavaScript Recording videos Saving a web page to PDF Dumping the HTML of a page Saving a web page to an HTTP Archive Dumping out an accessibility tree Using shot-scraper with GitHub Actions Contributing Back to top Toggle Light / Dark / Auto color theme Toggle table of contents sidebar Websites that need authentication ¶ If you want to take screenshots of a site that has some form of authentication, you will first need to authenticate with that website manually. You can do that using the shot-scraper auth command: shot-scraper auth \ https://datasette-auth-passwords-demo.datasette.io/-/login \ auth.json (For this demo, use username = root and password = password! ) This will open a browser window on your computer showing the page you specified. You can then sign in using that browser window - including 2FA or CAPTCHAs or other more complex form of authentication. When you are finished, hit <enter> at the shot-scraper command-line prompt. The browser will close and the authentication credentials (usually cookies) for that browser session will be written out to the auth.json file. To take authenticated screenshots you can then use the -a or --auth options to point to the JSON file that you created: shot-scraper https://datasette-auth-passwords-demo.datasette.io/ \ -a auth.json -o authed.png shot-scraper auth --help ¶ Full --help for shot-scraper auth : Usage : shot - scraper auth [ OPTIONS ] URL CONTEXT_FILE Open a browser so user can manually authenticate with the specified site , then save the resulting authentication context to a file . Usage : shot - scraper auth https : // github . com / auth . json Options : - b , -- browser [ chromium | firefox | webkit | chrome | chrome - beta ] Which browser to use -- browser - arg TEXT Additional arguments to pass to the browser -- user - agent TEXT User - Agent header to use -- devtools Open browser DevTools -- log - console Write console . log () to stderr -- help Show this message and exit . Next Taking multiple screenshots Previous Taking a screenshot Copyright © 2024, Simon Willison Made with Sphinx and @pradyunsg 's Furo On this page Websites that need authentication

### 10. Screencast | Playwright Python

- Type: web
- URL: https://playwright.dev/python/docs/api/class-screencast
- Title: Screencast | Playwright Python
- Description: Interface for capturing screencast frames from a page.
- Links:
  - https://playwright.dev/python/docs/api/class-screencast - Skip to main content
  - https://playwright.dev/python/ - Playwright for Python
  - https://playwright.dev/python/docs/intro - Docs
  - https://playwright.dev/python/docs/api/class-playwright - API
  - https://playwright.dev/docs/api/class-screencast - Node.js
  - https://playwright.dev/java/docs/api/class-screencast - Java
  - https://playwright.dev/dotnet/docs/api/class-screencast - .NET
  - https://playwright.dev/python/community/welcome - Community
  - https://github.com/microsoft/playwright-python
  - https://aka.ms/playwright/discord
  - https://playwright.dev/python/docs/api/class-apirequest - Classes
  - https://playwright.dev/python/docs/api/class-apirequestcontext - APIRequestContext
  - https://playwright.dev/python/docs/api/class-apiresponse - APIResponse
  - https://playwright.dev/python/docs/api/class-browser - Browser
  - https://playwright.dev/python/docs/api/class-browsercontext - BrowserContext
  - https://playwright.dev/python/docs/api/class-browsertype - BrowserType
  - https://playwright.dev/python/docs/api/class-cdpsession - CDPSession
  - https://playwright.dev/python/docs/api/class-clock - Clock
  - https://playwright.dev/python/docs/api/class-consolemessage - ConsoleMessage
  - https://playwright.dev/python/docs/api/class-credentials - Credentials

Excerpt:

Screencast | Playwright Python Skip to main content Playwright for Python Docs API Python Python Node.js Java .NET Community Search API reference Playwright Classes APIRequest APIRequestContext APIResponse Browser BrowserContext BrowserType CDPSession Clock ConsoleMessage Credentials Debugger Dialog Download ElementHandle Error FileChooser Frame FrameLocator JSHandle Keyboard Locator Mouse Page Request Response Route Screencast Selectors TimeoutError Touchscreen Tracing Video WebError WebSocket WebSocketRoute WebStorage Worker Assertions APIResponseAssertions LocatorAssertions PageAssertions API reference Classes Screencast On this page Screencast Interface for capturing screencast frames from a page. Methods ​ hide_actions ​ Added in: v1.59 screencast.hide_actions Removes action decorations. Usage screencast . hide_actions ( ) Returns NoneType # hide_overlays ​ Added in: v1.59 screencast.hide_overlays Hides overlays without removing them. Usage screencast . hide_overlays ( ) Returns NoneType # show_actions ​ Added in: v1.59 screencast.show_actions Enables visual annotations on interacted elements. Returns a disposable that stops showing actions when disposed. Usage screencast . show_actions ( ) screencast . show_actions ( ** kwargs ) Arguments cursor "none" | "pointer" (optional) Added in: v1.61 # Cursor decoration shown for pointer actions. "pointer" (the default) renders a mouse pointer that animates from the previous action point to the next one. "none" disables the cursor decoration. duration float (optional) # How long each annotation is displayed in milliseconds. Defaults to 500 . font_size int (optional) # Font size of the action title in pixels. Defaults to 24 . position "top-left" | "top" | "top-right" | "bottom-left" | "bottom" | "bottom-right" (optional) # Position of the action title overlay. Defaults to "top-right" . Returns [Disposable] # show_chapter ​ Added in: v1.59 screencast.show_chapter Shows a chapter overlay with a title and optional description, centered on the page with a blurred backdrop. Useful for narrating video recordings. The overlay is removed after the specified duration, or 2000ms. Usage screencast . show_chapter ( title ) screencast . show_chapter ( title , ** kwargs ) Arguments title str # Title text displayed prominently in the overlay. description str (optional) # Optional description text displayed below the title. duration float (optional) # Duration in milliseconds after which the overlay is automatically removed. D

