from mock_data import MOCK_MESSAGES
from pipeline import run_pipeline
from slack_bot import send_digest
from config import PROJECT_PHASE

def main():
    print(f"Running digest pipeline — project phase: {PROJECT_PHASE}\n")
    digests = run_pipeline(MOCK_MESSAGES, PROJECT_PHASE)
    for role, digest in digests.items():
        print(f"=== {role.replace('_', ' ').upper()} ===")
        print(digest)
        print()
        send_digest(role, digest)

if __name__ == "__main__":
    main()