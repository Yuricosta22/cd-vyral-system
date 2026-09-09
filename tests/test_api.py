from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "cd-vyral-system"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_dashboard_summary():
    response = client.get("/dashboard")
    assert response.status_code == 200
    payload = response.json()
    assert "total_leads" in payload
    assert "active_tasks" in payload
    assert "conversion_rate" in payload


def test_create_and_list_leads():
    payload = {
        "full_name": "Ana Souza",
        "email": "ana@example.com",
        "status": "new",
        "source": "Instagram",
    }
    create = client.post("/leads", json=payload)
    assert create.status_code == 201
    body = create.json()
    assert body["full_name"] == payload["full_name"]

    list_response = client.get("/leads")
    assert list_response.status_code == 200
    assert any(item["email"] == payload["email"] for item in list_response.json())


def test_create_and_list_tasks():
    payload = {
        "title": "Follow-up para Ana",
        "assigned_to": "Equipe Vendas",
        "status": "pending",
    }
    create = client.post("/tasks", json=payload)
    assert create.status_code == 201
    body = create.json()
    assert body["title"] == payload["title"]

    list_response = client.get("/tasks")
    assert list_response.status_code == 200
    assert any(item["title"] == payload["title"] for item in list_response.json())
