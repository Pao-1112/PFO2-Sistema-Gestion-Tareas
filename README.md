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
- Almacenamiento de contraseñas mediante hash.
- Página HTML de bienvenida accesible mediante el endpoint `/tareas`.
- Manejo de respuestas HTTP para indicar resultados y errores.

## 4. Endpoints disponibles

### POST /registro

Permite registrar un usuario nuevo.

**Datos de entrada (JSON):**

```json
{
  "usuario": "nombre",
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
  "usuario": "nombre",
  "contraseña": "1234"
}
```

**Respuesta exitosa (HTTP 200):**

```json
{
  "mensaje": "Inicio de sesión correcto.",
  "usuario": "nombre"
}
```

Si el usuario no existe o la contraseña es incorrecta, la API devuelve el código HTTP `401 Unauthorized`.

### GET /tareas

Devuelve una página HTML de bienvenida que permite comprobar que el servidor Flask está funcionando correctamente.

- **Método:** GET.
- **URL local:** http://127.0.0.1:5000/tareas

## 5. Base de datos SQLite

La aplicación utiliza una base de datos llamada `usuarios.db`.

La tabla `usuarios` contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| `id` | Identificador único del usuario. |
| `usuario` | Nombre de usuario, único y obligatorio. |
| `contraseña` | Hash de la contraseña, almacenado como texto. |

La tabla se crea automáticamente cuando se inicia la aplicación, si todavía no existe.

Las contraseñas se procesan mediante las funciones `generate_password_hash()` y `check_password_hash()` de Werkzeug. Al registrar un usuario, se genera un hash antes de almacenar la contraseña. Durante el inicio de sesión, se verifica la contraseña ingresada contra el hash almacenado.

## 6. Instalación y ejecución

### 6.1. Requisitos previos

- Tener Python instalado.
- Contar con los archivos del proyecto.
- Disponer de una terminal para ejecutar los comandos.

### 6.2. Obtener los archivos del proyecto

Clonar el repositorio de GitHub:

```bash
git clone https://github.com/pao-1112/PFO2-Sistema-Gestion-Tareas.git
```

Ingresar a la carpeta del proyecto:

```bash
cd PFO2-Sistema-Gestion-Tareas
```

También es posible descargar el repositorio como archivo ZIP desde GitHub y descomprimirlo.

### 6.3. Instalar las dependencias

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene las dependencias necesarias para ejecutar la aplicación.

Si el comando `pip` no funciona, se puede intentar con:

```bash
python -m pip install -r requirements.txt
```

### 6.4. Ejecutar el servidor

Ejecutar el siguiente comando:

```bash
python servidor.py
```

El servidor estará disponible en:

http://127.0.0.1:5000

La base de datos `usuarios.db` y la tabla `usuarios` se crean automáticamente al iniciar el servidor, si todavía no existen.

Se debe mantener abierta la terminal del servidor mientras se realizan las pruebas.

### 6.5. Ejecutar el cliente de consola

Abrir una segunda terminal, dentro de la carpeta del proyecto, y ejecutar:

```bash
python cliente.py
```

El cliente permite interactuar con la API para registrar usuarios, iniciar sesión y consultar el endpoint de tareas.

### 6.6. Probar el sistema

Para comprobar el funcionamiento de la aplicación:

1. Iniciar el servidor con `python servidor.py`.
2. Abrir una segunda terminal y ejecutar `python cliente.py`.
3. Registrar un usuario utilizando las credenciales indicadas por la consigna: usuario `nombre` y contraseña `1234`.
4. Iniciar sesión con esas credenciales.
5. Consultar el endpoint de tareas.
6. Verificar que las operaciones devuelvan las respuestas esperadas.

Si el usuario ya fue registrado anteriormente en la base de datos, no es necesario registrarlo otra vez para probar el inicio de sesión.

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

En la carpeta `capturas/` se incluyen imágenes que documentan el funcionamiento de la aplicación.

Las evidencias corresponden a las siguientes pruebas:

- Inicio del servidor Flask (`servidor.png` y `servidor1.png`).
- Registro exitoso de un usuario (`registro.png`).
- Inicio de sesión correcto (`login.png`).
- Consulta de la página HTML de bienvenida (`tareas.png`).
- Verificación del hash almacenado en SQLite (`hash_sqlite.png` y `hash_sqlite1.png`).

## 9. Configuración del entorno de desarrollo

Se recomienda utilizar Visual Studio Code u otro editor compatible con Python.

### Selección del intérprete de Python en Visual Studio Code

Si el proyecto no se ejecuta correctamente, verificar que Visual Studio Code esté utilizando una instalación válida de Python.

Para seleccionar el intérprete:

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Presionar `Ctrl + Shift + P`.
3. Buscar la opción `Python: Select Interpreter`.
4. Seleccionar la instalación de Python correspondiente al entorno de trabajo.

Si se utiliza un entorno virtual, debe seleccionarse el intérprete de ese entorno y asegurarse de que las dependencias estén instaladas allí.

La carpeta `.vscode/` contiene configuraciones locales del editor y no es necesaria para ejecutar la aplicación. Por este motivo, se excluye del repositorio mediante el archivo `.gitignore`.

### Solución de problemas frecuentes

- **Python no se reconoce como comando:** comprobar que esté instalado y disponible en el PATH del sistema. En Windows también se puede intentar ejecutar `py servidor.py`.
- **No se encuentra Flask o Requests:** instalar las dependencias con `python -m pip install -r requirements.txt`.
- **El puerto 5000 está ocupado:** verificar que no exista otra aplicación utilizando ese puerto.
- **No se puede conectar con el servidor:** comprobar que `servidor.py` siga ejecutándose y que el cliente utilice la dirección `http://127.0.0.1:5000`.
- **No aparecen los usuarios registrados:** comprobar que se esté utilizando el mismo archivo `usuarios.db` y que el servidor se ejecute desde la carpeta correcta.

## 10. Enlaces del proyecto

- **Repositorio en GitHub:** https://github.com/pao-1112/PFO2-Sistema-Gestion-Tareas
- **Documentación publicada en GitHub Pages:** https://pao-1112.github.io/PFO2-Sistema-Gestion-Tareas/