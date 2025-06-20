from app.db.engine import engine
from app.db.models.base import EntityBase

# Importá todos los modelos para que SQLAlchemy los registre y cree las tablas

def init_db():
    EntityBase.metadata.drop_all(bind=engine)  # Elimina todas las tablas (¡cuidado! pierde datos)
    EntityBase.metadata.create_all(bind=engine)  # Crea todas las tablas

if __name__ == "__main__":
    print("Creando base de datos...")
    init_db()
    print("Base creada correctamente.")
