# Unidad 1 – Medición y Métricas del Software

## 1. Conceptos fundamentales

### Medida, métrica e indicador

* **Medida**: Es el valor cuantitativo asignado a un atributo de un producto o proceso de software. Ejemplo: cantidad de líneas de código (LOC).
* **Métrica**: Es una función que transforma medidas en información útil para el análisis. Por ejemplo, la complejidad ciclomática se calcula a partir del número de nodos y aristas en un grafo de control de flujo.
* **Indicador**: Es una métrica o conjunto de métricas interpretadas en un contexto específico para tomar decisiones. Por ejemplo: "defectos por cada 1.000 LOC".

**Relación jerárquica**:
Medida → Métrica → Indicador

---

## 2. Clasificación de métricas según su propósito

### Métricas de producto

Evalúan las características del software producido:

* Tamaño (LOC, número de funciones)
* Complejidad (ciclomática, Halstead)
* Calidad (defectos, cumplimiento de requerimientos)

### Métricas de proceso

Relacionadas con cómo se desarrolla el software:

* Tiempo de desarrollo
* Tasa de fallas durante pruebas
* Productividad (funciones entregadas por mes)

### Métricas de proyecto

Orientadas al control de gestión:

* Progreso respecto al cronograma
* Porcentaje de tareas completadas
* Desviaciones de esfuerzo estimado

---

## 3. Métricas por fase del ciclo de vida del software

| Fase                  | Métricas típicas                                                                 |
| --------------------- | -------------------------------------------------------------------------------- |
| Requisitos / Análisis | Número de requisitos funcionales / no funcionales, entidades, casos de uso       |
| Diseño                | Acoplamiento, cohesión, profundidad de herencia, tamaño de módulos               |
| Implementación        | LOC, Halstead, complejidad ciclomática, número de métodos por clase              |
| Pruebas               | Porcentaje de cobertura, defectos por módulo, tasa de detección de errores       |
| Mantenimiento         | Tiempo medio entre fallos (MTBF), esfuerzo de mantenimiento, defectos corregidos |

---

## 4. Métricas para interfaz de usuario

* Número de pantallas o formularios
* Tiempo promedio de respuesta
* Número de acciones por tarea
* Número de pasos requeridos para una operación

Estas métricas ayudan a evaluar la usabilidad y eficiencia desde la perspectiva del usuario.

---

## 5. Métricas para la calidad del software

La calidad puede medirse a través de atributos como:

* **Fiabilidad**: tasa de errores, disponibilidad
* **Eficiencia**: tiempo de respuesta, uso de memoria
* **Mantenibilidad**: facilidad para localizar y corregir fallos
* **Portabilidad**: facilidad para migrar entre plataformas

Ejemplos:

* Número de defectos encontrados durante pruebas
* Densidad de defectos (defectos / 1.000 LOC)
* Porcentaje de código cubierto por tests

---

## 6. Métricas técnicas

### Métricas del código fuente

* **LOC**: número de líneas de código reales
* **Halstead**: métricas basadas en operadores y operandos

  * Longitud del programa
  * Volumen
  * Dificultad
  * Esfuerzo
* **Complejidad ciclomática (McCabe)**: mide los caminos lógicos posibles en un módulo

  * Fórmula: V(G) = E − N + 2P

    * E: aristas del grafo
    * N: nodos
    * P: componentes conexas

### Métricas del modelo de análisis y diseño

* Número de clases, atributos, relaciones
* Fan-in y fan-out de módulos
* Profundidad de herencia
* Número de métodos por clase

---

## 7. Adaptación de métricas a PyMEs

* Las pequeñas y medianas empresas pueden seleccionar un conjunto reducido de métricas:

  * LOC y defectos detectados
  * Productividad básica: funciones entregadas por semana
  * Tiempo invertido por tarea
  * Defectos post-entrega

El objetivo no es medir todo, sino aquello que permita **mejorar decisiones con bajo costo**.

---

## 8. Integración de métricas al proceso de Ingeniería de Software

* Las métricas deben integrarse desde el inicio del proceso y no sólo en etapas finales.
* Se recomienda establecer métricas por objetivo:

  * Control de calidad
  * Mejora continua
  * Evaluación de productividad
  * Planificación de recursos
* Las herramientas automatizadas (como SonarQube, PyLint, Test Coverage tools) pueden facilitar la recolección y análisis continuo de métricas.

---

## 9. Conclusiones

* Las métricas no son un fin en sí mismas, sino herramientas para tomar mejores decisiones técnicas y de gestión.
* Deben ser simples, relevantes y accionables.
* Es importante revisar periódicamente su utilidad, eliminando aquellas que no aporten valor.
* Su aplicación debe adaptarse al tamaño del equipo y madurez del proceso.
