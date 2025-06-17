# app/routers/admin.py
import sys

from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.security import usuario_actual_con_rol



router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@router.get("/zona-segura")
def solo_admin(user = Depends(usuario_actual_con_rol("admin"))):
    return {"msg": f"Bienvenido, {user.username}. Zona exclusiva para administradores."}
