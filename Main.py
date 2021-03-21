import os
import webbrowser
from tkinter.filedialog import askopenfilename
from PIL import Image
from datetime import date
from datetime import datetime
from Token import Token
from Token import Valor
from Token import Error

v = Valor()

def Menu():

    print()
    print()
    print("                Proyecto 1 - LFP A+")
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
    Retornar_Valores_Menu()
    
    if v.Lista_Error:
        Error_Encontrado()
    else:
        Token_Reconocido()
        Mostrar_Menu()
        

def Generar_Factura():
    v.fila = 1
    v.columna = 1
    v.cadena = ""
    AFD_FACTURA()
    Retornar_Valores_Factura()
    
    if v.Lista_Error:
        Error_Encontrado()
    else:
        Token_Reconocido()
        Mostrar_Factura()

def Generar_Arbol():
    archivo()

def archivo():

    nombre_sec = None
    
    numero = 0
    id = "menu"

    file = open("arbol.dot","w")

    file.write("digraph arbol{" + os.linesep)

    nombre_restaurante = ""

    for i in v.Lista_Token:
        if "TK_NOMBRE_RES" == i[0]:
            nombre_restaurante = i[1]

    nodo = "Raiz"
    cadena_nombre_res = nodo + ' [label="' + nombre_restaurante + '"]'
    file.write(str(cadena_nombre_res) + os.linesep)
    
    for i in v.Lista_Sec:
        cadena_escribir = nodo + " -> " + i.replace(" ","") + ";"
        file.write(str(cadena_escribir) + os.linesep)
        

    index = 0
    indice_valor = 0
    cantidad = 0
    precio = float(0)
    for i in v.Lista_Cantidad_Producto:
        valor = int(i)
        cantidad += valor

    while index < int(len(v.Lista_Sec)):
        indice = 0
        nombre_sec = v.Lista_Sec[index]
        file.write(str(nombre_sec) + os.linesep)
        cantidad_art = int(v.Lista_Cantidad_Producto[index])
        while indice < cantidad_art:
            nombre = v.Lista_Nom[indice_valor]
            precio = float(v.Lista_Pre[indice_valor])
            descrp = v.Lista_Des[indice_valor]
            id_numero = id + str(numero)
            cadena = id_numero + ' [label="' + nombre + '     Q.' + str(f"{precio:.2f}") + '\n' + descrp + '"]'
            file.write(str(cadena) + os.linesep)
            sec_nombre = nombre_sec + " -> " + id_numero + ";"
            file.write(str(sec_nombre) + os.linesep)
            numero += 1
            indice_valor += 1
            indice += 1
        index += 1
    
    file.write("}")
    file.close()

    os.system("dot.exe -Tpng arbol.dot -o Menu.png")

    imagen = Image.open("Menu.png")
    imagen.show()

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
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("igual")
            elif elemento == ":":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("dos_puntos")
            elif elemento == ";":
                v.columna += 1
                v.cantidad += 1
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
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 1
            elif elemento.isdigit():
                v.columna += 1
                v.cadena += elemento
                v.estado = 5
            elif elemento == "'":
                v.columna += 1
                v.estado = 2
            elif elemento == "#":
                print("Archivo analizado")
            else:
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Error("")
        elif v.estado == 1:
            if elemento.isalpha():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 1
            elif elemento == " ":
                if v.cadena.upper() == "RESTAURANTE":
                    Guardar_Token("Restaurante")
                    v.columna += 1
                    v.estado = 0
                else:
                    Guardar_Error("")
            elif elemento == "=":
                Guardar_Token("Restaurante")
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("igual")
            else:
                v.cadena = ""
                v.cantidad = 1
                v.columna += 1
                v.cadena += elemento
                Guardar_Error("")
        elif v.estado == 2:
            if elemento.isalpha():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento.isdigit():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == "_":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == "-":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == " ":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 2
            elif  elemento == "#":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 2
            elif elemento == "'":
                v.columna += 1
                v.estado = 3
        elif v.estado == 3:
            if elemento == ":":
                v.columna -= 1
                Guardar_Token("nombre_sec")
                v.columna += 1
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("dos_puntos")
            elif elemento == ";":
                v.columna -= 1
                Guardar_Token("nombre")
                v.columna += 1
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("punto_coma")
            elif elemento == "]":
                v.columna -= 1
                Guardar_Token("desc")
                v.columna += 1
                v.cadena += elemento
                #v.columna += 2
                Guardar_Token("corch_ce")
            elif elemento == ",":
                condicion_1 = v.cadena.replace("-", "")
                cond = condicion_1.replace(" ","")
                if cond.isalpha():
                    Guardar_Token("cliente")
                    v.cadena += elemento
                    v.columna += 1
                    v.cantidad += 1
                    Guardar_Token("coma")
                elif cond.isdigit():
                    Guardar_Token("nit")
                    v.cadena += elemento
                    v.columna += 1
                    v.cantidad += 1
                    Guardar_Token("coma")
                elif cond.isalnum():
                    Guardar_Token("dir")
                    v.cadena += elemento
                    v.columna += 1
                    v.cantidad += 1
                    Guardar_Token("coma")
            elif elemento == " ":
                v.columna += 1
                v.estado = 3
            elif elemento == "\n":
                v.columna -= 1
                Guardar_Token("nombre_res")
                v.fila += 1
                v.columna = 1
            else:
                v.cadena = ""
                v.cadena += elemento
                v.cantidad = 1
                v.columna += 1
                Guardar_Error("")
        elif v.estado == 4:
            if elemento.isalpha():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 4    
            elif elemento.isdigit():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 4
            elif elemento == "_":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 4
            elif elemento == ";":
                if v.cadena.isidentifier():
                    Guardar_Token("id")
                    v.columna += 1
                    v.cantidad += 1
                    v.cadena += elemento
                    Guardar_Token("punto_coma")
                else:
                    Guardar_Error("")
                    v.columna += 1
                    v.cadena += elemento
                    v.cantidad += 1
                    Guardar_Token("punto_coma")
            elif elemento == " ":
                if v.cadena == "":
                    v.estado = 4
                else:
                    v.columna += 1
                    v.cantidad += 1
                    v.cadena += elemento
                    Guardar_Error("id_inv")
            else:
                v.cadena += ""
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                Guardar_Error("")
        elif v.estado == 5:
            if elemento.isdigit():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 5
            elif elemento == " ":
                v.columna += 1
                #v.cadena += elemento
                #v.cantidad += 1
                #Guardar_Error("")
                v.estado = 5
            elif elemento == ";":
                v.columna -= 1
                Guardar_Token("precio")
                v.columna += 1
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("punto_coma")
            elif elemento == "%":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("prop")
            elif elemento == ".":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 6
            else:
                v.columna += 1
                v.cadena = ""
                v.cadena += elemento
                Guardar_Error("")
        elif v.estado == 6:
            if elemento.isdigit():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 6
            elif elemento == ";":
                if v.cadena[-1] == ".":
                    Guardar_Token("precio")
                    v.columna += 1
                    v.cantidad += 1
                    v.cadena += elemento
                    Guardar_Token("punto_coma")
                else:
                    Guardar_Token("precio")
                    v.columna += 1
                    v.cantidad += 1
                    v.cadena += elemento
                    Guardar_Token("punto_coma")
            elif elemento == " ":
                Guardar_Token("precio")
                v.columna += 1
                v.estado = 0

       
def AFD_FACTURA():
    v.entrada = v.entrada + "#"
    for elemento in v.entrada:
        if v.estado == 0:
            if elemento == "\n":
                v.fila += 1
                v.columna = 1
                v.estado = 0
            elif elemento == " ":
                v.columna += 1
                v.estado = 0
            elif elemento == ",":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("coma")
            elif elemento == "\t":
                v.columna += 1
                v.estado = 0
            elif elemento == "'":
                v.columna += 1
                v.estado = 1
            elif elemento.isdigit():
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estado = 2
            elif elemento.isalpha():
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                v.estado = 3
        elif v.estado == 1:
            if elemento.isalpha():
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estad0 = 1
            elif elemento.isdigit():
                v.cantidad += 1
                v.cadena += elemento
                v.columna += 1
                v.estado = 1
            elif elemento == " ":
                v.cantidad += 1
                v.cadena += elemento
                v.columna += 1
                v.estado = 1
            elif elemento == "-":
                v.cadena += elemento
                v.cantidad +=1
                v.columna += 1
                v.estado = 1
            elif elemento == ".":
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estado = 1
            elif elemento == ",":
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estado = 1
            elif elemento == "'":
                v.columna += 1
                if v.cadena.replace(" ","").isalpha():
                    v.columna -= 1
                    Guardar_Token("cliente")
                    v.columna += 1
                elif v.cadena.replace("-","").isdigit():
                    v.columna -= 1
                    Guardar_Token("nit")
                    v.columna += 1
                else:
                    v.columna -= 1
                    Guardar_Token("dir")
                    v.columna += 1
        elif v.estado == 2:
            if elemento.isdigit():
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                v.estado = 2
            elif elemento == " ":
                v.columna += 1
                v.estado = 2
            elif elemento == ",":
                Guardar_Token("cant_producto")
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("coma")
            elif elemento == "%":
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("prop")
            elif elemento == ".":
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                v.estado = 4
        elif v.estado == 3:
            if elemento.isalpha():
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estado = 3
            elif elemento.isdigit():
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estado = 3
            elif elemento == "_":
                v.cadena += elemento
                v.cantidad += 1
                v.columna += 1
                v.estado = 3
            elif elemento == " ":
                v.columna += 1
                v.estado = 3
            else:
                if v.cadena.isidentifier():
                    Guardar_Token("id")   
                    v.fila += 1
                    v.columna = 1
                else:
                    v.columna += 1
                    v.cantidad = 1
                    v.cadena += elemento
                    Guardar_Error("id_inv")
        elif v.estado == 4:
            if elemento.isdigit():
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                v.estado = 4
            elif elemento == "%":
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("prop")
            else:
                v.cadena = ""
                v.cadena += elemento
                v.columna += 1
                v.cantidad = 1
                Guardar_Error("") 

def Guardar_Token(token):
    token = Token(token, v.cadena, v.fila, v.columna - v.cantidad)

    v.Lista_Token.append(token.Retornartoken())

    v.cantidad = 0
    v.cadena = ""
    v.estado = 0
    
def Guardar_Error(tipo):
    error = Error(tipo, v.fila, v.columna - v.cantidad, v.cadena)

    v.Lista_Error.append(error.Retornar_Error())

    v.cantidad = 0
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
    
def Token_Reconocido():    
    contador = 1

    filew = open("Token.html", "w")

    filew.write("<html>")
    filew.write("<head>")
    filew.write("<title>TOKENS</title>")
    filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
    filew.write('<link rel="icon" href="comando.png">')
    filew.write("</head>")
    filew.write("<body>")        
    filew.write('<div class="container" style="text-align:center">')
    filew.write("<br>")
    filew.write("<br>")
    filew.write('<div class="jumbotron text-white bg-dark">')
    filew.write('<div class="container">')
    filew.write('<h1>Reporte de Tokens</h1>')
    filew.write('<p class="lead">A continuacion se muestran los tokens reconocidos por el AFD</p>')
    filew.write("</div>")
    filew.write("</div>")
    filew.write('<div class="table-responsive">')
    filew.write('<table class="table">')
    filew.write('<thead>')
    filew.write("</tr>")
    filew.write('<th class="bg-danger">NO.</th>')  
    filew.write('<th class="bg-light">TOKEN</th>')
    filew.write('<th class="bg-info">LEXEMA</th>')        
    filew.write('<th class="bg-warning">FILA</th>')  
    filew.write('<th class="text-light bg-dark">COLUMNA</th>')  
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
    filew.write("</div>")
    filew.write("<br>")
    filew.write("<br>")
    filew.write("</div>")
    filew.write("</body>")        
    filew.write("</html>")        
    
    #Cierre del archivo
    filew.close()

    #Abrir archivo en un navegador
    webbrowser.open_new_tab("Token.html")  

def Error_Encontrado():    
    contador = 1

    filew = open("Error.html", "w")

    filew.write("<html>")
    filew.write("<head>")
    filew.write("<title>ERRORES</title>")
    filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
    filew.write('<link rel="icon" href="comando.png">')
    filew.write("</head>")
    filew.write("<body>")        
    filew.write('<div class="container" style="text-align:center">')
    filew.write("<br>")
    filew.write("<br>")
    filew.write('<div class="jumbotron text-light bg-dark">')
    filew.write('<div class="container">')
    filew.write('<h1>Reporte de Errores</h1>')
    filew.write('<p class="lead">A continuacion se muestran los errores reconocidos por el AFD</p>')
    filew.write("</div>")
    filew.write("</div>")
    filew.write('<table class="table">')
    filew.write('<thead>')
    filew.write("</tr>")
    filew.write('<th class="bg-danger">NO.</th>')  
    filew.write('<th class="bg-light">FILA</th>')
    filew.write('<th class="bg-info">COLUMNA</th>')        
    filew.write('<th class="bg-warning">CARACTER</th>')  
    filew.write('<th class="text-light bg-dark">DESCRIPCION</th>')  
    filew.write("</tr>")
    filew.write("</thead>")
    filew.write("<tbody>")

    #Recorrer la lista hasta la cantidad de registros a mostrar                               
    for i in v.Lista_Error:

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
    webbrowser.open_new_tab("Error.html")  

def Mostrar_Menu():    
    filew = open("menu.html", "w")

    filew.write("<html>")
    filew.write("<head>")
    filew.write("<title>Menu</title>")
    filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
    filew.write('<link rel="icon" href="comando.png">')
    filew.write("</head>")
    filew.write("<body>")        
    filew.write('<div class="container">')
    filew.write("<br>")
    filew.write("<br>")
    
    filew.write('<div class="jumbotron text-white bg-dark">')
    filew.write('<div class="container" style="text-align:center">')
    for i in v.Lista_Token:
        if "TK_NOMBRE_RES" in i:
            cadena = '<h1 class="display-4">'+ i[1] +'</h1>'
            filew.write(str(cadena))
    filew.write("</div>")
    filew.write("</div>")

    nombre_sec = None
    
    numero = 0
    #id = "menu"

    index = 0
    indice_valor = 0
    cantidad = 0
    precio = float(0)
    for i in v.Lista_Cantidad_Producto:
        valor = int(i)
        cantidad += valor
    
    while index < int(len(v.Lista_Sec)):
        filew.write('<div class="jumbotron text-white bg-info">')
        filew.write('<div class="container">')
        indice = 0
        nombre_sec = "<h1>" + v.Lista_Sec[index] + "<h1>"
        filew.write("<br>")
        filew.write(str(nombre_sec) + os.linesep)
        cantidad_art = int(v.Lista_Cantidad_Producto[index])
        while indice < cantidad_art:
            nombre = v.Lista_Nom[indice_valor]
            precio = float(v.Lista_Pre[indice_valor])
            descrp = v.Lista_Des[indice_valor]
            cadena = "<h2>" + nombre + '&nbsp &nbsp &nbsp &nbsp &nbsp Q.' + str(f"{precio:.2f}") + "</h2>"
            filew.write(str(cadena) + os.linesep)
            cad_desc  = "<h3>" + descrp + "</h3>"
            filew.write(str(cad_desc) + os.linesep)
            filew.write("<br>")
            numero += 1
            indice_valor += 1
            indice += 1
        index += 1
        filew.write("</div>")
        filew.write("</div>")

    filew.write("<br>")
    filew.write("<br>")
    filew.write("</div>")
    filew.write("</body>")        
    filew.write("</html>")        

    filew.close()

    webbrowser.open_new_tab("menu.html")  

def Retornar_Valores_Menu():
    indice = 0
    cantidad = len(v.Lista_Token)
    contador = 0
    while indice < cantidad:
        if "TK_NOMBRE" == v.Lista_Token[indice][0]:
            contador += 1
        elif "TK_NOMBRE_SEC" == v.Lista_Token[indice][0]:
            v.Lista_Cantidad_Producto.append(contador)
            contador = 0
        else:
            pass
        indice += 1
    
    v.Lista_Cantidad_Producto.append(contador)
    v.Lista_Cantidad_Producto.pop(0)

    for i in v.Lista_Token:
        if "TK_IDENTIFICADOR" == i[0]:
            v.Lista_Ide.append(i[1])

    for i in v.Lista_Token:
        if "TK_NOMBRE_SEC" == i[0]:
            v.Lista_Sec.append(i[1])
    
    for i in v.Lista_Token:
        if "TK_NOMBRE" == i[0]:
            v.Lista_Nom.append(i[1])

    for i in v.Lista_Token:
        if "TK_PRECIO" == i[0]:
            v.Lista_Pre.append(i[1])

    for i in v.Lista_Token:
        if "TK_DESCRIPCION" == i[0]:
            v.Lista_Des.append(i[1])

def Retornar_Valores_Factura():
    for i in v.Lista_Token:
        if "TK_CANTIDAD_COMIDA" == i[0]:
            v.Cantidad_comida.append(i[1])

    for i in v.Lista_Token:
        if "TK_IDENTIFICADOR" == i[0]:
            v.Identificadores_factura.append(i[1])
    

def Mostrar_Factura():

    today = date.today()
    valor_total = float(0)
    valor_propina = None
    total_propina = None

    filew = open("factura.html", "w")

    filew.write("<html>")
    filew.write("<head>")
    filew.write("<title>Factura</title>")
    filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
    filew.write('<link rel="icon" href="comando.png">')
    filew.write("</head>")
    filew.write("<body>")        
    filew.write('<div class="container">')
    filew.write("<br>")
    filew.write("<br>")
    
    filew.write('<div class="card text-white bg-dark">')
    filew.write('<div class="card-body">')
    for i in v.Lista_Token:
        if "TK_NOMBRE_RES" in i:
            cadena = '<center><h1 class="card-title">'+ i[1] +'</h1></center>'
            filew.write(str(cadena))
    cadena_fac = '<center><h1 class="card-title">Factura No. '+ str(v.cantidad_factura) +'</h1></center>'
    filew.write(str(cadena_fac))
    cadena_fecha = '<center><h1 class="card-title">Fecha '+ str(today.day)+str("/")+str(today.month)+str("/")+str(today.year) +'</h1></center>' 
    filew.write(str(cadena_fecha))
    filew.write('<br>')
    filew.write('<p class="card-text">Datos del Cliente</p>')
    for i in v.Lista_Token:
        if "TK_NOMBRE_CLIENTE" == i[0]:
            cadena = '<p class="card-text">Nombre: ' + i[1] + '</p>'
            filew.write(str(cadena))

    for i in v.Lista_Token:
        if "TK_NIT_CLIENTE" == i[0]:
            cadena = '<p class="card-text">Nit: ' + i[1] + '</p>'
            filew.write(str(cadena))

    for i in v.Lista_Token:
        if "TK_DIRECCION_CLIENTE" == i[0]:
            cadena = '<p class="card-text">Dirección: ' + i[1] + '</p>'
            filew.write(str(cadena))

    filew.write('<br>')
    filew.write('Descripcion')
    filew.write('<table class="table text-white">')
    filew.write('<thead>')
    filew.write('<tr>')
    filew.write('<th scope="col">Cantidad')
    filew.write('</th>')
    filew.write('<th scope="col">Concepto')
    filew.write('</th>')
    filew.write('<th scope="col">Precio')
    filew.write('</th>')
    filew.write('<th scope="col">Total')
    filew.write('</th>')
    filew.write('<tr>')
    filew.write('</thead>')
    filew.write('<tbody>')

    try:
        indice_para_factura = 0
        while indice_para_factura < len(v.Lista_Ide):
            if v.Lista_Ide[indice_para_factura] in v.Identificadores_factura:
                indice_para_calculo = v.Lista_Ide.index(v.Lista_Ide[indice_para_factura])
                v.Lista_valor.append(indice_para_calculo)
            indice_para_factura += 1
        indice__f = 0
        for elemento in v.Lista_valor:
            indice = int(elemento)
            cantidad = int(v.Cantidad_comida[indice__f])
            concepto = v.Lista_Nom[indice__f]
            valor = float(v.Lista_Pre[indice])
            calculo = cantidad * valor
            v.Lista_calculo.append(calculo)

            filew.write('<tr>')
            cadena_cantidad = '<th scope="row">'+ str(cantidad) +'</th>'
            filew.write(str(cadena_cantidad))
            cadena_concepto = '<td>'+ str(concepto) +'</td>'
            filew.write(str(cadena_concepto))
            cadena_valor = '<td>Q'+ str(f"{valor:.2f}") +'</td>'
            filew.write(str(cadena_valor))
            cadena_calculo = '<td>Q'+ str(f"{calculo:.2f}") +'</td>'
            filew.write(str(cadena_calculo))
            filew.write('</tr>')
            
            indice__f += 1

    except:
        print()
    
    filew.write('<hr>')
    filew.write('<tr>')
    filew.write('<th scope="row"> Sub Total </th>')
    filew.write('<td>  </td>')
    filew.write('<td>  </td>')
    for i in v.Lista_calculo:
        valor_total += i
    cadena_sub_total = '<td>Q'+ str(f"{valor_total:.2f}") +'</td>'
    filew.write(str(cadena_sub_total))
    filew.write('</tr>')
    filew.write('<tr>')
    for i in v.Lista_Token:
        if "TK_PROPINA" == i[0]:
            valor_propina = i[1]
            cadena = '<th scope="row"> Propina ('+ str(i[1]) +')</th>'
            filew.write(str(cadena))
    filew.write('<td>  </td>')
    filew.write('<td>  </td>')
    valor_propina_sin_porcentaje = ""
    for i in valor_propina:
        if i.isdigit():
            valor_propina_sin_porcentaje += i
    total_propina = (int(valor_propina_sin_porcentaje)/100)*valor_total
    cadena_propina = '<td>Q'+ str(f"{total_propina:.2f}") +'</td>'
    filew.write(str(cadena_propina))
    filew.write('</tr>')
    filew.write('<hr>')
    filew.write('<tr>')
    filew.write('<th scope="row"> Total </th>')
    filew.write('<td>  </td>')
    filew.write('<td>  </td>')
    valor_total_con_propina = valor_total + total_propina
    cadena_valor_total = '<td>Q'+ str(f"{valor_total_con_propina:.2f}") +'</td>'
    filew.write(str(cadena_valor_total))
    filew.write('</tr>')
    filew.write('</tbody>')
    filew.write('</table>')
    filew.write("</div>")
    filew.write("</div>")
    filew.write("</div>")
    filew.write("<br>")
    filew.write("</body>")        
    filew.write("</html>")        

    filew.close()
    v.cantidad_factura += 1
    webbrowser.open_new_tab("factura.html")

def usoDic():

    dic = {}
    sec = ""
    nombre = ""
    #precio = float(0)
    #desc = ""
    
    contador = 0

    for i in v.Lista_Token:
        if "TK_NOMBRE_SEC" in i:
            sec = i[1]
            lista = []
            while v.Lista_Token[contador][1] != sec:
                if "TK_NOMBRE" in v.Lista_Token[contador]:
                    nombre = v.Lista_Token[contador][1]
                    lista.append(nombre)
                contador += 1
            dic[sec] = {"articulo":lista}
    
    print(dic)

Menu()