#file: backend/app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioRead
from app.db.session import get_db
from app.repositories.usuario_repository import UsuarioRepository
from app.dependencies.security import get_current_user

router = APIRouter()

@router.get(
    "/me",
    response_model=UsuarioRead,
    summary="Obtener el usuario autenticado",
    description="Devuelve la información del usuario autenticado. Requiere autenticación.",
    responses={
        200: {"description": "Usuario autenticado"},
        401: {"description": "No autenticado"},
    },
    tags=["Usuarios"],
)
def obtener_usuario_actual(current_user=Depends(get_current_user)):
    """
    Devuelve la información del usuario autenticado.
    """
    return current_user

@router.post(
    "/",
    response_model=UsuarioRead,
    status_code=201,
    summary="Crear un nuevo usuario",
    description="Crea un usuario en el sistema. Requiere autenticación.",
    responses={
        201: {"description": "Usuario creado exitosamente"},
        400: {"description": "Datos inválidos"},
        401: {"description": "No autenticado"},
    },
    tags=["Usuarios"],
)
def crear_usuario_endpoint(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Crea un nuevo usuario.

    - **username**: Nombre de usuario.
    - **password**: Contraseña.
    - **roles**: Lista de roles asignados al usuario.
    """
    repo = UsuarioRepository(db)
    return repo.create_usuario(usuario)

@router.get(
    "/{usuario_id}",
    response_model=UsuarioRead,
    summary="Obtener un usuario por ID",
    description="Devuelve la información de un usuario específico dado su ID. Requiere autenticación.",
    responses={
        200: {"description": "Usuario encontrado"},
        404: {"description": "Usuario no encontrado"},
        401: {"description": "No autenticado"},
    },
    tags=["Usuarios"],
)
def obtener_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Recupera un usuario por su ID.

    - **usuario_id**: ID del usuario a buscar.
    """
    repo = UsuarioRepository(db)
    usuario = repo.get_usuario_by_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

