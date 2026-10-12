# API REST de Tareas con Flask

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de una API REST utilizando Python y Flask, con una base de datos SQLite para almacenar usuarios y gestionar el registro y la autenticación.

La aplicación permite registrar usuarios, iniciar sesión mediante credenciales y acceder a un endpoint que muestra una página HTML de bienvenida.

Además, las contraseñas se almacenan mediante un hash para evitar guardarlas en texto plano.

## 2. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Flask:** framework para desarrollar la API REST.
- **SQLite:** sistema de base de datos para almacenar los usuarios.
- **Werkzeug:** biblioteca utilizada para generar y verificar hashes de contraseñas.
- **Requests:** biblioteca utilizada por el cliente de consola para realizar solicitudes HTTP.

## 3. Funcionalidades

La aplicación cuenta con las siguientes funcionalidades:

- Registro de usuarios.
- Validación de campos obligatorios.
- Prevención del registro de usuarios duplicados.
- Inicio de sesión mediante usuario y contraseña.
- Almacenamiento seguro de contraseñas mediante hash.
- Página HTML de bienvenida accesible mediante el endpoint `/tareas`.
- Manejo de respuestas HTTP para indicar resultados y errores.

## 4. Endpoints disponibles

### POST /registro

Permite registrar un usuario nuevo.

**Datos de entrada (JSON):**

```json
{
  "usuario": "paola",
  "contraseña": "1234"
}
```

**Respuesta exitosa (HTTP 201):**

```json
{
  "mensaje": "Usuario registrado correctamente."
}
```

Si se intenta registrar un usuario que ya existe, la API devuelve el código HTTP `409 Conflict`.

### POST /login

Permite autenticar a un usuario registrado.

**Datos de entrada (JSON):**

```json
{
  "usuario": "paola",
  "contraseña": "1234"
}
```

**Respuesta exitosa (HTTP 200):**

```json
{
  "mensaje": "Inicio de sesión correcto.",
  "usuario": "paola"
}
```

Si el usuario no existe o la contraseña es incorrecta, la API devuelve el código HTTP `401 Unauthorized`.

### GET /tareas

Devuelve una página HTML de bienvenida que permite comprobar que el servidor Flask está funcionando correctamente.

**URL local:**

`http://127.0.0.1:5000/tareas`

**Método:** GET.

## 5. Base de datos SQLite

La aplicación utiliza una base de datos llamada `usuarios.db`.

La tabla `usuarios` contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| `id` | Identificador único del usuario. |
| `usuario` | Nombre de usuario, único y obligatorio. |
| `contraseña` | Hash de la contraseña, almacenado como texto. |

La tabla se crea automáticamente cuando se inicia la aplicación, si todavía no existe.

### Seguridad de las contraseñas

Las contraseñas se procesan mediante las funciones `generate_password_hash()` y `check_password_hash()` de Werkzeug.

Al registrar un usuario, se genera un hash antes de guardar la contraseña en la base de datos. Al iniciar sesión, se verifica la contraseña ingresada contra el hash almacenado.

De esta manera, la contraseña original no se guarda en texto plano.

## 6. Instalación y ejecución

### Requisitos previos

- Tener Python instalado.
- Contar con los archivos del proyecto.

### Instalación de dependencias

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
pip install -r requirements.txt
```

Este archivo contiene las dependencias necesarias para ejecutar el servidor Flask y el cliente de consola.

### Ejecución del servidor

```bash
python servidor.py
```

El servidor estará disponible en `http://127.0.0.1:5000`.

### Ejecución del cliente de consola

Abrir una segunda terminal y ejecutar:

```bash
python cliente.py
```

El cliente permite interactuar con la API para registrar usuarios, iniciar sesión y consultar el endpoint de tareas.

## 7. Pruebas realizadas

Se realizaron pruebas para verificar el funcionamiento de la API:

- Registro exitoso de un usuario.
- Intento de registro de un usuario existente.
- Inicio de sesión con credenciales correctas.
- Inicio de sesión con contraseña incorrecta.
- Validación de campos obligatorios.
- Consulta del endpoint `GET /tareas`.
- Verificación del almacenamiento de contraseñas mediante hash en SQLite.

## 8. Evidencias de ejecución

En la carpeta `capturas/` se incluyen imágenes que documentan la ejecución del servidor y las pruebas realizadas.

Las evidencias contemplan:

- Inicio del servidor Flask.
- Registro de un usuario.
- Registro de un usuario existente (incorrecto)
- Inicio de sesión correcto.
- Rechazo de credenciales incorrectas.
- Consulta de la página HTML de bienvenida.
- Verificación del hash almacenado en SQLite.

## 9. Conclusión

El desarrollo permitió aplicar los conceptos de creación de API REST con Flask, manejo de solicitudes HTTP, persistencia de datos con SQLite y autenticación de usuarios.

También permitió incorporar buenas prácticas de seguridad mediante el almacenamiento de contraseñas con hash, evitando conservar las contraseñas originales en texto plano.

## 10. Respuestas conceptuales

### ¿Por qué hashear contraseñas?

Hashear contraseñas permite almacenarlas de forma más segura, sin guardar el texto original en la base de datos. Si alguien accede a la base de datos, no encontrará directamente las contraseñas de los usuarios.

En este proyecto se utiliza generate_password_hash() de Werkzeug para generar el hash y check_password_hash() para verificar las credenciales durante el inicio de sesión.

### ¿Cuáles son las ventajas de usar SQLite en este proyecto?

SQLite permite almacenar los datos de manera persistente en un archivo local, sin necesidad de instalar ni administrar un servidor de base de datos independiente.

Sus principales ventajas en este proyecto son:

- Simplicidad: es fácil de configurar y utilizar desde Python.

- Persistencia: los usuarios registrados permanecen almacenados después de cerrar la aplicación.

- Portabilidad: la base de datos se conserva en un archivo que puede trasladarse junto con el proyecto.

- Integración: Python incluye el módulo sqlite3, por lo que no es necesario instalar una biblioteca adicional para conectarse a SQLite.

## 11. Configuración del entorno de desarrollo

Se recomienda configurar el entorno de Python en Visual Studio Code según las necesidades de cada desarrollador.

La carpeta .vscode/ contiene configuraciones locales del editor y no es necesaria para ejecutar la aplicación. Por este motivo, se excluye del repositorio mediante el archivo .gitignore.

Al clonar el proyecto, cada desarrollador deberá seleccionar o configurar el intérprete de Python que utilizará en su entorno de trabajo.