# The Dark Forest: Why I Built Scheduled AI Agents 13 Months Early and Didn't Sell a Thing

Let me take you back thirteen months, to before [Claude Code](https://code.claude.com/) `/loop`, before [OpenClaw](https://en.wikipedia.org/wiki/OpenClaw), before any major AI tool had the concept of a scheduled agent. February 2025. Most people were still copy-pasting [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) output into their editors. [Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy) had just coined "[vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)." The question of the moment was whether AI could write code at all.

I was interested in a different question: could an AI agent outlive the conversation?

I wanted autonomy. Not the chatbot kind where you sit there prompting back and forth, but real autonomy. An agent that wakes up on a schedule, picks up its tools, does the work, and goes back to sleep. Checks my dependencies for vulnerabilities every morning. Triages issues overnight. Summarizes commits before I have coffee. Self-propagating workflows where one agent's output triggers the next agent's input, choosing different models and different tools at each step based on what the task actually needs.

Nothing could do this. Every AI tool was a conversation you had to be present for. So I built it myself, twice, in about two weeks.

The first version was [CRONAI](https://github.com/forayconsulting/cronai) (February 28, 2025), a quick [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) app. The second was [Maistro](https://github.com/forayconsulting/maistro) (March 7, 2025), a proper rebuild with my friend [Aaron Bockelie](https://github.com/aaronsb) contributing. Same core idea across both: write prompts in plain English, assign each step its own model and its own [MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol)-connected tools, chain workflows together, set a [cron](https://en.wikipedia.org/wiki/Cron) schedule, and let the whole thing run without you. The only agent CLI that could do any of this was [Goose](https://github.com/block/goose), which had launched one month earlier. MCP itself was three months old. The entire foundation I was building on was wet concrete.

I have been using various versions of this stuff since then. It was never a product. It was a utility that let me work faster on the bleeding edge. In the 13 months since, I built 57 repos of other tools along the same lines: MCP servers, agent prototypes, CLI skills, deployment patterns. CRONAI and Maistro were two of those.

Then, this quarter, every major AI company showed up to the same idea.

[OpenAI](https://en.wikipedia.org/wiki/OpenAI) shipped [Codex](https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)) **Automations** in February 2026. [Cursor](https://en.wikipedia.org/wiki/Cursor_(text_editor)) shipped **Automations** with cron triggers on March 5. [Anthropic](https://en.wikipedia.org/wiki/Anthropic) shipped `/loop` for [Claude Code](https://code.claude.com/) in March, with one outlet headlining it "[Claude Code Gets Cron Scheduling to Run as a Background Worker](https://winbuzzer.com/2026/03/09/anthropic-claude-code-cron-scheduling-background-worker-loop-xcxwbn/)." A startup called **CronBox** launched on [Product Hunt](https://www.producthunt.com/products/cronbox-2) with the tagline "Cron for the AI age."

Thirteen months of building and using scheduled AI agents as a personal utility, and now it is a product category.

## The Possibility Space

When I built these tools, the components barely existed. Goose was one month old. MCP was three months old. Claude Code was days old. There was no ecosystem of scheduled AI agent products because there was barely an ecosystem of AI agent CLIs.

I was working with the only tool that could plausibly do what I wanted ([Goose](https://github.com/block/goose) with [MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol)), using the oldest job scheduler in Unix ([cron](https://en.wikipedia.org/wiki/Cron)), held together with Flask and then Node.js. The ceiling of what was possible was low. But the shape of the idea was right.

Now there are 15+ AI CLI coding tools. MCP went from a handful of reference servers to an industry standard under the [Linux Foundation](https://en.wikipedia.org/wiki/Linux_Foundation), with 8 million server downloads and 5,800+ servers. The autonomous AI agent market is estimated at $8.5 billion. And the specific feature that multiple billion-dollar companies shipped in Q1 2026 is: put an AI agent on a cron schedule and let it work.

## Why I Didn't Try to Sell It

I can hear someone reading this and thinking: "You should have productized that. You had a 13-month head start."

No. What I would have had, at absolute best, is a small startup getting one-shotted by a minor Anthropic feature release right now. Claude Code's `/loop` shipped as a point release. Not a product launch, not a keynote. A point release. Cursor Automations? A beta toggle. These companies added "scheduled AI agents" the way they add any feature: as a line item in a changelog. You cannot build a moat around a cron job.

Look at what happened to [ClawdBot](https://en.wikipedia.org/wiki/OpenClaw). [Peter Steinberger](https://steipete.com/) built an open-source personal AI agent that went viral. 145,000 GitHub stars. Coverage in [TechCrunch](https://techcrunch.com/2026/01/27/everything-you-need-to-know-about-viral-personal-ai-assistant-clawdbot-now-moltbot/), [CNBC](https://www.cnbc.com/2026/02/02/openclaw-open-source-ai-agent-rise-controversy-clawdbot-moltbot-moltbook.html), [MacStories](https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/). Consulting businesses sprung up around it. Then Anthropic sent a trademark complaint and he had to rename it. Twice. ClawdBot became Moltbot became [OpenClaw](https://openclaw.ai/), all within a few weeks. The project is still alive and useful, but the trajectory tells the story. When you build in the gravity well of a platform owner, you are one decision away from disruption, whether by feature parity or by legal letter.

[CronBox](https://www.producthunt.com/products/cronbox-2) launched on Product Hunt this week. The founder noted that Claude Code's scheduling is "pretty restrictive." That may be true right now. It will not be true for long. Every limitation CronBox routes around is a feature request sitting on Anthropic's backlog. The product thesis is a countdown timer.

Short-term thinking is product-based. Long-term thinking is capability-based.

What I actually did with those 13 months was keep using these tools. I built MCP servers before most people knew what MCP was. I was writing Zoom transcript MCPs, [Oracle NetSuite](https://en.wikipedia.org/wiki/NetSuite) MCPs, [Google Slides](https://en.wikipedia.org/wiki/Google_Slides) MCPs, [Cloudflare](https://en.wikipedia.org/wiki/Cloudflare) MCP deployment patterns, [Gemini](https://en.wikipedia.org/wiki/Gemini_(language_model)) CLI skills, AI sandbox prototypes, and agent streaming implementations while most of the industry was still figuring out what "agentic" meant. CRONAI and Maistro were utilities in a larger practice of staying on the bleeding edge by building for myself, not for a market.

There are plenty of people like me. We build tools the day the APIs ship. We hit the walls before the docs exist. We write the workarounds that become next quarter's feature announcements. The instinct to productize is strong, but the math rarely works. The window between "too early for anyone to care" and "too late because the platform shipped it natively" is vanishingly small right now.

## When to Actually Build a Product

The right time to jump in is when you have a defensible moat or a perfect moment. You have domain expertise in an industry that will never adopt AI without someone like you walking them through it. You have proprietary data or relationships that cannot be replicated by a feature release. You are solving a coordination problem between multiple vendors that none of them are incentivized to solve. Or you are building at a layer of the stack where the platform owners are not competing.

"I built the feature before they did" is not a moat. It is a signal that you understand the problem space, which is valuable, but not as a product. It is valuable as judgment. It is valuable as capability.

## The Dark Forest

The AI space is a [dark forest](https://en.wikipedia.org/wiki/The_Dark_Forest). Every product you launch is a signal flare. If it works, it tells the platform owners exactly what to build next. If it goes viral, you are months away from being absorbed or outcompeted. If you pick a name too close to a trademark, you are weeks away from a legal notice.

The safe move is not to hide. It is to stay in motion. Build utilities, not products. Accumulate capability, not customers. Use the tools harder than anyone else so that when the right moment does come, one with a real moat, real defensibility, a problem that Anthropic or OpenAI cannot solve with a point release, you are the person who has been living on the bleeding edge long enough to see it clearly.

I built [CRONAI](https://github.com/forayconsulting/cronai) on a Friday morning in February 2025. I rebuilt it as [Maistro](https://github.com/forayconsulting/maistro) a week later. Thirteen months later, those same features are shipping across every major AI coding tool. I did not miss an opportunity. I spent those 13 months getting better at something more durable than any single product.

The dark forest rewards the ones who keep moving.
