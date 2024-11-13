from src.app import app


def test_get():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, world!"
