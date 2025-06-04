from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class MovimientoBase(BaseModel):
    producto_id: int
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    tipo: str = Field(..., min_length=1)
    cantidad: int = Field(..., gt=0)
    fecha: datetime


class MovimientoCreate(MovimientoBase):
    pass


class MovimientoUpdate(BaseModel):
    tipo: Optional[str] = Field(default=None, min_length=1)
    cantidad: Optional[int] = Field(default=None, gt=0)
    fecha: Optional[datetime] = None


class MovimientoOut(MovimientoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
