from pydantic import BaseModel, EmailStr
from typing import List

class RolRead(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioRead(UsuarioBase):
    id: int
    roles: List[RolRead] = []

    class Config:
        orm_mode = True
