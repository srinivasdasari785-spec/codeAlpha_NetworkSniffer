from scapy.all import *

def packet_callback(packet):
    print("\n--- Packet Captured ---")
    
    if packet.haslayer(IP):
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")

    if packet.haslayer(TCP):
        print("Protocol: TCP")

    elif packet.haslayer(UDP):
        print("Protocol: UDP")

    elif packet.haslayer(ICMP):
        print("Protocol: ICMP")

    if packet.haslayer(Raw):
        print(f"Payload: {packet[Raw].load}")

# Start sniffing
print("Starting packet capture...")
sniff(prn=packet_callback, store=False)