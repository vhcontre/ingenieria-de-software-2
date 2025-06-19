# domain/models/movimiento.py
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class TipoMovimiento(Enum):
    ingreso = "ingreso"
    egreso = "egreso"
    traslado = "traslado"

@dataclass
class Movimiento:
    id: Optional[int]
    producto_id: int
    deposito_origen_id: Optional[int]
    deposito_destino_id: Optional[int]
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento
    timestamp: datetime
