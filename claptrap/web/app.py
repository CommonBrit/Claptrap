from flask import Flask, render_template, jsonify

from claptrap.system.status import get_system_status
from claptrap.system.network import get_network_status
from claptrap.system.devices import get_device_health

app = Flask(__name__)


@app.route("/")
def home():
    status = get_system_status()
    network = get_network_status()
    devices = get_device_health()

    return render_template(
        "dashboard.html",
        status=status,
        network=network,
        devices=devices,
    )
    
@app.route("/api/status")
def api_status():
    status = get_system_status()
    network = get_network_status()
    devices = get_device_health()

    return jsonify({
        "system": status,
        "network": network,
        "devices": devices,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)