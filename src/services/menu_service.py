class MenuService:
    def __init__(self):
        self.nombre_restaurante = ""
        self.lista_sec = []
        self.lista_ide = []
        self.lista_nom = []
        self.lista_pre = []
        self.lista_des = []
        self.lista_cantidad_producto = []

    def procesar_tokens(self, lista_tokens):
        # Reiniciar datos
        self.nombre_restaurante = ""
        self.lista_sec = []
        self.lista_ide = []
        self.lista_nom = []
        self.lista_pre = []
        self.lista_des = []
        self.lista_cantidad_producto = []

        # Contar productos por sección
        contador = 0
        for token in lista_tokens:
            if token[0] == "TK_NOMBRE":
                contador += 1
            elif token[0] == "TK_NOMBRE_SEC":
                self.lista_cantidad_producto.append(contador)
                contador = 0
        
        self.lista_cantidad_producto.append(contador)
        if len(self.lista_cantidad_producto) > 0:
            self.lista_cantidad_producto.pop(0)

        # Extraer cada dato a su lista correspondiente
        for token in lista_tokens:
            tipo = token[0]
            lexema = token[1]

            if tipo == "TK_NOMBRE_RES":
                self.nombre_restaurante = lexema
            elif tipo == "TK_NOMBRE_SEC":
                self.lista_sec.append(lexema)
            elif tipo == "TK_IDENTIFICADOR":
                self.lista_ide.append(lexema)
            elif tipo == "TK_NOMBRE":
                self.lista_nom.append(lexema)
            elif tipo == "TK_PRECIO":
                self.lista_pre.append(lexema)
            elif tipo == "TK_DESCRIPCION":
                self.lista_des.append(lexema)