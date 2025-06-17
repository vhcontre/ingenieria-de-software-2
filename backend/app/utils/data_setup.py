from app.db.models.usuario import UsuarioORM
from app.db.models.rol import RolORM
from app.security.hashing import hashear_password


def crear_usuario_con_rol(db, username: str, password: str, rol: str):
    print(f"🔍 Verificando si existe el rol '{rol}'...")

    # Buscar o crear rol
    rol_obj = db.query(RolORM).filter_by(nombre=rol).first()
    if not rol_obj:
        print(f"➕ Rol '{rol}' no existe. Creando nuevo rol...")
        rol_obj = RolORM(nombre=rol)
        db.add(rol_obj)
        db.commit()
        db.refresh(rol_obj)
    else:
        print(f"✅ Rol '{rol}' ya existe.")

    print(f"🔐 Hasheando contraseña para usuario '{username}'...")
    hashed_pw = hashear_password(password)

    print(f"👤 Creando usuario '{username}' con rol '{rol}'...")
    user = UsuarioORM(
        username=username,
        email=f"{username}@test.com",
        hashed_password=hashed_pw,
        is_active=True
    )
    user.roles.append(rol_obj)

    db.add(user)
    db.commit()
    db.refresh(user)
    
    print(f"✅ Usuario '{username}' creado exitosamente con rol '{rol}'.\n")
    return user
