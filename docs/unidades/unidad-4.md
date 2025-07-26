# Unidad 4 – Prueba de Software

## 1. ¿Por qué es importante probar el software?

Las pruebas de software son una parte fundamental del desarrollo. Su objetivo es:

* Detectar errores antes de que el producto llegue al usuario.
* Asegurar que el sistema cumpla con los **requisitos funcionales y no funcionales**.
* Validar que el software se comporta correctamente ante condiciones normales y anómalas.

> "Las pruebas no demuestran que no hay errores, solo que los errores conocidos han sido eliminados."
> (Sommerville)

---

## 2. Fundamentos y objetivos de las pruebas

Las pruebas deben estar presentes desde **tempranas etapas** del desarrollo y forman parte de un proceso de **verificación y validación (V\&V)**.

| Verificación ("¿Hicimos el producto correctamente?") | Validación ("¿Hicimos el producto correcto?")  |
| ---------------------------------------------------- | ---------------------------------------------- |
| Revisa si se sigue el proceso y diseño previsto      | Revisa si satisface los requisitos del usuario |

---

## 3. Diseño de casos de prueba

Diseñar un caso de prueba implica definir:

* Entradas representativas
* Resultados esperados
* Condiciones iniciales
* Procedimientos de ejecución

El diseño puede basarse en la **estructura interna** del programa (caja blanca) o en la **funcionalidad externa** (caja negra).

---

## 4. Pruebas de caja blanca

Se basan en el **análisis del código fuente**.

### Técnicas comunes:

* **Cobertura de sentencias**: cada línea debe ejecutarse al menos una vez.
* **Cobertura de decisiones**: cada camino de decisión (if, switch) se prueba.
* **Pruebas del camino básico**: se prueba cada camino independiente posible.

### Métrica importante:

* **Complejidad ciclomática (McCabe)**:

  Mide la cantidad de caminos independientes en el código.
  Fórmula:
  `V(G) = E - N + 2P`
  Donde:

  * `E`: número de aristas del grafo
  * `N`: número de nodos
  * `P`: número de componentes conectados (normalmente 1)

Una mayor complejidad indica más riesgo y necesidad de pruebas adicionales.

---

## 5. Pruebas de caja negra

Evalúan la **funcionalidad del sistema** sin conocer su estructura interna.

Técnicas:

* **Partición de equivalencia**: se agrupan entradas similares que deberían producir el mismo resultado.
* **Análisis de valores límite**: se prueban los bordes de las particiones.
* **Tablas de decisión y árboles**: modelan combinaciones de condiciones.
* **Pruebas de estados**: para sistemas que reaccionan a eventos (máquinas de estados).

---

## 6. Estrategias de prueba

Una estrategia define **qué tipo de pruebas aplicar, cuándo y con qué herramientas**. El objetivo es cubrir progresivamente el sistema en todos sus niveles.

### Tipos de prueba:

| Tipo                  | Objetivo                                                       |
| --------------------- | -------------------------------------------------------------- |
| Prueba de unidad      | Probar funciones o clases individuales                         |
| Prueba de integración | Verificar cómo interactúan los módulos                         |
| Prueba de sistema     | Validar el sistema como un todo                                |
| Prueba de regresión   | Verificar que cambios no rompan funcionalidades previas        |
| Prueba de validación  | Confirmar que el sistema cumple con los requisitos del cliente |
| Prueba de humo        | Prueba superficial para detectar errores críticos              |
| Prueba de resistencia | Verificar funcionamiento ante alta carga o estrés              |
| Prueba de rendimiento | Medir velocidad, escalabilidad y eficiencia                    |

---

## 7. Integración: enfoques y pruebas

Cuando múltiples módulos deben funcionar juntos, se utilizan estrategias de integración:

* **Ascendente**: se prueban primero los módulos más bajos, agregando hacia arriba.
* **Descendente**: se prueba desde el módulo principal hacia los subordinados, usando stubs (simulaciones).
* **Big Bang**: se integran todos los módulos y se prueba el sistema completo (poco recomendable).

---

## 8. Pruebas automatizadas y herramientas

* Las pruebas modernas se automatizan para asegurar **repetibilidad y eficiencia**.
* Herramientas como **pytest, unittest (Python)**, **JUnit (Java)**, o **Postman** para APIs permiten ejecutar casos de prueba y generar reportes.
* Las pruebas pueden integrarse en **CI/CD pipelines** (por ejemplo, con GitHub Actions) para ejecutarse en cada push o pull request.

---

## 9. Criterios de finalización

Sommerville sugiere considerar que las pruebas han sido "suficientes" cuando:

* Se han cumplido los criterios de cobertura definidos.
* Se han detectado y corregido todos los errores críticos.
* El software cumple con los requisitos funcionales y de calidad.
* Los casos extremos han sido considerados.

---

## Conclusión

La prueba de software es un proceso **planificado, sistemático y riguroso** que forma parte esencial de cualquier desarrollo profesional. No solo busca detectar errores, sino también **aumentar la confianza** en que el sistema cumple con su propósito, incluso en condiciones inesperadas.