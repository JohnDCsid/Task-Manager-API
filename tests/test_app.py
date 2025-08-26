import json
import os
import pytest
from app import create_app




@pytest.fixture()
def client():
    app = create_app(testing=True)
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client




def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"




def test_create_and_list_tasks(client):
    # Create
    r = client.post("/tasks", data=json.dumps({"title": "Izlasīt grāmatu"}), content_type="application/json")
    assert r.status_code == 201
    body = r.get_json()
    assert body["title"] == "Izlasīt grāmatu"
    assert body["completed"] is False


    # List
    r = client.get("/tasks")
    assert r.status_code == 200
    items = r.get_json()
    assert isinstance(items, list)
    assert len(items) == 1




def test_complete_and_delete_task(client):
    # Create
    r = client.post("/tasks", json={"title": "Uzrakstīt testus"})
    task_id = r.get_json()["id"]
    
    
    # Complete
    r = client.put(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.get_json()["completed"] is True
    
    
    # Delete
    r = client.delete(f"/tasks/{task_id}")
    assert r.status_code == 204
    
    
    # Verify deletion
    r = client.get("/tasks")
    assert all(item["id"] != task_id for item in r.get_json())
    



def test_validation_missing_title(client):
    r = client.post("/tasks", json={})
    assert r.status_code == 400
    assert "title" in r.get_json()["error"]
