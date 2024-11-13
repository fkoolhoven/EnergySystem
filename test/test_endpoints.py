from src.app import app
from src.globals import API_ROOT


def test_consumption_endpoint():
    client = app.test_client()
    response = client.get(f"/{API_ROOT}/consumption")
    assert response.status_code == 200
