import pytest
from pydantic import ValidationError
from app.schemas.deposito import DepositoCreate, DepositoUpdate, DepositoOut


def test_deposito_create_valido():
    data = {"nombre": "Depósito Central", "direccion": "Av. Siempre Viva 123"}
    deposito = DepositoCreate(**data)
    assert deposito.nombre == data["nombre"]
    assert deposito.direccion == data["direccion"]


def test_deposito_create_invalido_faltan_campos():
    with pytest.raises(ValidationError):
        DepositoCreate()


def test_deposito_create_nombre_vacio():
    with pytest.raises(ValidationError):
        DepositoCreate(nombre="", direccion="Calle Falsa")


def test_deposito_update_parcial_valido():
    deposito = DepositoUpdate(nombre="Nuevo Nombre")
    assert deposito.nombre == "Nuevo Nombre"
    assert deposito.direccion is None


def test_deposito_update_nombre_vacio():
    with pytest.raises(ValidationError):
        DepositoUpdate(nombre="")


def test_deposito_out_from_orm():
    class DummyDeposito:
        def __init__(self, id, nombre, direccion):
            self.id = id
            self.nombre = nombre
            self.direccion = direccion

    orm_obj = DummyDeposito(1, "Depósito Norte", "Ruta 8")
    deposito_out = DepositoOut.model_validate(orm_obj)
    assert deposito_out.id == 1
    assert deposito_out.nombre == "Depósito Norte"
    assert deposito_out.direccion == "Ruta 8"
