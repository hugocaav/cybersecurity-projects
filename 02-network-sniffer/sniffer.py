from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def process_packet(packet):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Default protocol
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        print(f"[{timestamp}] {protocol} Packet: {ip_src} --> {ip_dst}")

# Start sniffing
print("[+] Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False)