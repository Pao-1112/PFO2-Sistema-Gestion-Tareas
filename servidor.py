from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

DATABASE = "usuarios.db"

def conectar_db():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla():
    conexion = conectar_db()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

@app.route("/registro", methods = ["POST"])
def registro():
    datos = request.get_json()

    if (not datos):
        return jsonify({
            "error": "Debe enviar los datos en formato JSON."
        }), 400

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if (not usuario or not contraseña):
        return jsonify({
            "error": "El usuario y la contraseña son obligatorios."
        }), 400

    contraseña_hasheada = generate_password_hash(contraseña)
    conexion = conectar_db()

    try:
        conexion.execute(
            """
            INSERT INTO usuarios (usuario, contraseña)
            VALUES (?,?)
            """,
            (usuario, contraseña_hasheada)
        )

        conexion.commit()

    except sqlite3.IntegrityError:
        return jsonify({
            "error" : "El usuario ya existe"
        }), 409

    finally:
        conexion.close()

    return jsonify({
        "mensaje" : "Usuario registrado correctamente."
    }), 201

@app.route("/login", methods = ["POST"])
def login():
    datos = request.get_json()

    if (not datos):
        return jsonify({
            "error": "Debe enviar los datos en formato JSON."
        }), 400
    
    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if (not usuario or not contraseña):
        return jsonify({
            "error": "El usuario y la contraseña son obligatorios"
        }), 400

    conexion = conectar_db()
    usuario_db = conexion.execute(
        """
        SELECT * FROM usuarios
        WHERE usuario = ?
        """,
        (usuario,)
    ).fetchone()

    conexion.close()

    if (usuario_db is None):
        return jsonify({
            "error" : "Usuario o contraseña incorrectos."
        }), 401

    contraseña_correcta = check_password_hash(
        usuario_db["contraseña"],
        contraseña
    )

    if (not contraseña_correcta):
        return jsonify({
            "error" : "Usuario o contraseña incorrectos."
        }), 401

    return jsonify({
        "mensaje" : "Inicio de sesión correcto.",
        "usuario" : usuario
    }), 200

@app.route("/tareas", methods = ["GET"])
def tareas():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>API de Tareas</title>
    </head>

    <body>
        <h1>¡Bienvenido a la API de Tareas!</h1>
        <p>El servidor Flask está funcionando correctamente.</p>
        <p>Endpoint: GET /tareas</p>
    </body>
    </html>
    """, 200

if (__name__ == "__main__"):
    crear_tabla()

    app.run(
        host = "127.0.0.1",
        port = 5000,
        debug = False
    )
    