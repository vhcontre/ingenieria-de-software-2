# tests/api/test_producto_api.py

def test_crear_producto_via_api(client):
    response = client.post("/productos/", json={
        "nombre": "Monitor",
        "sku": "SKU003",
        "descripcion": "Monitor LED 24''"
    })

    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Monitor"
    assert data["sku"] == "SKU003"
    assert "id" in data
