# app/db/models/usuario.py
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models.base import EntityBase

# Tabla intermedia Usuario-Rol
usuario_rol = Table(
    "usuario_rol",
    EntityBase.metadata,
    Column("usuario_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("rol_id", ForeignKey("roles.id"), primary_key=True)
)

class UsuarioORM(EntityBase):
    __tablename__ = "usuarios"
    
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    roles = relationship("Rol", secondary=usuario_rol, back_populates="usuarios")

class RolORM(EntityBase):
    __tablename__ = "roles"

    
    nombre = Column(String, unique=True, nullable=False)

    usuarios = relationship("Usuario", secondary=usuario_rol, back_populates="roles")