# 📅 Semana 2 – Diseño del Modelo de Dominio

## 📌 Índice

1. [Objetivos principales](#objetivos-principales)
2. [¿Por qué usar SQLite en lugar de MySQL?](#por-qué-usar-sqlite-en-lugar-de-mysql)
3. [Modelo de dominio y casos de uso](#modelo-de-dominio-y-casos-de-uso)
4. [Modelo de clases con SQLAlchemy ORM](#modelo-de-clases-con-sqlalchemy-orm)
5. [Inicialización de la base de datos](#inicialización-de-la-base-de-datos)
6. [Diseño en capas: ORM, Dominio y Schemas](#diseño-en-capas-orm-dominio-y-schemas)
7. [Estructura recomendada del proyecto](#estructura-recomendada-del-proyecto)
8. [Pruebas unitarias con Pytest](#pruebas-unitarias-con-pytest)

---

## Objetivos principales

| Semana | Objetivos principales                                             |
| ------ | ----------------------------------------------------------------- |
| 2      | ⚙️ Diseño del modelo de dominio                                   |
|        | 📁 Estructura inicial del backend (FastAPI + SQLAlchemy + SQLite) |
|        | 🧪 Primeras pruebas unitarias simples                             |

---

## ¿Por qué usar SQLite en lugar de MySQL?

**Sí, absolutamente.** Para un entorno educativo, **SQLite es ideal** por su facilidad, portabilidad y menor necesidad de configuración.

### 🔹 Ventajas

| Beneficio                          | Por qué es útil                         |
| ---------------------------------- | --------------------------------------- |
| 🧱 Sin servidor externo            | No requiere instalación adicional       |
| ⚡ Fácil de iniciar                 | Se crea como un archivo `.db`           |
| 🎒 Ligero y portátil               | Funciona en cualquier sistema operativo |
| 💻 Menos dependencias              | Sólo `sqlite3` y `SQLAlchemy`           |
| 📚 Ideal para FastAPI + SQLAlchemy | Rápido de integrar                      |

### 🔻 Desventajas (no problemáticas)

| Limitación                                   | ¿Afecta en este proyecto?          |
| -------------------------------------------- | ---------------------------------- |
| No sirve para alta concurrencia              | ❌ No es necesario                  |
| No soporta todas las funciones SQL avanzadas | ❌ No se utilizarán                 |
| No se usa en producción real                 | ✅ Pero no es el objetivo del curso |

✅ **Conclusión:** usar SQLite para desarrollo es la mejor decisión en este caso.

---

## Modelo de Dominio y Casos de Uso

📄 [`modelo-dominio.md`](#)

```markdown
# 🧩 Modelo de Dominio

## Entidades

### Producto
- id, nombre, sku, descripción (opcional), stock_global (calculado)

### Depósito
- id, nombre, ubicación

### Movimiento
- id, producto_id, depósitos (origen/destino), cantidad, fecha, tipo ('ingreso', 'egreso', 'traslado')

## Relaciones
- Producto tiene movimientos
- Movimiento vincula productos y depósitos
```

📄 [`casos-de-uso.md`](#)

```markdown
## Actores
- Administrador: gestiona productos y depósitos
- Operario: realiza movimientos

## Casos de uso
1. Registrar producto
2. Registrar depósito
3. Ingresar stock
4. Egresar stock
5. Trasladar producto
6. Consultar inventario
```

---

## Modelo de Clases con SQLAlchemy ORM

📁 Estructura:

```
app/db/models/
├── base.py
├── producto.py
├── deposito.py
├── movimiento.py
├── usuario.py
└── __init__.py
```

Se implementaron modelos con relaciones y buenas prácticas.

🔗 Ejemplos destacados:

* `Base` con `__repr__`, `__eq__`, `to_dict()`, `to_json()`
* `Producto`, `Deposito`, `Movimiento` con relaciones ORM
* `Usuario` y `Rol` con tabla intermedia `usuario_rol`

---

## Inicialización de la Base de Datos

📁 `app/create_db.py`:

```python
Base.metadata.create_all(bind=engine)
```

📄 `.env`:

```
DATABASE_URL=sqlite:///./test.db
```

📦 Requisitos:

```
fastapi
uvicorn
sqlalchemy
pydantic
python-dotenv
```

🛠️ Ejecutar:

```bash
python -m app.create_db
```

📊 DB visual: [DB Browser for SQLite](https://sqlitebrowser.org)

---

## Diseño en Capas: ORM, Dominio y Schemas

```plaintext
FastAPI/API
   ⬇
Pydantic Schemas
   ⬇
Domain Models (puro Python)
   ⬇
ORM SQLAlchemy
```

🔄 Se implementaron:

* `app/db/models/` (ORM)
* `app/domain/models/` (Dominio puro)
* `app/schemas/` (Pydantic DTOs)

---

## Estructura Recomendada del Proyecto

```
project/
├── app/
│   ├── db/models/       ← SQLAlchemy
│   ├── domain/models/   ← Clases puras de dominio
│   ├── schemas/         ← Esquemas de entrada/salida
│   └── main.py          ← FastAPI app
├── tests/               ← Pytest unit tests
│   └── schemas/
├── .env
└── requirements.txt
```

---

## Pruebas Unitarias con Pytest

🧪 Ejemplo: `tests/schemas/test_producto_schema.py`

```python
def test_producto_create_valido():
    producto = ProductoCreate(nombre="Pepsi", sku="PEP-001")
    assert producto.nombre == "Pepsi"
```

🔍 Validaciones cubiertas:

* Esquemas válidos e inválidos
* Restricciones de campos (mínimo, tipo)
* `model_validate` con objetos ORM

🧪 Configuración:

* Base de datos en memoria (`sqlite:///:memory:`)
* `conftest.py` con `TestClient` y sesiones de prueba

---

✅ Resultado al cierre de la semana

| Etapa                                                  | Estado      |
| ------------------------------------------------------ | ----------- |
| ⚙️ Diseño del modelo de dominio                        | ✅ Completo  |
| 📁 Estructura inicial del backend                      | ✅ Completo  |
| 🧪 Primeras pruebas unitarias (schemas y validaciones) | ✅ Completas |

---


