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
            return "RESERVADA_RES", self.lexema, self.fila, self.columna
        elif self.token == "igual":
            return "SIMB_IGUAL", self.lexema, self.fila, self.columna
        elif self.token == "porcen":
            return "SIMB_PORCENTUAL", self.lexema, self.fila, self.columna
        elif self.token == "coma":
            return "SIMB_COMA", self.lexema, self.fila, self.columna
        elif self.token == "id":
            return "IDENTIFICADOR", self.lexema, self.fila, self.columna
        elif self.token == "nombre":
            return "NOMBRE", self.lexema, self.fila, self.columna
        elif self.token == "desc":
            return "DESCRIPCION", self.lexema, self.fila, self.columna
        elif self.token == "nombre_res":
            return "NOMBRE_RES", self.lexema, self.fila, self.columna
        elif self.token == "nombre_sec":
            return "NOMBRE_SEC", self.lexema, self.fila, self.columna
        elif self.token == "dos_puntos":
            return "DOS_PUNTOS", self.lexema, self.fila, self.columna
        elif self.token == "corch_ab":
            return "CORCHETE_AB", self.lexema, self.fila, self.columna
        elif self.token == "punto_coma":
            return "PUNTO_COMA", self.lexema, self.fila, self.columna
        elif self.token == "punto":
            return "SIMB_PUNTO", self.lexema, self.fila, self.columna
        elif self.token == "corch_ce":
            return "CORCHETE_CE", self.lexema, self.fila, self.columna
        elif self.token == "numero":
            return "NUMERO_ENTERO", self.lexema, self.fila, self.columna
        elif self.token == "decimal":
            return "NUMERO_DECIMAL", self.lexema, self.fila, self.columna
        elif self.token == "cliente":
            return "NOMBRE_CLIENTE", self.lexema, self.fila, self.columna
        elif self.token == "nit":
            return "NIT_CLIENTE", self.lexema, self.fila, self.columna
        elif self.token == "dir":
            return "DIRECCION_CLIENTE", self.lexema, self.fila, self.columna
        elif self.token == "prop":
            return "PORCENTAJE", self.lexema, self.fila, self.columna
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
        self.token = []
        self.index = 0