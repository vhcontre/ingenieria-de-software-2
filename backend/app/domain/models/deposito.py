# domain/models/deposito.py
from pydantic import BaseModel
from typing import Optional

class BaseModelWithId(BaseModel):
    id: int

    class Config:
        orm_mode = True

class Deposito(BaseModelWithId):
    nombre: str
    ubicacion: Optional[str] = None