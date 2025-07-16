from app.main import app
from fastapi.testclient import TestClient


def test_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 404  # No /health endpoint yet, placeholder
