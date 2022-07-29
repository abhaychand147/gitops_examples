from fastapi.testclient import TestClient
from api.fruit import app

client = TestClient(app)

def test_first_endpoint():
    response = client.get("/first")
    assert response.status_code == 200
    assert response.json() == {"First:API"}
