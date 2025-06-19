# archivo: app/scripts/test_crear_deposito.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_deposito():
    print("📦 Probando creación de depósito...")

    # Primero: hacer login
    login_response = client.post("/auth/login", data={"username": "admin", "password": "admin123"})
    print("🔐 Login:", login_response.status_code, login_response.json())
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Luego: crear depósito
    deposito_data = {"nombre": "Depósito Test"}
    response = client.post("/depositos/", json=deposito_data, headers=headers)

    print("📦 Resultado creación depósito:", response.status_code)
    print("📝 Respuesta JSON:", response.json() if response.status_code < 500 else response.text)

    assert response.status_code == 201
    assert "id" in response.json()

if __name__ == "__main__":
    test_crear_deposito()
