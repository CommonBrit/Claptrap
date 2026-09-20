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


def get_system_status():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "architecture": platform.machine(),
        "uptime": get_uptime_hours(),
        "memory": memory.percent,
        "disk": disk.percent,
        "temperature": get_cpu_temperature(),
    }


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