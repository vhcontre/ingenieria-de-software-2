from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    sku: str = Field(..., min_length=1)
    descripcion: Optional[str] = None
    stock: int = Field(default=0, ge=0)


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=1)
    sku: Optional[str] = Field(default=None, min_length=1)
    descripcion: Optional[str] = None
    stock: int = Field(default=0, ge=0)


class ProductoOut(ProductoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
