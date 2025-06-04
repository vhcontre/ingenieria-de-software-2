from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class DepositoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    direccion: Optional[str] = None


class DepositoCreate(DepositoBase):
    pass


class DepositoUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=1)
    direccion: Optional[str] = None


class DepositoOut(DepositoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
