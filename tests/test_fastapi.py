from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_add():
    payload = {"num1": 21, "num2": 10}
    
    response = client.post("/add/", json=payload)  # ✅ POST request
    assert response.status_code == 200
    assert response.json() == {"result": 31 }



    response = client.post("/subtract/", json=payload)  # ✅ POST request
    assert response.status_code == 200
    assert response.json() == {"result": 11 }


    response = client.post("/multiply/", json=payload)  # ✅ POST request
    assert response.status_code == 200
    assert response.json() == {"result": 210 }

    response = client.post("/divide/", json=payload)  # ✅ POST request
    assert response.status_code == 200
    assert response.json() == {"result": 2.1 }

