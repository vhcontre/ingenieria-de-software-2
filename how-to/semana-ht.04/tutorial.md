# 📅 Semana 3 – CRUD, Validaciones y Serialización

| Semana | Objetivos principales                        |
| ------ | -------------------------------------------- |
| 3      | 🔄 CRUD de depósitos y productos             |
|        | 🧱 Validaciones y serialización con Pydantic |
|        | 📥 Operaciones básicas desde la consola      |

---

## 1. CRUD de Depósito

Se implementa el repositorio de **Depósito** con funciones básicas:

```python
create_deposito(deposito_in: DepositoCreate) -> DepositoOut  
get_deposito(id: int) -> DepositoOut  
update_deposito(id: int, deposito_in: DepositoUpdate) -> DepositoOut  
delete_deposito(id: int) -> None
```

🧱 Se usan:

* Modelos ORM (`DepositoORM`) para persistencia
* Schemas Pydantic (`DepositoCreate`, `DepositoUpdate`, `DepositoOut`) para validar y serializar
* Mapper ORM ↔ dominio (`deposito_orm_to_domain`)

---

## 2. CRUD de Producto

Se repite la lógica aplicada en depósitos.

✔️ Validación de **SKU único** antes de crear o actualizar un producto:

```python
if self.db.query(ProductoORM).filter_by(sku=producto_in.sku).first():
    raise ValueError("SKU ya existente")
```

---

## 3. Validaciones con Pydantic

Las validaciones están definidas en los schemas. Ejemplo:

```python
class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    sku: str = Field(..., min_length=1)
```

También se utilizan para control de entrada/salida (`ProductoCreate`, `ProductoUpdate`, `ProductoOut`).

---

## 4. Operaciones desde consola

Se creó una consola interactiva con el siguiente menú:

```
1. Crear depósito
2. Consultar depósito
3. Actualizar depósito
4. Eliminar depósito
5. Crear producto
6. Listar productos
0. Salir
```

Permite probar CRUD de manera manual desde terminal y verificar el correcto funcionamiento de los repositorios.

---

## 5. Estructura de carpetas sugerida

```
app/
├── db/
│   └── models/
│       └── deposito.py
├── domain/
│   └── models/
│       └── deposito.py
├── schemas/
│   └── deposito.py
├── repositories/
│   └── deposito_repository.py
├── console/
│   └── deposito_console.py
```

---

## 6. Ejemplo de schema (`schemas/deposito.py`)

```python
from pydantic import BaseModel, Field
from typing import Optional
from pydantic import ConfigDict

class DepositoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    ubicacion: Optional[str] = None

class DepositoCreate(DepositoBase):
    pass

class DepositoUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=1)
    ubicacion: Optional[str] = None

class DepositoOut(DepositoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
```

---

## 7. Ejemplo de repositorio (`repositories/deposito_repository.py`)

```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.db.models.deposito import DepositoORM
from app.schemas.deposito import DepositoCreate, DepositoUpdate
from domain.models.deposito import Deposito
from mappers.deposito_mapper import deposito_orm_to_domain

class DepositoRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, deposito_in: DepositoCreate) -> Deposito:
        orm = DepositoORM(**deposito_in.dict())
        self.db.add(orm)
        self.db.commit()
        self.db.refresh(orm)
        return deposito_orm_to_domain(orm)

    def get(self, deposito_id: int) -> Deposito:
        orm = self.db.query(DepositoORM).filter_by(id=deposito_id).first()
        if orm is None:
            raise NoResultFound(f"Depósito con ID {deposito_id} no encontrado")
        return deposito_orm_to_domain(orm)

    def update(self, deposito_id: int, deposito_in: DepositoUpdate) -> Deposito:
        orm = self.db.query(DepositoORM).filter_by(id=deposito_id).first()
        if orm is None:
            raise NoResultFound(f"Depósito con ID {deposito_id} no encontrado")
        for attr, value in deposito_in.dict(exclude_unset=True).items():
            setattr(orm, attr, value)
        self.db.commit()
        self.db.refresh(orm)
        return deposito_orm_to_domain(orm)

    def delete(self, deposito_id: int) -> None:
        orm = self.db.query(DepositoORM).filter_by(id=deposito_id).first()
        if orm is None:
            raise NoResultFound(f"Depósito con ID {deposito_id} no encontrado")
        self.db.delete(orm)
        self.db.commit()
```

---

## 8. Estado de avance y cierre

| Objetivo Semana 3                         | Estado |
| ----------------------------------------- | ------ |
| CRUD de productos y depósitos             | ✅      |
| Validaciones y serialización con Pydantic | ✅      |
| Operaciones desde consola                 | ✅      |

🧪 También se probaron casos con entradas inválidas y SKU duplicado, mejorando la robustez.

---

## 🏁 Conclusión

> Semana 3 finalizada exitosamente.
> El sistema cuenta con una base sólida: repositorios funcionales, validaciones completas, y pruebas manuales efectivas desde consola.
