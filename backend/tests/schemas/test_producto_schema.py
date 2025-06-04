import pytest
from pydantic import ValidationError
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoOut


def test_producto_create_valido():
    data = {
        "nombre": "Producto A",
        "sku": "SKU001",
        "descripcion": "Descripción del producto"
    }
    producto = ProductoCreate(**data)
    assert producto.nombre == data["nombre"]
    assert producto.sku == data["sku"]
    assert producto.descripcion == data["descripcion"]


def test_producto_create_invalido_faltan_campos():
    data = {
        "sku": "SKU001"
    }
    with pytest.raises(ValidationError):
        ProductoCreate(**data)


def test_producto_create_tipo_invalido():
    data = {
        "nombre": 123,
        "sku": True,
        "descripcion": 9.99
    }
    with pytest.raises(ValidationError):
        ProductoCreate(**data)


def test_producto_create_campos_vacios():
    data = {
        "nombre": "",
        "sku": "",
        "descripcion": ""
    }
    with pytest.raises(ValidationError):
        ProductoCreate(**data)


def test_producto_update_valido_parcial():
    data = {
        "nombre": "Nuevo nombre"
    }
    producto = ProductoUpdate(**data)
    assert producto.nombre == "Nuevo nombre"
    assert producto.sku is None
    assert producto.descripcion is None


def test_producto_update_invalido_nombre_vacio():
    with pytest.raises(ValidationError):
        ProductoUpdate(nombre="")  # min_length=1


def test_producto_out_from_orm():
    class DummyProducto:
        def __init__(self, id, nombre, sku, descripcion):
            self.id = id
            self.nombre = nombre
            self.sku = sku
            self.descripcion = descripcion

    orm_obj = DummyProducto(1, "Producto B", "SKU002", "Otra descripción")
    producto_out = ProductoOut.model_validate(orm_obj)
    assert producto_out.id == 1
    assert producto_out.nombre == "Producto B"
    assert producto_out.sku == "SKU002"
    assert producto_out.descripcion == "Otra descripción"
