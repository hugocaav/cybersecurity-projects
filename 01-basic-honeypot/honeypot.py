import socket
from datetime import datetime

# Configuration
HOST = '0.0.0.0' # Listen on all available network interfaces
PORT = 2222 # TCP port to monitor for incoming connections

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen()

print(f"[+] Honeypot is active and listening on port {PORT}")

try:
    while True:
        # Accept an incoming connection
        connection, address = server_socket.accept()

        # Log the connection details
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] Connection from {address[0]}:{address[1]}"
        print(log_entry)

        # Write the log to a file
        with open("connections.log", "a") as log_file:
            log_file.write(log_entry + "\n")

        # Close the connection
        connection.close()

except KeyboardInterrupt:
    print("\n[!] Honeypot stopped by user.")

finally:
    server_socket.close()
    print("[*] Socket closed.")