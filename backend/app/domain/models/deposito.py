from dataclasses import dataclass
from typing import Optional

@dataclass
class Deposito:
    id: Optional[int]
    nombre: str
    ubicacion: Optional[str] = None
