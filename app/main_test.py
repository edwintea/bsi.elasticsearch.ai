from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_book():
    response = client.get("/media/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Only test",
        "author": "Edwin Warming Gunawan",
        "availability": True
    }