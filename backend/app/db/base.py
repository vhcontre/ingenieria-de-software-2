from app.db.engine import engine
from app.db.models.base import Base

# Importá todos los modelos para que SQLAlchemy los registre y cree las tablas
from app.db.models.usuario import Usuario, Rol, usuario_rol
from app.db.models.producto import Producto
from app.db.models.deposito import Deposito
from app.db.models.movimiento import Movimiento

def init_db():
    Base.metadata.drop_all(bind=engine)  # Elimina todas las tablas (¡cuidado! pierde datos)
    Base.metadata.create_all(bind=engine)  # Crea todas las tablas

if __name__ == "__main__":
    print("Creando base de datos...")
    init_db()
    print("Base creada correctamente.")
