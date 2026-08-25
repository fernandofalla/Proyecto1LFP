import sys
from src.ui.file_dialog import seleccionar_archivo
from src.analyzer.afd_menu import AFDMenu
from src.analyzer.afd_factura import AFDFactura
from src.services.menu_service import MenuService
from src.services.factura_service import FacturaService
from src.generators.html_generator import HTMLGenerator
from src.generators.graph_generator import GraphGenerator

class MenuApp:
    def __init__(self):
        # Componentes
        self.afd_menu = AFDMenu()
        self.afd_factura = AFDFactura()
        self.menu_service = MenuService()
        self.factura_service = FacturaService()
        self.html_gen = HTMLGenerator()
        self.graph_gen = GraphGenerator()

        # Textos cargados
        self.texto_menu = ""
        self.texto_orden = ""
        self.tokens_menu = []
        self.errores_menu = []

    def mostrar_encabezado(self):
        print()
        print()
        print("                Proyecto 1 - LFP A+")
        print("     ------------------------------------------")
        print("     |   Nombre: Luis Fernando Falla Guzmán   |")
        print("     |   Carné: 201700700                     |")
        print("     ------------------------------------------")
        print()
        print("1. Cargar menú")
        print("2. Cargar orden")
        print("3. Generar menú")
        print("4. Generar factura")
        print("5. Generar árbol")
        print("6. Salir")
        print()

    def cargar_menu(self):
        contenido = seleccionar_archivo()
        if contenido:
            self.texto_menu = contenido
            print(">> Menú cargado correctamente.")
        else:
            print(">> No se seleccionó ningún archivo de menú.")

    def cargar_orden(self):
        contenido = seleccionar_archivo()
        if contenido:
            self.texto_orden = contenido
            print(">> Orden cargada correctamente.")
        else:
            print(">> No se seleccionó ningún archivo de orden.")

    def generar_menu(self):
        if not self.texto_menu:
            print(">> No se ha cargado ningún archivo de menú.")
            return

        self.tokens_menu, self.errores_menu = self.afd_menu.analizar(self.texto_menu)

        if self.errores_menu:
            print(">> Se encontraron errores en el menú. Generando reporte...")
            self.html_gen.generar_reporte_errores(self.errores_menu)
        else:
            self.menu_service.procesar_tokens(self.tokens_menu)
            self.html_gen.generar_reporte_tokens(self.tokens_menu)

            print()
            decision = input(">> ¿Desea limitar los precios? [Si - No]: ").strip().upper()
            if decision == "SI":
                try:
                    limite = float(input(">> Ingrese el límite: "))
                    self.html_gen.generar_menu(self.menu_service, precio_limite=limite)
                except ValueError:
                    print(">> Límite no válido. Mostrando menú completo.")
                    self.html_gen.generar_menu(self.menu_service)
            else:
                self.html_gen.generar_menu(self.menu_service)

    def generar_factura(self):
        if not self.texto_orden:
            print(">> No se ha cargado ningún archivo de orden.")
            return

        if not self.menu_service.nombre_restaurante:
            print(">> Primero debes cargar y generar el menú antes de facturar.")
            return

        tokens_fac, errores_fac, tokens_ids = self.afd_factura.analizar(self.texto_orden)

        if errores_fac:
            print(">> Se encontraron errores en la orden. Generando reporte...")
            self.html_gen.generar_reporte_errores(errores_fac)
        else:
            if not self.factura_service.validar_propina(tokens_fac):
                print(">> Propina no válida (debe ser entre 0% y 100%).")
                return

            self.html_gen.generar_reporte_tokens(tokens_fac)
            datos_calculados = self.factura_service.calcular_factura(
                tokens_fac, tokens_ids, self.menu_service
            )
            self.html_gen.generar_factura(datos_calculados, self.menu_service.nombre_restaurante)

    def generar_arbol(self):
        if not self.menu_service.nombre_restaurante:
            print(">> Primero debes cargar y procesar el menú.")
            return

        print(">> Generando árbol con Graphviz...")
        self.graph_gen.generar_arbol(self.menu_service)

    def ejecutar(self):
        while True:
            self.mostrar_encabezado()
            opcion = input(">> Ingrese una opción: ").strip()

            if opcion == "1":
                self.cargar_menu()
            elif opcion == "2":
                self.cargar_orden()
            elif opcion == "3":
                self.generar_menu()
            elif opcion == "4":
                self.generar_factura()
            elif opcion == "5":
                self.generar_arbol()
            elif opcion == "6":
                print(">> Saliendo del programa...")
                sys.exit(0)
            else:
                print(">> Opción incorrecta, intente de nuevo.")


def iniciar_programa():
    app = MenuApp()
    app.ejecutar()