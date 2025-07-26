# 📅 Semana 2 — Gestión del Riesgo + Extensión del Modelo

## 📑 Índice

1. [🎯 Objetivos de la semana](#-objetivos-de-la-semana)
2. [🗣️ Discurso de apertura](#️-discurso-de-apertura)
3. [📘 Teoría aplicada (Somerville)](#-teoría-aplicada-somerville)
4. [💬 Actividad dialógica](#-actividad-dialógica)
5. [🔍 Análisis y extensión del modelo](#-análisis-y-extensión-del-modelo)
6. [🔧 Actividades prácticas de Git](#-actividades-prácticas-de-git)
7. [📝 Entregables de la semana](#-entregables-de-la-semana)
8. [✅ Checklist de comprensión](#-checklist-de-comprensión)

---

## 🎯 Objetivos de la semana

- Comprender el concepto de **riesgo** en el desarrollo de software.
- Aplicar identificación y evaluación de riesgos sobre el proyecto real.
- Mejorar el modelo de dominio con roles, permisos y reglas de negocio.
- Usar Issues en GitHub para trazar tareas vinculadas a riesgos.

---

## 🗣️ Discurso de apertura

> “En todo proyecto, lo que puede fallar... fallará. Pero si lo anticipamos, tenemos el control.”

> “Hoy vamos a identificar **los riesgos reales** del sistema que estamos construyendo. Desde errores humanos hasta pérdida de datos. Vamos a pensar como ingenieros: no sólo escribir código, sino anticiparnos al caos.”

---

## 📘 Teoría aplicada (Somerville)

> *"La gestión del riesgo implica identificar, evaluar y planificar acciones frente a eventos que puedan amenazar el éxito del proyecto."*  
> — *Somerville, Capítulo 22: Gestión del Riesgo*

🎓 Tipos de riesgo:
- Riesgo de proyecto (retrasos, cambios de alcance)
- Riesgo técnico (tecnologías nuevas, errores)
- Riesgo humano (rotación, falta de experiencia)
- Riesgo organizacional (fallas de comunicación, conflictos)

🧠 Herramientas prácticas:
- Matriz de impacto vs. probabilidad
- Lista priorizada de riesgos
- Plan de contingencia (¿qué hacemos si…?)

---

## 💬 Actividad dialógica

**Escenario de conversación**:
> “El equipo trabaja a buen ritmo… pero no hay backups. Un día, un alumno borra accidentalmente la base de datos. ¿Qué hacemos? ¿Lo teníamos previsto?”

🗣 Actividad en grupo:
1. Listar 3 riesgos reales del proyecto.
2. Asignar impacto (Alto / Medio / Bajo).
3. ¿Cuál sería una acción preventiva?

🎯 Resultado: suben la tabla en Markdown a `/docs/semana-2/riesgos.md`

---

## 🔍 Análisis y extensión del modelo

### Actividad:

- Revisar el diagrama de la semana anterior.
- Incorporar entidades para:
  - **Usuario con rol** (admin / operador)
  - **Permisos o restricciones**
  - ¿Hay campos sensibles? ¿Quién puede modificarlos?

🎯 Resultado:
- Diagrama actualizado en `/docs/semana-2/`
- Archivo `.drawio` + export `.png`
- Descripción de decisiones tomadas

---

## 🔧 Actividades prácticas de Git

- Crear **una nueva rama**: `semana-2`
- Asignar Issues según roles del equipo
- Realizar commits con mensaje: `"Asocia a #XX: Mejora en el modelo de usuarios"`
- Crear un Pull Request al finalizar los cambios

🛠 Tip sugerido:
- Incluir `docs/semana-2/` con decisiones de diseño
- Agregar sección `riesgos.md` al PR

---

## 📝 Entregables de la semana

- [ ] Documento `riesgos.md` con 3 riesgos reales analizados
- [ ] Diagrama actualizado con roles/permisos
- [ ] Pull Request desde rama `semana-2` con descripción clara
- [ ] Commits asociados a Issues
- [ ] Capturas del modelo o diagramas en Markdown

---

## ✅ Checklist de comprensión

- [ ] Sé qué es un riesgo en un proyecto de software
- [ ] Puedo clasificar al menos 3 tipos de riesgo
- [ ] Comprendí cómo usar GitHub Issues para trazar acciones vinculadas a riesgos
- [ ] Actualicé correctamente el modelo de datos y subí el nuevo diagrama

---
