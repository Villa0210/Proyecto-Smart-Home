#---Proyecto smart home---
import os
"""---Anotaciones para abrir y cerrar archivos correctamente---
a: Abre el archivo para agregar datos al final. Si el archivo no existe, lo
crea.
r: Abre el archivo para leer los datos que contiene.
w: Abre el archivo para escribir datos. Si el archivo no existe, lo crea. Si
existe sobrescribe la informacion que contenga.
a+: Abre el archivo para leer y escribir datos en el.
"""
import os
def crearArchivoUsuarios(): #x ahora crea un archivo para los usuarios para posteriormente añadir la info
    with open("usuarios.txt", "w") as file:
        pass
    print("\n---¡Archivo de info de usuario creado correctamente!---\n")

def crearHabitacionDispositivos(): #x ahora crea un archivo para los usuarios para posteriormente añadir la info
    with open("habitacionDispisitivos.txt", "w") as file:
        pass
    print("\n---¡Archivo de info de usuario creado correctamente!---\n")
    
def agregarInfoUsuario():
    print("\n=== Registro de Nuevo Usuario ===")
    usuarios = []
    while True:
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico: ")
        pin = input("Ingrese su PIN: ")

        nuevoUsuario = {"Nombre": nombre, "Correo": correo, "PIN": pin, "Casas": []}
        usuarios.append(nuevoUsuario)
        print("¡Usuario registrado exitosamente!")
        guardarUsuarios(usuarios)
        #Agregar opcion
        break

def guardarUsuarios(usuarios):
    with open("usuarios.txt", "a+") as file:
        for usuario in usuarios:
            file.write(f"{usuario['Nombre']},{usuario['Correo']},{usuario['PIN']}\n")

def mostrarInfoUsuarios():
    print("\n\n--Lista final con info de usuario---\n\n")
    file = open("usuarios.txt", "r")
    mensaje = file.read()
    print(mensaje)
    file.close()
    

def agregarHabitacionDispositivos():
    casas = []

    while True:
        casa = {}
        casa["Nombre"] = input("ingrese el nombre de la casa: ")
        casa["Habitaciones"] = []

        while True:
            habitacion = {}
            habitacion["Nombre"] = input("Ingrese el nombre de la habitacion: ")
            habitacion["Dispositivos"] = []

            while True:
                dispositivo = {}
                dispositivo["Nombre"] = input("Ingrese el nombre del dispositivo: ")
                dispositivo["Tipo"] = input("ingrese el tipo del dispositivo: ")
                habitacion["Dispositivos"].append(dispositivo)

                opcionDispositivo = input("¿desea agregar otro dispositivo a esta habitacion? (1=Si, Otra tecla=No): ")
                if opcionDispositivo != "1":
                    break

            casa["Habitaciones"].append(habitacion)

            opcionHabitacion = input("¿desea agregar otra habitación a esta casa? (1=Sí, Otra tecla=No): ")
            if opcionHabitacion != "1":
                break

        casas.append(casa)

        opcionCasa = input("¿Desesa agregar otra casa? (1=Si Otra tecla=No): ")
        if opcionCasa != "1":
            break

    with open("habitacionDispositivos.txt", "w") as file: #aqui eran lso bucles de for
        for casa in casas:
            file.write(f"{casa['Nombre']}")
            for habitacion in casa['Habitaciones']:
                file.write(f"{habitacion['Nombre']}")
                for dispositivo in habitacion['Dispositivos']:
                    file.write(f"{dispositivo['Nombre']}, {dispositivo['Tiipo']}")

    print("\n---¡Archivo de habitaciones y dispositivos creado correctamente---\n")

def leerUsuarios():
    try:
        file = open("usuarios.txt", "r")
        mensaje= file.read()
        print(mensaje)
        file.close()

    except FileNotFoundError:
        pass
        print("Archivo no de usarios encontrado.haga uno")



def leerHabitacionesDispositivos():
    try:
        file = open("habitacionDispositivos.txt", "r")
        mensaje= file.read()
        print(mensaje)

    except FileNotFoundError:
        pass
        print("Archivo de habitacionesDispositivos no encontrado. Haga uno")


def menu():
    print("Bienvenido al programa. Seleccione una opcion")
    opcion = str(input("Seleciione una opcion: 1=Registrar usuario 2= Ver info de usuario Otra tecla=Ver info de dispositivos: "))
    if opcion == "1":
        crearArchivoUsuarios()
        agregarInfoUsuario()
        agregarHabitacionDispositivos()
        leerHabitacionesDispositivos()
    elif opcion =="2":
        leerUsuarios()
    else:
        leerHabitacionesDispositivos()
    

menu()

