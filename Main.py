import os
from Token import Token
from Token import Valor
from Token import Error

v = Valor()



def Menu():

    print()
    print()
    print("                 Proyecto 1 - LFP A+")
    print("     ------------------------------------------")
    print("     |   Nombre: Luis Fernando Falla Guzmán   |")
    print("     |   Carné: 201700700                     |")
    print("     ------------------------------------------")
    print()
    print("0. Mostrar")
    print("1. Cargar menú")
    print("2. Cargar orden")
    print("3. Generar menú")
    print("4. Generar factura")
    print("5. Generar árbol")
    print("6. Salir")
    print()
    print(">> Ingrese una opción:")
    
    opcion = input(">> ")

    if opcion == "0":
        mostrar()
        Menu()
    elif opcion == "1":
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

def mostrar():
    AFD(v.entrada)
    print("Lista de Tokens")
    print()
    Mostrar_Token()
    print("Lista de Errores")
    print()
    Mostrar_Error()

def Cargar_Menu():
    archivo = input("Ingrese archivo: ")

    entrada = open(archivo, "r")

    for i in entrada.read():
        v.entrada += i

def Cargar_Orden():
    pass

def Generar_Menu():
    pass

def Generar_Factura():
    pass

def Generar_Arbol():
    pass

def AFD(entrada):
    v.entrada = v.entrada + "#"

    for elemento in v.entrada:
        if v.estado == 0:
            if elemento == " ":
                v.columna += 1
                v.estado = 0
            elif elemento == '\n':
                v.fila += 1
                v.columna = 1
                v.estado = 0
            elif elemento == "\t":
                v.columna += 1
                v.estado = 0
            elif elemento == "=":
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("igual")
            elif elemento == ":":
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("dos_puntos")
            elif elemento == ";":
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("punto_coma")
            elif elemento == "[":
                v.cadena += elemento
                Guardar_Token("corch_ab")
                v.columna += 1
                v.estado = 4
            elif elemento == "]":
                v.cadena += elemento
                Guardar_Token("corch_ce")
                v.columna += 1
            elif elemento.isalpha():
                v.columna += 1
                v.cadena += elemento
                v.estado = 1
            elif elemento.isdigit():
                v.columna += 1
                v.cadena += elemento
                v.estado = 5
            elif elemento == "'":
                v.columna += 1
                v.estado = 2
        elif v.estado == 1:
            if elemento.isalpha():
                v.columna += 1
                v.cadena += elemento
                v.estado = 1
            elif elemento == " ":
                v.columna += 1
                v.estado = 1
            elif elemento == "=":
                Guardar_Token("Restaurante")
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("igual")
        elif v.estado == 2:
            if elemento.isalpha():
                v.columna += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento.isdigit():
                v.columna += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == "_":
                v.columna += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == " ":
                v.columna += 1
                v.cadena += elemento
                v.estado = 2
            elif  elemento == "#":
                v.columna += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == "'":
                v.columna += 1
                v.estado = 3
        elif v.estado == 3:
            if " " in  v.cadena:
                Guardar_Token("nombre_res")
            else:
                Guardar_Token("nombre_sec")
        elif v.estado == 4:
            if elemento.isalpha():
                v.columna += 1
                v.cadena += elemento
                v.estado = 4    
            elif elemento.isdigit():
                v.columna += 1
                v.cadena += elemento
                v.estado = 4
            elif elemento == "_":
                v.columna += 1
                v.cadena += elemento
                v.estado = 4
            elif elemento == ";":
                Guardar_Token("id")
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("punto_coma")
            elif elemento == " ":
                if v.cadena == "":
                    v.estado = 4
                else:
                    v.columna += 1
                    v.cadena += elemento
                    Guardar_Error("id_inv")
        elif v.estado == 5:
            if elemento.isdigit():
                v.columna += 1
                v.cadena += elemento
                v.estado = 5
            elif elemento == " ":
                v.columna += 1
                v.estado = 5
            elif elemento == ";":
                Guardar_Token("numero")
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("punto_coma")
            elif elemento == ".":
                v.columna += 1
                v.cadena += elemento
                v.estado = 6
        elif v.estado == 6:
            if elemento.isdigit():
                v.columna += 1
                v.cadena += elemento
                v.estado = 6
            elif elemento == ";":
                if v.cadena[-1] == ".":
                    Guardar_Token("numero")
                    v.columna += 1
                    v.cadena += elemento
                    Guardar_Token("punto_coma")
                else:
                    Guardar_Token("decimal")
                    v.columna += 1
                    v.cadena += elemento
                    Guardar_Token("punto_coma")
       


def Guardar_Token(token):
    token = Token(token, v.cadena, v.fila, v.columna)

    v.Lista_Token.append(token.Retornartoken())

    v.cadena = ""
    v.estado = 0

def Guardar_Error(tipo):
    error = Error(tipo, v.fila, v.columna, v.cadena)

    v.Lista_Error.append(error.Retornar_Error())

    v.cadena = ""
    v.estado = 0

def Mostrar_Token():
    for i in v.Lista_Token:
        print(i)

def Mostrar_Error():
    for i in v.Lista_Error:
        print(i)

Menu()