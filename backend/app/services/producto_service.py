from app.db.models.producto import Producto
from app.db import db_session

def add_producto(producto: Producto) -> Producto:
    """
    Agrega un nuevo producto al sistema.
    :param producto: Instancia del producto a agregar.
    :return: Producto agregado.
    """
    if not producto.nombre or not producto.sku:
        raise ValueError("El nombre y el SKU del producto son obligatorios")
    if len(producto.sku) < 3:
        raise ValueError("El SKU debe tener al menos 3 caracteres")
    
    db_session.add(producto)
    db_session.commit()
    print(f"Producto agregado: {producto}")
    
    return producto