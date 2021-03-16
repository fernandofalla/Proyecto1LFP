import os
import webbrowser
from tkinter.filedialog import askopenfilename
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
    print("Lista de Tokens en Menu")
    print()
    Mostrar_Token_Menu()
    print()
    print("Lista de Tokens en Factura")
    print()
    Mostrar_Token_Factura()
    print()
    print("Lista de Errores")
    print()
    Mostrar_Error()

def Cargar_Menu():
    try:
        
        archivo = askopenfilename()

        entrada = open(archivo, "r")

        for i in entrada.read():
            v.entrada += i
            
    except:
        print("Archivo incorrecto")

def Cargar_Orden():
    try:
        
        archivo = askopenfilename()

        entrada = open(archivo, "r")
        v.entrada = ""

        for i in entrada.read():
            v.entrada += i
            
    except:
        print("Archivo incorrecto")

def Generar_Menu():
    AFD()
    mostrarListaToken()

def Generar_Factura():
    v.fila = 1
    v.columna = 1
    v.cadena = ""
    AFD()
    mostrarListaToken()

def Generar_Arbol():
    pass

def AFD():
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
            elif elemento == "-":
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
                v.estado = 3
        elif v.estado == 3:
            if elemento == ":":
                Guardar_Token("nombre_sec")
                v.cadena += elemento
                v.columna += 1
                Guardar_Token("dos_puntos")
            elif elemento == ";":
                Guardar_Token("nombre")
                v.cadena += elemento
                v.columna += 1
                Guardar_Token("punto_coma")
            elif elemento == "]":
                Guardar_Token("desc")
                v.cadena += elemento
                v.columna += 1
                Guardar_Token("corch_ce")
            elif elemento == ",":
                condicion_1 = v.cadena.replace("-", "")
                cond = condicion_1.replace(" ","")
                if cond.isalpha():
                    Guardar_Token("cliente")
                    v.cadena += elemento
                    v.columna += 1
                    Guardar_Token("coma")
                elif cond.isdigit():
                    Guardar_Token("nit")
                    v.cadena += elemento
                    v.columna += 1
                    Guardar_Token("coma")
                elif cond.isalnum():
                    Guardar_Token("dir")
                    v.cadena += elemento
                    v.columna += 1
                    Guardar_Token("coma")
            elif elemento == " ":
                v.columna += 1
                v.estado = 3
            elif elemento == "\n":
                Guardar_Token("nombre_res")
                v.fila += 1
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
            elif elemento == "%":
                v.columna += 1
                v.cadena += elemento
                Guardar_Token("prop")
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

def Mostrar_Token_Menu():
    for i in v.Lista_Token:
        print(i)

def Mostrar_Token_Factura():
    for i in v.Lista_Token:
        if "NOMBRE_CLIENTE" in i:
            print(i)
        elif "NIT_CLIENTE" in i:
            print(i)
        elif "DIRECCION_CLIENTE" in i:
            print(i)

def Mostrar_Error():
    for i in v.Lista_Error:
        print(i)
    
def mostrarListaToken():    
    contador = 1

    filew = open("reporte.html", "w")

    filew.write("<html>")
    filew.write("<head>")
    filew.write("<title>BASILISK</title>")
    filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
    filew.write('<link rel="icon" href="comando.png">')
    filew.write("</head>")
    filew.write("<body>")        
    filew.write('<div class="container" style="text-align:center">')
    filew.write("<br>")
    filew.write("<br>")
    filew.write('<div class="jumbotron jumbotron-fluid">')
    filew.write('<div class="container">')
    filew.write('<h1 class="display-4">Reporte Tokens</h1>')
    filew.write('<p class="lead">A continuacion se muestran los tokens reconocidos por el AFD</p>')
    filew.write("</div>")
    filew.write("</div>")
    filew.write('<table class="table">')
    filew.write('<thead>')
    filew.write("</tr>")
    filew.write('<th class="bg-danger">NO.</th>')  
    filew.write('<th class="bg-light">TOKEN</th>')
    filew.write('<th class="bg-info">LEXEMA</th>')        
    filew.write('<th class="bg-warning">FILA</th>')  
    filew.write('<th class="bg-dark">COLUMNA</th>')  
    filew.write("</tr>")
    filew.write("</thead>")
    filew.write("<tbody>")

    #Recorrer la lista hasta la cantidad de registros a mostrar                               
    for i in v.Lista_Token:

        filew.write("<tr>")          
        filew.write("<td>")
        filew.write(str(contador))
        filew.write("</td>")
        filew.write("<td>")
        filew.write(str(i[0]))
        filew.write("</td>")
        filew.write("<td>")
        filew.write(str(i[1]))
        filew.write("</td>")   
        filew.write("<td>")
        filew.write(str(i[2]))
        filew.write("</td>")
        filew.write("<td>")
        filew.write(str(i[3]))
        filew.write("</td>")              
        filew.write("</tr>")    

        contador += 1                    
                        
    filew.write("</tbody>")
    filew.write("</table>")
    filew.write("<br>")
    filew.write("<br>")
    filew.write("</div>")
    filew.write("</body>")        
    filew.write("</html>")        
    
    #Cierre del archivo
    filew.close()

    #Abrir archivo en un navegador
    webbrowser.open_new_tab("reporte.html")  

Menu()