import os

def Menu():

    print()
    print()
    print("                 Proyecto 1 - LFP A+")
    print("     ------------------------------------------")
    print("     |   Nombre: Luis Fernando Falla Guzmán   |")
    print("     |   Carné: 201700700                     |")
    print("     ------------------------------------------")
    print()
    print("1. Cargar menú")
    print("2. Cargar orden")
    print("3. Generar menú")
    print("4. Generar factura")
    print("5. Generar árbol")
    print("6. Salir")
    print()
    print(">> Ingrese una opción:")
    
    opcion = input(">> ")

    if opcion == "1":
        Cargar_Menu()
        Menu()
    elif opcion == "2":
        Cargar_Orden()
        Menu()
    elif opcion == "3":
        Generar_Menu()
        Menu()
    elif opcion == "4":
        Generar_Factura()
        Menu()
    elif opcion == "5":
        Generar_Arbol()
        Menu()
    elif opcion == "6":
        exit()
    else:
        print("Opcion incorrecta")
        Menu()


def Cargar_Menu():
    pass

def Cargar_Orden():
    pass

def Generar_Menu():
    pass

def Generar_Factura():
    pass

def Generar_Arbol():
    pass

def AFD():
    pass

def Guardar_Token():
    pass

def Guardar_Error():
    pass

