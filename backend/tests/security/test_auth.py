from app.security.auth import obtener_password_hash
from app.db.models.usuario import UsuarioORM
from app.db.models.rol import RolORM
from fastapi.testclient import TestClient

# 🔧 Crear usuario admin para pruebas
def crear_usuario_admin(db):
    print("🔧 Creando usuario con rol ADMIN")
    rol_admin = RolORM(nombre="admin")
    db.add(rol_admin)
    db.commit()
    db.refresh(rol_admin)

    hashed_pw = obtener_password_hash("admin_password")
    user = UsuarioORM(
        username="admin",
        email="admin@example.com",
        hashed_password=hashed_pw,
        is_active=True,
        roles=[rol_admin]
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"✅ Usuario admin creado: {user.username}")
    return user

# ✅ Test: login exitoso
def test_login_ok(client, db_session):
    print("\n🚀 Ejecutando test_login_ok")
    crear_usuario_admin(db_session)

    print("🔐 Enviando solicitud de login...")
    response = client.post("/auth/login", data={
        "username": "admin",
        "password": "admin_password"
    })

    print(f"📨 Respuesta del login: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    assert "access_token" in response.json()
    print("✅ Login exitoso confirmado.")

# ✅ Test: acceso a endpoint protegido con token válido
def test_endpoint_protegido(client, db_session):
    print("\n🔒 Ejecutando test_endpoint_protegido")
    crear_usuario_admin(db_session)

    print("🔐 Login para obtener token...")
    login_response = client.post("/auth/login", data={"username": "admin", "password": "admin_password"})
    token = login_response.json()["access_token"]

    print("📡 Accediendo a /usuarios/me con token...")
    response = client.get("/usuarios/me", headers={"Authorization": f"Bearer {token}"})
    print(f"🔍 Estado de respuesta: {response.status_code}")
    assert response.status_code == 200
    print("✅ Acceso autorizado.")

# ✅ Test: acceso al endpoint solo admin
def test_endpoint_admin_role(client, db_session):
    print("\n🔐 Ejecutando test_endpoint_admin_role")
    crear_usuario_admin(db_session)

    login_response = client.post("/auth/login", data={"username": "admin", "password": "admin_password"})
    token = login_response.json()["access_token"]

    print("🚪 Accediendo a zona segura con rol admin...")
    response = client.get("/admin/zona-segura", headers={"Authorization": f"Bearer {token}"})
    print(f"🔍 Estado de respuesta: {response.status_code}")
    assert response.status_code == 200
    print("✅ Acceso permitido a zona segura.")

# ❌ Test: operador no puede acceder a zona admin
def test_endpoint_operador_role_forbidden(client, db_session):
    print("\n🚫 Ejecutando test_endpoint_operador_role_forbidden")
    print("🧱 Creando usuario con rol OPERADOR")
    rol_operador = RolORM(nombre="operador")
    db_session.add(rol_operador)
    db_session.commit()
    db_session.refresh(rol_operador)

    hashed_pw = obtener_password_hash("op_password")
    user = UsuarioORM(
        username="operador",
        email="op@example.com",
        hashed_password=hashed_pw,
        is_active=True,
        roles=[rol_operador]
    )
    db_session.add(user)
    db_session.commit()

    print("🔐 Login operador...")
    login_response = client.post("/auth/login", data={"username": "operador", "password": "op_password"})
    token = login_response.json()["access_token"]

    print("🚪 Intentando acceder a zona segura con operador...")
    response = client.get("/admin/zona-segura", headers={"Authorization": f"Bearer {token}"})
    print(f"❗ Respuesta: {response.status_code} (esperado: 403)")
    assert response.status_code == 403
    print("✅ Acceso denegado como se esperaba.")
