# domain/models/producto.py

from typing import Optional

class Producto:
    def __init__(self, id: Optional[int], nombre: str, sku: str, descripcion: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.sku = sku
        self.descripcion = descripcion

    def cambiar_nombre(self, nuevo_nombre: str):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nuevo_nombre

    def __repr__(self):
        return f"Producto(id={self.id}, nombre={self.nombre}, sku={self.sku})"
