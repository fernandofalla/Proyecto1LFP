import os

Lista_nombre_res = ["Restaurante LFP"]
Lista_sec = ["Bebidas","Desayunos","Almuerzos"]
Lista_cantidad_pre = [2,2,2]
Lista_nom = ["Bebida1","Bebida2","Desayuno1","Desayuno2","Almuerzo1","Almuerzo2"]
Lista_pre = ["1.00","2.00","5.00","4.00","9.00","9.00"]
Lista_des = ["Desc Bebida1","Desc Bebida2","Desc Desayuno1","Desc Desayuno2","Desc Almuerzo1","Desc Almuerzo2"]

def archivo():
    #cantidad_sec = len(Lista_sec)
    #index = 0
    nombre_sec = None
    numero_sec = 0
    id_sec = "seccion"
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

archivo()

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



