# I Built a Cron Job for AI Agents 13 Months Before Everyone Else Did

On February 28, 2025, I spent about 14 minutes building a tool called CRONAI. It was a Friday morning. I wrote a Flask web app with a sidebar of named configurations, a cron schedule picker, and a shell script that piped natural-language commands into the Goose CLI to run AI agent sessions on a recurring schedule via MCP Servers. I pushed 21 commits, closed my laptop, and moved on.

I genuinely forgot about it until this week.

## What I Actually Built

The idea was simple. I wanted to write a list of instructions in plain English, attach a cron schedule, and have an AI agent wake up and do the work without me. The example config I shipped had commands like "Generate a daily summary of yesterday's activities" and "Check for security vulnerabilities in our dependencies." You'd pick a schedule from a dropdown (every 10 minutes, hourly, daily, weekly), hit save, and the system would install a crontab entry pointing at a bash script that piped your commands into a Goose session connected to MCP Servers.

That was the whole thing. A web UI for managing scheduled AI agent jobs.

## What Existed When I Built It

February 2025 was a weird moment for AI tooling. Here's what the landscape looked like:

- **Aider** was the main open-source CLI coding tool, focused on pair programming with git integration. It had been around since mid-2023.
- **Goose** (Block/Square) had just launched in January 2025, one month earlier. It was new, open source, and supported MCP Servers for extensibility. This is what I built CRONAI around.
- **Claude Code** launched that same month (February 2025) as a research preview. It was brand new and limited.
- **Cursor** existed as an IDE, but had no agent mode, no background agents, no CLI, nothing autonomous.
- **MCP (Model Context Protocol)** was about three months old. Anthropic had open-sourced it in November 2024. Adoption was thin. A handful of reference servers existed for GitHub, Slack, Postgres.
- **Copilot** was autocomplete in your editor. No agent mode. No CLI.
- **OpenAI Codex** (the agent, not the old code completion model) did not exist yet.

Andrej Karpathy coined "vibe coding" that same month. The conversation was about whether AI could write code at all, not about whether it could run autonomously on a schedule. Nobody was talking about scheduled AI agents as a product category.

The tools that existed were interactive. You sat with them. You prompted, they responded, you iterated. The idea of writing instructions, setting a timer, and walking away was not part of the conversation.

## What Happened After

Here is a timeline of what the industry shipped in the 13 months between my prototype and today:

**April 2025**: OpenAI launches Codex CLI, an open-source terminal coding agent. Interactive only.

**May 2025**: Claude Code reaches general availability alongside Claude 4. OpenAI launches cloud-based Codex as a research preview. Cursor ships version 0.50 with Background Agents, allowing parallel task execution. All of these are on-demand, not scheduled.

**June 2025**: Google launches Gemini CLI. Another terminal agent, another interactive tool.

**September 2025**: GitHub Copilot CLI launches in public preview. Amazon Q Developer CLI has been around since March. The terminal is now an AI battleground, but everything still requires a human to start it.

**October 2025**: OpenAI ships Codex GA with Slack integration. Claude Code launches on the web.

**December 2025**: Claude Code ships async background subagents (v2.0.60). Agents can now be spawned and left to run while you do other things. This is getting closer.

**February 2026**: GitHub Copilot CLI reaches general availability. OpenAI ships the Codex desktop app with a feature called **Automations**: instructions plus optional skills, running on a schedule you define. When an Automation finishes, results land in a review queue. OpenAI engineers use them for daily issue triage, summarizing CI failures, and generating release briefs.

**March 5, 2026**: Cursor launches **Automations**. Trigger-based AI agents that fire on GitHub PRs, Slack messages, Linear issues, PagerDuty alerts, cron schedules, and webhooks. Each agent spins up in an isolated cloud sandbox, follows instructions, executes the task, and verifies its own output.

**March 2026**: Anthropic ships the `/loop` command for Claude Code (v2.1.71). Cron-style scheduling that turns Claude Code into an autonomous background worker. Standard cron expressions. Local timezone. Up to 50 scheduled tasks per session. The headline from one outlet: "Claude Code Gets Cron Scheduling to Run as a Background Worker."

**March 25, 2026** (today): A product called **CronBox** launches on Product Hunt. Its tagline is "Cron for the AI age." Schedule AI agent jobs in the cloud. Each agent gets an ephemeral sandbox. The creator notes that Claude Code's scheduling is "pretty restrictive" and built CronBox to do more. The name is almost identical to mine.

## The Possibility Space I Was Working In

This is the part I find interesting. When I built CRONAI, the components I needed barely existed. Goose was one month old. MCP was three months old. Claude Code was days old. There was no ecosystem of scheduled AI agent products because there was barely an ecosystem of AI agent CLIs.

I was working with the only tool that could plausibly do what I wanted (Goose with MCP), using the oldest job scheduler in Unix (cron), glued together with a Flask app I could build in minutes. The ceiling of what was possible was low. But the shape of the idea was right.

Now there are at least 15 AI CLI coding tools. The autonomous AI agent market is estimated at $8.5 billion in 2026. Gartner says 33% of enterprise software will include agentic AI by 2028. MCP has gone from a handful of reference servers to an industry standard with an enterprise readiness roadmap. Devin, the autonomous coding agent, is valued at $4 billion. Goldman Sachs is running AI agents alongside 12,000 human developers.

And the specific feature that multiple billion-dollar companies shipped in Q1 2026, the thing that made headlines, is: put an AI agent on a cron schedule and let it work.

## What I Think This Means

I am not claiming I invented anything. Cron has existed since 1975. AI agents existed before February 2025. Putting them together is not a breakthrough. It is a straightforward combination of two obvious things.

But that is sort of the point. The idea was obvious to me 13 months before it was obvious to the companies building these tools. Not because I am smarter, but because I was a user with a specific need and no patience. I did not want to sit with an AI agent. I wanted to hand it a list of things to do and come back later. The simplest version of that is a cron job.

The gap between my prototype and what shipped this month is not conceptual. It is operational. The industry added sandboxing, cloud execution, credential management, review queues, and a lot of polish. The core loop is the same: define instructions, set a schedule, let the agent run, review the results.

I think there is a pattern here that goes beyond this specific tool. When you are a practitioner who uses AI tools every day, you bump into the walls of what is possible before the people building the tools do. You build ugly workarounds. Those workarounds sometimes turn out to be the next feature that ships in the product you were working around.

The 14 minutes I spent on CRONAI were not wasted. They were just early.
