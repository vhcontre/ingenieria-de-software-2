from app.db.session import SessionLocal
from app.utils.data_setup import crear_usuario_con_rol

# Creamos conexión a la base
db = SessionLocal()

# Crear usuarios de prueba
crear_usuario_con_rol(db, "vcontreras", "admin123", "admin")
crear_usuario_con_rol(db, "operador", "operador123", "operador")

# Cerramos la conexión
db.close()
