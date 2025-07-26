# Unidad 5 – Administración de la Configuración

## 1. ¿Qué es la administración de la configuración del software?

La administración de la configuración (en inglés *Software Configuration Management*, SCM) es una disciplina esencial para el desarrollo de software que busca **controlar y rastrear cambios** a lo largo del ciclo de vida del sistema.

Incluye:

* Identificar qué debe controlarse (versiones, documentación, código, configuraciones).
* Gestionar los cambios de manera sistemática.
* Asegurar que todos los miembros del equipo trabajen con versiones consistentes.

> Según Sommerville:
> "SCM es un conjunto de actividades que ayudan a identificar y controlar los elementos del software, manejar los cambios sistemáticamente y mantener la integridad del producto a través del tiempo."

---

## 2. Administración del cambio

El software **evoluciona constantemente**. Las causas más comunes de cambio son:

* Nuevos requerimientos del cliente
* Correcciones de errores
* Mejoras de rendimiento o seguridad
* Adaptación a nuevos entornos tecnológicos

Para manejar los cambios se sigue un proceso estructurado:

1. **Solicitud de cambio** (Change Request)
2. **Evaluación del impacto**: técnica, económica y de plazos
3. **Aprobación o rechazo**
4. **Implementación del cambio**
5. **Actualización de la documentación**
6. **Notificación a los equipos afectados**

> Evitar cambios descontrolados reduce el riesgo de errores, incompatibilidades o pérdida de trazabilidad.

---

## 3. Gestión de versiones

Una versión es una **fotografía del sistema en un momento dado**. Se usan herramientas y procesos para registrar qué cambios se hicieron, por quién, y cuándo.

### Tipos de versiones:

* **Versión mayor (major)**: cambios grandes, incompatibles, nuevas funcionalidades.
* **Versión menor (minor)**: mejoras compatibles.
* **Parches o revisiones**: corrección de errores, pequeñas modificaciones.

Ejemplo de esquema de versionado:
`v2.1.4` → (major 2) . (minor 1) . (patch 4)

### Buenas prácticas:

* Usar herramientas como **Git**, **SVN** o **Mercurial**.
* Etiquetar versiones estables (tags).
* Escribir mensajes de commit claros y concisos.
* Asociar cambios a issues o tareas del proyecto.

---

## 4. Construcción del sistema (Build)

Una *build* es el **proceso automático de compilar, enlazar, empaquetar y preparar** el sistema para pruebas o entrega.

Incluye:

* Validar que el código compila correctamente.
* Ejecutar pruebas automáticas (unitarias, integración).
* Empaquetar artefactos (por ejemplo, un archivo `.whl`, `.jar`, `.exe`).
* Generar documentación técnica (opcional).

Este proceso puede automatizarse con herramientas como:

* **GitHub Actions**
* **GitLab CI/CD**
* **Jenkins**
* **Make, Gradle, Maven, npm**

---

## 5. Gestión de entregas de software (*release management*)

Consiste en planificar y controlar **cuándo, cómo y qué versiones del software** se entregan a los usuarios o clientes.

Incluye:

* Definir hitos importantes (versiones alfa, beta, producción).
* Establecer un calendario de releases.
* Crear notas de versión claras (changelog).
* Validar la estabilidad y calidad del sistema antes de liberar.
* Empaquetar y distribuir artefactos de forma segura.

### Ciclo típico de versiones:

```
→ Desarrollo → Testing interno → Beta → Release Candidate → Producción
```

En contextos modernos, se busca una estrategia de **entregas frecuentes y automatizadas**, conocida como **DevOps** o **Entrega continua** (*Continuous Delivery*).

---

## Conclusión

La administración de la configuración no es solo técnica, sino también organizativa. Permite:

* Evitar conflictos entre desarrolladores
* Garantizar reproducibilidad de versiones anteriores
* Trazar la evolución del software
* Reducir riesgos de errores en producción

Una correcta implementación de SCM es clave para proyectos profesionales, especialmente en equipos distribuidos o con múltiples integrantes.
