#path: backend/app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.security.auth import authenticate_user, create_access_token
from app.schemas.token import Token

router = APIRouter()

@router.post(
    "/login",
    response_model=Token,
    summary="Iniciar sesión",
    description="Autentica un usuario y devuelve un token JWT.",
    responses={
        200: {"description": "Inicio de sesión exitoso"},
        401: {"description": "Credenciales inválidas"},
    },
    tags=["Autenticación"],
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Autentica un usuario y retorna un token JWT.

    - **username**: Nombre de usuario.
    - **password**: Contraseña.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}