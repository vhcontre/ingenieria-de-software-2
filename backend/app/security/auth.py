from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext
from app.db.models.usuario import UsuarioORM
from sqlalchemy.orm import Session

# Clave secreta para firmar el token
SECRET_KEY = "Super-$ecret-key2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def obtener_password_hash(password):
    return pwd_context.hash(password)

def autenticar_usuario(db: Session, username: str, password: str):
    usuario = db.query(UsuarioORM).filter(UsuarioORM.username == username).first()
    if not usuario:
        return None
    if not verificar_password(password, usuario.hashed_password):
        return None
    return usuario

def crear_token_acceso(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
