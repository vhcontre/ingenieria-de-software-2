#  How to 5 – Autenticación y Autorización (JWT + Roles)

##  Índice

1. [Objetivos de la unidad](#objetivos-de-la-unidad)
2. [1. ¿Qué es JWT y para qué lo usamos?](#1-qué-es-jwt-y-para-qué-lo-usamos)
3. [2. Estructura del token JWT](#2-estructura-del-token-jwt)
4. [3. Instalación de dependencias](#3-instalación-de-dependencias)
5. [4. Creación y validación de tokens JWT](#4-creación-y-validación-de-tokens-jwt)
6. [5. Definición de roles y usuarios simulados](#5-definición-de-roles-y-usuarios-simulados)
7. [6. Middleware de autorización](#6-middleware-de-autorización)
8. [7. Protección de rutas con roles](#7-protección-de-rutas-con-roles)
9. [8. Pruebas de endpoints protegidos](#8-pruebas-de-endpoints-protegidos)
10. [✅ Recomendaciones finales](#✅-recomendaciones-finales)

---

## Objetivos de la unidad

* Implementar autenticación JWT en FastAPI.
* Definir y aplicar roles de usuario (`admin`, `operador`).
* Proteger rutas mediante autorización basada en roles.
* Desarrollar pruebas de seguridad para endpoints protegidos.

---

## 1. ¿Qué es JWT y para qué lo usamos?

JWT (JSON Web Token) es un estándar para transmitir información segura entre partes. Se compone de tres partes: encabezado, payload y firma.
En nuestro sistema lo usamos para:

* Autenticar usuarios mediante tokens.
* Incluir su rol y nombre en el token.
* Validar cada petición a la API.

---

## 2. Estructura del token JWT

Un token tiene tres partes codificadas en base64 y separadas por puntos:

```
header.payload.signature
```

Ejemplo de payload usado en este proyecto:

```json
{
  "sub": "operador_1",
  "rol": "operador",
  "exp": 1700000000
}
```

---

## 3. Instalación de dependencias

Instalamos los paquetes necesarios:

```bash
pip install python-jose[cryptography]
```

También deberías tener instalado FastAPI y uvicorn si aún no lo hiciste:

```bash
pip install fastapi uvicorn
```

---

## 4. Creación y validación de tokens JWT

```python
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave-secreta-super-segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

---

## 5. Definición de roles y usuarios simulados

Para esta etapa usamos una estructura simple para simular usuarios:

```python
fake_users_db = {
    "admin": {"username": "admin", "password": "admin123", "rol": "admin"},
    "operador": {"username": "operador", "password": "op123", "rol": "operador"}
}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user
```

---

## 6. Middleware de autorización

Creamos una dependencia que verifica y decodifica el token en cada request:

```python
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        rol = payload.get("rol")
        if username is None or rol is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"username": username, "rol": rol}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
```

---

## 7. Protección de rutas con roles

Podemos proteger rutas agregando condiciones según el rol:

```python
def verify_admin(user=Depends(get_current_user)):
    if user["rol"] != "admin":
        raise HTTPException(status_code=403, detail="Solo admins")
    return user

@app.get("/productos/")
def get_products(current_user=Depends(verify_admin)):
    return {"productos": [...]}
```

Otra ruta accesible por ambos roles:

```python
@app.post("/movimientos/")
def create_movement(current_user=Depends(get_current_user)):
    return {"mensaje": f"Movimiento creado por {current_user['username']}"}
```

---

## 8. Pruebas de endpoints protegidos

Usamos `TestClient` para probar rutas con token:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_token_y_ruta_protegida():
    login_data = {"username": "admin", "password": "admin123"}
    response = client.post("/login", data=login_data)
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/productos/", headers=headers)

    assert response.status_code == 200
```

También testeamos fallos de autenticación:

```python
def test_acceso_no_autenticado():
    response = client.get("/productos/")
    assert response.status_code == 401
```

---

## ✅ Recomendaciones finales

* Por ahora, los usuarios son simulados. En proyectos reales, deben ir en una base de datos.
* El middleware actual cubre la validación básica, pero puede expandirse a logs, auditorías, o integración con OAuth.
* Siempre que protejas rutas críticas, **asegurate de tener pruebas automáticas** que verifiquen los permisos.


