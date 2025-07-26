# 📘 Unidad 7 – Integración de Jinja2 para Interfaz Web

---

## 🎯 Objetivos de la Unidad 7

* Integrar el motor de plantillas Jinja2 con FastAPI para renderizar páginas HTML dinámicas.
* Crear rutas web que sirvan contenido HTML generado con Jinja2.
* Definir plantillas básicas reutilizables para la interfaz de usuario.

---

## 1. ¿Qué es Jinja2 y por qué usarlo?

Jinja2 es un motor de plantillas para Python que permite separar la lógica de negocio del diseño visual, generando HTML dinámico con variables, estructuras condicionales y bucles.

> Ventajas:
>
> * Reutilización de código con plantillas base (layouts).
> * Separación clara entre backend y frontend.
> * Fácil integración con FastAPI y otros frameworks.

---

## 2. Configuración básica de Jinja2 con FastAPI

### Paso 1: Instalar dependencias

Si no lo tenés instalado, agregá `jinja2` y `aiofiles` (para servir archivos estáticos):

```bash
pip install jinja2 aiofiles
```

---

### Paso 2: Configurar FastAPI para usar plantillas Jinja2

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Montar carpeta de archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Crear instancia de templates apuntando a la carpeta templates/
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Pasar variables a la plantilla
    return templates.TemplateResponse("index.html", {"request": request, "title": "Inicio"})
```

---

### Paso 3: Estructura de carpetas recomendada

```
/app
  /static         # CSS, JS, imágenes
  /templates      # Archivos HTML con plantillas Jinja2
  main.py         # Código FastAPI
```

---

## 3. Creación de plantillas básicas

### Plantilla base `base.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>{% block title %}Mi App{% endblock %}</title>
    <link rel="stylesheet" href="/static/styles.css" />
</head>
<body>
    <header>
        <h1>Mi Sistema de Inventario</h1>
        <nav>
            <a href="/">Inicio</a> |
            <a href="/productos">Productos</a> |
            <a href="/movimientos">Movimientos</a>
        </nav>
    </header>

    <main>
        {% block content %}
        <!-- Contenido específico va aquí -->
        {% endblock %}
    </main>

    <footer>
        <p>© 2025 Mi Empresa</p>
    </footer>
</body>
</html>
```

---

### Plantilla `index.html` extendiendo `base.html`

```html
{% extends "base.html" %}

{% block title %}Página de Inicio{% endblock %}

{% block content %}
<h2>Bienvenido al sistema</h2>
<p>Usá el menú para navegar.</p>
{% endblock %}
```

---

## 4. Rutas y vistas web

### Ejemplo de ruta que lista productos

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/productos", response_class=HTMLResponse)
async def list_products(request: Request):
    productos = obtener_productos()  # Función que trae datos de la DB
    return templates.TemplateResponse(
        "productos.html", {"request": request, "productos": productos}
    )
```

---

### Plantilla `productos.html`

```html
{% extends "base.html" %}

{% block title %}Listado de Productos{% endblock %}

{% block content %}
<h2>Productos</h2>
<ul>
    {% for producto in productos %}
    <li>{{ producto.nombre }} - Stock: {{ producto.stock_actual }}</li>
    {% else %}
    <li>No hay productos registrados.</li>
    {% endfor %}
</ul>
{% endblock %}
```

---

## 5. Servir archivos estáticos

* CSS, imágenes y JavaScript deben estar dentro de la carpeta `/static`.
* FastAPI sirve esos archivos con la ruta `/static/...`.
* Recordá referenciarlos en las plantillas con rutas absolutas `/static/...`.

---

## 6. Resumen y próximos pasos

| Paso                                              | Estado                          |
| ------------------------------------------------- | ------------------------------- |
| Configurar Jinja2 con FastAPI                     | ✅ Completo                      |
| Crear plantilla base y extendida                  | ✅ Completo                      |
| Crear ruta para páginas HTML                      | ✅ Completo                      |
| Servir archivos estáticos                         | ✅ Completo                      |
| Integrar datos dinámicos (productos, movimientos) | Pendiente para próximas semanas |

---

## 7. Ejercicio propuesto para estudiantes

* Crear una plantilla `movimientos.html` para listar movimientos de entrada y salida.
* Crear la ruta `/movimientos` que renderice esa plantilla con datos reales.
* Agregar un formulario HTML básico para registrar un nuevo movimiento (sin funcionalidad POST aún).
