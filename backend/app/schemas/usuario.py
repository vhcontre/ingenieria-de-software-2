# This file is part of the "FastAPI + SQLAlchemy + Alembic" project.
# file: app/schemas/usuario.py
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import Optional


class UsuarioBase(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=6)


class UsuarioUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=3)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=6)
    es_activo: Optional[bool] = None


class UsuarioOut(UsuarioBase):
    id: int
    es_activo: bool = Field(..., alias="is_active")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

UsuarioRead = UsuarioOut