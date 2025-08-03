#  How to 6 – Pruebas de integración, Documentación con Swagger y CI con GitHub Actions

---

##  Objetivos de la Unidad 6

* Implementar pruebas de integración que validen flujos completos del sistema.
* Documentar los endpoints REST usando Swagger con FastAPI para facilitar el consumo de la API.
* Configurar un pipeline de integración continua (CI) con GitHub Actions para automatizar pruebas y análisis de código.

---

## 1. Pruebas de integración

### ¿Qué son las pruebas de integración?

Las pruebas de integración verifican que múltiples partes del sistema trabajen correctamente juntas, simulando escenarios reales de uso.

> Por ejemplo:
>
> 1. El usuario hace login y obtiene un token JWT.
> 2. Usa ese token para crear un producto.
> 3. Registra movimientos de entrada y salida para ese producto.
> 4. Finalmente, verifica que el stock esté actualizado.

### ¿Por qué son importantes?

* Detectan problemas en la interacción entre capas (API, base de datos, seguridad).
* Simulan el comportamiento real que tendrá un cliente de la API.
* Complementan a los tests unitarios que validan partes aisladas.

---

### Ejemplo: test de flujo completo de integración

```python
# tests/integration/test_flujo_completo.py

def test_complete_flow(client, db_session):
    # Crear usuario admin en la base
    crear_usuario_con_rol(db_session, "admin", "admin123", "admin")

    # Login para obtener token JWT
    login_response = client.post(
        "/auth/login", data={"username": "admin", "password": "admin123"}
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Crear un producto nuevo
    producto_data = {"nombre": "Laptop", "sku": "LT123", "stock_minimo": 2}
    r_producto = client.post("/productos/", json=producto_data, headers=headers)
    assert r_producto.status_code == 201

    # Registrar movimiento de entrada (stock)
    movimiento_entrada = {"sku_producto": "LT123", "tipo": "entrada", "cantidad": 5}
    r_entrada = client.post("/movimientos/", json=movimiento_entrada, headers=headers)
    assert r_entrada.status_code == 201

    # Registrar movimiento de salida (stock)
    movimiento_salida = {"sku_producto": "LT123", "tipo": "salida", "cantidad": 3}
    r_salida = client.post("/movimientos/", json=movimiento_salida, headers=headers)
    assert r_salida.status_code == 201

    # Consultar stock final y verificar que sea 2 (5 - 3)
    r_stock = client.get("/productos/LT123/stock", headers=headers)
    assert r_stock.status_code == 200
    assert r_stock.json()["stock_actual"] == 2
```

> **Nota:** Asegurarse que el `client` y `db_session` sean fixtures configuradas para pruebas, y que la creación de usuarios y roles funcione correctamente.

---

## 2. Documentación con Swagger en FastAPI

### ¿Qué es Swagger?

Swagger es una interfaz web que FastAPI genera automáticamente para documentar los endpoints y facilitar su prueba sin necesidad de un cliente externo.

### Cómo mejorar la documentación de tus endpoints:

* Añadiendo `summary` y `description` a los métodos de los routers.
* Usando modelos Pydantic en `response_model` para mostrar la estructura de respuesta.
* Añadiendo ejemplos claros en los modelos o en la documentación.

### Ejemplo de endpoint documentado

```python
from fastapi import APIRouter

router = APIRouter()

@router.post(
    "/productos/",
    response_model=ProductoResponse,
    summary="Crear un producto nuevo",
    description="Este endpoint permite crear un producto con SKU único y stock mínimo.",
)
async def create_product(producto: ProductoCreate):
    # Lógica para crear producto
    pass
```

### Verificación

Luego de ejecutar la aplicación, acceder a `http://localhost:8000/docs` para ver la documentación interactiva.

---

## 3. Integración continua con GitHub Actions

### ¿Por qué usar CI?

* Automatiza la ejecución de tests en cada cambio de código.
* Mejora la calidad y evita que errores lleguen a producción.
* Facilita la colaboración en equipo.

### Configuración básica del workflow `ci.yml`

Crear el archivo `.github/workflows/ci.yml` en tu repositorio con este contenido:

```yaml
name: CI - Test y Lint

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Clonar repositorio
      uses: actions/checkout@v3

    - name: Configurar Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.11"

    - name: Instalar dependencias
      run: |
        python -m venv venv
        source venv/bin/activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest ruff

    - name: Ejecutar tests
      run: |
        source venv/bin/activate
        pytest -v

    - name: Ejecutar linter Ruff
      run: |
        source venv/bin/activate
        ruff check app tests
```

---

## 4. Siguientes pasos recomendados

* Completar los tests de integración para todos los flujos críticos.
* Revisar y mejorar la documentación con ejemplos y descripciones claras.
* Mantener actualizado el pipeline de CI agregando más herramientas si es necesario (e.g. cobertura de tests).
* Crear tags o releases para marcar versiones estables al final de cada sprint.

---

## Resumen rápido de comandos útiles

* Ejecutar tests localmente:

```bash
pytest -v
```

* Ejecutar linter Ruff localmente:

```bash
ruff check app tests
```

* Crear tag de versión estable:

```bash
git tag -a v0.6.0 -m "Versión estable cierre de Semana 6"
git push origin v0.6.0
```
