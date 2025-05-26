#!/usr/bin/env python3

import socket
import re
import ipaddress

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"\n[+] Local IP Address Detected: {local_ip}")

network = ipaddress.ip_network(local_ip + '/24', strict=False)
print(f"[+] Scanning IP range: {network}\n")

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
while True:
    print("Enter the range of ports to scan in format: <int>-<int> (ex. 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

open_results = []

for ip in network.hosts():
    print(f"\n[>] Scanning host: {ip}")
    open_ports = []
    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((str(ip), port))
                print(f"[+] Port {port} is OPEN on {ip}")
                open_ports.append(port)
        except:
            print(f"[-] Port {port} is closed on {ip}")

    if open_ports:
        open_results.append((str(ip), open_ports))

with open("scan_result.txt", "w") as f:
    for ip, ports in open_results:
        for port in ports:
            f.write(f"{ip}: Port {port} is OPEN\n")

if not open_results:
    with open("scan_result.txt", "w") as f:
        f.write("No open ports found in the scanned range.\n")


print("\n[✓] Scan complete. Results saved to scan_result.txt")
