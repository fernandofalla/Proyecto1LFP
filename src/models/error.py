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
        elif self.tipo == "num_inc":
            return self.fila, self.columna, self.caracter, "Numero incorrecto"
        elif self.tipo == "":
            return self.fila, self.columna, self.caracter, "Simbolo desconocido"