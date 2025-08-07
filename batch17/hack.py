import subprocess
import socket

# Range of ports to scan (you can customize this)
port_range = range(20, 1025)

# Timeout for socket connections (in seconds)
socket_timeout = 10

for x in range(1, 13):  # 192.168.1.1 to 192.168.1.12
    ip = f"192.168.1.{x}"
    print(f"\nPinging {ip}...")

    # Cross-platform ping
    try:
        result = subprocess.run(["ping", "-n", "1", ip], stdout=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        continue

    if result.returncode == 0:
        print(f"{ip} is up. Scanning ports...")
        open_ports = []

        for port in port_range:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(socket_timeout)
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)

        if open_ports:
            print(f"Open ports on {ip}: {open_ports}")
        else:
            print(f"No open ports found on {ip}.")
    else:
        print(f"{ip} is down or not responding.")
