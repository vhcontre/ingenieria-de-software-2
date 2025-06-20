
# app/db/models/__init__.py
from .base import EntityBase
from .usuario import UsuarioORM, usuario_rol
from .rol import RolORM
from .producto import ProductoORM
from .deposito import DepositoORM
from .movimiento import MovimientoORM

# así SQLAlchemy los "ve" al momento de correr Alembic u otras operaciones
