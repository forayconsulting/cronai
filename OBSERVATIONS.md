# Scheduled AI Agents, the Dark Forest, and Why I Didn't Build a Product

Let me take you back thirteen months, to before Cursor Automations, before Codex Automations, before Claude Code's `/loop`, before any major AI tool had the concept of a scheduled agent. Back to February 2025, when the fanciest thing most people were doing with AI was copying and pasting ChatGPT output into their code editors.

I had a different problem. I did not want to sit with an AI agent. I wanted to hand it a list of things to do, set a timer, and walk away. Check for security vulnerabilities in my dependencies every morning. Summarize yesterday's commits before I sit down with coffee. Triage issues overnight. The kind of stuff that does not need me watching.

The problem was that nothing could do this. Every AI tool in February 2025 was interactive. You prompt, it responds, you iterate. The agent could not outlive the conversation.

So I built it myself. Twice.

## CRONAI and Maistro

The first version was CRONAI, built on February 28, 2025. A Flask web app I threw together in about 14 minutes. You wrote a list of plain-English instructions, picked a cron schedule from a dropdown, and it installed a crontab entry that piped your commands into a Goose session connected to MCP Servers. Goose was the only agent CLI that supported MCP at the time, and it was barely a month old itself. MCP was three months old. The whole stack was held together with duct tape and optimism.

It worked, but it was limited. Commands were just strings in a bash array. One model, one set of tools, no streaming, no visibility into what the agent was actually doing.

Seven days later I started over and built Maistro. Same idea, real architecture. Node.js with WebSocket streaming so I could watch the agent work in real time. Per-prompt MCP server selection, so each step in a workflow could use different tools. OpenRouter integration for switching models mid-sequence, because some prompts need a reasoning model and some just need speed. Configurations could trigger other configurations, chaining agent workflows together. REST API with Swagger docs. Docker with multi-arch builds. Aaron Bockelie jumped in within a week and contributed Docker improvements and API documentation.

The underlying idea never changed across either tool. Write prompts, pick your tools, set a schedule, let the agent work without you.

I used both tools through the spring and moved on to building other things: MCP servers for Zoom transcripts, Oracle NetSuite, Google Slides, Slack. A Cloudflare MCP deployment pattern. A Gemini CLI skill. An AI sandbox prototype. Fifty-seven repos over 13 months, most of them tools I built because I needed them and they did not exist yet. CRONAI and Maistro were just two of those.

## What the Industry Shipped After

Here is a compressed timeline of the 13 months between my utilities and today:

**Apr 2025**: OpenAI launches Codex CLI. Interactive only.

**May 2025**: Claude Code reaches GA. OpenAI launches cloud Codex. Cursor 0.50 ships Background Agents. All on-demand, not scheduled.

**Jun 2025**: Google launches Gemini CLI. Cursor 1.0.

**Sep 2025**: GitHub Copilot CLI in public preview. The terminal is a battleground, but everything still requires a human to kick it off.

**Dec 2025**: Claude Code ships async background subagents. MCP gets donated to the Linux Foundation's Agentic AI Foundation.

**Feb 2026**: OpenAI ships the Codex desktop app with **Automations**: instructions plus skills, running on a schedule. Results land in a review queue. Engineers use them for daily issue triage, summarizing CI failures, generating release briefs. GitHub Copilot CLI reaches GA.

**Mar 5, 2026**: Cursor launches **Automations**. Trigger-based AI agents that fire on cron schedules, GitHub PRs, Slack messages, Linear issues, PagerDuty alerts, webhooks.

**Mar 2026**: Anthropic ships `/loop` for Claude Code (v2.1.71). Cron-style scheduling that turns Claude Code into an autonomous background worker. Standard cron expressions. Up to 50 scheduled tasks per session. One headline: "Claude Code Gets Cron Scheduling to Run as a Background Worker."

**Mar 25, 2026** (today): A product called **CronBox** launches on Product Hunt. Tagline: "Cron for the AI age." The creator notes Claude Code's scheduling is "pretty restrictive" and built something more capable.

The features Maistro had in March 2025 (per-prompt model selection, per-prompt MCP server configuration, chained workflows, scheduled execution) are now shipping as headline features across Codex, Cursor, and Claude Code in Q1 2026.

## The Possibility Space

When I built these tools, the components barely existed. Goose was one month old. MCP was three months old. Claude Code was days old. There was no ecosystem of scheduled AI agent products because there was barely an ecosystem of AI agent CLIs.

I was working with the only tool that could plausibly do what I wanted (Goose with MCP), using the oldest job scheduler in Unix (cron), held together with Flask and then Node.js. The ceiling of what was possible was low. But the shape of the idea was right.

Now there are 15+ AI CLI coding tools. MCP has gone from a handful of reference servers to an industry standard donated to the Linux Foundation, with 8 million server downloads and 5,800+ servers. The autonomous AI agent market is estimated at $8.5 billion. And the specific feature that multiple billion-dollar companies chose to ship in Q1 2026 is: put an AI agent on a cron schedule and let it work.

## Why I Didn't Try to Sell It

I can hear someone reading this and thinking: "You should have productized that. You had a 13-month head start."

No. What I would have had, at absolute best, is a small startup getting one-shotted by a minor Anthropic feature release right now. Claude Code's `/loop` shipped as a point release. Not a product launch, not a keynote announcement. A point release. Cursor Automations? A beta toggle. These companies added "scheduled AI agents" the same way they add any feature: as a line item in a changelog. You cannot build a moat around a cron job.

Look at what happened to ClawdBot. Peter Steinberger built an open-source personal AI agent that went viral. 145,000 GitHub stars. Coverage in TechCrunch, CNBC, MacStories. Consulting businesses sprung up around it overnight. Then Anthropic sent a trademark complaint and he had to rename it. Twice. ClawdBot became Moltbot became OpenClaw, all within a few weeks. That project is still alive and useful, but the trajectory shows the problem clearly. When you build in the gravity well of a platform owner, you are one decision away from disruption, whether by feature parity or by legal letter.

CronBox launched on Product Hunt today. The founder noted that Claude Code's scheduling is "pretty restrictive." That may be true right now. It will not be true for long. Every limitation CronBox routes around is a feature request on Anthropic's backlog. The product thesis is a countdown timer.

Short-term thinking is product-based. Long-term thinking is capability-based.

What I actually did with those 13 months was keep using these tools. I built MCP servers before most people knew what MCP was. I was writing Zoom transcript MCPs, Oracle NetSuite MCPs, Google Slides MCPs, Cloudflare MCP deployment patterns, Gemini CLI skills, AI sandbox prototypes, and agent streaming implementations while the industry was still figuring out what "agentic" meant. CRONAI and Maistro were utilities in a larger practice of staying on the bleeding edge by building for myself, not for a market.

There are plenty of people like me. We build tools the day the APIs ship. We hit the walls before the docs exist. We write the workarounds that become next quarter's feature announcements. The instinct to productize is strong, but the math rarely works. The window between "too early for anyone to care" and "too late because the platform shipped it natively" is vanishingly small in AI right now.

## When to Actually Build a Product

The right time to jump in and build is when you have a defensible moat or a perfect moment. That means one of a few things: you have domain expertise in an industry that will never adopt AI without someone like you walking them through it. You have proprietary data or relationships that cannot be replicated by a feature release. You are solving a coordination problem between multiple vendors that none of them are incentivized to solve. Or you are building at a layer of the stack where the platform owners are not competing.

"I built the feature before they did" is not a moat. It is a signal that you understand the problem space, which is valuable, but not as a product. It is valuable as judgment. It is valuable as capability.

## The Dark Forest

The AI space is a dark forest. Every product you launch is a signal flare. If it works, it tells the platform owners exactly what to build next. If it goes viral, you are months away from being absorbed or outcompeted. If you pick a name too close to a trademark, you are weeks away from a legal notice.

The safe move is not to hide. It is to stay in motion. Build utilities, not products. Accumulate capability, not customers. Use the tools harder than anyone else so that when the right moment does arrive, a moment with a real moat, real defensibility, a problem that Anthropic or OpenAI cannot solve with a point release, you are the person who has been living in the future long enough to see it clearly.

I built CRONAI in 14 minutes on a Friday morning in February 2025. I rebuilt it as Maistro seven days later with model switching, MCP orchestration, and chained workflows. Thirteen months later, those same features are shipping across every major AI coding tool. I did not miss an opportunity. I spent those 13 months getting better at something more durable than any single product.

The dark forest rewards the ones who keep moving.
