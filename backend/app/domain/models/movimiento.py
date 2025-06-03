from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enum import Enum
from domain.models.producto import Producto
from domain.models.deposito import Deposito
from domain.models.usuario import Usuario

class TipoMovimiento(str, Enum):
    ingreso = "ingreso"
    egreso = "egreso"
    traslado = "traslado"

@dataclass
class Movimiento:
    id: Optional[int]
    producto: Producto
    deposito_origen: Optional[Deposito]
    deposito_destino: Optional[Deposito]
    usuario: Usuario
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento
