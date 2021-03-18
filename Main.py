import os
import webbrowser
from tkinter.filedialog import askopenfilename
from PIL import Image
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
        Retornar_Valores()
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
    Retornar_Valores()
    Token_Reconocido()
    if v.Lista_Error != None:
        Error_Encontrado()
    Mostrar_Menu()

def Generar_Factura():
    v.fila = 1
    v.columna = 1
    v.cadena = ""
    AFD()
    Token_Reconocido()
    if v.Lista_Error != None:
        Error_Encontrado()

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
        elif v.estado == 1:
            if elemento.isalpha():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 1
            elif elemento == " ":
                v.columna += 1
                v.cantidad += 1
                v.estado = 1
            elif elemento == "=":
                Guardar_Token("Restaurante")
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("igual")
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
                v.estado = 3
        elif v.estado == 3:
            if elemento == ":":
                Guardar_Token("nombre_sec")
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("dos_puntos")
            elif elemento == ";":
                Guardar_Token("nombre")
                v.cadena += elemento
                v.columna += 1
                v.cantidad += 1
                Guardar_Token("punto_coma")
            elif elemento == "]":
                Guardar_Token("desc")
                v.cadena += elemento
                v.columna += 2
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
                Guardar_Token("nombre_res")
                v.fila += 1
                v.columna = 1
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
                Guardar_Token("id")
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("punto_coma")
            elif elemento == " ":
                if v.cadena == "":
                    v.estado = 4
                else:
                    v.columna += 1
                    v.cantidad += 1
                    v.cadena += elemento
                    Guardar_Error("id_inv")
        elif v.estado == 5:
            if elemento.isdigit():
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 5
            elif elemento == " ":
                v.columna += 1
                v.estado = 5
            elif elemento == ";":
                Guardar_Token("precio")
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                Guardar_Token("punto_coma")
            elif elemento == "%":
                v.columna += 1
                v.cantidad +=1
                v.cadena += elemento
                Guardar_Token("prop")
            elif elemento == ".":
                v.columna += 1
                v.cantidad += 1
                v.cadena += elemento
                v.estado = 6
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
       


def Guardar_Token(token):
    token = Token(token, v.cadena, v.fila, v.columna - v.cantidad)

    v.Lista_Token.append(token.Retornartoken())

    v.cantidad = 0
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
    id = "menu"

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

def Retornar_Valores():
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


    print(v.Lista_Cantidad_Producto)

def usoDic():

    dic = {}
    sec = ""
    nombre = ""
    precio = float(0)
    desc = ""
    
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