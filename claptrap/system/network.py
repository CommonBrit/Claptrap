import socket
import subprocess

def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def get_default_gateway():
    result = subprocess.run(
        ["ip", "route"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.splitlines():
        if line.startswith("default"):
            return line.split()[2]

    return "Unknown"


def ping_host(host):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        capture_output=True,
        text=True
    )

    return result.returncode == 0


def check_internet():
    return ping_host("1.1.1.1")


def check_dns():
    try:
        socket.gethostbyname("example.com")
        return True
    except socket.gaierror:
        return False
    
    
def get_network_status():
    ip_address = get_ip_address()
    gateway = get_default_gateway()

    return {
        "ip": ip_address,
        "gateway": gateway,
        "gateway_online": ping_host(gateway),
        "internet_online": check_internet(),
        "dns_working": check_dns(),
    }