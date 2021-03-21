import os
import webbrowser
from PIL import Image
from datetime import date
from datetime import datetime


Lista_nombre_res = ["Restaurante LFP"]
Lista_sec = ["Bebidas","Desayunos","Almuerzos"]
Lista_cantidad_pre = [2,2,2]

Lista_ide = ["bebida_1","Bebida_2","Pos_002","pos_001"]
Lista_nom = ["Bebida1","Bebida2","Postre1"]
Lista_pre = ["1.00","2.00","5.00","4.00","9.00","9.00","30.00"]
Lista_des = ["Desc @Bebida1","Desc Bebida2","Desc Desayuno1","Desc Desayuno2","Desc Almuerzo1","Desc Almuerzo2","Desc Postre 1"]

Lista_dom = ["1 av. 4-33 zona 3, Fraijanes, Guatemala"]

cantidad_comida = [2,4]
identificadores_factura = ["bebida_1","Pos_002"]


indice_para_calculo = None
Lista_valor = []
Lista_calculo = []
Lista_total = []

cadena_cliente = "Luis Fernando"
cadena_nit = "12323223"
cadena_domicilio = "1 av. 4-33 zona 3, Fraijanes"
cadena_propina = "8%"
cadena_identificador = "pos_001"


today = date.today()

now = datetime.now()

#print(str(today.day)+str("/")+str(today.month)+str("/")+str(today.year))




#print(cadena_cliente.replace(" ","").isalpha())
#print(cadena_nit.replace("-","").isdigit())
#print(cadena_domicilio.isidentifier())
#print(cadena_propina.replace("%","").isdigit())

#print(cadena_identificador.isidentifier())


#for i in Lista_dom:
#    if i == chr(44) or i == chr(45) or i == chr(46) :
#        print("Hello")

#Lista_ide
#Identificadores_factura
#Lista_valor


def factura():
    try:
        indice_para_factura = 0
        while indice_para_factura < len(Lista_ide):
            if Lista_ide[indice_para_factura] in identificadores_factura:
                indice_para_calculo = Lista_ide.index(Lista_ide[indice_para_factura])
                Lista_valor.append(indice_para_calculo)
            indice_para_factura += 1
        indice__f = 0
        for elemento in Lista_valor:
            indice = int(elemento)
            print(indice)
            cantidad = int(cantidad_comida[indice__f])
            concepto = Lista_nom[indice]
            valor = float(Lista_pre[indice])
            calculo = cantidad * valor
            Lista_calculo.append(calculo)

            print(cantidad," ",concepto," "+str(f"{valor:.2f}")+" Q"+str(f"{calculo:.2f}"))
            indice__f += 1

    except:
        print()
        
factura()    



def archivo():
    #cantidad_sec = len(Lista_sec)
    #index = 0
    nombre_sec = None
    numero_sec = 0
    #id_sec = "seccion"
    numero = 0
    id = "menu"

    file = open("reporte.dot","w")

    file.write("digraph matriz{" + os.linesep)
    
    #for i in Lista_nombre_res:
    #    cadena = i.replace(" ","") + ";"
    #    nombre_res = i.replace(" ","")
    #    file.write(str(cadena) + os.linesep)
    
    #for i in Lista_sec:
    #    nombre_sec = i.replace(" ","")
    #    cadena = i.replace(" ","") + ";"
    #    file.write(str(cadena) + os.linesep)
    nodo = "Raiz"
    cadena_nombre_res = nodo + ' [label="' + Lista_nombre_res[0] + '"]'
    file.write(str(cadena_nombre_res) + os.linesep)

    for i in Lista_sec:
        cadena_escribir = nodo + " -> " + i.replace(" ","_") + ";"
        file.write(str(cadena_escribir) + os.linesep)
        numero_sec += 1

    index = 0
    indice_valor = 0
    cantidad = 0

    for i in Lista_cantidad_pre:
        valor = int(i)
        cantidad += valor

    while index < int(len(Lista_sec)):
        indice = 0
        nombre_sec = Lista_sec[index]
        file.write(str(nombre_sec) + os.linesep)
        cantidad_art = int(Lista_cantidad_pre[index])
        while indice < cantidad_art:
            nombre = Lista_nom[indice_valor]
            precio = Lista_pre[indice_valor]
            descrp = Lista_des[indice_valor]
            id_numero = id + str(numero)
            cadena = id_numero + ' [label="' + nombre + '     Q.' + precio + '\n' + descrp + '"]'
            file.write(str(cadena) + os.linesep)
            sec_nombre = nombre_sec + " -> " + id_numero + ";"
            file.write(str(sec_nombre) + os.linesep)
            numero += 1
            indice_valor += 1
            indice += 1
        index += 1
    
    file.write("}")
    file.close()

    os.system("dot.exe -Tpng reporte.dot -o z.png")
    
    imagen = Image.open("z.png")
    imagen.show()

def mostrar():
    index = 0
    indice_valor = 0
    cantidad = 0

    for i in Lista_cantidad_pre:
        valor = int(i)
        cantidad += valor

    while index < int(len(Lista_sec)):
        indice = 0
        nombre_sec = Lista_sec[index]
        print(nombre_sec)
        cantidad_art = int(Lista_cantidad_pre[index])
        while indice < cantidad_art:
            nombre = Lista_nom[indice_valor]
            precio = Lista_pre[indice_valor]
            descrp = Lista_des[indice_valor]
            
            print()
            print(nombre + " Q." + precio)
            print(descrp)
            print()
            indice_valor += 1
            indice += 1
        index += 1

#archivo()

'''
file = open("prueba.dot","w")

file.write("digraph matriz{" + os.linesep)

file.write("Nodo_1" + os.linesep)

file.write("}" + os.linesep)

file.close()

os.system("dot.exe -Tpng prueba.dot -o prueba.png")
'''
#os.system("dot.exe -Tpng reporte.dot -o sepuede.png")

#mostrar()
#archivo()

def Mostrar_Factura():
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
    
    filew.write('<div class="card text-white bg-warning">')
    filew.write('<div class="card-body">')
    #for i in v.Lista_Token:
    #    if "TK_NOMBRE_RES" in i:
    #        cadena = '<h1 class="display-4">'+ i[1] +'</h1>'
    #       filew.write(str(cadena))
    filew.write('<center><h5 class="card-title">Restaurante LFP</h5></center>')
    filew.write('<center><h5 class="card-title">Factura No. 01</h5></center>')
    filew.write('<center><h5 class="card-title">Fecha 20/03/2021</h5></center>')
    filew.write('<br>')
    filew.write('<p class="card-text">Datos del Cliente</p>')
    filew.write('<p class="card-text">Nombre: Luis Falla</p>')
    filew.write('<p class="card-text">Nit: 203211232432</p>')
    filew.write('<p class="card-text">Direccion: 1 av 4-33 zona 3</p>')
    filew.write('<br>')
    filew.write('Descripcion')
    filew.write('<table class="table">')
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
    filew.write('<tr>')
    filew.write('<th scope="row"> 2 </th>')
    filew.write('<td> Bebida 1 </td>')
    filew.write('<td> Q11.00 </td>')
    filew.write('<td> Q22.00 </td>')
    filew.write('</tr>')
    filew.write('<tr>')
    filew.write('<th scope="row"> 4 </th>')
    filew.write('<td> Postre 2 </td>')
    filew.write('<td> Q20.00 </td>')
    filew.write('<td> Q80.00 </td>')
    filew.write('</tr>')
    filew.write('<hr>')
    filew.write('<tr>')
    filew.write('<th scope="row"> Sub Total </th>')
    filew.write('<td>  </td>')
    filew.write('<td>  </td>')
    filew.write('<td> Q102.00 </td>')
    filew.write('</tr>')
    filew.write('<tr>')
    filew.write('<th scope="row"> Propina (8%) </th>')
    filew.write('<td>  </td>')
    filew.write('<td>  </td>')
    filew.write('<td> Q102.00 </td>')
    filew.write('</tr>')
    filew.write('<hr>')
    filew.write('<tr>')
    filew.write('<th scope="row"> Total </th>')
    filew.write('<td>  </td>')
    filew.write('<td>  </td>')
    filew.write('<td> Q110.00 </td>')
    filew.write('</tr>')
    filew.write('</tbody>')
    filew.write('</table>')
    filew.write("</div>")
    filew.write("</div>")
    filew.write("</div>")
    filew.write("</body>")        
    filew.write("</html>")        

    filew.close()

    webbrowser.open_new_tab("factura.html")  

#Mostrar_Factura()

#print(chr(39))