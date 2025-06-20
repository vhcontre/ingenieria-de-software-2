# file: app/db/models/usuario.py
from sqlalchemy import Column, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models.base import EntityBase

# Tabla intermedia Usuario-Rol
usuario_rol = Table(
    "usuario_rol",
    EntityBase.metadata,
    Column("usuario_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("rol_id", ForeignKey("roles.id"), primary_key=True),
    extend_existing=True
)

class UsuarioORM(EntityBase):
    __tablename__ = "usuarios"
    __table_args__ = {'extend_existing': True} 
    
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    roles = relationship("RolORM", secondary="usuario_rol", back_populates="usuarios")

