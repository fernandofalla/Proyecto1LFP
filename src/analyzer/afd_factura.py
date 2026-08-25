from src.models.token import Token
from src.models.error import Error

class AFDFactura:
    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        self.estado = 0
        self.fila = 1
        self.columna = 1
        self.cadena = ""
        self.cantidad = 0
        self.lista_token = []
        self.lista_error = []
        self.lista_token_factura = []
        self.cadena_aux_factura = ""
        self.cantidad_aux_factura = 0
        self.columna_aux_factura = 0

    def guardar_token(self, token_tipo):
        t = Token(token_tipo, self.cadena, self.fila, self.columna - self.cantidad)
        self.lista_token.append(t.Retornartoken())
        self.cantidad = 0
        self.cadena = ""
        self.estado = 0

    def guardar_token_factura(self, token_tipo):
        t = Token(token_tipo, self.cadena_aux_factura, self.fila, self.columna_aux_factura - self.cantidad_aux_factura)
        self.lista_token_factura.append(t.Retornartoken())
        self.cantidad_aux_factura = 0
        self.cadena_aux_factura = ""
        self.estado = 0

    def guardar_error(self, error_tipo):
        e = Error(error_tipo, self.fila, self.columna - self.cantidad, self.cadena)
        self.lista_error.append(e.Retornar_Error())
        self.cantidad = 0
        self.cadena = ""
        self.estado = 0

    def analizar(self, entrada):
        self.reiniciar()
        entrada = entrada + "#"

        for elemento in entrada:
            if self.estado == 0:
                if elemento == "\n":
                    self.fila += 1
                    self.columna = 1
                elif elemento == " " or elemento == "\t":
                    self.columna += 1
                elif elemento == ",":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("coma")
                elif elemento == "'":
                    self.columna += 1
                    self.estado = 1
                elif elemento.isdigit():
                    self.cadena += elemento
                    self.cantidad += 1
                    self.columna += 1
                    self.estado = 2
                elif elemento.isalpha():
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.estado = 3
                elif elemento == "#":
                    break
                else:
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_error("")

            elif self.estado == 1:
                if elemento.isalpha() or elemento.isdigit() or elemento in [" ", "-", ".", ","]:
                    self.cadena += elemento
                    self.cantidad += 1
                    self.columna += 1
                elif elemento == "'":
                    self.columna += 1
                    if self.cadena.replace(" ", "").isalpha():
                        self.columna -= 1
                        self.guardar_token("cliente")
                        self.columna += 1
                    elif self.cadena.replace("-", "").isdigit():
                        self.columna -= 1
                        self.guardar_token("nit")
                        self.columna += 1
                    else:
                        self.columna -= 1
                        self.guardar_token("dir")
                        self.columna += 1

            elif self.estado == 2:
                if elemento.isdigit():
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                elif elemento == " ":
                    self.columna += 1
                elif elemento == ",":
                    self.guardar_token("cant_producto")
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_token("coma")
                elif elemento == "%":
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_token("prop")
                elif elemento == ".":
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.estado = 4

            elif self.estado == 3:
                if elemento.isalpha() or elemento.isdigit() or elemento in ["_", " "]:
                    self.cadena += elemento
                    self.cantidad += 1
                    self.columna += 1
                else:
                    if self.cadena.isidentifier():
                        self.cadena_aux_factura = self.cadena
                        self.cantidad_aux_factura = self.cantidad
                        self.columna_aux_factura = self.columna
                        self.guardar_token("id")
                        self.guardar_token_factura("id")
                        self.fila += 1
                        self.columna = 1
                    else:
                        self.columna += 1
                        self.cantidad = 1
                        self.cadena += elemento
                        self.guardar_error("id_inv")

            elif self.estado == 4:
                if elemento.isdigit():
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                elif elemento == "%":
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_token("prop")
                else:
                    self.cadena = ""
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad = 1
                    self.guardar_error("")

        return self.lista_token, self.lista_error, self.lista_token_factura