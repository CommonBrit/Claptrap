import socket
import platform
import psutil


def get_uptime_hours():
    with open("/proc/uptime", "r") as file:
        uptime_seconds = float(file.readline().split()[0])

    return uptime_seconds / 3600


def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temperature = float(file.read()) / 1000

    return temperature


def show_system_status():
    hostname = socket.gethostname()
    operating_system = platform.system()
    architecture = platform.machine()

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    uptime = get_uptime_hours()
    cpu_temp = get_cpu_temperature()

    print("CLAPTRAP SYSTEM STATUS")
    print("----------------------")
    print(f"Hostname: {hostname}")
    print(f"Operating System: {operating_system}")
    print(f"Architecture: {architecture}")
    print(f"Uptime: {uptime:.2f} hours")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")
    print(f"CPU Temperature: {cpu_temp:.1f}°C")


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

        elif command == "help":
            print("Available commands:")
            print("  status")
            print("  uptime")
            print("  temperature")
            print("  help")
            print("  exit")

        elif command == "exit":
            print("Claptrap shutting down. Try not to miss me.")
            break

        else:
            print(f"Unknown command: {command}")


main()
