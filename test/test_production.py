import json

import pytest

from src.app import app
from src.globals import (
    API_ROOT,
    MAX_AIR_DENSITY,
    MAX_WIND_SPEED,
    MIN_AIR_DENSITY,
    MIN_WIND_SPEED,
    OK,
)
from src.system.production.wind_turbine import WindTurbine


@pytest.fixture
def expected_wind_turbine_production():
    wind_turbine = WindTurbine()
    swept_area = wind_turbine.calculate_swept_area()
    min_production = WindTurbine.calculate_production(
        MIN_AIR_DENSITY, swept_area, MIN_WIND_SPEED
    )
    max_production = WindTurbine.calculate_production(
        MAX_AIR_DENSITY, swept_area, MAX_WIND_SPEED
    )
    return min_production, max_production


@pytest.mark.parametrize("time", ["05:15", "12:59", "20:33"])
def test_wind_turbine_consumption(time, expected_wind_turbine_production):
    min_production, max_production = expected_wind_turbine_production
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/production?time={time}")
    assert response.status_code == OK
    data = json.loads(response.data)
    assert data["Wind Turbine"] >= min_production
    assert data["Wind Turbine"] <= max_production
