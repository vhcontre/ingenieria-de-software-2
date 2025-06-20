# app/routers/admin.py

from fastapi import APIRouter, Depends
from app.dependencies.security import usuario_actual_con_rol

router = APIRouter(tags=["Administración"])

@router.get("/zona-segura")
def solo_admin(user = Depends(usuario_actual_con_rol("admin"))):
    return {"msg": f"Bienvenido, {user.username}. Zona exclusiva para administradores."}


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.db.session import get_db
# from app.dependencies.security import usuario_actual_con_rol
# from app.schemas.usuario import UsuarioRead
# from app.repositories.usuario_repository import UsuarioRepository

# router = APIRouter()

# @router.get(
#     "/usuarios",
#     response_model=list[UsuarioRead],
#     summary="Listar todos los usuarios",
#     description="Devuelve una lista de todos los usuarios. Requiere autenticación y rol de administrador.",
#     responses={
#         200: {"description": "Lista de usuarios"},
#         401: {"description": "No autenticado"},
#         403: {"description": "Acceso denegado"},
#     },
#     tags=["Administración"],
# )
# def listar_usuarios(
#     db: Session = Depends(get_db),
#     current_user=Depends(usuario_actual_con_rol("admin")),  # Solo admin puede acceder
# ):
#     """
#     Lista todos los usuarios del sistema.

#     - **Requiere rol admin**
#     """
#     repo = UsuarioRepository(db)
#     return repo.get_all_usuarios()