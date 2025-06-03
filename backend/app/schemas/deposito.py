from pydantic import BaseModel
from typing import Optional

class DepositoCreate(BaseModel):
    nombre: str
    ubicacion: Optional[str] = None

class DepositoRead(BaseModel):
    id: int
    nombre: str
    ubicacion: Optional[str] = None

    class Config:
        orm_mode = True
