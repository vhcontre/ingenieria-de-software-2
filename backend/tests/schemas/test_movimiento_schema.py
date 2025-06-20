import pytest
from datetime import datetime
from pydantic import ValidationError
from app.schemas.movimiento import MovimientoCreate, MovimientoUpdate, MovimientoOut


def test_movimiento_create_valido():
    data = {
        "producto_id": 1,
        "deposito_origen_id": None,
        "deposito_destino_id": 2,
        "tipo": "entrada",
        "cantidad": 10,
        "fecha": datetime.now(),
        "timestamp": datetime.now()
    }
    movimiento = MovimientoCreate(**data)
    assert movimiento.tipo == "entrada"
    assert movimiento.cantidad == 10


def test_movimiento_create_cantidad_invalida():
    data = {
        "producto_id": 1,
        "deposito_destino_id": 2,
        "tipo": "salida",
        "cantidad": 0,
        "fecha": datetime.now(),
        "timestamp": datetime.now()
    }
    with pytest.raises(ValidationError):
        MovimientoCreate(**data)


def test_movimiento_create_tipo_vacio():
    data = {
        "producto_id": 1,
        "deposito_destino_id": 2,
        "tipo": "",
        "cantidad": 5,
        "fecha": datetime.now(),
        "timestamp": datetime.now()
    }
    with pytest.raises(ValidationError):
        MovimientoCreate(**data)


def test_movimiento_update_valido():
    data = {
        "tipo": "traslado",
        "cantidad": 15,
        "timestamp": datetime.now()
    }
    movimiento = MovimientoUpdate(**data)
    assert movimiento.tipo.value == "traslado"
    assert movimiento.cantidad == 15


def test_movimiento_update_invalido():
    with pytest.raises(ValidationError):
        MovimientoUpdate(cantidad=0)


def test_movimiento_out_from_orm():
    class DummyMovimiento:
        def __init__(self, id, producto_id, deposito_origen_id, deposito_destino_id, tipo, cantidad, fecha):
            self.id = id
            self.producto_id = producto_id
            self.deposito_origen_id = deposito_origen_id
            self.deposito_destino_id = deposito_destino_id
            self.tipo = tipo
            self.cantidad = cantidad
            self.fecha = fecha
            self.timestamp=datetime.now()

    dummy = DummyMovimiento(1, 1, None, 2, "entrada", 20, datetime.now())
    out = MovimientoOut.model_validate(dummy)
    assert out.id == 1
    assert out.tipo == "entrada"
    assert out.cantidad == 20
