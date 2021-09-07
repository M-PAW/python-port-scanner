import socket
import termcolor


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f" {port} - Open")
    except:
        print(f" {port} - Filtered / Closed")
