import socket
from datetime import datetime

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 2222        # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Honeypot listening on port {PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            log = f"[{datetime.now()}] Connection from {addr[0]}:{addr[1]}\n"
            print(log.strip())
            with open("connections.log", "a") as file:
                file.write(log)
