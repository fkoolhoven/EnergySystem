from src.app import app
from src.globals import API_ROOT, BAD_REQUEST, NOT_FOUND, OK


def test_false_endpoint():
    client = app.test_client()
    response = client.get("/something")
    assert response.status_code == NOT_FOUND


def test_consumption_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/consumption")
    assert response.status_code == OK

    response = client.get(f"/{API_ROOT}/consumption?time=something")
    assert response.status_code == BAD_REQUEST


def test_production_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/production")
    assert response.status_code == OK

    response = client.get(f"/{API_ROOT}/production?time=something")
    assert response.status_code == BAD_REQUEST


def test_storage_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/storage")
    assert response.status_code == OK

    response = client.get(f"/{API_ROOT}/storage?time=something")
    assert response.status_code == BAD_REQUEST


def test_status_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/status")
    assert response.status_code == OK
