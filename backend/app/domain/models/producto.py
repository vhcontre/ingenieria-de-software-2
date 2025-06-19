# domain/models/producto.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Producto:
    id: Optional[int]
    nombre: str
    sku: str
    descripcion: Optional[str] = None
    stock: int = 0
    stock_minimo: int = 0 
    def __post_init__(self):
        if not self.nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not self.sku:
            raise ValueError("El SKU del producto no puede estar vacío.")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")
