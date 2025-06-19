#path: backend/app/security/auth.py
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.db.models.usuario import UsuarioORM
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.db.session import get_db


# Clave secreta para firmar el token
SECRET_KEY = "Super-$ecret-key2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def obtener_password_hash(password):
    return pwd_context.hash(password)

def __autenticar_usuario__(db: Session, username: str, password: str):
    usuario = db.query(UsuarioORM).filter(UsuarioORM.username == username).first()
    if not usuario:
        return None
    if not verificar_password(password, usuario.hashed_password):
        return None
    return usuario

def authenticate_user(db: Session, username: str, password: str):
    usuario = db.query(UsuarioORM).filter(UsuarioORM.username == username).first()
    if not usuario:
        return None
    if not verificar_password(password, usuario.hashed_password):
        return None
    return usuario

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UsuarioORM:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    usuario = db.query(UsuarioORM).filter(UsuarioORM.username == username).first()
    if usuario is None:
        raise credentials_exception
    return usuario