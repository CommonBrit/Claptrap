from claptrap.system.network import ping_host

DEVICES = {
    "router": {
        "name": "Home Router",
        "ip": "192.168.1.1",
        "type": "Network"
    },
    "claptrap": {
        "name": "Claptrap",
        "ip": "192.168.1.123",
        "type": "Raspberry Pi"
    }
}


def show_devices():
    print("KNOWN DEVICES")
    print("-------------")

    for device_id, device in DEVICES.items():
        print(
            f"{device_id}: "
            f"{device['name']} - "
            f"{device['ip']} - "
            f"{device['type']}"
        )
        
        
def check_device(device_id):
    device = DEVICES.get(device_id)

    if device is None:
        print(f"Unknown device: {device_id}")
        return

    online = ping_host(device["ip"])

    if online:
        status = "Online"
    else:
        status = "Offline"

    print(f"{device['name']} ({device['ip']}): {status}")
    
    
def check_all_devices():
    print("DEVICE HEALTH")
    print("-------------")

    for device_id, device in DEVICES.items():
        online = ping_host(device["ip"])

        if online:
            status = "Online"
        else:
            status = "Offline"

        print(f"{device['name']} ({device['ip']}): {status}")
        
        
def get_device_health():
    device_health = []

    for device_id, device in DEVICES.items():
        device_health.append({
            "id": device_id,
            "name": device["name"],
            "ip": device["ip"],
            "type": device["type"],
            "online": ping_host(device["ip"]),
        })

    return device_health