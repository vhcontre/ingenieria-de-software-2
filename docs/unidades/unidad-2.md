# Unidad 2 – Gestión del Riesgo en Ingeniería de Software

## 1. ¿Qué es el riesgo en proyectos de software?

En el contexto del desarrollo de software, un **riesgo** es cualquier evento o condición incierta que podría afectar negativamente al proyecto en términos de **calidad**, **plazo**, **costos**, **seguridad** o **alcance**.

> “Un riesgo es un problema potencial que todavía no ha ocurrido.”
> (Sommerville)

La **gestión de riesgos** busca anticipar problemas antes de que ocurran, para minimizar su impacto o evitar que sucedan.

---

## 2. Tipos de riesgos comunes

### Según su naturaleza:

| Tipo de riesgo   | Ejemplos                                                                   |
| ---------------- | -------------------------------------------------------------------------- |
| Técnicos         | Tecnología no probada, fallas en herramientas, bajo rendimiento esperado   |
| del Proyecto     | Subestimación de tiempos/costos, rotación del equipo, falta de experiencia |
| Organizacionales | Cambios en la dirección, prioridades de negocio que afectan el proyecto    |
| Externos         | Cambios regulatorios, proveedores inestables, ataques externos             |
| de Seguridad     | Fallos de autenticación, brechas de datos, acceso no autorizado            |

---

## 3. Identificación del riesgo

Esta etapa consiste en **enumerar posibles eventos negativos** que podrían afectar el proyecto.

Técnicas comunes:

* Tormenta de ideas (brainstorming) con el equipo
* Análisis de proyectos anteriores
* Revisión de los entregables del proyecto
* Checklists estandarizados (IEEE, PMBOK)

**Ejemplo**:

* ¿Qué pasa si renuncia un programador clave?
* ¿Qué pasa si la herramienta de CI/CD falla justo antes de entregar?

---

## 4. Proyección del riesgo

La proyección busca **evaluar la probabilidad** y **el impacto** de cada riesgo.

| Riesgo                               | Probabilidad | Impacto | Exposición al riesgo |
| ------------------------------------ | ------------ | ------- | -------------------- |
| Rotación del personal clave          | Alta         | Alta    | Alta                 |
| Cambio en requerimientos del cliente | Media        | Alta    | Media-alta           |
| Falla en servidor de base de datos   | Baja         | Alta    | Media                |

**Exposición al riesgo = Probabilidad × Impacto**

---

## 5. Tablas para la evaluación del riesgo

Una forma habitual de organizar la información es mediante una **matriz de evaluación de riesgos**.

### Matriz de impacto / probabilidad:

|                        | **Bajo impacto** | **Medio impacto** | **Alto impacto** |
| ---------------------- | ---------------- | ----------------- | ---------------- |
| **Baja probabilidad**  | Bajo riesgo      | Bajo riesgo       | Riesgo moderado  |
| **Media probabilidad** | Bajo riesgo      | Riesgo moderado   | Riesgo alto      |
| **Alta probabilidad**  | Riesgo moderado  | Riesgo alto       | Riesgo crítico   |

Esta matriz permite **priorizar** los riesgos y decidir en cuáles actuar primero.

---

## 6. Evaluación del impacto

Al evaluar el impacto, se analizan consecuencias potenciales:

* **Costo**: ¿cuánto aumentaría el presupuesto si ocurre?
* **Tiempo**: ¿cuántos días o semanas podría retrasarse el proyecto?
* **Calidad**: ¿podría afectar la satisfacción del usuario?
* **Seguridad**: ¿se verían expuestos datos sensibles?

---

## 7. Refinamiento del riesgo

Una vez identificados y evaluados, los riesgos se pueden **refinar**, es decir, analizar con mayor detalle:

* Descomponer riesgos amplios en subriesgos concretos
* Reanalizar la probabilidad a la luz de nueva información
* Estimar recursos necesarios para mitigarlos

---

## 8. Reducción y gestión del riesgo

Aquí se definen **estrategias** para tratar los riesgos más importantes. Existen varias opciones:

| Estrategia     | Descripción                                                               |
| -------------- | ------------------------------------------------------------------------- |
| **Evitar**     | Eliminar la causa del riesgo. Ej: no usar una tecnología riesgosa.        |
| **Transferir** | Delegar el riesgo a un tercero (ej: contratar un servicio con SLA).       |
| **Mitigar**    | Reducir la probabilidad o impacto. Ej: capacitar al equipo, usar backups. |
| **Aceptar**    | Reconocer el riesgo y prepararse. Ej: tener recursos de contingencia.     |

---

## 9. Riesgos de seguridad

Son aquellos que afectan la **confidencialidad, integridad y disponibilidad** del software.

Ejemplos:

* Accesos indebidos
* Inyección de código malicioso
* Filtración de información

Medidas:

* Aplicar buenas prácticas de autenticación/autorización
* Cifrado de datos sensibles
* Auditorías de seguridad

---

## 10. Plan de Reducción, Supervisión y Gestión del Riesgo (RSGR)

El RSGR es un **plan estructurado** que define:

1. **Riesgos identificados**: listado con su nivel de criticidad.
2. **Planes de contingencia**: qué hacer si el riesgo ocurre.
3. **Responsables**: quién debe actuar ante cada tipo de riesgo.
4. **Mecanismos de monitoreo**: cómo detectar señales de que un riesgo podría activarse.
5. **Estrategias de reducción**: acciones preventivas concretas.
6. **Calendario de revisión**: cuándo revisar y actualizar el plan.

---

## Conclusión

* La gestión de riesgos no elimina la incertidumbre, pero **prepara al equipo** para afrontarla con menor impacto.
* Es un proceso **continuo** que debe mantenerse a lo largo del ciclo de vida del proyecto.
* Los equipos más maduros documentan, discuten y revisan riesgos con frecuencia como parte de sus reuniones de seguimiento.
