from scapy.all import sniff, DNS, DNSQR, IP

# Callback function that runs when a packet is captured
def process_packet(packet):
    # Check if it's a DNS request (qr == 0)
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        print(f"[!] DNS Request Detected:")
        # Print the domain being queried
        print(f"    Domain: {packet[DNSQR].qname.decode('utf-8')}")
        # Print the source IP address of the request
        print(f"    Source IP: {packet[IP].src}")

# Start sniffing DNS traffic on port 53 (UDP)
print("[+] Monitoring DNS requests... (Press Ctrl+C to stop)")
sniff(filter="udp port 53", prn=process_packet, store=False)