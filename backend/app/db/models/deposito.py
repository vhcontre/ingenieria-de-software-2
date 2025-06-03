# app/db/models/deposito.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.models.base import EntityBase

class DepositoORM(EntityBase):
    __tablename__ = "depositos"
    
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)

    movimientos_origen = relationship("Movimiento", foreign_keys="[Movimiento.deposito_origen_id]", back_populates="deposito_origen")
    movimientos_destino = relationship("Movimiento", foreign_keys="[Movimiento.deposito_destino_id]", back_populates="deposito_destino")

