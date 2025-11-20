#AlvaradoAlejandro_FPY_1101-001DFV4

import os 
os.system("cls")
registro=()
usuario={}

def ingreso():
    while True:


        neUser=input("Ingrese el nombre de usuario:")

        if neUser in registro:

            print("Usuario ya existente, intenta otro: ")

        else:
            registro[usuario]=neUser
            usuario[neUser]
            break
def buscar():
    busqueda=input("Ingrese el usuario a buscar")
    if busqueda in registro:
        print(usuario[busqueda])
    else:
        print("El usuario no esta registrado")


def eliminar():
    eliminar=input("ingrese el usuario a eliminar: ")
    if eliminar in usuario:
        print(usuario[eliminar])
    else:
        print("el usuario fue eliminado.")

def salir():
    salir=print("gracias por usar la app. :D")



while True:
    print("Menu:" 
          "1: Ingresar usuario. " 
          "2: Buscar usuario. "
          "3: Eliminar usuario. "
          "4: Salir.")

    try:
          opcion=int(input("Ingrese la opcion a elegir:"))
    except:
        print("Opcion no valida")
        if opcion == 1:
            registro()
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            eliminar()
        elif opcion == 4:
            salir()