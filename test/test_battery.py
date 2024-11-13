import json

from src.app import app, system
from src.globals import API_ROOT, BATTERY_ALERT_THRESHOLD


def test_battery_empty():
    system.battery.store_energy(system.battery.max_capacity)
    system.battery.use_energy(system.battery.max_capacity)
    assert system.battery.charge_level == 0

    client = app.test_client()
    response = client.get(f"/{API_ROOT}/status")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["Status"] == "Battery is empty"


def test_battery_full():
    system.battery.store_energy(system.battery.max_capacity)
    system.battery.use_energy(system.battery.max_capacity)
    system.battery.store_energy(system.battery.max_capacity)
    assert system.battery.charge_level == system.battery.max_capacity

    client = app.test_client()
    response = client.get(f"/{API_ROOT}/status")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["Status"] == "Battery is full"


def test_battery_running_low():
    system.battery.store_energy(system.battery.max_capacity)
    system.battery.use_energy(system.battery.max_capacity - BATTERY_ALERT_THRESHOLD / 2)

    client = app.test_client()
    response = client.get(f"/{API_ROOT}/status")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["Status"] == "Battery is running low"


def test_no_alert():
    system.battery.store_energy(system.battery.max_capacity)
    system.battery.use_energy(system.battery.max_capacity / 2)

    client = app.test_client()
    response = client.get(f"/{API_ROOT}/status")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["Status"] == "No alert"
