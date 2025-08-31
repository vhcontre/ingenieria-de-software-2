


from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductoBase(BaseModel):
    nombre: str
    descrpcion: Optional[str] = None
    precio: float
    stock: int
    categoria: Optional[str] = None
    

    

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass


class ProductoRead(ProductoBase):
    id: int
    fecha_creacion: datetime
    
    class Config:
        orm_mode = True