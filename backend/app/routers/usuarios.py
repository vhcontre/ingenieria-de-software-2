from fastapi import APIRouter, Depends
from app.db.models.usuario import UsuarioORM
from app.security.auth import obtener_usuario_actual
from app.security.roles import validar_rol

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

# Endpoint para usuario autenticado (cualquiera)
@router.get("/me")
def leer_usuario_actual(usuario: UsuarioORM = Depends(obtener_usuario_actual)):
    return {
        "username": usuario.username,
        "email": usuario.email,
        "roles": [rol.nombre for rol in usuario.roles]
    }

# Endpoint solo para admin
@router.get("/admin-only", dependencies=[Depends(validar_rol("admin"))])
def datos_admin():
    return {"mensaje": "Acceso solo para usuarios con rol admin"}

# Endpoint solo para operador
@router.get("/operador-only", dependencies=[Depends(validar_rol("operador"))])
def datos_operador():
    return {"mensaje": "Acceso solo para usuarios con rol operador"}
