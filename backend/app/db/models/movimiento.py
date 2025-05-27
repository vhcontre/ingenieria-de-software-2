from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum

from app.db.models.base import Base

class TipoMovimiento(PyEnum):
    ingreso = "ingreso"
    egreso = "egreso"
    traslado = "traslado"

class Movimiento(Base):
    __tablename__ = "movimientos"
    
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"), nullable=True)
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    tipo = Column(Enum(TipoMovimiento), nullable=False)

    producto = relationship("Producto")
    deposito_origen = relationship("Deposito", foreign_keys=[deposito_origen_id])
    deposito_destino = relationship("Deposito", foreign_keys=[deposito_destino_id])
    usuario = relationship("Usuario")
