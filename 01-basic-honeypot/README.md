# 🛡️ Project 01 - Basic Honeypot

## 🎯 Objective
Create a simple honeypot that listens on a specific port and logs all incoming connections for monitoring suspicious activity.

---

## 🛠 Tools Used
- Python 3
- macOS/Linux Terminal
- Built-in `socket` module

---

## 🚀 How to Run
```bash
python3 honeypot.py
```

Logs will be saved in `connections.log` with timestamps and source IP addresses.

---

## 📚 Use Case
In real-world cybersecurity, honeypots are used to detect, study, and log malicious behavior from attackers. A system administrator might deploy a honeypot on unused ports to observe unauthorized scanning activity and gather forensic data for threat intelligence.

> 🧠 This simple TCP honeypot simulates a fake service that logs IP addresses attempting to connect, helping you understand how attackers examine networks and how logs are used in incident response.

---

## 📸 Sample Output
```
[+] Honeypot listening on port 2222
[2025-06-17 10:24:01] Connection from 192.168.1.5:45623
```

---

## ⚠️ Ethical Notice
Use honeypots only on systems and networks you are authorized to monitor.

---