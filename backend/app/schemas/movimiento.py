from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional


class TipoMovimiento(str, Enum):
    ingreso = "ingreso"
    egreso = "egreso"
    traslado = "traslado"


class MovimientoBase(BaseModel):
    producto_id: int
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento


class MovimientoCreate(BaseModel):
    producto_id: int
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    usuario_id: int
    cantidad: int
    tipo: TipoMovimiento


class MovimientoRead(MovimientoBase):
    id: int

    class Config:
        from_attributes = True
