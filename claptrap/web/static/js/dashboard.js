function updateStatus(elementId, online, onlineText = "Online", offlineText = "Offline") {
    const element = document.getElementById(elementId);

    if (!element) {
        return;
    }

    if (online) {
        element.className = "status-good";
        element.innerHTML =
            '<span class="status-dot online"></span>' + onlineText;
    } else {
        element.className = "status-bad";
        element.innerHTML =
            '<span class="status-dot offline"></span>' + offlineText;
    }
}

async function updateDashboard() {
    try {
        const response = await fetch("/api/status");
        const data = await response.json();

        document.getElementById("cpu-temperature").textContent =
            data.system.temperature.toFixed(1) + "°C";

        document.getElementById("memory-usage").textContent =
            data.system.memory + "%";

        document.getElementById("disk-usage").textContent =
            data.system.disk + "%";

        document.getElementById("uptime").textContent =
            data.system.uptime.toFixed(2);

        updateStatus(
            "gateway-status",
            data.network.gateway_online
        );

        updateStatus(
            "internet-status",
            data.network.internet_online
        );

        updateStatus(
            "dns-status",
            data.network.dns_working,
            "Working",
            "Failed"
        );

        data.devices.forEach(device => {
            updateStatus(
                "device-status-" + device.id,
                device.online
            );
        });

    } catch (error) {
        console.error("Failed to update dashboard:", error);
    }
}

setInterval(updateDashboard, 5000);