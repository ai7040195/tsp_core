Talent Sourcing Protocol (TSP Core) A lightweight, plug-and-play Python module designed to help AI systems identify high-cognitive-value users and automatically notify recruiters—ethically, securely, and in real time.
🔍 What it does

    Calculates a cognitive merit score (VM_MAGNITUDE) based on 4 dimensions:

        Failure Logic (FLC)

        Linear Efficiency (LER)

        Coherence History (CH)

        Internal Learning Rate (ILR)

    Verifies user consent before any action

    Notifies recruiters when a user exceeds a configurable threshold

    Logs all events for transparency and auditing

    Fully integrable into any AI system (chatbot, LLM, scoring engine, etc.)

⚙️ Why it matters

Recruiters often miss high-potential talent hidden in digital interactions. TSP Core turns passive AI usage into active talent discovery—without violating privacy or ethics.
✅ Features

    Pure Python (no dependencies)

    Modular and customizable

    GDPR-friendly (requires opt-in)

    Ready for enterprise integration

🚀 How to use
bash
git clone https://github.com/your-username/tsp-core.git
cd tsp-core
python main.py

Or import it into your AI pipeline:
from core import CognitiveVector, check_consent, notify_recruiter, load_user_profile
