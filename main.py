from scan import scan
def main():
    targets = input(" [+] Enter Targets To Scan: ")
    ports = int(input(" [+] Enter Number Or Ports To Scan: "))

    if ',' in targets:
        print(" [+] Scanning Muliple Targets...")
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), ports)
    else:
        scan(targets, ports)

main()