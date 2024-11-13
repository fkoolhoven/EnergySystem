import json

import pytest

from src.app import app
from src.globals import API_ROOT, OK
from src.system.battery import Battery


@pytest.fixture
def expected_battery_charge_level():
    battery = Battery()
    return {
        "05:15": battery.__getattribute__("max_capacity"),
        "12:59": battery.__getattribute__("max_capacity"),
        "20:33": battery.__getattribute__("max_capacity"),
    }


@pytest.mark.parametrize("time", ["05:15", "12:59", "20:33"])
def test_battery_charge_level(time, expected_battery_charge_level):
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/storage?time={time}")
    assert response.status_code == OK
    data = json.loads(response.data)
    assert data["Battery"] == expected_battery_charge_level[time]