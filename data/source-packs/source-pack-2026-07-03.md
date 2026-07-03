# Firsthand AI source pack 2026-07-03

Coverage: 2026-07-02T00:02:00Z to 2026-07-03T00:02:00Z
Items: 44 Counts: {'x': 38, 'blogs': 3, 'videos': 2, 'podcasts': 1}

## 1. [x] Eventually, much of AI will converge towards intuition-guided symbolic world modeling, i.e. deep learning-guided program
- Source: François Chollet fchollet
- Published: 2026-07-02T20:29:11+00:00
- Link: https://x.com/fchollet/status/2072779641639875048
- Summary: Eventually, much of AI will converge towards intuition-guided symbolic world modeling, i.e. deep learning-guided program synthesis. It is inevitable. Symbolic modeling lets a system construct a compact, reusable, highly generalizable mental model of a problem space using minimal data.

## 2. [x] going to world cup games is always awesome, but watching the USA win in the USA during USA birthday week was just incred
- Source: Sam Altman sama
- Published: 2026-07-02T20:04:57+00:00
- Link: https://x.com/sama/status/2072773542576586790
- Summary: going to world cup games is always awesome, but watching the USA win in the USA during USA birthday week was just incredible

## 3. [x] Excited to listen to this. @ssankar is a patriot and a visionary and it's been an honor to serve alongside him, @boztank
- Source: Kevin Weil kevinweil
- Published: 2026-07-02T19:53:54+00:00
- Link: https://x.com/kevinweil/status/2072770763804004467
- Summary: Excited to listen to this. @ssankar is a patriot and a visionary and it's been an honor to serve alongside him, @boztank, @bobmcgrewai and the Det 201 squad this past year. We need more collaboration between SV and DC 🇺🇸  @elizabeth has ruled out the mustache for me though.

## 4. [blogs] llm-coding-agent 0.1a0
- Source: Simon Willison Simon Willison
- Published: 2026-07-02T19:33:12+00:00
- Link: https://simonwillison.net/2026/Jul/2/llm-coding-agent/
- Summary: <p><strong>Release:</strong> <a href="https://github.com/simonw/llm-coding-agent/releases/tag/0.1a0">llm-coding-agent 0.1a0</a></p>         <p>Another Fable 5 experiment. Now that my <a href="https://llm.datasette.io/">LLM library</a> has evolved into more of an agent framework it's time to see what a simple coding agent would look like built on it.</p> <p>I started a <a href="https://github.com/simonw/llm-coding-agent/tree/2466fa03ba8e5122c3bfa93d52167d33bce40ac6">new Python library</a> using my <a href="https://github.com/simonw/python-lib-template-repository">python-lib-template-repository</a> GitHub template repository, then ran these two prompts (here's the <a href="https://claude.ai/code/session_01TEUBvBbMipbFSoqjMiJ7ha">Claude Code for web transcript</a>):</p> <blockquote> <p><code>Write a spec.md for this project - it will depend on the latest “llm” alpha from PyPI and implement a Claude code style coding agent complete with tools for reading and editing files and executing commands</code></p> </blockquote> <p>Then:</p> <blockquote> <p><code>Commit the spec, then build it using red/green TDD in a series of sensible commits (each with passing tests and updated docs) - occasionally manually test it using the OpenAI API key in your environment</code></p> </blockquote> <p>Here's the <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/README.md">resulting README file</a> and the <a href="https://github.com/simonw/llm-coding-agent/commits/0.1a0">sequence of commits</a>.</p> <p>I've shipped a slop-alpha to PyPI, so you can run the new agent like this:</p> <pre><code>uvx --prerelease=allow --with llm-coding-agent llm code </code></pre> <p>It's pretty good for a first attempt! Here's the (Fable-authored) <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/README.md">README</a>, which lists recipes like <code>llm code --yolo</code> and <code>llm code --allow "pytest*" --allow "git diff*"</code>.</p> <p>It also presents <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/README.md#codingagent">a Python API</a> based around a <code>CodingAgent(model="gpt-5.5", root="/path", approve=True).run("Fix the failing test in tests/test_parser.py")</code> class which I didn't ask for but I'm delighted to see implemented.</p> <p>Here's the suite of tools <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/llm_coding_agent/tools.py#L22">it implemented</a>, listed using <code>uvx ... llm tools</code>:</p> <blockquote> <p><code>CodingTools_edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -&gt; str</code></p> <p>Replace an exact string in a file.</p> <p>old_string must match the file contents exactly (including whitespace) and must identify a unique location unless replace_all is true. Returns a diff of the change so it can be verified.</p> <p><code>CodingTools_execute_command(command: str, timeout: int = 120) -&gt; str</code></p> <p>Run a shell command in the session root directory.</p> <p>Returns combined stdout and stderr followed by an Exit code line. timeout is in seconds (maximum 600); on timeout the whole process tree is killed.</p> <p><code>CodingTools_list_files(pattern: str = '**/*', path: str = '.') -&gt; str</code></p> <p>List files matching a glob pattern, newest first.</p> <p>Skips hidden directories, node_modules, __pycache__ and (in a git repository) anything covered by .gitignore. Returns at most 200 paths relative to the searched directory.</p> <p><code>CodingTools_read_file(path: str, offset: int = 0, limit: int = 2000) -&gt; str</code></p> <p>Read a text file, returning numbered lines like cat -n.</p> <p>Paths are relative to the session root. Use offset (0-based first line) and limit (max lines) to page through files too large to read in one call.</p> <p><code>CodingTools_search_files(pattern: str, path: str = '.', glob: str = None, max_results: int = 100) -&gt; str</code></p> <p>Search file contents for a regular expression.</p> <p>Returns matches as path:line_number:line, capped at max_results. Use glob (e.g. "*.py") to restrict which files are searched.</p> <p><code>CodingTools_write_file(path: str, content: str) -&gt; str</code></p> <p>Create or overwrite a file with the given content.</p> <p>Parent directories are created as needed. Prefer edit_file for modifying existing files.</p> </blockquote> <p>I tried it out by running <code>llm code --yolo</code> and then prompting:</p> <blockquote> <p><code>mkdir /tmp/demo and then in that folder create a simple swiftui CLI app for telling the time in ascii art</code></p> </blockquote> <p>Here's <a href="https://gist.github.com/simonw/750009007050124cd1b390cfe8488e41">the transcript</a>, in which GPT-5.5 reasoning notes that "SwiftUI isn't suitable for a true CLI" and then builds an app that outputs this on <code>swift run AsciiTime</code>:</p> <pre style="font-size: 9px;">       █    █████         ████     █             █     ███         ██    █        █        █   ██      █     ██    █   █         █    ████           ███     █             █       █          █        █    █        █    █      █      █      █          ███   ████          ████    ███           ███   █████ </pre>                   <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/llm-tool-use">llm-tool-use</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>

## 5. [x] everyone come down to the AIE Expo at 12.30, there's a SPECIAL **FLASH** SURPRISE (you'll know it when u see it) and the
- Source: Swyx swyx
- Published: 2026-07-02T19:12:49+00:00
- Link: https://x.com/swyx/status/2072760421627597198
- Summary: everyone come down to the AIE Expo at 12.30, there's a SPECIAL **FLASH** SURPRISE (you'll know it when u see it) and then come to Expo Stage 2 for a very special @latentspacepod live pod with Etched! https://t.co/fisw6g3UKr

## 6. [x] Thought I’d share a fun activity I did with my 8-year-old daughter and Codex today:

1. She drew a picture of a dragon.

- Source: Peter Yang petergyang
- Published: 2026-07-02T18:57:51+00:00
- Link: https://x.com/petergyang/status/2072756657856422379
- Summary: Thought I’d share a fun activity I did with my 8-year-old daughter and Codex today:  1. She drew a picture of a dragon.  2. We uploaded her drawing to Codex and used image gen to make a few more dragon poses. She used voice to give Codex feedback until we got the result below.  3. We sent it to customstickers(dot)com to print sticker sheets (it's about $20 for 10 sheets).  Now she can share her stickers with her friends when they arrive in the mail next week. Try it if you have kids stuck at home this summer :)

## 7. [x] very proud that the biggest applause line in the AIE keynotes this year was normalizing men talking about their feelings
- Source: Swyx swyx
- Published: 2026-07-02T18:50:10+00:00
- Link: https://x.com/swyx/status/2072754722059239471
- Summary: very proud that the biggest applause line in the AIE keynotes this year was normalizing men talking about their feelings and mental health in hypergrowth  thanks @mikeyk for indulging all my cheeky questions on Fable and Tag!! https://t.co/8rml4RU8gl

## 8. [blogs] Using DSPy to evaluate and improve Datasette Agent's SQL system prompts
- Source: Simon Willison Simon Willison
- Published: 2026-07-02T18:25:00+00:00
- Link: https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/
- Summary: <p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/dspy-datasette-agent-prompts#readme">Using DSPy to evaluate and improve Datasette Agent&#x27;s SQL system prompts</a></p>         <p>One of this morning's AIE keynotes covered <a href="https://github.com/stanfordnlp/dspy">dspy</a>, which reminded me I've been meaning to see if it could help me improve the system prompt used by <a href="https://agent.datasette.io">Datasette Agent</a> - so I fired off an asynchronous research task in Claude Code for web using Claude Fable 5:</p> <blockquote> <p><code>Pip install the latest Datasette alpha and datasette-agent and dspy - then figure out how to use dspy to evaluate and improve the main system prompts used by Datasette Agent for the feature where it can execute read only SQL queries to answer user questions about data.</code></p> </blockquote> <p>Fable chose to test using GPT 4.1 mini and nano, and identified several promising looking directions for improvements. I particularly like this one:</p> <blockquote> <p>The schema listing gives only table names; the "don't call describe_table if you already have the information" advice caused column-name guessing (page_count, o.order_id, first_name) and error-retry loops in baseline traces. Either include column names in the prompt's schema listing or soften that advice.</p> </blockquote>                   <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/evals">evals</a>, <a href="https://simonwillison.net/tags/dspy">dspy</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>

## 9. [x] I havea bunch of YouTube adsense revenue trapped in my account b/c Google won't confirm my tax info...and there's no way
- Source: Peter Yang petergyang
- Published: 2026-07-02T18:18:08+00:00
- Link: https://x.com/petergyang/status/2072746659713606016
- Summary: I havea bunch of YouTube adsense revenue trapped in my account b/c Google won't confirm my tax info...and there's no way to reach a real human to talk to.  Anyone have any connections who work at YouTube or Adsense? https://t.co/0W6liHjVoA

## 10. [x] We've been explaining AI Gateway as a C̶o̶n̶t̶e̶n̶t̶ Token Delivery Network. Like a CDN for AI models.

One great featur
- Source: Guillermo Rauch rauchg
- Published: 2026-07-02T17:57:06+00:00
- Link: https://x.com/rauchg/status/2072741369848746315
- Summary: We've been explaining AI Gateway as a C̶o̶n̶t̶e̶n̶t̶ Token Delivery Network. Like a CDN for AI models.  One great feature of CDNs is the ability to dynamically re-route or deny traffic without redeployment.  When Fable was suddenly retired, we worried about production workloads depending on it. Even Fable aside, models get retired quite often as GPU capacity is heavily contested. Yet our data shows people still having happy production traffic of older model versions!  We're solving this now with AI Gateway Rules. e.g.: you can now rewrite model "routes" on the fly!  𝚟𝚎𝚛𝚌𝚎𝚕 𝚊𝚒-𝚐𝚊𝚝𝚎𝚠𝚊𝚢 𝚛𝚞𝚕𝚎𝚜 𝚊𝚍𝚍 \   --𝚝𝚢𝚙𝚎 𝚛𝚎𝚠𝚛𝚒𝚝𝚎 \   --𝚜𝚘𝚞𝚛𝚌𝚎 𝚊𝚗𝚝𝚑𝚛𝚘𝚙𝚒𝚌/𝚌𝚕𝚊𝚞𝚍𝚎-𝚏𝚊𝚋𝚕𝚎-𝟻 \   --𝚍𝚎𝚜𝚝𝚒𝚗𝚊𝚝𝚒𝚘𝚗 𝚊𝚗𝚝𝚑𝚛𝚘𝚙𝚒𝚌/𝚌𝚕𝚊𝚞𝚍𝚎-𝚘𝚙𝚞𝚜-𝟻  This adds to the repertoire of capabilities and techniques AI Gateway brings to the table to recover lost tokens. If you drop tokens, you lose revenue and customers 💸  Kudos to @rtaneja_ @crowprose @shaper – we went from CLI design to production-grade capability very quickly!

## 11. [x] Grok Build is now installed in Railway sandboxes
- Source: xAI xai
- Published: 2026-07-02T17:46:06+00:00
- Link: https://x.com/xai/status/2072738598663946648
- Summary: Grok Build is now installed in Railway sandboxes

## 12. [x] I am interviewing @NousResearch Hermes co-founder @karan4d tomorrow, what topics would you like to see us cover?

I alre
- Source: Peter Yang petergyang
- Published: 2026-07-02T17:42:07+00:00
- Link: https://x.com/petergyang/status/2072737599362621866
- Summary: I am interviewing @NousResearch Hermes co-founder @karan4d tomorrow, what topics would you like to see us cover?  I already covered setup, integrations, and basic cron jobs in a previous tutorial - so what else would y'all like to hear about?  This chart is a vertical line lol https://t.co/Bqacty1252

## 13. [x] This is true
- Source: Aditya Agarwal adityaag
- Published: 2026-07-02T17:34:13+00:00
- Link: https://x.com/adityaag/status/2072735608485945555
- Summary: This is true

## 14. [x] Claude Tag is unlocking productivity across our entire org: eng, product, data, sales, marketing. Our internal version l
- Source: Cat Wu _catwu
- Published: 2026-07-02T17:17:53+00:00
- Link: https://x.com/_catwu/status/2072731500928508331
- Summary: Claude Tag is unlocking productivity across our entire org: eng, product, data, sales, marketing. Our internal version lands 65% of product PRs.  We cover the CEO/CTO playbook for rolling it out, why security was designed in from day one, and what this means for the future of work.

## 15. [blogs] Understand to participate
- Source: Simon Willison Simon Willison
- Published: 2026-07-02T17:07:14+00:00
- Link: https://simonwillison.net/2026/Jul/2/understand-to-participate/
- Summary: <p>I saw Geoffrey Litt speak at <a href="https://www.ai.engineer/worldsfair/2026">AIE</a> yesterday, and one framing he used particularly resonated with me:</p> <p><strong>Understand to participate</strong></p> <p>Geoffrey was talking about the challenge of collaborating with coding agents as they construct increasingly large and sophisticated changes, and the need to avoid taking on <a href="https://simonwillison.net/tags/cognitive-debt/">cognitive debt</a> as your understanding drifts from how the code actually works.</p> <p>His argument is that you need to understand the code to a depth that enables you to participate further with the model:</p> <blockquote> <p>You can learn what the agent is doing to make sure you can be an active participant in the creative process. [...]</p> <p>You need a rich set of concepts in your mind to think creatively and fluently about how to move something forward. If you're lacking that fluency, your ability to participate in the project is meaningfully limited.</p> </blockquote> <p>The AIE talks are all recorded - all 300+ of them! - and should be trickling out over the next three weeks. Geoffrey's is one that I recommend catching on YouTube.</p> <p>Geoffrey also published <a href="https://twitter.com/geoffreylitt/status/2072522251300409556">a thread version of his talk</a> on Twitter.</p>      <p>Tags: <a href="https://simonwillison.net/tags/geoffrey-litt">geoffrey-litt</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/cognitive-debt">cognitive-debt</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a></p>

## 16. [x] The best application for models to run locally on hardware you own would be personal robots. There’s no way anyone is go
- Source: Aravind Srinivas AravSrinivas
- Published: 2026-07-02T17:03:06+00:00
- Link: https://x.com/AravSrinivas/status/2072727777179258986
- Summary: The best application for models to run locally on hardware you own would be personal robots. There’s no way anyone is going to get comfortable streaming your home to a server. And when this happens, the local hardware will also become a token faucet for your digital tasks.

## 17. [x] A conversation with Boris Cherny and Cat Wu on the path from Claude Code to Claude Tag, and how it spread from engineeri
- Source: Claude claudeai
- Published: 2026-07-02T16:54:29+00:00
- Link: https://x.com/claudeai/status/2072725610061803522
- Summary: A conversation with Boris Cherny and Cat Wu on the path from Claude Code to Claude Tag, and how it spread from engineering to the rest of Anthropic.  Claude Fable 5 is now available in Claude Tag. https://t.co/8oNM5WaWzj

## 18. [x] Intelligence is now metered 🥲 

Have to use this very wisely https://t.co/4F3Ph6jrZx
- Source: Peter Yang petergyang
- Published: 2026-07-02T16:35:54+00:00
- Link: https://x.com/petergyang/status/2072720933446701170
- Summary: Intelligence is now metered 🥲   Have to use this very wisely https://t.co/4F3Ph6jrZx

## 19. [videos] Fable 5 vs GPT 5.6 Sol: The Early Results
- Source: AI Explained AI Explained
- Published: 2026-07-02T16:27:26+00:00
- Link: https://www.youtube.com/watch?v=y24lF1q4SFY
- Summary: Fable 5 (newly re-released) vs GPT 5.6 Sol, what comparisons can we unearth? Plus, Sonnet 5, a 5% equity seizure by US Govt, the ‘largest heist’, Beetlejuice and more…    Exclusive Vids in AI Insiders ($9!): https://www.patreon.com/AIExplained   Chapters: 00:00 - Introduction 01:06 - Fable Timeline 02:59 - Sol Release? 06:01 - the Chinese Angle 07:35 - 5% Stake 09:10 - Fable vs Sol - the numbers 13:57 - Sol Misalignment 15:27 - Claude Sonnet 5 16:24 - GLM 5.2 + New Paper on Large Model Learning  GPT 5.6 Sol Release: https://openai.com/index/previewing-gpt-5-6-sol/ Altman on Concentrated Power: https://x.com/giacomomiolo/status/2070609506925478352 System Card: https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf  GLM 5.2: https://www.patreon.com/AIExplained/posts/glm-5-2-and-nsa-161869508  Altman Memo: https://www.theinformation.com/articles/trump-administration-asks-openai-stagger-release-new-model-security-concerns?rc=sy0ihq  Fable 5 Revised Timeline: https://www.anthropic.com/news/redeploying-fable-5  Claude Sonnet 5: https://www.anthropic.com/news/claude-sonnet-5  Mythose 5 System Card: https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf  Anthropic Accuse Alibaba Cloud / Qwen: https://www.bbc.co.uk/news/articles/cwyklykn5dwo  Betelgeuse: https://upload.wikimedia.org/wikipedia/commons/6/69/Well_known_stars_2.png  OpenAI 5%: https://edition.cnn.com/2026/07/02/business/openai-trump-stake-intl  Why Larger Models Learn More: https://arxiv.org/pdf/2605.29548  Patreon Post: https://www.patreon.com/AIExplained/posts/glm-5-2-and-nsa-161869508    Non-hype Newsletter: https://signaltonoise.beehiiv.com/  Podcast: https://aiexplainedopodcast.buzzsprout.com/

## 20. [x] Private connectivity between services is 🔑 for backends.

1️⃣ Register 𝚋𝚒𝚗𝚍𝚒𝚗𝚐𝚜 in 𝚟𝚎𝚛𝚌𝚎𝚕.𝚓𝚜𝚘𝚗 (1LOC)
2️⃣ Read it:

𝚗𝚎𝚠 
- Source: Guillermo Rauch rauchg
- Published: 2026-07-02T16:14:56+00:00
- Link: https://x.com/rauchg/status/2072715658157027375
- Summary: Private connectivity between services is 🔑 for backends.  1️⃣ Register 𝚋𝚒𝚗𝚍𝚒𝚗𝚐𝚜 in 𝚟𝚎𝚛𝚌𝚎𝚕.𝚓𝚜𝚘𝚗 (1LOC) 2️⃣ Read it:  𝚗𝚎𝚠 𝚄𝚁𝙻("/𝚊𝚙𝚒", 𝚙𝚛𝚘𝚌𝚎𝚜𝚜.𝚎𝚗𝚟.𝙱𝙰𝙲𝙺𝙴𝙽𝙳_𝙸𝙽𝚃𝙴𝚁𝙽𝙰𝙻_𝚄𝚁𝙻)  Works for Node, Python, 𝙳𝚘𝚌𝚔𝚎𝚛𝚏𝚒𝚕𝚎… you name it

## 21. [videos] Should You Still Study Math in the AI Era? – Grant Sanderson (@3blue1brown )
- Source: Dwarkesh Patel Dwarkesh Patel
- Published: 2026-07-02T16:04:10+00:00
- Link: https://www.youtube.com/watch?v=35mQq0AmC_8
- Summary: Full episode: https://www.youtube.com/watch?v=TfyPshgMbug Me on twitter: https://x.com/dwarkesh_sp

## 22. [x] Everyone in NYC has the same dog. It's a french bulldog. This needs to be studied
- Source: Guillermo Rauch rauchg
- Published: 2026-07-02T15:58:51+00:00
- Link: https://x.com/rauchg/status/2072711610712330658
- Summary: Everyone in NYC has the same dog. It's a french bulldog. This needs to be studied

## 23. [x] True
- Source: Elon Musk elonmusk
- Published: 2026-07-02T15:27:35+00:00
- Link: https://x.com/elonmusk/status/2072703739866083721
- Summary: True

## 24. [x] Good analysis of rent control  https://t.co/vu4iReeoH3
- Source: Elon Musk elonmusk
- Published: 2026-07-02T15:24:35+00:00
- Link: https://x.com/elonmusk/status/2072702987915415887
- Summary: Good analysis of rent control  https://t.co/vu4iReeoH3

## 25. [x] Watching our product owners pitch and demo internally with @v0⁠s feels like science fiction, especially with our design 
- Source: Guillermo Rauch rauchg
- Published: 2026-07-02T15:16:43+00:00
- Link: https://x.com/rauchg/status/2072701005377016112
- Summary: Watching our product owners pitch and demo internally with @v0⁠s feels like science fiction, especially with our design system fidelity. It gives the company end-user empathy and decision-making velocity that we never had with text or slides. Demos &gt; memos.

## 26. [x] Starship static fire
- Source: Elon Musk elonmusk
- Published: 2026-07-02T14:57:04+00:00
- Link: https://x.com/elonmusk/status/2072696059835367870
- Summary: Starship static fire

## 27. [x] I think the days of companies relying only on frontier models are coming to an end.

1. Tokenmaxxing at frontier-model A
- Source: Peter Yang petergyang
- Published: 2026-07-02T14:15:02+00:00
- Link: https://x.com/petergyang/status/2072685484011344032
- Summary: I think the days of companies relying only on frontier models are coming to an end.  1. Tokenmaxxing at frontier-model API prices makes no sense.  Uber burned through its entire 2026 AI budget in 4 months, Microsoft moved engineers off Claude Code due to cost, and companies are realizing that running everything on frontier models can get expensive fast. Tokenmaxxing makes sense when you’re on a subsidized $200/month plan, but it’s unsustainable at API rates.  2. Companies will rely on a portfolio of models.  Coinbase recently cut its AI spend nearly in half by switching engineers to Chinese open-source models like GLM and Kimi. Airbnb and Pinterest have done the same with Alibaba’s Qwen models. I believe this will be the default path forward: using frontier models for high-stakes work and cheaper models for everything else.  3. China’s open-source strategy is working.  Chinese models are taking market share from frontier models at US companies. China is also building the full AI stack, from energy, like solar and nuclear, to data centers to domestic chips. The Chinese government is planning a $295B investment in AI data centers, with at least 80% of chips built domestically.  4. Frontier labs are in a Catch-22 situation.  If they release great open-source models, they might undercut their own frontier API revenue. If they gate the best models behind a trusted list, companies will just lean on open alternatives more. The last major US open-source model was OpenAI’s gpt-oss series back in August 2025, which already feels like decades ago in the AI space.  5. The US needs to think about its AI strategy holistically.  I believe restricting access to frontier models will only hurt American innovation. Banning US companies from using Chinese models won’t work either. Just look at how China took over the global electric vehicle market. To maintain our edge, we need the best closed and open models while scaling our energy grid and data centers much faster.  📌 More in my recent essay: https://t.co/jj568Tx1NU

## 28. [x] Announcing Built with Claude: Life Sciences, a global virtual hackathon.

Join us and @GladstoneInst for a week of resea
- Source: Claude claudeai
- Published: 2026-07-02T14:00:37+00:00
- Link: https://x.com/claudeai/status/2072681853971001849
- Summary: Announcing Built with Claude: Life Sciences, a global virtual hackathon.  Join us and @GladstoneInst for a week of researching and building with Claude Science and Claude Code, with a prize pool of $100k in credits. https://t.co/wzrSBHJgeP

## 29. [podcasts] Why NVIDIA Is Giving Away AI Models | Bryan Catanzaro
- Source: The MAD Podcast with Matt Turck The MAD Podcast with Matt Turck
- Published: 2026-07-02T11:30:00+00:00
- Link: https://podcasters.spotify.com/pod/show/firstmark/episodes/Why-NVIDIA-Is-Giving-Away-AI-Models--Bryan-Catanzaro-e3li7o6
- Summary: <p>NVIDIA is a chip company. So why does it put hundreds of researchers on building AI models — and then give them away for free? Bryan Catanzaro is VP of Applied Deep Learning Research at NVIDIA and one of the people whose work quietly underpins modern AI: he helped create cuDNN (NVIDIA's first deep learning product), co-invented DLSS, and named and built Megatron, the framework behind how much of the industry trains large models. Today he leads Nemotron, NVIDIA's family of open models — and Nemotron 3 Ultra, released just weeks ago, is one of the strongest open-weights models to come out of the US.</p><p><br /></p><p>Matt Turck sits down with Bryan for a genuinely deep conversation: the real business logic behind a chip company building its own models, the state of open vs. closed AI, and whether the US is falling behind China in open models. Then they go inside Nemotron itself — four-bit (NVFP4) pretraining, hybrid Mamba-Transformer architecture, mixture-of-experts, multi-token prediction, and multi-teacher distillation — all explained in plain language. Plus a rare look at how a modern AI research org actually runs, what it was like working alongside Andrew Ng and Dario Amodei at Baidu, why Bryan doesn't believe in the singularity, and his contrarian case that open AI is safer than closed.</p><p><br /></p><p>A reference conversation for anyone trying to understand where AI is really headed.</p><p><br /></p><p>(00:00) — Cold open &amp; Intro</p><p>(01:33) — Is open source AI catching the frontier?</p><p>(05:29) — Do closed labs blocking distillation slow open source down?</p><p>(07:42) — Is the US falling behind China?</p><p>(10:30) — Why companies actually choose open models</p><p>(12:39) — A &quot;crazy&quot; 2008 bet: machine learning on GPUs</p><p>(15:33) — Working with Andrew Ng and Dario Amodei at Baidu</p><p>(17:41) — Coming back to NVIDIA: DLSS and the birth of Megatron</p><p>(21:55) — The real reason NVIDIA builds its own models</p><p>(24:28) — Is Moore's Law really dead?</p><p>(33:37) — The Nemotron family: Nano, Super, Ultra</p><p>(35:09) — Built for agents: why NVIDIA bets on speed</p><p>(36:02) — How you train a 550B model in 4 bits</p><p>(39:25) — Hybrid Mamba-Transformer, explained simply</p><p>(42:31) — Mixture of experts — and why NVIDIA built NVL72 around it</p><p>(47:26) — Why a 1-million-token context window matters</p><p>(49:26) — Multi-token prediction: how the model predicts 5 tokens at once</p><p>(52:47) — Multi-teacher distillation: teaching one model from many</p><p>(58:01) — Where reinforcement learning goes next</p><p>(01:00:16) — Inside NVIDIA's research org: &quot;the mission is the boss&quot;</p><p>(01:04:03) — How NVIDIA decides who gets the GPUs</p><p>(01:10:53) — Why NVIDIA still feels entrepreneurial after 33 years</p><p>(01:12:58) — Why Bryan doesn't believe in the singularity</p><p>(01:17:50) — The AI backlash</p><p>(01:19:18) — The controversial case: open AI is safer than closed</p>

## 30. [x] Can't wait to see what people will do with GPT-5.6 Sol Ultra. Stash your hardest prompts somewhere.
- Source: Tibo thsottiaux
- Published: 2026-07-02T09:06:48+00:00
- Link: https://x.com/thsottiaux/status/2072607914217320644
- Summary: Can't wait to see what people will do with GPT-5.6 Sol Ultra. Stash your hardest prompts somewhere.

## 31. [x] for what it's worth, i only invite double-length track keynotes when I'm very sure that both speaker and content deserve
- Source: Swyx swyx
- Published: 2026-07-02T06:07:09+00:00
- Link: https://x.com/swyx/status/2072562702703046855
- Summary: for what it's worth, i only invite double-length track keynotes when I'm very sure that both speaker and content deserve it. Today, @chrmanning and @abshkbh did double duty at AIE and by all accounts* people loved the opportunity to go deeper on sandboxing and world models. Look at this insane room - and the online audience is going to be >1000x this!!  *i unfortunately have to do show duties so rely on secondhand accounts

## 32. [x] Never thought I give @Steve_Yegge a shoutout. He was just early, like most visionaries. Now everyone is building factori
- Source: Peter Steinberger steipete
- Published: 2026-07-02T04:06:15+00:00
- Link: https://x.com/steipete/status/2072532278476148881
- Summary: Never thought I give @Steve_Yegge a shoutout. He was just early, like most visionaries. Now everyone is building factories.

## 33. [x] As someone still trying to learn how to read code this is great! Installing the explain-diff skill asap
- Source: Peter Yang petergyang
- Published: 2026-07-02T03:39:59+00:00
- Link: https://x.com/petergyang/status/2072525669704384612
- Summary: As someone still trying to learn how to read code this is great! Installing the explain-diff skill asap

## 34. [x] If you’ve ever wondered why we will need 100X more AI inference in the future, and  what it’s going to be driven by, thi
- Source: Aaron Levie levie
- Published: 2026-07-02T03:14:59+00:00
- Link: https://x.com/levie/status/2072519377371459836
- Summary: If you’ve ever wondered why we will need 100X more AI inference in the future, and  what it’s going to be driven by, this is another good example.   Devin pushes forward an idea of agentic mapreduce, which means we’ll now have swarms of agents that are processing large amounts of data (code) to handle tasks that humans never could have done before.  “Devin maps relevant signals across the repo, fans out focused agents over bounded shards, reduces their findings into one report, then verifies serious vulnerabilities in isolated sandboxes before marking them confirmed.”  In this case it’s code security, but there are tons of other use-cases in code and knowledge work. We see this at Box with customers that want to process and understand millions of documents for risk, insights, relationships, and more. This will play out in pharma, banking, and many other industries across all forms of unstructured data.  As an aside, these types of capabilities are generally only possible when you can deploy a variety of models (both the frontier and lower cost) because of the sheer amount of tokens that go into these use-cases. This is going to be a major value proposition for the applied AI layer.

## 35. [x] I’m looking for a semi-private hack space for a few days in SF for me and some of the OpenClaw maintainers. We need to c
- Source: Peter Steinberger steipete
- Published: 2026-07-02T00:22:04+00:00
- Link: https://x.com/steipete/status/2072475858435276840
- Summary: I’m looking for a semi-private hack space for a few days in SF for me and some of the OpenClaw maintainers. We need to cook. DM leads my way 🙏🦞

## 36. [x] Here's my Fable 5 vibe check:

It's still really ****ing good. 

This is a step function above any other model. Hope GPT
- Source: Peter Yang petergyang
- Published: 2026-07-01T23:59:32+00:00
- Link: https://x.com/petergyang/status/2072470191511113732
- Summary: Here's my Fable 5 vibe check:  It's still really ****ing good.   This is a step function above any other model. Hope GPT 5.6 can match.

## 37. [x] Codex for making a personalized daily digest:
- Source: Greg Brockman gdb
- Published: 2026-07-01T23:54:15+00:00
- Link: https://x.com/gdb/status/2072468859047772664
- Summary: Codex for making a personalized daily digest:

## 38. [x] WordPress on @vercel Fluid with Active CPU from a single 𝙳𝚘𝚌𝚔𝚎𝚛𝚏𝚒𝚕𝚎.𝚟𝚎𝚛𝚌𝚎𝚕. MySQL on @planetscale. 30s deployments incl.
- Source: Guillermo Rauch rauchg
- Published: 2026-07-01T23:32:08+00:00
- Link: https://x.com/rauchg/status/2072463293654942090
- Summary: WordPress on @vercel Fluid with Active CPU from a single 𝙳𝚘𝚌𝚔𝚎𝚛𝚏𝚒𝚕𝚎.𝚟𝚎𝚛𝚌𝚎𝚕. MySQL on @planetscale. 30s deployments incl. "𝚍𝚘𝚌𝚔𝚎𝚛 𝚋𝚞𝚒𝚕𝚍" in the cloud. Just one command: 𝚗̶𝚘̶𝚠̶ 𝚟𝚎𝚛𝚌𝚎𝚕. https://t.co/q1X5ZOFVIx

## 39. [x] Claude Fable 5 is finally back, but you only have until July 7 to use it on your Claude subscription.

I made a new tuto
- Source: Peter Yang petergyang
- Published: 2026-07-01T23:15:00+00:00
- Link: https://x.com/petergyang/status/2072458983886205333
- Summary: Claude Fable 5 is finally back, but you only have until July 7 to use it on your Claude subscription.  I made a new tutorial walking through 5 use cases worth trying Fable on:  → Find Fable-worthy work → Get life and business advice → Make projects ship-ready → Plan the next big thing → Refactor your project or codebase  As usual, it’s no BS, and I show you Fable’s actual output.  📌 Watch now: https://t.co/XElMEV3FwK

## 40. [x] Free money, housing, etc acts as a massive financial forcing function to draw illegals to America and Europe
- Source: Elon Musk elonmusk
- Published: 2026-07-01T22:39:56+00:00
- Link: https://x.com/elonmusk/status/2072450156801446239
- Summary: Free money, housing, etc acts as a massive financial forcing function to draw illegals to America and Europe

## 41. [x] Every once in a while, I meet a very very smart but default-pessimistic person in SF. They are often from the growthy/wa
- Source: Aditya Agarwal adityaag
- Published: 2026-07-01T22:37:46+00:00
- Link: https://x.com/adityaag/status/2072449611550380526
- Summary: Every once in a while, I meet a very very smart but default-pessimistic person in SF. They are often from the growthy/wall-street part of the world.  And my first thought is: "Why would you want to be in this city? We run on optimism. Are you here to be a contrarian in your sadness?"

## 42. [x] How did I ever function without AI? 
cc chefcook @theo https://t.co/G0LJNvA3Kb
- Source: Peter Steinberger steipete
- Published: 2026-07-01T22:29:11+00:00
- Link: https://x.com/steipete/status/2072447453622882338
- Summary: How did I ever function without AI?  cc chefcook @theo https://t.co/G0LJNvA3Kb

## 43. [x] https://t.co/cNEdVN6nop
- Source: Elon Musk elonmusk
- Published: 2026-07-01T22:20:46+00:00
- Link: https://x.com/elonmusk/status/2072445332315902174
- Summary: https://t.co/cNEdVN6nop

## 44. [x] you can just reset rate limits on things
- Source: Greg Brockman gdb
- Published: 2026-07-01T22:14:10+00:00
- Link: https://x.com/gdb/status/2072443674307535239
- Summary: you can just reset rate limits on things
