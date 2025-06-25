## 📅 Formularios web para movimientos

| Semana | Objetivos principales                                             |
| ------ | ----------------------------------------------------------------- |
| 8      | 💾 Formularios web para movimientos                               |
|        | 🧪 Validación y manejo de formularios con Jinja2 y FastAPI        |

----

### Nuevas funcionalidades
- Implementación del formulario web para registrar movimientos (ingreso, egreso, traslado).
- Integración de formulario con backend FastAPI para crear movimientos y actualizar stock.
- Validaciones en backend para controlar existencia de producto, stock suficiente y campos obligatorios.
- Manejo de errores en la interfaz web para mostrar mensajes sin perder datos ingresados.
- Redirección automática tras registro exitoso hacia el listado de productos.
- Uso de plantillas Jinja2 para la presentación de formularios y mensajes de error.
- Mejora en la experiencia de usuario con persistencia de datos en formularios al fallar validaciones.

### Correcciones y mejoras
- Ajustes en el repositorio `MovimientoRepository` para lógica completa de alta con control de stock.
- Eliminación de recarga total de formulario en caso de error, mostrando feedback claro.
- Estructura del proyecto mantenida con rutas organizadas y dependencias correctamente gestionadas.

### Pendientes para próximas semanas
- Ampliar interfaz web con listados dinámicos de movimientos.
- Incorporar paginación y filtros en listados.