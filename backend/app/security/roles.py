from fastapi import Depends, HTTPException, status
from app.security.auth import obtener_usuario_actual

def validar_rol(rol_requerido: str):
    def role_dependency(usuario=Depends(obtener_usuario_actual)):
        roles_usuario = [rol.nombre for rol in usuario.roles]  # asumiendo relación many-to-many en ORM
        if rol_requerido not in roles_usuario:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tiene permisos suficientes"
            )
        return usuario
    return role_dependency
