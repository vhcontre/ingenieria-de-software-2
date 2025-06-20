from app.security.auth import obtener_password_hash
from app.db.models.usuario import UsuarioORM
from app.db.models.rol import RolORM

def crear_usuario_admin(db):
    """Fixture para crear un usuario admin en la base de datos de prueba"""
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

def test_login_ok(client, db_session):
    """Test: login exitoso con credenciales correctas"""
    # Configuración
    crear_usuario_admin(db_session)

    # Ejecución
    response = client.post(
        "/auth/login",
        data={"username": "admin", "password": "admin_password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    
    # Verificación
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_endpoint_protegido(client, db_session):
    """Test: acceso a endpoint protegido con token válido"""
    # Configuración
    crear_usuario_admin(db_session)

    # Login
    login_resp = client.post(
        "/auth/login",
        data={"username": "admin", "password": "admin_password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert login_resp.status_code == 200, login_resp.text
    token = login_resp.json()["access_token"]

    # Acceso a endpoint protegido
    resp = client.get(
        "/usuarios/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Verificación
    assert resp.status_code == 200, resp.text

def test_endpoint_admin_role(client, db_session):
    """Test: usuario admin puede acceder a zona restringida"""
    # Configuración
    crear_usuario_admin(db_session)

    # Login
    login_response = client.post(
        "/auth/login",
        data={"username": "admin", "password": "admin_password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    token = login_response.json()["access_token"]

    # Acceso a endpoint admin
    response = client.get(
        "/admin/zona-segura",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Verificación
    assert response.status_code == 200

def test_endpoint_operador_role_forbidden(client, db_session):
    """Test: usuario operador no puede acceder a zona admin"""
    # Configuración
    rol_operador = RolORM(nombre="operador")
    db_session.add(rol_operador)
    db_session.commit()

    # Crear usuario operador
    user = UsuarioORM(
        username="operador",
        email="op@example.com",
        hashed_password=obtener_password_hash("op_password"),
        is_active=True,
        roles=[rol_operador]
    )
    db_session.add(user)
    db_session.commit()

    # Login
    login_response = client.post(
        "/auth/login",
        data={"username": "operador", "password": "op_password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    token = login_response.json()["access_token"]

    # Intentar acceder a endpoint admin
    response = client.get(
        "/admin/zona-segura",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Verificación
    assert response.status_code == 403