from dataclasses import dataclass
from typing import List, Optional
from domain.models.rol import Rol

@dataclass
class Usuario:
    id: Optional[int]
    username: str
    email: Optional[str]
    hashed_password: str
    is_active: bool
    roles: List[Rol]
