# domain/models/usuario.py
from dataclasses import dataclass, field
from typing import List, Optional
from domain.models.rol import Rol

@dataclass
class Usuario:
    id: Optional[int]
    username: str
    email: Optional[str] = None
    hashed_password: str
    is_active: bool
    roles: List[Rol] = field(default_factory=list)

