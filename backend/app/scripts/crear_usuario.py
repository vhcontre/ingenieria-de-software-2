# file: scripts/crear_usuario.py (ejecútalo una vez)

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.usuario import UsuarioORM
from app.db.models.rol import RolORM
from app.security.auth import obtener_password_hash

db: Session = SessionLocal()

# Crear o buscar el rol admin
rol_admin = db.query(RolORM).filter_by(nombre="admin").first()
if not rol_admin:
    rol_admin = RolORM(nombre="admin")
    db.add(rol_admin)
    db.commit()
    db.refresh(rol_admin)

# Crear el usuario admin y asociar el rol
nuevo_usuario = UsuarioORM(
    username="admin",
    email="admin@email.com",
    hashed_password=obtener_password_hash("admin123"),
    is_active=True,
    roles=[rol_admin]
)

db.add(nuevo_usuario)
db.commit()
db.close()
print("✅ Usuario y rol admin creados con éxito.")