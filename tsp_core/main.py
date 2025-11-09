import json
from core.evaluator import CognitiveVector
from core.consent import check_consent
from core.notifier import notify_recruiter
from core.user import load_user_profile
from utils.logger import log_event

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    user = load_user_profile()

    vector = CognitiveVector(**user["cognitive_metrics"])
    vm = vector.magnitude()

    log_event(f"User {user['id']} VM_MAGNITUDE: {vm}")

    if vm >= config["vm_threshold"] and check_consent(user):
        notify_recruiter(user, vm, config)
        log_event(f"User {user['id']} notified to recruiter.")

if __name__ == "__main__":
    main()

