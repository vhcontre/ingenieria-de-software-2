# tests/db/test_producto_model.py

from app.db.models.producto import ProductoORM

def test_crear_producto_modelo(db_session):
    producto = ProductoORM(nombre="Mouse", sku="SKU001", descripcion="Mouse óptico")
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)

    assert producto.id is not None
    assert producto.nombre == "Mouse"
    assert producto.sku == "SKU001"
