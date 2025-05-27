from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    sku: str
    descripcion: str

class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id: int

    class Config:
        orm_mode = True
