from datetime import datetime, timezone


def test_flujo_completo(client, db_session):
    from app.utils.data_setup import crear_usuario_con_rol

    print("🔧 Creando usuario 'admin' con rol...")
    crear_usuario_con_rol(db_session, "admin", "admin123", "admin")

    print("🔐 Logueando usuario...")
    login_response = client.post("/auth/login", data={"username": "admin", "password": "admin123"})
    print("🔐 Login response:", login_response.status_code, login_response.json())
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    print("📦 Creando producto...")
    producto_data = {"nombre": "Café", "sku": "CAFE123", "stock": 0, "stock_minimo": 10}
    resp_prod = client.post("/productos/", json=producto_data, headers=headers)
    print("📦 Producto response:", resp_prod.status_code, resp_prod.json() if resp_prod.status_code < 500 else resp_prod.text)
    assert resp_prod.status_code == 201
    producto_id = resp_prod.json()["id"]

    print("🏢 Creando depósito...")
    deposito_data = {"nombre": "Depósito Central"}
    resp_dep = client.post("/depositos/", json=deposito_data, headers=headers)
    print("🏢 Depósito response:", resp_dep.status_code, resp_dep.json() if resp_dep.status_code < 500 else resp_dep.text)
    assert resp_dep.status_code == 201
    deposito_id = resp_dep.json()["id"]

    print("➕ Registrando entrada de stock...")
    entrada_data = {
        "tipo": "ingreso",
        "fecha": datetime.now(timezone.utc).isoformat(),
        "cantidad": 20,
        "producto_id": producto_id,
        "deposito_destino_id": deposito_id,
        "usuario_id": 1
    }
    resp_entrada = client.post("/movimientos/", json=entrada_data, headers=headers)
    print("📥 Entrada response:", resp_entrada.status_code, resp_entrada.json() if resp_entrada.status_code < 500 else resp_entrada.text)
    assert resp_entrada.status_code == 201

    print("➖ Registrando salida de stock...")
    
    salida_data = {
        "tipo": "egreso",
        "fecha": datetime.now(timezone.utc).isoformat(),
        "cantidad": 5,
        "producto_id": producto_id,
        "deposito_destino_id": deposito_id,
        "usuario_id": 1
    }

    resp_salida = client.post("/movimientos/", json=salida_data, headers=headers)
    print("📤 Salida response:", resp_salida.status_code, resp_salida.json() if resp_salida.status_code < 500 else resp_salida.text)
    assert resp_salida.status_code == 201

    print("📊 Verificando stock final del producto...")
    resp_final = client.get(f"/productos/{producto_id}", headers=headers)
    print("📊 Producto final response:", resp_final.status_code, resp_final.json() if resp_final.status_code < 500 else resp_final.text)
    assert resp_final.status_code == 200
    producto_final = resp_final.json()

    print(f"✅ Stock final: {producto_final['stock']} (esperado: 15)")
    assert producto_final["stock"] == 15
