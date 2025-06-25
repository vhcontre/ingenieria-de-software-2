# 📦 CHANGELOG

Todas las versiones y mejoras del sistema de inventario.

---

## [v0.6.0] - 2025-06-20

🔒 Versión estable al cierre de **Semana 6**

### 🆕 Features
- Autenticación con JWT (login de usuarios)
- Middleware de autorización por roles (admin / operador)
- Endpoints protegidos según permisos

### 📦 Backend
- CRUD de productos, depósitos y movimientos
- Reglas de negocio de stock mínimo y trazabilidad

### 📄 Documentación
- Swagger generado automáticamente (`/docs` y `/redoc`)
- Esquemas Pydantic actualizados

### ✅ Tests
- Test unitarios para modelos, esquemas y repositorios
- Test de integración completo (login → crear producto → entrada → salida)
- Cobertura de seguridad con roles

### 🔧 DevOps
- Configuración de **GitHub Actions**
  - Ejecución automática de `pytest`
  - Linter Python (`ruff`)
  - Corrección de problemas en pipelines

---

## [v0.5.0] - 2025-06-13

✔️ Semana 5: Inicio de autenticación, creación de modelos `Usuario` y `Rol`.

## [v0.4.0] - 2025-06-06

✔️ Semana 4: Entrada y salida de stock, validación y trazabilidad de movimientos.

## [v0.3.0] - 2025-05-30

✔️ Semana 3: Validación y listados con paginación desde consola.

## [v0.2.0] - 2025-05-24

✔️ Semana 2: Creación de base de datos, modelos iniciales y arquitectura de capas.

## [v0.1.0] - 2025-05-17

🔧 Semana 1: Análisis, diseño del sistema y control de versiones inicial.
