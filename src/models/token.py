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
            return "TK_NIT", self.lexema, self.fila, self.columna
        elif self.token == "dir":
            return "TK_DIRECCION", self.lexema, self.fila, self.columna
        elif self.token == "prop":
            return "TK_PROPINA", self.lexema, self.fila, self.columna
        elif self.token == "precio":
            return "TK_PRECIO", self.lexema, self.fila, self.columna
        elif self.token == "cant_producto":
            return "TK_CANTIDAD_COMIDA", self.lexema, self.fila, self.columna
        else:
            return "SIMBOLO DESCONOCIDO", self.lexema, self.fila, self.columna