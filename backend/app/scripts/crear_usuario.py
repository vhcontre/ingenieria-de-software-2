# file: scripts/crear_usuario.py (ejecútalo una vez)

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.usuario import UsuarioORM
from app.security.auth import obtener_password_hash

db: Session = SessionLocal()

nuevo_usuario = UsuarioORM(
    username="admin",
    email="admin@email.com",
    hashed_password=obtener_password_hash("admin123"),
    is_active=True
)

db.add(nuevo_usuario)
db.commit()
db.close()
print("✅ Usuario creado con éxito.")
