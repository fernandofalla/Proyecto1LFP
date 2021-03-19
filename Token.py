class Token:

    def __init__(self, token, lexema, fila, columna):
        self.token = token
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    def mostrar(self):
        print(self.token, self.lexema, self.fila, self.columna)

    def Retornartoken(self):
        if self.token == "Restaurante":
            return "TK_RESTAURANTE", self.lexema, self.fila, self.columna
        elif self.token == "igual":
            return "TK_IGUAL", self.lexema, self.fila, self.columna
        elif self.token == "porcen":
            return "TK_PORCENTUAL", self.lexema, self.fila, self.columna
        elif self.token == "coma":
            return "TK_COMA", self.lexema, self.fila, self.columna
        elif self.token == "id":
            return "TK_IDENTIFICADOR", self.lexema, self.fila, self.columna
        elif self.token == "nombre":
            return "TK_NOMBRE", self.lexema, self.fila, self.columna
        elif self.token == "desc":
            return "TK_DESCRIPCION", self.lexema, self.fila, self.columna
        elif self.token == "nombre_res":
            return "TK_NOMBRE_RES", self.lexema, self.fila, self.columna
        elif self.token == "nombre_sec":
            return "TK_NOMBRE_SEC", self.lexema, self.fila, self.columna
        elif self.token == "dos_puntos":
            return "TK_DOS_PUNTOS", self.lexema, self.fila, self.columna
        elif self.token == "corch_ab":
            return "TK_CORCHETE_AB", self.lexema, self.fila, self.columna
        elif self.token == "punto_coma":
            return "TK_PUNTO_COMA", self.lexema, self.fila, self.columna
        elif self.token == "punto":
            return "TK_PUNTO", self.lexema, self.fila, self.columna
        elif self.token == "corch_ce":
            return "TK_CORCHETE_CE", self.lexema, self.fila, self.columna
        elif self.token == "numero":
            return "TK_NUMERO_ENTERO", self.lexema, self.fila, self.columna
        elif self.token == "decimal":
            return "TK_NUMERO_DECIMAL", self.lexema, self.fila, self.columna
        elif self.token == "cliente":
            return "TK_NOMBRE_CLIENTE", self.lexema, self.fila, self.columna
        elif self.token == "nit":
            return "TK_NIT_CLIENTE", self.lexema, self.fila, self.columna
        elif self.token == "dir":
            return "TK_DIRECCION_CLIENTE", self.lexema, self.fila, self.columna
        elif self.token == "prop":
            return "TK_PORCENTAJE", self.lexema, self.fila, self.columna
        elif self.token == "precio":
            return "TK_PRECIO", self.lexema, self.fila, self.columna
        elif self.token == "cant_producto":
            return "TK_CANTIDAD_COMIDA", self.lexema, self.fila, self.columna
        else:
            return "SIMBOLO DESCONOCIDO", self.lexema, self.fila, self.columna
        '''
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        elif self.token == "":
            return "", self.lexema, self.fila, self.columna
        '''
       
class Error:

    def __init__(self, tipo, fila, columna, caracter):
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.caracter = caracter
    
    def Mostrar_Error(self):
        print(self.fila, self.columna, self.caracter)
    
    def Retornar_Error(self):
        if self.tipo == "id_inv":
            return self.fila, self.columna, self.caracter, "Identificador no valido"
       
class Valor:

    def __init__(self):
        self.entrada = ""
        self.cadena = ""
        self.cadenaAux = ""
        self.estado = 0
        self.Lista_Token = []
        self.Lista_Error = []
        self.aux = ""
        self.fila = 1
        self.columna = 1
        self.cantidad = 0
        self.token = []
        self.index = 0
        self.Lista_Sec = []
        self.Lista_Nom = []
        self.Lista_Pre = []
        self.Lista_Des = []
        self.Lista_Cantidad_Producto = []