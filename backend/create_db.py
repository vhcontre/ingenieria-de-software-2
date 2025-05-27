from app.db.base import init_db

if __name__ == "__main__":
    print("Creando la base de datos...")
    init_db()
    print("Base de datos creada con éxito.")
