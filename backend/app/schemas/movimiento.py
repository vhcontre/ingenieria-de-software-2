# -*- coding: utf-8 -*-
# backend/app/schemas/movimiento.py
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from app.domain.models.movimiento import TipoMovimiento


class MovimientoBase(BaseModel):
    producto_id: int
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    tipo: TipoMovimiento 
    cantidad: int = Field(..., gt=0)
    fecha: datetime
    usuario_id: Optional[int] = None

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoUpdate(BaseModel):
    tipo: TipoMovimiento = Field(default=None)
    cantidad: Optional[int] = Field(default=None, gt=0)
    fecha: Optional[datetime] = None

class MovimientoRead(MovimientoBase):
    id: int
    timestamp: datetime
class MovimientoOut(MovimientoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
