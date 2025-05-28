import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_todo(client):
    response = client.post("/todos", json={"title": "Test tâche"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test tâche"
    assert data["done"] == False

def test_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_mark_done(client):
    # Créer une tâche d'abord
    client.post("/todos", json={"title": "À faire"})
    response = client.put("/todos/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["done"] == True

def test_delete_todo(client):
    # Créer une tâche d'abord
    client.post("/todos", json={"title": "À supprimer"})
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Tâche supprimée"
