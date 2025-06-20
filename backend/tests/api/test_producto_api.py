# tests/api/test_producto_api.py

# def test_crear_producto(client):
#     # 1. Hacer login para obtener token
#     login_resp = client.post("/auth/login", data={"username": "admin", "password": "admin123"})
#     assert login_resp.status_code == 200
#     token = login_resp.json()["access_token"]
#     # 2. Armar headers con token
#     headers = {"Authorization": f"Bearer {token}"}
#     # 3. Hacer la llamada protegida con los headers
#     producto_data = {"nombre": "Café", "sku": "CAFE123", "stock": 0, "stock_minimo": 10}
#     resp = client.post("/productos/", json=producto_data, headers=headers)
#     assert resp.status_code == 201

def test_crear_producto(client, crear_usuario_admin):
    # No necesitamos llamar explícitamente a crear_usuario_admin
    # porque ya está como fixture y se ejecuta automáticamente
    
    # 1. Login para obtener token
    login_resp = client.post(
        "/auth/login",
        data={"username": "admin", "password": "admin123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert login_resp.status_code == 200, login_resp.text
    token = login_resp.json()["access_token"]

    # 2. Crear producto
    producto_data = {"nombre": "Café", "sku": "CAFE123", "stock": 0, "stock_minimo": 10}
    resp = client.post(
        "/productos/",
        json=producto_data,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert resp.status_code == 201, resp.text
    assert resp.json()["nombre"] == "Café"