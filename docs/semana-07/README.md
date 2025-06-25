## 📅 Integración de Jinja2

| Semana | Objetivos principales                                             |
| ------ | ----------------------------------------------------------------- |
| 7      | 🌐 Integración de Jinja2 para interfaz web                        |
|        | 📄 Creación de plantillas y rutas web básicas                     |


# 📅 Semana 7 – Interfaz Web con Jinja2

## 🎯 Objetivos alcanzados

- 🌐 Integración de Jinja2 como motor de plantillas web en FastAPI
- 📄 Creación de vistas HTML para mostrar productos
- 🧱 Uso de base.html como plantilla base para layout común
- 🧭 Navegación web básica entre secciones
- 📊 Visualización dinámica del stock de productos desde base de datos

---

## 📁 Estructura y cambios clave

- `app/main.py`: se agregó soporte para plantillas (`Jinja2Templates`)
- `app/routers/web_interface.py`: nuevas rutas tipo `GET /web/...`
- `app/templates/base.html`: plantilla base reutilizable
- `app/templates/productos.html`: tabla con productos usando Jinja2
- `app/static/`: carpeta creada para incluir archivos CSS en el futuro
- `requirements.txt`: se agregó `python-multipart` como dependencia requerida

---

## ✅ Pruebas realizadas

- Navegación por `/web/productos` desde el navegador
- Renderización de tabla con datos reales desde base de datos
- Verificación de diseño base y navegación
- Tests funcionales pasando localmente (`pytest`)
- GitHub Actions corregido tras agregar dependencias

---

## 🏁 Cierre de semana

- Interfaz web inicial operativa y estable
- Preparado el entorno para trabajar formularios en Semana 8
