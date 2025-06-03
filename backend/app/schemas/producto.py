# app/schemas/producto.py
from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    sku: str
    descripcion: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id: int

    class Config:
        orm_mode = True
