import requests

URL_BASE = "http://127.0.0.1:5000"

def registrar_usuario():
    usuario = input("Ingrese usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()

    datos = {
        "usuario" : usuario,
        "contraseña" : contraseña
    }

    respuesta = requests.post(
        f"{URL_BASE}/registro",
        json = datos
    )

    print("\nRespuesta del servidor:")
    print(respuesta.json())

def iniciar_sesion():
    usuario = input("Ingrese usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()

    datos = {
        "usuario" : usuario,
        "contraseña" : contraseña
    }

    respuesta = requests.post(
        f"{URL_BASE}/login",
        json = datos
    )

    print("\nRespuesta del servidor:")
    print(respuesta.json())

def consultar_tareas():
    respuesta = requests.get(
        f"{URL_BASE}/tareas"
    )

    print("\nRespuesta del servidor:")
    print(respuesta.text)

def menu():
    while True:
        print("\n===== CLIENTE API =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Consultar tareas")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if (opcion == "1"):
            registrar_usuario()

        elif (opcion == "2"):
            iniciar_sesion()

        elif (opcion == "3"):
            consultar_tareas()

        elif (opcion == "4"):
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")

if (__name__ == "__main__"):
    menu()
