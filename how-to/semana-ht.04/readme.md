### 🚀 How to 3 – Objetivo central

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