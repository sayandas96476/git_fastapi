from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_item():
    payload = {"num1": 2, "num2": 3}
    
    response = client.post("/add/", json=payload)  # ✅ POST request
    assert response.status_code == 200
    assert response.json() == {"result": 5 }
