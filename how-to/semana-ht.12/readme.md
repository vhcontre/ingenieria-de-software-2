#  How to 10: Dockerización


###  Objetivos principales

| Objetivo                                                      | Estado       |
| ------------------------------------------------------------- | ------------ |
|  Dockerización del backend y base de datos                  | ✅ Completado |
|  Integración de CI/CD con GitHub Actions (simulada o local) | ✅ Completado |

---

###  Aprendizajes y decisiones técnicas

| Tema                             | Detalle                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
|  Contenerización con Docker    | Se crearon imágenes Docker para el backend FastAPI y para la base de datos (PostgreSQL o SQLite) |
|  Docker Compose                | Orquestación de servicios para facilitar despliegue y desarrollo local                           |
|  CI/CD con GitHub Actions      | Workflow configurado para construir imágenes, ejecutar tests y simular despliegues               |
|  Variables de entorno          | Se parametrizó configuración sensible como URLs de base de datos, claves secretas, puertos       |
|  Montaje de volúmenes          | Datos persistentes para la base de datos dentro del contenedor                                   |
|  Manejo de dependencias Python | Uso de `requirements.txt` y virtual environments dentro del contenedor                           |

---

### ✅ Avances realizados

| Implementación                                        | Estado                  |
| ----------------------------------------------------- | ----------------------- |
| Dockerfile para backend FastAPI                       | ✅ Funcional             |
| Dockerfile o imagen oficial para base de datos        | ✅ Integrada             |
| Archivo `docker-compose.yml` para orquestar servicios | ✅ Configurado y probado |
| GitHub Actions configurado para CI/CD                 | ✅ Ejecuta tests y build |
| Documentación para uso y despliegue con Docker        | ✅ Actualizada           |

---

###  Estado del proyecto al cierre de la semana 10

* Proyecto listo para ser desplegado con Docker en cualquier entorno.
* Proceso de desarrollo y pruebas automatizado con GitHub Actions.
* Configuración segura y parametrizada.
* Base para futuras mejoras en despliegue y escalabilidad.

---

### ️ Archivos clave modificados / agregados

* `Dockerfile` (backend)
* `docker-compose.yml`
* `.github/workflows/ci.yml` (actualizado con pasos de docker build/test)
* `README.md` o `docs/Estado_Semana10.md` (documentación docker y CI/CD)

---

###  Recomendaciones finales

* Verificar que el entorno local Docker funcione antes de desplegar en producción.
* Mantener las imágenes actualizadas y usar tags semánticos.
* Documentar los comandos principales para arrancar, parar y reconstruir contenedores.
* Continuar con pruebas automatizadas para asegurar estabilidad.