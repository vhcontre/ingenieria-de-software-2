# 📅 Semana 8: Formulario Web para Movimientos con Validación en FastAPI + Jinja2



## Objetivos

* Implementar un formulario web para registrar movimientos de stock (ingresos, egresos, traslados).
* Validar los datos enviados en el backend con FastAPI y mostrar mensajes de error en la interfaz.
* Integrar la lógica de creación de movimientos con el repositorio.
* Mejorar la experiencia de usuario mediante redirección y mensajes claros.

---

## Paso 1 – Crear la plantilla HTML del formulario

En `app/templates/movimiento_form.html` definimos el formulario que el usuario completará:

```html
{% extends "base.html" %}
{% block content %}
<h2>📦 Registrar Movimiento</h2>

<form action="/web/movimientos" method="post">
    <label for="producto_id">Producto ID:</label>
    <input type="number" name="producto_id" required><br>

    <label for="usuario_id">Usuario ID:</label>
    <input type="number" name="usuario_id" required><br>

    <label for="tipo">Tipo de movimiento:</label>
    <select name="tipo" required>
        <option value="ingreso">Ingreso</option>
        <option value="egreso">Egreso</option>
    </select><br>

    <label for="cantidad">Cantidad:</label>
    <input type="number" name="cantidad" required><br>

    <label for="deposito_origen_id">Depósito origen (opcional):</label>
    <input type="number" name="deposito_origen_id"><br>

    <label for="deposito_destino_id">Depósito destino (opcional):</label>
    <input type="number" name="deposito_destino_id"><br>

    <button type="submit">Registrar</button>
</form>

{% if error %}
<p style="color: red;">{{ error }}</p>
{% endif %}
{% endblock %}
```

### Explicación

* El formulario envía una petición POST a `/web/movimientos`.
* Usamos campos básicos como `producto_id`, `usuario_id`, `tipo` (ingreso o egreso), `cantidad` y depósitos opcionales.
* La sección `{% if error %} ... {% endif %}` sirve para mostrar errores devueltos desde el backend.

---

## Paso 2 – Crear las rutas para mostrar y procesar el formulario

En `app/routers/web_interface.py` agregamos las rutas para GET (mostrar formulario) y POST (procesar datos):

```python
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import get_db
from app.repositories.movimiento_repository import MovimientoRepository
from app.domain.models.movimiento import Movimiento, TipoMovimiento as DomainTipoMovimiento
from app.web_ui import templates

router = APIRouter()

@router.get("/web/movimientos")
def mostrar_formulario_movimiento(request: Request):
    return templates.TemplateResponse("movimiento_form.html", {"request": request})

@router.post("/web/movimientos")
def procesar_formulario_movimiento(
    request: Request,
    producto_id: int = Form(...),
    usuario_id: int = Form(...),
    tipo: str = Form(...),
    cantidad: int = Form(...),
    deposito_origen_id: int = Form(None),
    deposito_destino_id: int = Form(None),
    db: Session = Depends(get_db)
):
    try:
        repo = MovimientoRepository(db)

        movimiento = Movimiento(
            id=None,
            producto_id=producto_id,
            usuario_id=usuario_id,
            cantidad=cantidad,
            tipo=DomainTipoMovimiento(tipo),  # Convertimos string a enum
            deposito_origen_id=deposito_origen_id,
            deposito_destino_id=deposito_destino_id,
            fecha=datetime.now().date(),
            timestamp=datetime.now()
        )

        repo.create_movimiento(movimiento)

        # Redirigimos al listado de productos tras éxito
        return RedirectResponse("/web/productos", status_code=303)

    except Exception as e:
        # Si ocurre error, mostramos el formulario con el mensaje de error
        return templates.TemplateResponse(
            "movimiento_form.html",
            {"request": request, "error": str(e)}
        )
```

### Explicación

* `GET /web/movimientos` muestra el formulario vacío.
* `POST /web/movimientos` recibe los datos del formulario, los valida y crea el movimiento con el repositorio.
* En caso de error (por ejemplo, stock insuficiente, producto no existe, etc.), vuelve a mostrar el formulario con el mensaje.
* Usamos `RedirectResponse` con código 303 para evitar repost de formulario al actualizar la página.

---

## Paso 3 – Dependencias necesarias

Para que el procesamiento de formularios funcione con FastAPI, es necesario tener instalado:

```
python-multipart
```

Si no está instalado, podés hacerlo con:

```bash
pip install python-multipart
```

---

## Paso 4 – Probar en el navegador

1. Ejecutá tu aplicación FastAPI con uvicorn:

```bash
uvicorn app.main:app --reload
```

2. Abrí en tu navegador:

```
http://localhost:8000/web/movimientos
```

3. Completa el formulario con datos válidos y envialo.

4. Verificá que:

* Si los datos son correctos, se redirige al listado de productos.
* Si hay algún error, se muestra el mensaje correspondiente sin perder lo que ya ingresaste.

---

## Recomendaciones adicionales

* **Validaciones:** La lógica de validación de stock y reglas de negocio están en el repositorio y modelo dominio. Aprovechamos que el backend levanta excepciones y las mostramos aquí.
* **UX:** Se puede mejorar la interfaz agregando mensajes de éxito, estilos CSS y formularios más amigables en próximas semanas.
* **Extensiones:** En el futuro podés agregar formularios para editar o eliminar movimientos, filtros, y reportes visuales.

---

# Conclusión

Con esta implementación:

* Tus usuarios pueden ingresar movimientos de stock desde una interfaz web sencilla.
* Se asegura la integridad de datos mediante validaciones backend.
* La interacción es clara, con redirección y mensajes de error visibles.
* Está listo para evolucionar hacia una aplicación más completa.