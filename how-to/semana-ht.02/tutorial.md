###  How to 1 — Setup + GitHub + Análisis del Sistema

````markdown
#  How to 1 — Setup + GitHub + Análisis del Sistema

##  Índice

1. [ Objetivos generales](#-objetivos-generales)
2. [ Setup del entorno](#-setup-del-entorno)
3. [ Estructura del proyecto](#-estructura-del-proyecto)
4. [ Estructura de pruebas](#-estructura-de-pruebas)
5. [ Documentación y archivos clave](#-documentación-y-archivos-clave)
6. [⚙️ Configuración y contenedores](#️-configuración-y-contenedores)
7. [ Introducción a Git y GitHub](#-introducción-a-git-y-github)
8. [ Análisis del sistema y diagramas](#-análisis-del-sistema-y-diagramas)
9. [ Entregables de la semana](#-entregables-de-la-semana)
10. [✅ Checklist de comprensión](#-checklist-de-comprensión)

---

##  Objetivos generales

- Configurar el entorno de desarrollo profesional.
- Comprender la estructura técnica del proyecto base.
- Introducir conceptos de Git y GitHub con flujo de ramas.
- Iniciar el análisis del sistema con primeros modelos conceptuales.

---

##  Setup del entorno

### Requisitos mínimos:

- Visual Studio Code instalado
- Python 3.10+
- Git instalado y cuenta en GitHub
- Plantillas Jinja2 habilitadas para frontend

### Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate.bat      # Windows
````

### Instalar paquetes base:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic
```

---

##  Estructura del proyecto

```
inventario-2025/
├── backend/
│   ├── app/
│   │   ├── api/             # Rutas agrupadas por entidad
│   │   ├── core/            # Configuración general
│   │   ├── db/              # Conexión + modelos + schemas
│   │   ├── domain/          # Lógica pura del negocio
│   │   ├── services/        # Reglas de negocio
│   │   ├── templates/       # Plantillas Jinja2
│   │   └── main.py          # Entry point
│   ├── alembic/             # Migraciones
│   └── scripts/             # Auxiliares
├── docs/                    # Diagramas y documentación por semana
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

##  Estructura de pruebas

```
test/
├── api/
├── db/
├── domain/
├── integration/
├── repositories/
├── schemas/
├── security/
├── services/
└── conftest.py
```

---

##  Documentación y archivos clave

| Archivo          | Descripción                    |
| ---------------- | ------------------------------ |
| `README.md`      | Guía general del proyecto      |
| `changelog.md`   | Historial de cambios semanales |
| `docs/semana-X/` | Entregables de cada etapa      |

---

## ⚙️ Configuración y contenedores

* `docker-compose.yml`: backend + base de datos
* `Dockerfile`: imagen backend
* `.env`: configuración sensible
* `.gitignore`: exclusiones necesarias

---

##  Introducción a Git y GitHub

### Conceptos clave:

* ¿Qué es Git / GitHub?
* Flujo: `clone → branch → add → commit → push → PR`
* Fork, Pull Request, `.gitignore`
* Uso de Issues para dividir tareas

### Inicializar proyecto:

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<<user>>/inventario-2025.git
git push -u origin main
```

### Buenas prácticas:

* Commits atómicos y frecuentes
* Mensajes claros y descriptivos
* PR con resumen de avances y dudas

---

##  Análisis del sistema y diagramas

### Caso de uso general:

> “Como operador quiero registrar entradas y salidas de productos en distintos depósitos, para mantener actualizado el stock y recibir alertas si algún producto baja del mínimo permitido.”

### Casos de uso clave:

* ABM de productos y depósitos
* Movimiento de stock
* Login y permisos
* Consulta de stock
* Alertas

### Diagramas sugeridos:

* Diagrama de casos de uso
* Modelo de entidades inicial
* Flujo de stock (entrada/salida)

 Subir `.drawio` y captura como imagen en `docs/semana-1/`

---

##  Entregables de la semana

* [ ] Repositorio en GitHub con estructura básica
* [ ] README inicial completo
* [ ] Pull request hecho desde rama personalizada
* [ ] Casos de uso redactados (en Markdown)
* [ ] Diagramas subidos en `/docs/semana-1/`

---

## ✅ Checklist de comprensión

* [ ] Pude crear y activar un entorno virtual
* [ ] Instalé correctamente FastAPI y dependencias
* [ ] Sé hacer un `git commit` y un `git push`
* [ ] Comprendo el caso de uso general del sistema
* [ ] Puedo explicar qué hace cada carpeta del backend
