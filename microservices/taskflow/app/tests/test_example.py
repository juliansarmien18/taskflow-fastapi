from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_taskflow():
    response = client.post("/taskflow/", json={"name": "Test Taskflow", "description": "A taskflow for testing"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Taskflow"

def test_read_taskflow():
    response = client.post("/taskflow/", json={"name": "Test Taskflow", "description": "A taskflow for testing"})
    item_id = response.json()["id"]
    response = client.get(f"/taskflow/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Taskflow"

def test_update_taskflow():
    response = client.post("/taskflow/", json={"name": "Test Taskflow", "description": "A taskflow for testing"})
    item_id = response.json()["id"]
    response = client.put(f"/taskflow/{item_id}", json={"name": "Updated Taskflow", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Taskflow"

def test_delete_taskflow():
    response = client.post("/taskflow/", json={"name": "Test Taskflow", "description": "A taskflow for testing"})
    item_id = response.json()["id"]
    response = client.delete(f"/taskflow/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Taskflow"
