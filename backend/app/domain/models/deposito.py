from typing import Optional
from domain.models.base_model import BaseModelWithId

class Deposito(BaseModelWithId):
    nombre: str
    ubicacion: Optional[str] = None
