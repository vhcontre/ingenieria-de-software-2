from app.domain.models.producto import Producto

def test_producto_creacion():
    producto = Producto(id=1, nombre="Coca", sku="COC-123", descripcion="Bebida gaseosa")
    assert producto.nombre == "Coca"
    assert producto.sku == "COC-123"
