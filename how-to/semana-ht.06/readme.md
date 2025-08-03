##  How to 5 – Autenticación y Autorización

> Semana clave donde nuestro sistema comienza a **proteger recursos sensibles**, limitando el acceso según roles (`admin` / `operador`) y usando **JWT** para autenticación. Además, incorporamos middleware para autorización y pruebas sobre endpoints autenticados.

---

###  1. Implementación de autenticación con JWT

* Se configuró el sistema para trabajar con **JSON Web Tokens (JWT)**:

  * Se generó un token al momento de "login" (operación simulada).
  * Se usó el paquete `python-jose` para la firma y validación del token.
  * Se implementó una función `create_access_token()` para emitir el JWT.
  * El token contiene el `sub` (identificador del usuario) y el `rol` como `claim`.

* Ejemplo de payload:

  ```json
  {
    "sub": "usuario_admin",
    "rol": "admin",
    "exp": "..."
  }
  ```

---

###  2. Definición de roles y permisos

* Se definieron dos roles principales:

  * `admin`: puede acceder a todos los endpoints del sistema.
  * `operador`: acceso limitado a ciertas operaciones (por ejemplo, solo puede registrar movimientos, pero no editar productos ni ver reportes).

* En el sistema, el rol se utiliza para condicionar el acceso a recursos protegidos, mediante un middleware.

---

###  3. Middleware de autorización

* Se implementó un **middleware personalizado** para leer y validar el JWT desde el header `Authorization`.

* Este middleware:

  * Extrae y decodifica el token.
  * Verifica que el token sea válido y no haya expirado.
  * Inyecta el `rol` y `username` en el `request.state`, para que estén disponibles en los endpoints.
  * Opcionalmente, puede rechazar la petición si no tiene permisos suficientes.

* También se crearon **dependencias reutilizables** con `Depends()` que:

  * Verifican si hay un token válido.
  * Verifican si el usuario tiene el rol necesario para acceder.

---

###  4. Protección de endpoints

* Se protegieron distintos endpoints del sistema usando las dependencias de seguridad:

  * `/productos`: solo accesible por `admin`.
  * `/movimientos`: accesible por `admin` y `operador`, pero con permisos distintos según método.
  * `/reportes`: solo `admin`.

* En cada endpoint, se agregó una dependencia como:

  ```python
  @app.get("/productos")
  def list_products(current_user: User = Depends(verify_admin)):
      ...
  ```

---

###  5. Pruebas automatizadas de endpoints autenticados

* Se desarrollaron pruebas con `pytest` para:

  * Simular login y obtener JWT válido.
  * Acceder a endpoints protegidos usando el token en headers.
  * Probar respuestas esperadas (200 OK, 403 Forbidden, 401 Unauthorized).
  * Asegurar que usuarios sin token o con rol incorrecto no accedan.

* Se usó el cliente de prueba de FastAPI (`TestClient`) y se pasaron headers manualmente.

---

###  6. Consideraciones adicionales

* No se implementó un sistema de usuarios real (con base de datos), sino que se simularon usuarios válidos con contraseñas hardcodeadas (modo demo).
* El objetivo fue **comprender el flujo JWT completo** y cómo usarlo para proteger recursos REST.
* Se sentaron las bases para una posible futura autenticación real conectada a base de datos.