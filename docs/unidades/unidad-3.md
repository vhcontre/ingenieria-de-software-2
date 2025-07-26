# Unidad 3 – Diseño Arquitectónico y Patrones

## 1. ¿Qué es el diseño arquitectónico en software?

El diseño arquitectónico es la **primera etapa del diseño de software**. En esta fase se define **la estructura general del sistema**, incluyendo los componentes principales, cómo se comunican entre sí y cómo se distribuyen en el sistema.

> "La arquitectura del software establece un marco general en el cual se desarrollará todo el sistema."
> (Sommerville)

**Objetivos principales**:

* Dividir el sistema en **subsistemas o módulos**
* Establecer **interfaces claras** entre componentes
* Mejorar la **modificabilidad**, **mantenibilidad** y **escalabilidad**
* Facilitar decisiones técnicas y de equipo

---

## 2. Componentes típicos de una arquitectura

* **Módulos o componentes**: partes funcionales del sistema (servicios, controladores, modelos, etc.)
* **Conectores**: mecanismos de comunicación (API, sockets, bases de datos, colas de mensajes)
* **Interfaces**: contratos públicos entre componentes
* **Capas**: agrupación de componentes por nivel de abstracción o función (por ejemplo, presentación, lógica, datos)

### Estilos arquitectónicos comunes

| Estilo                | Descripción                                           |
| --------------------- | ----------------------------------------------------- |
| Arquitectura en capas | Separación en niveles como UI, lógica, persistencia   |
| Cliente-servidor      | Un cliente solicita servicios a un servidor           |
| Microservicios        | Cada servicio implementa una funcionalidad específica |
| Basado en eventos     | Componentes que reaccionan a eventos o mensajes       |
| Pipe and filter       | Flujo de datos a través de filtros secuenciales       |

---

## 3. Diseño de la interfaz de usuario (UI)

El diseño de UI es clave para que el software sea **fácil de usar, accesible y comprensible**.

**Aspectos principales**:

* Claridad y consistencia visual
* Respuestas inmediatas al usuario (feedback)
* Control por parte del usuario
* Prevención de errores (o mensajes útiles)
* Adaptabilidad a distintos dispositivos

Sommerville recomienda involucrar a los usuarios finales lo antes posible para prototipar, probar y refinar la interfaz.

---

## 4. ¿Qué son los patrones de diseño?

Los **patrones de diseño** son **soluciones reutilizables** a problemas comunes en el desarrollo de software orientado a objetos.

> “Un patrón de diseño es una solución general, comprobada y reutilizable a un problema común de diseño.”
> (Gamma et al., *Design Patterns*, 1995)

No son fragmentos de código específicos, sino **estructuras conceptuales** que guían decisiones de arquitectura y codificación.

---

## 5. Clasificación de patrones (según GoF)

| Tipo de patrón | Ejemplo            | Propósito                                    |
| -------------- | ------------------ | -------------------------------------------- |
| Creacionales   | Singleton, Factory | Manejo flexible de la creación de objetos    |
| Estructurales  | Adapter, Composite | Composición entre clases y objetos           |
| Comportamiento | Observer, Strategy | Comunicación y responsabilidad entre objetos |

---

## 6. ¿Cuándo usar patrones de diseño?

Los patrones se utilizan cuando:

* Se detecta un problema **recurrente** en el diseño
* Hay necesidad de **flexibilidad**, **mantenimiento** o **extensibilidad**
* Se quiere mejorar la **comunicación entre desarrolladores** usando un lenguaje común

### Ejemplos:

* Necesito una única instancia compartida → uso `Singleton`
* Necesito intercambiar algoritmos sin modificar clases → uso `Strategy`
* Necesito que varios objetos reaccionen a un cambio → uso `Observer`

---

## 7. Consideraciones para aplicar patrones

Al usar patrones hay que tener en cuenta:

* **No abusar**: no todo problema requiere un patrón. A veces una solución simple es mejor.
* **Contexto específico**: el patrón debe ajustarse al problema, no al revés.
* **Costo vs beneficio**: algunos patrones introducen complejidad adicional.
* **Documentación clara**: cuando se aplica un patrón, es importante dejar documentado el motivo y su implementación.

---

## 8. Relación entre patrones y desarrollo de software

Los patrones:

* Favorecen la **reutilización de conocimiento**
* Ayudan a mantener un **estilo de arquitectura coherente**
* Promueven la **comunicación efectiva** dentro del equipo
* Son esenciales en **arquitecturas modernas** como MVC, microservicios, REST, etc.

---

## 9. Selección adecuada de un patrón

Para elegir un patrón, es útil responder:

1. ¿Cuál es el **problema concreto** que intento resolver?
2. ¿Este problema ya fue resuelto de forma **probada y estandarizada**?
3. ¿Qué consecuencias tiene aplicar este patrón a largo plazo?
4. ¿Está el equipo familiarizado con este patrón?

---

## Conclusión

* El diseño arquitectónico define el esqueleto de todo sistema de software.
* Un diseño bien estructurado mejora la escalabilidad, el mantenimiento y la claridad.
* Los patrones de diseño son herramientas conceptuales para resolver problemas conocidos de manera sistemática.
* Aplicados correctamente, los patrones ayudan a producir sistemas más robustos y adaptables.
