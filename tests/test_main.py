from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_comercializacao():
    response = client.get("/comercializacaoList")
    assert response.status_code == 200

def test_exportacao():
    response = client.get("/exportacaoList")
    assert response.status_code == 200

def test_importacao():
    response = client.get("/importacaoList")
    assert response.status_code == 200

def test_processamento():
    response = client.get("/processamentoList")
    assert response.status_code == 200

def test_producao():
    response = client.get("/producaoList")
    assert response.status_code == 200