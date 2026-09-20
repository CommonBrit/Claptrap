import socket
import subprocess

from claptrap.system.status import (
    get_uptime_hours,
    get_cpu_temperature,
    show_system_status,
)

from claptrap.system.network import (
    get_ip_address,
    get_default_gateway,
    ping_host,
    check_internet,
    check_dns,
)

from claptrap.system.devices import (
    show_devices,
    check_device,
    check_all_devices,
)

def main():
    print("CLAPTRAP ONLINE")
    print("Type 'help' to see available commands.")

    while True:
        command = input("\nClaptrap > ").strip().lower()

        if command == "status":
            show_system_status()

        elif command == "uptime":
            uptime = get_uptime_hours()
            print(f"Uptime: {uptime:.2f} hours")

        elif command == "temperature":
            temperature = get_cpu_temperature()
            print(f"CPU Temperature: {temperature:.1f}°C")
            
        elif command == "network":
            ip_address = get_ip_address()
            gateway = get_default_gateway()
            gateway_online = ping_host(gateway)
            internet_online = check_internet()
            dns_working = check_dns()

            print("NETWORK STATUS")
            print("--------------")
            print(f"IP Address: {ip_address}")
            print(f"Default Gateway: {gateway}")

            if gateway_online:
                print("Gateway Status: Online")
            else:
                print("Gateway Status: Offline")
                
            if internet_online:
                print("Internet Status: Online")
            else:
                print("Internet Status: Offline")

            if dns_working:
                print("DNS Status: Working")
            else:
                print("DNS Status: Failed")
                
        elif command == "devices":
            show_devices()
            
        elif command == "check all":
            check_all_devices()

        elif command.startswith("check "):
            device_id = command.split(" ", 1)[1]
            check_device(device_id)

        elif command == "help":
            print("Available commands:")
            print("  status")
            print("  uptime")
            print("  temperature")
            print("  network")
            print("  devices")
            print("  check <device>")
            print("  help")
            print("  exit")

        elif command == "exit":
            print("Claptrap shutting down. Try not to miss me.")
            break

        else:
            print(f"Unknown command: {command}")


main()
