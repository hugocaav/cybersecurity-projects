# 🕵️ Project 02 - Network Sniffer with Scapy

## 🎯 Objective
Capture live network packets and display basic metadata (IP source, destination, and protocol). Simulates functionality of tools like Wireshark.

---

## 🛠 Tools Used
- Python 3
- Scapy library (`pip install scapy`)

---

## 🚀 How to Run
```bash
python3 sniffer.py
```

Optionally, run with elevated permissions:
```bash
sudo python3 sniffer.py
```

---

## 📚 Use Case
Network sniffers are used by SOC analysts, penetration testers, and threat hunters to inspect live traffic for anomalies or malware behavior. They're vital for detecting suspicious activity on enterprise or personal networks.

> 🧠 This script teaches how to inspect packets at a basic level, see live traffic, and recognize real-time IP communication patterns.

---

## 📸 Sample Output
```
[2025-06-17 11:53:04] TCP Packet: 172.19.30.104 --> 34.117.41.85
[2025-06-17 11:53:05] UDP Packet: 172.18.15.253 --> 8.8.8.8
```

---

## ⚠️ Legal Reminder
Only sniff traffic on networks you own or are permitted to monitor. Capturing third-party traffic without consent is illegal.

---