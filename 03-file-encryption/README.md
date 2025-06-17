# 🔐 Project 03 – File Encryption with Python (Fernet)

## 🎯 Objective
Encrypt and decrypt text files using symmetric encryption to demonstrate basic cryptography principles and the importance of key management.

---

## 🛠 Tools Used
- Python 3
- `cryptography` package (Fernet)

Install dependencies:
```bash
pip3 install cryptography
```

---

## 🚀 How to Run
```bash
python3 encryptor.py
```

This will:
- Generate a key (`key.key`)
- Encrypt `secret.txt` → creates `secret.txt.enc`
- Decrypt the encrypted file → creates `decrypted_secret.txt`

---

## 📚 Use Case
Encryption is essential for protecting sensitive data at rest or in transit. Organizations use tools like this to encrypt logs, personal data, or confidential files before storage or transfer.

> 🧠 This project shows how to build a working encryption/decryption tool using Fernet (which applies AES + HMAC) and explains the importance of securely handling keys.

---

## 📸 Example Output
```
Encrypted: secret.txt → secret.txt.enc
Decrypted: secret.txt.enc → decrypted_secret.txt
```

---

## ⚠️ Security Advice
Never share your `key.key` file publicly. Anyone with the key can decrypt your data. Add these lines to `.gitignore`:
```
*.key
*.enc
decrypted_*
```

---