from src.app import app
from src.globals import API_ROOT


def test_consumption_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/consumption")
    assert response.status_code == 200


def test_production_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/production")
    assert response.status_code == 200


def test_storage_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/storage")
    assert response.status_code == 200


def test_status_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/status")
    assert response.status_code == 200
