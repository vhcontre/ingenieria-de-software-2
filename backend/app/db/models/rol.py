from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.models.base import EntityBase

class RolORM(EntityBase):
    __tablename__ = "roles"

    nombre = Column(String, unique=True, nullable=False)

    usuarios = relationship("UsuarioORM", secondary="usuario_rol", back_populates="roles")
