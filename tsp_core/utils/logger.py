import time
import json

def log_event(message: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            log_file = config.get("log_file", "tsp_log.txt")
    except Exception:
        log_file = "tsp_log.txt"

    with open(log_file, "a") as log:
        log.write(log_entry)

