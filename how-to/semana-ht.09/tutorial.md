# 📘 Unidad 7 – Integración de Jinja2 para interfaz web



## 📅 Objetivos principales

* Integrar Jinja2 con FastAPI para renderizar páginas HTML.
* Crear rutas que muestren vistas web con datos reales desde la base.
* Organizar archivos estáticos y plantillas para la interfaz.

---

## ✅ ¿Qué haremos?

1. Instalar `jinja2` y `aiofiles` para soporte de plantillas y archivos estáticos.
2. Configurar FastAPI para servir plantillas y estáticos.
3. Crear una plantilla base (`base.html`) con estructura HTML común.
4. Crear una plantilla que liste productos (`productos.html`).
5. Crear la ruta `/web/productos` que muestra productos de la DB.
6. Registrar el router web en `main.py`.
7. Probar la vista en el navegador.

---

## 🔧 Paso 1: Instalación de dependencias

```bash
pip install jinja2 aiofiles
```

---

## 🧱 Paso 2: Configurar en `main.py`

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")
```

---

## 🗂️ Paso 3: Estructura de carpetas

```
app/
├── static/
│   └── styles.css
├── templates/
│   ├── base.html
│   └── productos.html
├── main.py
└── routers/
    └── web_interface.py
```

---

## 🧪 Paso 4: Plantilla base (`base.html`)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>{% block title %}Inventario{% endblock %}</title>
    <link rel="stylesheet" href="/static/styles.css" />
</head>
<body>
    <header>
        <h1>📦 Sistema de Inventario</h1>
        <nav>
            <a href="/web/productos">Productos</a>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

---

## 📦 Paso 5: Plantilla productos (`productos.html`)

```html
{% extends "base.html" %}

{% block title %}Listado de Productos{% endblock %}

{% block content %}
<h2>📋 Listado de Productos</h2>

<table border="1" cellspacing="0" cellpadding="8">
    <tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>SKU</th>
        <th>Descripción</th>
        <th>Stock Actual</th>
        <th>Stock Mínimo</th>
    </tr>
    {% for producto in productos %}
    <tr>
        <td>{{ producto.id }}</td>
        <td>{{ producto.nombre }}</td>
        <td>{{ producto.sku }}</td>
        <td>{{ producto.descripcion }}</td>
        <td>{{ producto.stock }}</td>
        <td>{{ producto.stock_minimo }}</td>
    </tr>
    {% else %}
    <tr><td colspan="6">No hay productos registrados.</td></tr>
    {% endfor %}
</table>
{% endblock %}
```

---

## 🚏 Paso 6: Crear ruta `/web/productos` (`routers/web_interface.py`)

```python
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.producto_repository import ProductoRepository
from app.main import templates  # o donde definas templates

router = APIRouter()

@router.get("/web/productos")
def ver_productos(request: Request, db: Session = Depends(get_db)):
    repo = ProductoRepository(db)
    productos = repo.get_all_productos()
    return templates.TemplateResponse("productos.html", {"request": request, "productos": productos})
```

---

## ⚙️ Paso 7: Registrar router en `main.py`

```python
from app.routers import web_interface

app.include_router(web_interface.router)
```

---

## 🧪 Paso 8: Probar la vista

* Ejecutá tu API (`uvicorn app.main:app --reload`)
* Abrí en el navegador `http://localhost:8000/web/productos`
* Deberías ver la tabla con los productos cargados desde la base.

---

## ✅ Resumen de la Unidad 7

| Objetivo                                 | Estado  |
| ---------------------------------------- | ------- |
| Instalar y configurar Jinja2 y aiofiles  | ✅ Listo |
| Crear plantilla base y productos         | ✅ Listo |
| Crear ruta web con renderizado dinámico  | ✅ Listo |
| Integrar con base de datos y repositorio | ✅ Listo |
| Probar la visualización en navegador     | ✅ Listo |
