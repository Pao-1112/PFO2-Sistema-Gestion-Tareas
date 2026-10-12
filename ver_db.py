import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("SELECT usuario, contraseña FROM usuarios")

for fila in cursor.fetchall():
    print("Usuario:", fila[0])
    print("Hash:", fila[1])

conexion.close()