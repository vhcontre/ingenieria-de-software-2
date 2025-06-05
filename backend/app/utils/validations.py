# app/utils/validations.py

from sqlalchemy.orm import Session
from app.db.models.producto import ProductoORM

def check_unicidad_producto(
    db: Session, nombre: str | None, sku: str | None, exclude_id: int | None = None
):
    """
    Valida que no exista otro producto con el mismo nombre o SKU.
    Si se pasa `exclude_id`, se ignora ese ID en la búsqueda (para updates).
    Lanza ValueError si encuentra conflicto.
    """
    if nombre:
        query = db.query(ProductoORM).filter(ProductoORM.nombre == nombre)
        if exclude_id is not None:
            query = query.filter(ProductoORM.id != exclude_id)
        if query.first():
            raise ValueError("Ya existe otro producto con ese nombre.")

    if sku:
        query = db.query(ProductoORM).filter(ProductoORM.sku == sku)
        if exclude_id is not None:
            query = query.filter(ProductoORM.id != exclude_id)
        if query.first():
            raise ValueError("Ya existe otro producto con ese SKU.")
