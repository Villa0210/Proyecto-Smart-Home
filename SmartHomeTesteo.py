#---Proyecto smart home---
import os

def crearArchivoUsuarios():#Crea un archivo para usuarios para posteriormente añadir la info
    if not os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "w"):
            pass
        print("\n---¡Archivo de info de usuario creado correctamente!---\n")

    else:
        pass
    print("\n---¡Archivo de info de usuario cargado correctamente!---\n")



def cargarUsuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "r") as file:
            for linea in file:
                nombre, correo, pin, *casas = linea.strip().split(',')
                usuarios.append({"Nombre": nombre, "Correo": correo, "PIN": pin, "Casas":casas})
    except FileNotFoundError:
        pass
    print("Cargar usuarios:", usuarios)
    print("Los usuarios se cargaron CORRECTAMENTE")
    return usuarios
