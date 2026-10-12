# Sistema de Gestión de Tareas con API y Base de Datos

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de una API con Flask y SQLite que permite registrar usuarios, validar sus credenciales y comprobar el funcionamiento del servidor mediante un endpoint de prueba.

El sistema almacena los usuarios en una base de datos SQLite y utiliza hashes para proteger las contraseñas almacenadas.

La aplicación cuenta con un servidor (`servidor.py`) y un cliente por consola (`cliente.py`) que permite interactuar con la API mediante un menú de opciones.

## 2. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Flask:** framework para desarrollar la API.
- **SQLite:** base de datos para almacenar los usuarios.
- **Werkzeug:** biblioteca utilizada para generar y verificar los hashes de las contraseñas.
- **Requests:** biblioteca utilizada por el cliente para enviar solicitudes HTTP al servidor.

## 3. Funcionalidades

- Registro de usuarios.
- Validación de los campos obligatorios.
- Detección de usuarios duplicados.
- Inicio de sesión mediante la verificación de credenciales.
- Almacenamiento de contraseñas mediante hashes.
- Consulta del endpoint de prueba `/tareas`.
- Respuestas HTTP que permiten identificar el resultado de las solicitudes.

## 4. Endpoints de la API

### 4.1. Registro de usuarios

**Método:** `POST`

**Endpoint:** `/registro`

Permite registrar un usuario en la base de datos.

**Ejemplo de solicitud JSON:**

```json
{
  "usuario": "nombre",
  "contraseña": "1234"
}
```

**Respuestas principales:**

- `201 Created`: usuario registrado correctamente.
- `400 Bad Request`: faltan datos obligatorios o la solicitud no contiene datos JSON válidos.
- `409 Conflict`: el usuario ya existe.

### 4.2. Inicio de sesión

**Método:** `POST`

**Endpoint:** `/login`

Permite verificar las credenciales de un usuario registrado.

**Ejemplo de solicitud JSON:**

```json
{
  "usuario": "nombre",
  "contraseña": "1234"
}
```

**Respuestas principales:**

- `200 OK`: inicio de sesión correcto.
- `400 Bad Request`: faltan datos obligatorios o la solicitud no contiene datos JSON válidos.
- `401 Unauthorized`: usuario o contraseña incorrectos.

### 4.3. Consulta de tareas

**Método:** `GET`

**Endpoint:** `/tareas`

Devuelve una página HTML de bienvenida que permite comprobar que el servidor Flask está funcionando correctamente.

**URL local:** `http://127.0.0.1:5000/tareas`

Este endpoint es una respuesta de prueba. No implementa operaciones de creación, consulta, modificación o eliminación de tareas almacenadas en una base de datos.

## 5. Cliente de la API

El archivo `cliente.py` permite interactuar con el servidor mediante un menú por consola.

Las opciones disponibles son:

1. **Registrar usuario:** solicita un nombre de usuario y una contraseña, y envía los datos al endpoint `POST /registro`.
2. **Iniciar sesión:** solicita las credenciales y las envía al endpoint `POST /login` para validar el acceso.
3. **Consultar tareas:** realiza una solicitud `GET /tareas` y muestra la respuesta HTML recibida del servidor.
4. **Salir:** finaliza la ejecución del cliente.

El cliente utiliza la biblioteca `Requests` para comunicarse con el servidor local mediante la dirección `http://127.0.0.1:5000`.

## 6. Base de datos y seguridad

La base de datos `usuarios.db` se crea automáticamente al iniciar el servidor, si todavía no existe.

Contiene la tabla `usuarios`, con los siguientes campos:

| Campo | Descripción |
|---|---|
| `id` | Identificador único del usuario. |
| `usuario` | Nombre de usuario, obligatorio y único. |
| `contraseña` | Hash de la contraseña almacenada. |

Para proteger las contraseñas se utilizan las funciones `generate_password_hash()` y `check_password_hash()` de Werkzeug.

Las contraseñas no se almacenan directamente en texto plano. Al iniciar sesión, el sistema verifica la contraseña ingresada utilizando el hash guardado en la base de datos.

Además, las consultas SQL utilizan parámetros para evitar incorporar directamente los datos ingresados por el usuario en las sentencias SQL.

## 7. Instalación y ejecución

### 7.1. Requisitos previos

- Python instalado.
- Git instalado para clonar el repositorio.
- Las dependencias especificadas en `requirements.txt`.

### 7.2. Clonar el repositorio

Clonar el repositorio de GitHub desde la terminal:

```bash
git clone https://github.com/pao-1112/PFO2-Sistema-Gestion-Tareas.git
```

Ingresar a la carpeta del proyecto:

```bash
cd PFO2-Sistema-Gestion-Tareas
```

También es posible descargar el repositorio como archivo ZIP desde GitHub y descomprimirlo en la computadora.


### 7.3. Instalar las dependencias

Ejecutar el siguiente comando desde la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

### 7.4. Ejecutar el servidor

En una terminal, ejecutar:

```bash
python servidor.py
```

El servidor se iniciará en la dirección local `http://127.0.0.1:5000`.

### 7.5. Ejecutar el cliente

Abrir una segunda terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python cliente.py
```

Desde el menú del cliente se pueden probar las operaciones disponibles.

**Importante:** el servidor debe permanecer en ejecución mientras se utiliza el cliente. Si se intenta registrar un usuario que ya existe, se deberá utilizar otro nombre de usuario o iniciar sesión con las credenciales correspondientes.

## 8. Pruebas realizadas

Se realizaron pruebas para verificar el funcionamiento de los componentes principales del proyecto:

- Inicio del servidor Flask.
- Registro exitoso de un usuario.
- Manejo del intento de registrar un usuario existente.
- Inicio de sesión con credenciales correctas.
- Rechazo de credenciales incorrectas.
- Respuesta del endpoint `GET /tareas`.
- Verificación del almacenamiento de la contraseña mediante un hash en SQLite.

Las capturas de pantalla correspondientes se encuentran en la carpeta `capturas/` del repositorio. El documento `Evidencias_PFO2.pdf` reúne las evidencias de las pruebas y las respuestas a las preguntas conceptuales solicitadas en la consigna.

## 9. Solución de problemas

- **Python no se reconoce como comando:** verificar que esté instalado y disponible en el PATH. En Windows también se puede probar `py servidor.py`.
- **Faltan módulos:** ejecutar `python -m pip install -r requirements.txt`.
- **El puerto 5000 está ocupado:** detener el proceso que lo utiliza antes de iniciar el servidor.
- **El cliente no se conecta:** comprobar que el servidor esté activo y que el cliente utilice la dirección y el puerto correctos.
- **No se encuentra el usuario:** verificar que se esté utilizando la misma base de datos `usuarios.db` y que las credenciales sean correctas.

## 10. Enlaces del proyecto

- **Repositorio de GitHub:** https://github.com/pao-1112/PFO2-Sistema-Gestion-Tareas
- **GitHub Pages:** https://pao-1112.github.io/PFO2-Sistema-Gestion-Tareas/
