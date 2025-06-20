import pytest
from pydantic import ValidationError
from app.schemas.deposito import DepositoCreate, DepositoUpdate, DepositoOut


def test_deposito_create_valido():
    data = {"nombre": "Depósito Central", "ubicacion": "Av. Olivos 123"}
    deposito = DepositoCreate(**data)
    assert deposito.nombre == data["nombre"]
    assert deposito.ubicacion == data["ubicacion"]


def test_deposito_create_invalido_faltan_campos():
    with pytest.raises(ValidationError):
        DepositoCreate()


def test_deposito_create_nombre_vacio():
    with pytest.raises(ValidationError):
        DepositoCreate(nombre="", ubicacion="Calle Falsa")


def test_deposito_update_parcial_valido():
    deposito = DepositoUpdate(nombre="Nuevo Nombre")
    assert deposito.nombre == "Nuevo Nombre"
    assert deposito.ubicacion is None


def test_deposito_update_nombre_vacio():
    with pytest.raises(ValidationError):
        DepositoUpdate(nombre="")


def test_deposito_out_from_orm():
    class DummyDeposito:
        def __init__(self, id, nombre, ubicacion):
            self.id = id
            self.nombre = nombre
            self.ubicacion = ubicacion

    orm_obj = DummyDeposito(1, "Depósito Norte", "Ruta 8")
    deposito_out = DepositoOut.model_validate(orm_obj)
    assert deposito_out.id == 1
    assert deposito_out.nombre == "Depósito Norte"
    assert deposito_out.ubicacion == "Ruta 8"
