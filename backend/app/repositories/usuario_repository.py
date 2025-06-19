from sqlalchemy.orm import Session
from app.db.models.usuario import UsuarioORM
from app.schemas.usuario import UsuarioCreate

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_usuario(self, usuario_in: UsuarioCreate):
        usuario = UsuarioORM(
            username=usuario_in.username,
            email=usuario_in.email,
            hashed_password="hashed_password_placeholder",  # Debes hashear la contraseña real aquí
            es_activo=True
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def get_usuario_by_id(self, usuario_id: int):
        return self.db.query(UsuarioORM).filter(UsuarioORM.id == usuario_id).first()

    def get_all_usuarios(self):
        return self.db.query(UsuarioORM).all()