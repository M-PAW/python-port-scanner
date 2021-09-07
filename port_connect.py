import socket
import termcolor

def port_connect(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        termcolor.cprint(f" [+] Port {port} - Open", 'green')
        socket.close()
    except:
        termcolor.cprint(f" [-] Port {port} - Filtered / Closed", 'red')
