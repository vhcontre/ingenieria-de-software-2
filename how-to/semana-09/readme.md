# 📅 Semana 9: Módulo de Alertas y Reportes

| Objetivo principal                               | Descripción y pasos clave                                                         |
| ------------------------------------------------ | --------------------------------------------------------------------------------- |
| 📊 **Módulo de alertas y reportes (HTML o CSV)** | Crear reportes visuales y exportables para monitorear stock, movimientos, alertas |
| ✅ **Navegación entre vistas**                    | Agregar navegación fluida entre vistas: productos, movimientos y reportes         |
| 🧪 **Pruebas backend y formularios web**         | Testear correctamente el nuevo módulo con pruebas unitarias y de integración      |
| 🌿 **Flujo Git: rama + PR para integrar módulo** | Trabajar en branch separado, abrir PR para revisión, integrar en main             |

---

## ✅ Paso 1: Diseño del módulo de alertas/reportes

### 1.1 ¿Qué alertas y reportes queremos?

* Alertas de productos bajo stock mínimo.
* Reportes diarios/semanales en HTML (tablas, gráficos básicos) o CSV para exportar.
* Posibilidad de filtrar por rango de fechas y productos.

### 1.2 Implementación técnica sugerida

* Crear ruta en FastAPI para reportes (`/web/reportes`).
* Renderizar plantilla Jinja2 con los datos calculados.
* Agregar botón para descargar CSV.
* Crear un repositorio o servicio para consultas específicas de reportes.

---

## ✅ Paso 2: Navegación entre vistas

* En plantilla base (`base.html`), agregar menú con enlaces a:

  * Productos (`/web/productos`)
  * Movimientos (`/web/movimientos`)
  * Reportes (`/web/reportes`)

---

## ✅ Paso 3: Pruebas

* Tests unitarios para los métodos de consulta de reportes.
* Tests funcionales para vistas web (validar que carga la página, muestra datos, descarga CSV).
* Validar casos extremos: sin datos, con muchos datos, filtros inválidos.

---

## ✅ Paso 4: Flujo Git para integrar módulo

* Crear rama nueva: `feature/semana-9-reportes`
* Desarrollar módulo y pruebas en esa rama.
* Abrir Pull Request con descripción clara.
* Revisar y aprobar PR, luego merge a `main`.

---

## 🧭 Milestone y Issues sugeridos

| Issue Nº | Título                                             | Etiquetas          |
| -------- | -------------------------------------------------- | ------------------ |
| #1       | Crear ruta y vista web para reportes y alertas     | `feature`, `web`   |
| #2       | Implementar exportación CSV para reportes          | `feature`, `csv`   |
| #3       | Agregar navegación en menú base                    | `ui`, `web`        |
| #4       | Tests backend para consultas y generación reportes | `test`, `backend`  |
| #5       | Tests frontend para vistas y formularios           | `test`, `frontend` |
| #6       | Abrir PR desde rama `feature/semana-9-reportes`    | `ci`, `git`        |
