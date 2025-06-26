---
# 🧨 Project 04 – DNS Spoofing Awareness Tool

## 🎯 Objective
Simulate DNS traffic monitoring to understand how DNS spoofing works and how attackers may redirect traffic to malicious sites.

---

## 🛠 Tools Used
- Python 3
- Scapy (`pip install scapy`)

---

## 🚀 How to Run
```bash
sudo python3 dns_simulator.py
```

Open a browser and visit a site (e.g., `https://example.com`) to generate DNS traffic.

---

## 📚 Use Case
DNS spoofing is a common method used by attackers to redirect users to fake websites by altering DNS responses. This project helps you understand how a network sniffer can monitor DNS queries to detect suspicious behavior.

> 🧠 This tool captures DNS requests and displays the domains being queried along with the source IP address. It's a safe simulation that builds awareness of DNS-based threats.

---

## 📸 Sample Output
```
[+] Monitoring DNS requests... (Press Ctrl+C to stop)
[!] DNS Request Detected:
    Domain: example.com.
    Source IP: 192.168.1.10
```

---

## ⚠️ Ethical Notice
Only run this tool on networks you own or are explicitly authorized to monitor.

---