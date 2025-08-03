#  How to 10: Dockerización del Backend y Base de Datos

---

## 1. Requisitos previos para trabajar con Docker en Windows

Para ejecutar Docker en Windows y trabajar con contenedores, necesitás:

* **Docker Desktop para Windows**:
  La herramienta oficial para usar Docker en Windows.
  [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

* **WSL2 (Subsistema de Windows para Linux, versión 2)**:
  Docker Desktop usa WSL2 para correr contenedores Linux eficientemente.
  Se recomienda instalar alguna distro Linux compatible (Ubuntu es la más popular).

* **PowerShell o Terminal de Windows**:
  Para ejecutar comandos Docker.

---

## 2. Instalación y configuración inicial

1. Descargar Docker Desktop desde el sitio oficial e instalarlo siguiendo las instrucciones.

2. Durante la instalación, habilitar WSL2 si se solicita.

3. Reiniciar la PC si es necesario.

4. Verificar que Docker Desktop esté corriendo (icono de ballena visible en la bandeja).

5. En PowerShell, correr los comandos para comprobar versiones:

```bash
docker --version
docker compose version
```

Deberías ver la versión instalada sin errores.

---

## 3. Construcción y levantamiento de la aplicación con Docker Compose

### Paso 3.1: Construir las imágenes Docker

Desde la raíz del proyecto donde esté tu archivo `docker-compose.yml`, ejecutar:

```bash
docker compose build
```

Esto construye las imágenes para el backend y la base de datos (si corresponde).

---

### Paso 3.2: Levantar los servicios

Ejecutar:

```bash
docker compose up
```

Esto inicia los contenedores en modo interactivo, mapeando el puerto `8000` local al contenedor backend.

Podés acceder a la API vía navegador o Postman en:

```
http://localhost:8000/web/productos
```

---

### Paso 3.3: Detener los servicios

Para parar y eliminar los contenedores:

```bash
docker compose down
```

---

## 4. Comandos útiles para manejo de contenedores

* Listar contenedores activos:

```bash
docker ps
```

* Ver logs del backend:

```bash
docker compose logs backend
```

---

## 5. Consideraciones finales

* Asegurate que tu `Dockerfile` y `docker-compose.yml` estén correctamente configurados para el entorno Windows (rutas relativas, volúmenes, variables de entorno).

* Si usás SQLite, el archivo de base de datos debe mapearse a un volumen persistente para no perder datos al reiniciar el contenedor.

* Para entornos con bases de datos como PostgreSQL, configura usuario, contraseña y puerto en variables de entorno dentro del `docker-compose.yml`.

* Controlá la versión de Python en el `Dockerfile` para evitar incompatibilidades.