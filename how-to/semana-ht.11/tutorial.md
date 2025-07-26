# 📅 How to 9 – Módulo de Alertas y Reportes (FastAPI + Jinja2 + CSV)

## 1. Introducción

En esta semana vamos a implementar un módulo esencial para nuestro sistema: un conjunto de reportes y alertas que nos permitan monitorear el estado del inventario, especialmente para detectar productos bajo stock mínimo. También habilitaremos la exportación de reportes en CSV, mejoraremos la navegación de la interfaz web, y escribiremos pruebas para asegurar calidad.

---

## 2. Preparación del entorno

Asegurarse de tener instaladas estas dependencias en `requirements.txt`:

```bash
pip install fastapi jinja2 aiofiles pandas python-multipart
```

> *Pandas* será usado para generar archivos CSV de forma sencilla.

---

## 3. Diseño de las funcionalidades

### 3.1 Alertas

* Detectar productos cuyo stock actual sea menor que su stock mínimo.
* Mostrar alertas en la interfaz web con listado.

### 3.2 Reportes

* Vista web con tabla de productos con sus stocks.
* Posibilidad de descargar reporte en CSV.
* Filtrado por rango de fechas (movimientos).

### 3.3 Navegación

* Menú con enlaces claros para ir a Productos, Movimientos y Reportes.

---

## 4. Implementación paso a paso

---

### 4.1 Estructura de carpetas y archivos

```
app/
├── templates/
│   ├── base.html
│   ├── productos.html
│   ├── movimientos.html
│   ├── reportes.html        # Nueva plantilla para reportes y alertas
├── static/
│   └── styles.css
├── routers/
│   ├── web_interface.py     # Se ampliará para incluir rutas de reportes
│   └── reportes.py         # Nueva ruta para reportes (opcional)
├── repositories/
│   └── reporte_repository.py  # Nueva clase para consultas específicas
```

---

### 4.2 Actualizar plantilla base con menú de navegación

Editá `app/templates/base.html` para agregar un menú más completo:

```html
<nav>
    <a href="/web/productos">Productos</a> |
    <a href="/web/movimientos">Movimientos</a> |
    <a href="/web/reportes">Reportes</a>
</nav>
```

---

### 4.3 Crear plantilla para reportes (`reportes.html`)

```html
{% extends "base.html" %}

{% block title %}Reportes e Alertas{% endblock %}

{% block content %}
<h2>📊 Reportes de Inventario</h2>

<h3>⚠️ Productos bajo stock mínimo</h3>
{% if alertas %}
    <ul>
        {% for producto in alertas %}
            <li>{{ producto.nombre }} - Stock actual: {{ producto.stock }} (Mínimo: {{ producto.stock_minimo }})</li>
        {% endfor %}
    </ul>
{% else %}
    <p>No hay productos con stock bajo el mínimo.</p>
{% endif %}

<hr>

<h3>📥 Descargar reporte CSV</h3>
<form action="/web/reportes/csv" method="get">
    <button type="submit">Descargar CSV de productos</button>
</form>
{% endblock %}
```

---

### 4.4 Crear repositorio para consultas de reportes

`app/repositories/reporte_repository.py`:

```python
from sqlalchemy.orm import Session
from app.domain.models.producto import Producto

class ReporteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_productos_bajo_stock(self):
        return self.db.query(Producto).filter(Producto.stock < Producto.stock_minimo).all()

    def get_all_productos(self):
        return self.db.query(Producto).all()
```

---

### 4.5 Crear rutas para reportes

En `app/routers/reportes.py`:

```python
from fastapi import APIRouter, Request, Depends, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.reporte_repository import ReporteRepository
from app.web_ui import templates
import pandas as pd
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

@router.get("/web/reportes")
def ver_reportes(request: Request, db: Session = Depends(get_db)):
    repo = ReporteRepository(db)
    alertas = repo.get_productos_bajo_stock()
    return templates.TemplateResponse("reportes.html", {"request": request, "alertas": alertas})

@router.get("/web/reportes/csv")
def descargar_reporte_csv(db: Session = Depends(get_db)):
    repo = ReporteRepository(db)
    productos = repo.get_all_productos()

    # Crear DataFrame
    data = [{
        "ID": p.id,
        "Nombre": p.nombre,
        "SKU": p.sku,
        "Stock Actual": p.stock,
        "Stock Mínimo": p.stock_minimo
    } for p in productos]

    df = pd.DataFrame(data)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=productos.csv"
    return response
```

---

### 4.6 Registrar router en `main.py`

```python
from app.routers import reportes

app.include_router(reportes.router)
```

---

### 4.7 Agregar tests para reportes (ejemplo básico)

En `tests/test_reportes.py`:

```python
def test_get_reportes(client, db_session):
    response = client.get("/web/reportes")
    assert response.status_code == 200
    assert "Reportes de Inventario" in response.text

def test_descargar_csv(client, db_session):
    response = client.get("/web/reportes/csv")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"
```

---

## 5. Pruebas manuales

* Levantar servidor
* Acceder a `/web/reportes` y validar listado de alertas
* Descargar CSV y abrirlo con Excel o editor de texto
* Probar navegación desde el menú base

---

## 6. Buenas prácticas y consideraciones

* Mantener consultas en repositorios para separar lógica
* Usar StreamingResponse para descargas de archivos
* Documentar rutas con `summary` y `description` para Swagger
* Agregar tests para asegurar funcionamiento y evitar regresiones

---

## 7. Flujo Git

* Crear branch: `feature/semana-9-reportes`
* Hacer commits claros y descriptivos
* Abrir PR para revisión
* Integrar a `main` cuando esté aprobado

---

## 8. Cierre y resumen

Al terminar esta semana tendrás:

* Un módulo web para visualizar alertas y descargar reportes CSV.
* Navegación mejorada para la interfaz web.
* Tests que validan funcionalidad del módulo.
* Flujo de trabajo en Git profesional para integración y colaboración.
