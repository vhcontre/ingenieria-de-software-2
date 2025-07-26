## 📦 Semana 4 – Módulo de Movimientos de Stock + Reglas de Negocio

| Semana | Objetivos principales                                                                          |
| ------ | ---------------------------------------------------------------------------------------------- |
| 4      | 📦 Iniciar el CRUD de movimientos (entrada/salida)                                             |
|        | 🔄 Establecer relaciones entre entidades (producto ↔ depósito ↔ movimiento)                    |
|        | 🧪 Implementar y testear validaciones de stock                                                 |
|        | 🌐 (Opcional) Iniciar el primer formulario web con FastAPI + Jinja2 para registrar movimientos |

---

### 🎯 Objetivos específicos de la semana

* [x] Crear la **entidad Movimiento** en dominio y base de datos
* [x] Definir relaciones: `producto_id`, `deposito_id` (FK en ORM y dominio)
* [x] Implementar validaciones de lógica de negocio (stock positivo, existencia de entidades)
* [x] Crear consola de movimientos (o endpoint/form si se avanza con FastAPI)
* [x] Calcular stock acumulado a partir de los movimientos

---

### 🧱 Modelo de dominio: `Movimiento`

Se creó el modelo `Movimiento` en la capa de dominio, con atributos:

```python
class Movimiento:
    def __init__(self, id, tipo, cantidad, producto_id, deposito_id, fecha):
        self.id = id
        self.tipo = tipo  # "entrada" o "salida"
        self.cantidad = cantidad
        self.producto_id = producto_id
        self.deposito_id = deposito_id
        self.fecha = fecha
```

> 🧠 Se comienza a aplicar **DDD (Domain-Driven Design)**: la entidad contiene lógica de validación y no es solo un contenedor de datos.

---

### 🗃️ ORM: tabla `movimientos`

```python
class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id = Column(UUID, primary_key=True, default=uuid4)
    tipo = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)
    producto_id = Column(UUID, ForeignKey("productos.id"))
    deposito_id = Column(UUID, ForeignKey("depositos.id"))
    fecha = Column(DateTime, default=datetime.utcnow)
```

> ✅ Se agregan claves foráneas a `productos` y `depositos`, consolidando las relaciones.

---

### 🔄 Relaciones entre entidades

* Un **movimiento** siempre refiere a un producto y un depósito existentes.
* Se valida en consola o servicio que ambos existan antes de registrar.
* Para un **movimiento de salida**, debe haber stock suficiente en ese depósito.

---

### 🧪 Validaciones de lógica de negocio

Desde la consola o el servicio se aplican:

* ❌ No se permite cantidad ≤ 0
* ❌ No se permite registrar una salida con stock insuficiente
* ❌ No se permite registrar si el producto o depósito no existen
* ✅ Se puede consultar stock acumulado por producto y depósito

---

### 📈 Cálculo de stock

Se implementa una función o servicio para calcular el stock:

```python
def calcular_stock(producto_id, deposito_id) -> int:
    entradas = sum(m.cantidad for m in movimientos if m.tipo == "entrada")
    salidas = sum(m.cantidad for m in movimientos if m.tipo == "salida")
    return entradas - salidas
```

> Se puede adaptar a un `StockService` en el dominio si se prefiere encapsular mejor esta lógica.

---

### 🖥️ Consola de movimiento (si aplica)

```
1. Registrar movimiento
2. Listar movimientos
3. Consultar stock actual de producto en depósito
0. Volver al menú principal
```

---

### 🌐 (Opcional) Primer formulario web

Si el grupo avanzó con FastAPI + Jinja2, se creó una vista con formulario:

* Inputs: tipo (entrada/salida), producto, depósito, cantidad
* Validaciones en backend con Pydantic
* Al registrar, redirecciona a la lista o muestra confirmación

---

### 🧪 Pruebas (si se implementaron)

* Se pueden escribir pruebas unitarias para:

  * Verificar que no se permite stock negativo
  * Verificar que se rechazan movimientos con IDs inexistentes
  * Confirmar que el stock acumulado se calcula correctamente

---

### 📚 Vinculación teórica (Somerville)

* **Unidad 3 / 4**: lógica de negocio → reglas de consistencia
* **Unidad 5**: relaciones entre entidades, diseño robusto
* **Unidad 6**: modelo de datos, constraints, dominio orientado a reglas