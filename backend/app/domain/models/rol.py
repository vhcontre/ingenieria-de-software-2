# domain/models/rol.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Rol:
    id: Optional[int]
    nombre: str
