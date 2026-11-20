"""Unit-тесты для API пользователей.

TestClient из fastapi.testclient использует httpx под капотом —
поэтому в workflow устанавливается пакет httpx.
"""

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_existed_user():
    """Существующий пользователь возвращается с кодом 200 и верными данными."""
    response = client.get("/users/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_get_not_existed_user():
    """Несуществующий пользователь даёт 404."""
    response = client.get("/users/999")

    assert response.status_code == 404


def test_health_check():
    """Корневой эндпоинт отвечает, что сервис жив."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
