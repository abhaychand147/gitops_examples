from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_first_endpoint():
    response = client.get("/first")
    assert response.status_code == 200
    assert response.json() == {"First:API"}
    
    
def test_second_endpoint():
    response = client.get("/second")
    assert response.status_code == 200
    assert response.json() == {"second":"api"}
