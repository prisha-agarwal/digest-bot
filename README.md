# Daily Digest Bot

A Slack bot that sends each member of a robotics hardware team a personalized daily digest — surfacing the most relevant updates from across all channels based on their role and current project phase.

## The Problem

Robotics hardware teams rely on Slack for day-to-day communication across mechanical engineering, electrical engineering, supply chain, product, and management. While effective for collaboration, this creates knowledge silos: important updates get buried in channel-specific threads, and critical cross-team dependencies go unnoticed until it's too late.

## What It Does

Instead of everyone manually monitoring every channel, each team member receives a morning DM with only what matters to them — prioritized by urgency and filtered by role.

The engineering manager's digest goes further: it surfaces cross-team connections that no individual would catch. For example, a supplier delay posted in `#supply-chain` and a tolerance failure posted in `#mech-eng` are separate conversations — but the bot recognizes they are the same crisis and connects them in a single digest.

## How It Works

The pipeline runs in four steps before the LLM is ever called:

1. **Ingest** — pulls messages across all Slack channels
2. **Score** — assigns urgency to each message based on reaction count, whether it was replied to, and whether it came from a manager
3. **Filter** — each role has a priority keyword map; messages are matched and ranked per role
4. **Contextualize** — the current project phase (prototyping / testing / pre-launch) is injected into the prompt, shifting what counts as critical

Only after these steps does the Claude API generate the personalized digest. This means the intelligence is in the pipeline, not just the prompt.

## Roles Supported

- Mechanical Engineer
- Electrical Engineer
- Supply Chain
- Engineering Manager
- Product Manager

## Project Structure

- `main.py` — runs the pipeline and sends digests
- `config.py` — role priority maps and project phase
- `mock_data.py` — simulated Slack messages across channels
- `pipeline.py` — urgency scoring, role filtering, digest generation
- `slack_bot.py` — sends personalized DMs via Slack SDK
- `.env` — API keys (not committed)

## Setup

1. Clone the repo and navigate into it
2. Install dependencies — `pip install anthropic slack-sdk python-dotenv`
3. Create a `.env` file with your `ANTHROPIC_API_KEY`, `SLACK_BOT_TOKEN`, and `SLACK_SIGNING_SECRET`
4. Add your Slack user ID to `slack_bot.py` under your role
5. Run with `python3 main.py`

## Changing the Project Phase

In `config.py`, update `PROJECT_PHASE` to one of:
- `"prototyping"` — design changes expected, delays low priority
- `"testing"` — hardware failures and spec deviations are highest priority  
- `"pre-launch"` — everything is critical, any blocker threatens the timeline

## What's Next

- Real Slack API integration to replace mock data with live messages
- User feedback loop — thumbs up/down on digest bullets to improve role filtering over time
- Manager dashboard to update project phase and tune role priority weights without touching code