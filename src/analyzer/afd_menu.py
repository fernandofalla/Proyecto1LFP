from src.models.token import Token
from src.models.error import Error

class AFDMenu:
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

    def guardar_token(self, token_tipo):
        t = Token(token_tipo, self.cadena, self.fila, self.columna - self.cantidad)
        self.lista_token.append(t.Retornartoken())
        self.cantidad = 0
        self.cadena = ""
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
                if elemento == " ":
                    self.columna += 1
                elif elemento == '\n':
                    self.fila += 1
                    self.columna = 1
                elif elemento == "\t":
                    self.columna += 1
                elif elemento == "=":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("igual")
                elif elemento == ":":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("dos_puntos")
                elif elemento == ";":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("punto_coma")
                elif elemento == "[":
                    self.cadena += elemento
                    self.guardar_token("corch_ab")
                    self.columna += 1
                    self.estado = 4
                elif elemento == "]":
                    self.cadena += elemento
                    self.guardar_token("corch_ce")
                    self.columna += 1
                elif elemento.isalpha():
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.estado = 1
                elif elemento.isdigit():
                    self.columna += 1
                    self.cadena += elemento
                    self.estado = 5
                elif elemento == "'":
                    self.columna += 1
                    self.estado = 2
                elif elemento == "#":
                    break
                else:
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_error("")

            elif self.estado == 1:
                if elemento.isalpha():
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                elif elemento == " ":
                    if self.cadena.upper() == "RESTAURANTE":
                        self.guardar_token("Restaurante")
                        self.columna += 1
                    else:
                        self.guardar_error("")
                elif elemento == "=":
                    self.guardar_token("Restaurante")
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("igual")
                else:
                    self.cadena = ""
                    self.cantidad = 1
                    self.columna += 1
                    self.cadena += elemento
                    self.guardar_error("")

            elif self.estado == 2:
                if elemento.isalpha() or elemento.isdigit() or elemento in ["_", "-", " ", "#"]:
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                elif elemento == "'":
                    self.columna += 1
                    self.estado = 3

            elif self.estado == 3:
                if elemento == ":":
                    self.columna -= 1
                    self.guardar_token("nombre_sec")
                    self.columna += 1
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_token("dos_puntos")
                elif elemento == ";":
                    self.columna -= 1
                    self.guardar_token("nombre")
                    self.columna += 1
                    self.cadena += elemento
                    self.columna += 1
                    self.cantidad += 1
                    self.guardar_token("punto_coma")
                elif elemento == "]":
                    self.columna -= 1
                    self.guardar_token("desc")
                    self.cadena += elemento
                    self.guardar_token("corch_ce")
                elif elemento == " ":
                    self.columna += 1
                    self.cantidad += 1
                elif elemento == "\n":
                    self.columna -= 1
                    self.guardar_token("nombre_res")
                    self.fila += 1
                    self.columna = 1
                    self.estado = 0
                else:
                    self.cadena = ""
                    self.cadena += elemento
                    self.cantidad = 1
                    self.columna += 1
                    self.guardar_error("")

            elif self.estado == 4:
                if elemento.isalpha() or elemento.isdigit() or elemento == "_":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                elif elemento == ";":
                    if self.cadena.isidentifier():
                        self.guardar_token("id")
                        self.columna += 1
                        self.cantidad += 1
                        self.cadena += elemento
                        self.guardar_token("punto_coma")
                    else:
                        self.guardar_error("")
                        self.columna += 1
                        self.cadena += elemento
                        self.cantidad += 1
                        self.guardar_token("punto_coma")
                elif elemento == " ":
                    if self.cadena == "":
                        self.columna += 1
                    else:
                        self.columna += 1
                        self.estado = 7
                else:
                    self.cadena += elemento
                    self.cantidad += 1
                    self.columna += 1
                    self.guardar_error("")

            elif self.estado == 5:
                if elemento.isdigit():
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                elif elemento == " ":
                    self.columna += 1
                elif elemento == ";":
                    self.columna -= 1
                    self.guardar_token("precio")
                    self.columna += 2
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("punto_coma")
                elif elemento == "%":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("prop")
                elif elemento == ".":
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.estado = 6
                else:
                    self.columna += 1
                    self.cadena += elemento
                    self.cantidad += 1
                    self.guardar_error("num_inc")

            elif self.estado == 6:
                if elemento.isdigit():
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                elif elemento == ";":
                    self.guardar_token("precio")
                    self.columna += 1
                    self.cantidad += 1
                    self.cadena += elemento
                    self.guardar_token("punto_coma")
                elif elemento == " ":
                    self.guardar_token("precio")
                    self.columna += 1
                    self.estado = 0

            elif self.estado == 7:
                if elemento == " ":
                    self.columna -= 1
                    self.guardar_token("id")
                    self.columna += 2
                    self.estado = 0
                elif elemento == ";":
                    self.columna -= 1
                    self.guardar_token("id")
                    self.columna += 2
                    self.cantidad = 1
                    self.cadena += elemento
                    self.guardar_token("punto_coma")
                else:
                    self.columna += 1
                    self.cantidad += 2
                    self.cadena += " " + elemento
                    self.guardar_error("id_inv")

        return self.lista_token, self.lista_error