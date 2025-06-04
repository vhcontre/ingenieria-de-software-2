import pytest
from pydantic import ValidationError
from app.schemas.rol import RolCreate, RolRead

def test_rol_create_valid():
    data = {
        "nombre": "Administrador",
        "descripcion": "Acceso total al sistema"
    }
    rol = RolCreate(**data)
    assert rol.nombre == "Administrador"
    assert rol.descripcion == "Acceso total al sistema"

def test_rol_read_valid():
    data = {
        "id": 1,
        "nombre": "Usuario",
        "descripcion": "Acceso limitado"
    }
    rol = RolRead(**data)
    assert rol.id == 1
    assert rol.nombre == "Usuario"
    assert rol.descripcion == "Acceso limitado"

def test_rol_read_invalid_missing_id():
    data = {
        "nombre": "Invitado",
        "descripcion": "Acceso limitado"
    }
    with pytest.raises(ValidationError):
        RolRead(**data)

def test_rol_create_missing_nombre():
    data = {
        "descripcion": "Sin nombre"
    }
    with pytest.raises(ValidationError):
        RolCreate(**data)
