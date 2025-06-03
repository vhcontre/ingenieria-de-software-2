# app/db/models/base.py

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer
import json

class EntityBase(DeclarativeBase):
    """Clase base para todos los modelos, con atributos y métodos comunes."""

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash((self.__class__, self.id))

    def to_dict(self):
        """Devuelve una representación en diccionario del modelo."""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def to_json(self):
        """Devuelve una representación JSON del modelo."""
        return json.dumps(self.to_dict(), default=str)