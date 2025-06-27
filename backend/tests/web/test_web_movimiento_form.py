# tests/web/test_web_movimiento_form.py
import datetime
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.domain.models.movimiento import TipoMovimiento as DomainTipoMovimiento

client = TestClient(app)

@pytest.fixture
def fecha_actual():
    return datetime.utcnow()

@pytest.fixture
def setup_db(db_session):
    from app.db.models.producto import ProductoORM
    from app.db.models.usuario import UsuarioORM
    from app.db.models.deposito import DepositoORM
    producto = ProductoORM(nombre="Test Producto", sku="SKU-TEST", stock=100, stock_minimo=1)
    usuario = UsuarioORM(username="testuser", email="testuser@example.com", hashed_password="x", is_active=True)
    deposito = DepositoORM(nombre="Depósito Test", ubicacion="Calle Falsa 123")
    db_session.add_all([producto, usuario, deposito])
    db_session.commit()
    return {
        "producto_id": producto.id,
        "usuario_id": usuario.id,
        "deposito_id": deposito.id
    }

def test_web_movimiento_post_ok(setup_db):
    ids = setup_db
    response = client.post(
        "/web/movimientos",
        data={
            "producto_id": ids["producto_id"],
            "deposito_origen_id": ids["deposito_id"],
            "deposito_destino_id": ids["deposito_id"],
            "usuario_id": ids["usuario_id"],
            "cantidad": 5,
            "tipo": DomainTipoMovimiento.ingreso.value
        },
        follow_redirects=False  # Importante: así capturamos el 303
    )
    assert response.status_code == 303  # redirección a productos

def test_web_movimiento_post_error(setup_db):
    ids = setup_db
    response = client.post(
        "/web/movimientos",
        data={
            "producto_id": 9999,  # Producto inexistente
            "deposito_origen_id": ids["deposito_id"],
            "deposito_destino_id": ids["deposito_id"],
            "usuario_id": ids["usuario_id"],
            "cantidad": 5,
            "tipo": DomainTipoMovimiento.ingreso.value
        }
    )
    assert response.status_code == 200
    assert "Producto no encontrado" in response.text

