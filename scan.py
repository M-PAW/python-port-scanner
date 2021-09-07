import termcolor
from port_connect import port_connect

def scan(target, ports):
    print(f"\n [+] Starting Scan... \n [+] {target}...")
    for port in range(1, ports+1):
        port_connect(target, port)

