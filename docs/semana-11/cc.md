# Ejemplo: complejidad ciclomatica

**Enunciado (pequeño):**
Tenemos una función que toma dos números `x` y `y`. Si `x > 0` evaluamos `y`: si `y > 0` hacemos la acción A, si no hacemos la acción B. Si `x <= 0` hacemos la acción C. Al final imprimimos “fin”.

**Código (Python — corresponde al enunciado):**

```python
def ejemplo(x, y):
    # Nodo 1 (Start) -> Nodo 2 (decisión A)
    if x > 0:                    # Nodo 2: decisión A
        if y > 0:                # Nodo 3: decisión B
            acción_a()           # Nodo 4: acción A
        else:
            acción_b()           # Nodo 5: acción B
    else:
        acción_c()               # Nodo 6: acción C
    print("fin")                 # Nodo 7: End
```

> Donde `acción_a()`, `acción_b()`, `acción_c()` son pasos simples (por ejemplo, prints o llamadas).

---

## 1) Dibujito (flujo) — nodos y aristas (ASCII)

```
[1 Start] -> [2: if x>0?]
               /        \
        True /            \ False
           v                v
        [3: if y>0?]      [6: acción_c]
         /     \               |
    True/       \False         |
      v           v            |
    [4: A]      [5: B]         |
      \           /            |
       \         /             |
        \       /              |
         v     v               v
           [7: print "fin"] <- 
```

---

## 2) Contemos NODOS (N) y ARISTAS (E)

* Nodos (N): 7

  1. Start
  2. decisión `x > 0`
  3. decisión `y > 0`
  4. acción A
  5. acción B
  6. acción C
  7. End (`print("fin")`)

* Aristas (E): contamos cada flecha posible

  1. 1 → 2
  2. 2 → 3 (si `x>0`)
  3. 2 → 6 (si `x<=0`)
  4. 3 → 4 (si `y>0`)
  5. 3 → 5 (si `y<=0`)
  6. 4 → 7
  7. 5 → 7
  8. 6 → 7
     → **E = 8**

* Componente conectada (P): 1 (es un único subgrafo)

---

## 3) Fórmula de McCabe (complejidad ciclomática)

[
M = E - N + 2P
]

Sustituimos:

[
M = 8 - 7 + 2.1 = 3
]

También existe una forma alternativa: **M = D + 1**, donde D = número de puntos de decisión (if, while, for, case, operadores lógicos que separan caminos). Aquí hay 2 decisiones (`x>0` y `y>0`), por tanto M = 2 + 1 = 3 — coincide.

---

## 4) Interpretación práctica (qué significa `M = 3`)

* El número **3** indica la **cantidad mínima de caminos linealmente independientes** por los que puede fluir el programa.
* Para pruebas unitarias, idealmente necesitás **al menos 3 pruebas** que cubran cada camino fundamental:

  1. `x > 0` y `y > 0` → ruta: Start → 2 true → 3 true → 4 → End
  2. `x > 0` y `y <= 0` → ruta: Start → 2 true → 3 false → 5 → End
  3. `x <= 0` → ruta: Start → 2 false → 6 → End

Eso garantiza que probás cada rama lógica esencial.

---

## 5) Cómo se traducen constructs comunes a complejidad

* Cada `if`, `while`, `for`, `case` (switch) típicamente **añade +1** a M.
* Un `for` con un `if` dentro añade 2 (uno por el for, otro por el if), salvo que se simplifique.
* Expresiones booleanas compuestas con `&&`/`||` pueden aumentar los caminos (cada condición compuesta puede contarse como decisión adicional según cómo se evalúe).

---

## 6) Consejos para reducir la complejidad

* **Extraer funciones**: dividir en funciones pequeñas (cada función con M baja).
* **Uso de guard clauses (retornos tempranos)** para evitar anidar `if` dentro de `if`.
* **Polimorfismo** u otras técnicas de diseño para evitar enormes cadenas de `switch`/`if`.
* **Limitar funciones** a una única responsabilidad (Single Responsibility Principle).
* Objetivo práctico: mantener M por función entre **1 y 10** — idealmente bajo 6 para facilidad de mantenimiento y pruebas.



## 7) Ejemplo alternativo muy simple para mostrar cómo sube M

* Un `if` solo → M = 2 (1 decisión + 1)
* Un `if` con `else if` (dos decisiones encadenadas) → M = 3
* Un `for` + `if` → M = 3 (for + if = 2 decisiones → +1 → 3)
