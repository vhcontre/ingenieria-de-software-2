import pytest
from pydantic import ValidationError
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut


def test_usuario_create_valido():
    data = {"username": "juanp", "email": "juan@example.com", "password": "secreto123"}
    usuario = UsuarioCreate(**data)
    assert usuario.username == data["username"]
    assert usuario.password == data["password"]


def test_usuario_create_invalido_email():
    data = {"username": "juanp", "email": "noesunmail", "password": "secreto123"}
    with pytest.raises(ValidationError):
        UsuarioCreate(**data)


def test_usuario_create_password_corta():
    data = {"username": "juanp", "email": "juan@example.com", "password": "123"}
    with pytest.raises(ValidationError):
        UsuarioCreate(**data)


def test_usuario_update_valido():
    data = {"email": "nuevo@mail.com", "password": "nuevaclave"}
    usuario = UsuarioUpdate(**data)
    assert usuario.email == "nuevo@mail.com"
    assert usuario.password == "nuevaclave"


def test_usuario_update_password_corta():
    with pytest.raises(ValidationError):
        UsuarioUpdate(password="abc")


def test_usuario_out_from_orm():
    class DummyUsuario:
        def __init__(self, id, username, email, es_activo):
            self.id = id
            self.username = username
            self.email = email
            self.es_activo = es_activo

    dummy = DummyUsuario(1, "admin", "admin@mail.com", True)
    usuario_out = UsuarioOut.model_validate(dummy)
    assert usuario_out.username == "admin"
    assert usuario_out.email == "admin@mail.com"
