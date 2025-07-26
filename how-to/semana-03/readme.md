### 📌 Paso 1: Resumen general de la **Semana 3 - IS2**

Vamos a hacer memoria de lo trabajado hasta ahora, con foco en la continuidad:

#### ✅ Hasta la Semana 2:

* **Modelo de dominio** diseñado
* **ORM con SQLAlchemy** creado (clases `Product`, `Movement`)
* **Pydantic schemas** implementados
* Primeras **pruebas unitarias** con `pytest` funcionando
  → Todo centrado en validar el **modelo de negocio** y su coherencia estructural.

---

### 🚀 Semana 3 – Objetivo central

> **Construcción de los servicios de lógica de negocio y la capa de acceso a datos**

#### 🧩 Componentes clave esperados:

* Carpeta `services/` con funciones como `create_product`, `get_product_by_id`, `list_products`
* Carpeta `repositories/` o `db_access/` con funciones de acceso tipo `insert_product`, `query_product_by_id`, etc.
* Reutilización del modelo SQLAlchemy
* Validación usando los **schemas de entrada/salida**
* **Pruebas unitarias de los servicios** con `pytest`
* Posible separación de DTOs vs Entidades

---

### 📁 Estructura típica esperada

```
📦 project_root/
├── models/
│   └── product.py
├── schemas/
│   └── product_schema.py
├── services/
│   └── product_service.py
├── repositories/
│   └── product_repository.py
├── tests/
│   ├── test_product_service.py
│   └── ...
```