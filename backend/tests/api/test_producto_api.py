# tests/api/test_producto_api.py

def test_crear_producto(client):
    # 1. Hacer login para obtener token
    login_resp = client.post("/auth/login", data={"username": "admin", "password": "admin123"})
    assert login_resp.status_code == 200
    token = login_resp.json()["access_token"]

    # 2. Armar headers con token
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Hacer la llamada protegida con los headers
    producto_data = {"nombre": "Café", "sku": "CAFE123", "stock": 0, "stock_minimo": 10}
    resp = client.post("/productos/", json=producto_data, headers=headers)

    assert resp.status_code == 201
