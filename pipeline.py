import anthropic
from config import ROLE_PRIORITY_MAP, PHASE_CONTEXT, PROJECT_PHASE
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def score_urgency(message):
    score = 0
    if message["is_manager"]:
        score += 3
    if not message["replied"]:
        score += 2
    score += min(message["reactions"], 3)
    return score

def filter_for_role(messages, role):
    keywords = ROLE_PRIORITY_MAP[role]
    scored = []
    for msg in messages:
        text_lower = msg["text"].lower()
        keyword_match = any(k in text_lower for k in keywords)
        urgency = score_urgency(msg)
        if keyword_match or msg["is_manager"]:
            formatted = f"[#{msg['channel']}] {msg['user']}: {msg['text']}"
            scored.append((urgency, formatted))
    scored.sort(reverse=True)
    limit = 6 if role == "engineering_manager" else 5
    return [text for _, text in scored[:limit]]

def generate_digest(role, messages, phase):
    if not messages:
        return "Nothing urgent for you today."

    phase_context = PHASE_CONTEXT.get(phase, "")
    role_label = role.replace("_", " ").title()
    messages_text = "\n".join(f"- {m}" for m in messages)
    max_bullets = 5 if role == "engineering_manager" else 4

    prompt = f"""You are generating a daily Slack digest for a {role_label} on an AI software team.

Project phase context: {phase_context}

Relevant messages from today across all Slack channels:
{messages_text}

Write a concise digest with 2-{max_bullets} bullet points. Each bullet must follow this exact format:
[PRIORITY] #channel | Sender — one sentence summary of what they need to know or do

Where PRIORITY is one of: CRITICAL, HIGH, or MEDIUM
Where #channel is the Slack channel the message came from
Where Sender is the person who posted it

Important: explicitly surface information from channels this person might not normally monitor.
If two issues from different channels appear related (for example a data pipeline issue and a model accuracy drop), 
connect them explicitly in the relevant bullet.
Make each bullet directly actionable for a {role_label}. No intro text, just the bullets."""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def run_pipeline(messages, phase):
    digests = {}
    for role in ROLE_PRIORITY_MAP.keys():
        filtered = filter_for_role(messages, role)
        digest = generate_digest(role, filtered, phase)
        digests[role] = digest
    return digests
