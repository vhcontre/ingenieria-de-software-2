# domain/models/producto.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Producto:
    id: Optional[int]
    nombre: str
    sku: str
    descripcion: Optional[str] = None
