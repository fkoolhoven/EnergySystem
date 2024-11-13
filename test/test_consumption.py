import json

import pytest

from src.app import app
from src.globals import API_ROOT, OK
from src.system.consumption.refrigerator import Refrigerator


@pytest.fixture
def expected_refrigerator_consumption():
    refrigerator = Refrigerator()
    return {
        "05:15": refrigerator.__getattribute__("consumption"),
        "12:59": refrigerator.__getattribute__("consumption"),
        "20:33": refrigerator.__getattribute__("consumption"),
    }


@pytest.mark.parametrize("time", ["05:15", "12:59", "20:33"])
def test_refrigerator_consumption(time, expected_refrigerator_consumption):
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/consumption?time={time}")
    assert response.status_code == OK
    data = json.loads(response.data)
    assert data["Refrigerator"] == expected_refrigerator_consumption[time]
