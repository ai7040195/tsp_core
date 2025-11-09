import json

def load_user_profile():
    return {
        "id": "user_001",
        "email": "utente@example.com",
        "consent": True,
        "cognitive_metrics": {
            "flc": 4.0,
            "ler": 4.0,
            "ch": 3.0,
            "ilr": 3.0
        }
    }

