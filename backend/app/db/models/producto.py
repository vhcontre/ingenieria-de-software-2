# app/db/models/producto.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.models.base import EntityBase

class ProductoORM(EntityBase):
    __tablename__ = "productos"
    
    nombre = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    descripcion = Column(String)

    movimientos = relationship("Movimiento", back_populates="producto")