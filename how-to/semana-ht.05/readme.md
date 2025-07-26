### 🧩 Semana 4

| Tema                            | Descripción                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 📦 Módulo de movimientos        | Iniciar el CRUD de movimientos de stock (entrada/salida)                                                      |
| 🔄 Relaciones entre entidades   | Asignar productos a depósitos, establecer relaciones (FK) en ORM y dominio                                    |
| 🧪 Pruebas de lógica de negocio | Verificar reglas: no permitir stock negativo, validar existencia de depósito/producto al registrar movimiento |
| 💾 Formularios web (opcional)   | Si hay tiempo: primer acercamiento a una vista web con formulario de carga de movimiento                      |


### 🎯 Objetivo general

Agregar la funcionalidad para **registrar movimientos de stock** entre depósitos, incorporando validaciones, relaciones entre entidades, y consolidando el modelo de dominio.

---

### 🧠 Contenidos técnicos trabajados

#### 1. 🔗 Relaciones entre entidades (Producto, Depósito y Movimiento)

* Se introduce la entidad `Movimiento`.
* Se vincula con `Producto` y `Depósito` mediante ID o referencias (dependiendo del enfoque).
* Definición de los atributos de `Movimiento`:

  ```python
  id: UUID
  fecha: datetime
  tipo: Literal["entrada", "salida"]
  cantidad: int
  producto_id: UUID
  deposito_id: UUID
  ```

#### 2. 🧱 Modelo de dominio

* Se diseña el **modelo `Movimiento` en la capa de dominio**.
* Se crean validaciones de lógica de negocio como métodos de instancia o servicios.
* Consideraciones:

  * No se permite realizar un movimiento con cantidad negativa o cero.
  * No se permite egreso si no hay suficiente stock.
  * Se requiere que el producto y depósito estén registrados.

#### 3. 🗂️ Repositorio y persistencia

* Se implementa el `MovimientoRepository`, análogo a productos y depósitos.
* Se integran los métodos:

  ```python
  add(movimiento: Movimiento)
  list() -> List[Movimiento]
  get_by_id(id: UUID) -> Optional[Movimiento]
  ```

#### 4. 🧪 Reglas de validación (lógica de negocio)

* Validaciones embebidas en servicio o en constructor:

  * `assert producto_existente`
  * `assert deposito_existente`
  * `assert cantidad > 0`
  * Para egresos: `assert stock_actual >= cantidad`

#### 5. 🧾 Consola de interacción

* Se agregan comandos como:

  ```
  [1] Registrar movimiento
  [2] Ver movimientos registrados
  ```
* Se consulta la existencia previa de producto y depósito antes de registrar.
* Se actualiza el stock (acumulado) según el tipo de movimiento.

#### 6. 📈 Acumulación de stock (modelo simple)

* Se construye una función para calcular el stock por producto y depósito:

  ```python
  def calcular_stock(producto_id: UUID, deposito_id: UUID) -> int
  ```
* O bien un `StockService` con métodos:

  ```python
  get_stock(producto_id, deposito_id)
  ```

---

### 📌 Extras opcionales (si el grupo avanzó más)

#### ✔️ Validación con Pydantic

* Se introduce `MovimientoSchema` (entrada y salida).
* Conversión entre esquema y modelo de dominio.

#### ✔️ Comienzo del formulario web (si aplicó)

* Se arma un formulario HTML mínimo para registrar movimiento con FastAPI + Jinja2.
* Se aplican validaciones básicas en frontend/backend.

---

### 📚 Conexión con teoría (Somerville u otros)

* Relación con **Unidad 1: Métricas**: medir cantidad de movimientos, tipos, stock promedio.
* Preparación para **Unidad 4: Pruebas**: ya se trabaja lógica con validaciones simples y se pueden testear.
* Ejemplo de consolidación de **modelo de dominio** con integridad de datos.

