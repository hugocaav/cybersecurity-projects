# 🛡️ Project 1 - Basic Honeypot

# Objective
Create a simple honeypot that listens on a specific port and logs all incoming connections for monitoring suspicious activity.

# Tools
- Python 3
- macOS Terminal
- `socket` module (built-in)

# Usage
Run the honeypot:
```bash
python3 honeypot.py

📚 Use Case
In real-world cybersecurity, honeypots are used to detect, study, and log malicious behavior from attackers. A system administrator might deploy a honeypot on unused ports to observe unauthorized scanning activity and gather forensic data for threat intelligence.

🧠 This simple TCP honeypot simulates a fake service that logs IP addresses attempting to connect, helping to understand how attackers examine networks and how logs are used in incident response.