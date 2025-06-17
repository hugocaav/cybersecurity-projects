# 🛡️ Hugo's CyberSecurity Lab

> Hands-on cybersecurity portfolio with practical projects, from beginner to advanced.

---

## 👨‍💻 About Me

I'm Hugo Cabrera, a Computer Science student passionate about cybersecurity, cloud engineering, and software development. I learn best by building real things. This lab documents my journey from zero to specialist through 70 practical projects.

---

## 🗺️ Project Roadmap

| Project # | Title                              | Status | Link |
|-----------|------------------------------------|--------|------|
| 01        | Basic Honeypot                     | ✅ Done | [View](./beginner/01-basic-honeypot) |
| 02        | Network Sniffer                    | ✅ Done | [View](./beginner/02-network-sniffer) |
| 03        | File Encryption with Python        | ✅ Done | [View](./beginner/03-file-encryption) |
| 04        | (Coming Soon)                      | ⬜ To Do | - |

> 🔧 This list will grow weekly.

---

## 🧠 Technologies Used

- Python 3
- Scapy
- cryptography (Fernet)
- Linux/macOS Terminal
- Git & GitHub

---

## 📚 Use Cases (Why This Matters)

Each project simulates real-world use cases:

- ✅ **Honeypot**: Monitor attack attempts on fake services
- ✅ **Sniffer**: Analyze suspicious traffic or inspect protocols
- ✅ **File encryption**: Secure sensitive data before transmission or storage

This proves I can build, explain, and apply core security concepts.

---

## 🔐 Security-Aware Practices

- `.gitignore` added to exclude private files:
  
  ```
  *.key
  *.enc
  decrypted_*
  __pycache__/
  connections.log
  ```
- Avoid uploading real IP addresses or logs
- README files include ethical and legal disclaimers where needed

## 📥 Setup Instructions (for any project)

```bash
# Clone the repo
git clone git@github.com:hugocaav/cybersecurity-projects.git
cd cybersecurity-projects

# Navigate to a project
cd beginner/02-network-sniffer

# Install dependencies
pip3 install -r requirements.txt

# Run the script
python3 sniffer.py
```

> Optional: Some projects require `sudo` access (e.g., packet sniffers).

---

## 📌 Notes

This portfolio is public to share my learning journey, connect with recruiters, and prove hands-on skill. All code is original or modified from trusted sources, and credited where applicable.

> Want to collaborate or offer feedback? Reach out on [LinkedIn](https://linkedin.com/in/hugoecaav) or [GitHub](https://github.com/hugocaav).

---

## 🔄 Coming Next

- [ ] DNS Spoofing
- [ ] Web Vulnerability Scanner
- [ ] Malware Sandbox
