import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_info_endpoint(client):
    """Teste 1: Validação do endpoint principal de informação."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["service_name"] == "Internal Service Info Desk"
    assert "version" in data


def test_health_endpoint(client):
    """Teste 2: Validação do endpoint /health."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_404_edge_case(client):
    """Teste 3: Validação de caso de erro (rota inexistente)."""
    response = client.get('/invalid-route')
    assert response.status_code == 404
