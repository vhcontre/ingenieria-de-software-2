from pydantic import BaseModel, Field
from typing import Optional

class DepositoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    ubicacion: Optional[str] = None  # <-- debe estar aquí

class DepositoCreate(DepositoBase):
    pass

class DepositoUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=1)
    ubicacion: Optional[str] = None

class DepositoOut(DepositoBase):
    id: int

    class Config:
        orm_mode = True
