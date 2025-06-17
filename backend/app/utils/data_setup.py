from app.db.models.usuario import UsuarioORM
from app.db.models.rol import RolORM
from app.security.hashing import hashear_password


def crear_usuario_con_rol(db, username: str, password: str, rol: str):
    # 🔐 Buscar o crear el rol
    rol_obj = db.query(RolORM).filter_by(nombre=rol).first()
    if not rol_obj:
        rol_obj = RolORM(nombre=rol)
        db.add(rol_obj)
        db.commit()
        db.refresh(rol_obj)

    # 🧑 Crear usuario con contraseña hasheada
    hashed_pw = hashear_password(password)
    user = UsuarioORM(username=username, email=f"{username}@test.com", hashed_password=hashed_pw, is_active=True)
    user.roles.append(rol_obj)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
