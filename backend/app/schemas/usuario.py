from typing import Optional, List
from pydantic import BaseModel, EmailStr

class RolSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True

class UsuarioBase(BaseModel):
    username: str
    email: Optional[EmailStr]
    is_active: bool = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]

class UsuarioRead(UsuarioBase):
    id: int
    roles: List[RolSchema] = []

    class Config:
        from_attributes = True
