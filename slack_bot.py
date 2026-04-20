from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

ROLE_TO_SLACK_USER = {
    "mechanical_engineer": "U0AUBSK82SV",
    "electrical_engineer": "U_ELEC_ID",
    "supply_chain": "U_SUPPLY_ID",
    "engineering_manager": "U0AU1H2K6JG",
    "product_manager": "U_PM_ID"
}

def send_digest(role, digest_text):
    user_id = ROLE_TO_SLACK_USER.get(role)
    if not user_id or user_id.startswith("U_"):
        print(f"[SKIP] No real user ID for {role}, printing instead:\n{digest_text}\n")
        return
    try:
        dm = client.conversations_open(users=user_id)
        channel_id = dm["channel"]["id"]
        role_label = role.replace("_", " ").title()
        client.chat_postMessage(
            channel=channel_id,
            text=f"*Your Daily Digest — {role_label}*\n\n{digest_text}"
        )
        print(f"[SENT] Digest sent to {role}")
    except SlackApiError as e:
        print(f"[ERROR] {e.response['error']}")
