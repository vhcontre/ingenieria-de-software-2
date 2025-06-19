# app/db/models/producto.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.models.base import EntityBase

class ProductoORM(EntityBase):
    __tablename__ = "productos"
    
    nombre = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    descripcion = Column(String)
    stock = Column(Integer, default=0, nullable=False)
    stock_minimo = Column(Integer, nullable=False, default=0) 


    movimientos = relationship("MovimientoORM", back_populates="producto")

# Importación al final para evitar dependencias circulares
from .movimiento import MovimientoORM
