import os
import webbrowser
from datetime import date

class HTMLGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generar_reporte_tokens(self, lista_tokens):
        ruta = os.path.join(self.output_dir, "Token.html")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("<html><head><title>TOKENS</title>")
            f.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
            f.write('</head><body><div class="container text-center"><br><br>')
            f.write('<div class="jumbotron text-white bg-dark"><h1>Reporte de Tokens</h1>')
            f.write('<p class="lead">Tokens reconocidos por el AFD</p></div>')
            f.write('<table class="table"><thead><tr>')
            f.write('<th class="bg-danger">NO.</th><th class="bg-light">TOKEN</th><th class="bg-info">LEXEMA</th>')
            f.write('<th class="bg-warning">FILA</th><th class="text-light bg-dark">COLUMNA</th></tr></thead><tbody>')

            for idx, tok in enumerate(lista_tokens, 1):
                f.write(f"<tr><td>{idx}</td><td>{tok[0]}</td><td>{tok[1]}</td><td>{tok[2]}</td><td>{tok[3]}</td></tr>")

            f.write("</tbody></table><br><br></div></body></html>")

        webbrowser.open_new_tab(os.path.abspath(ruta))

    def generar_reporte_errores(self, lista_errores):
        ruta = os.path.join(self.output_dir, "Error.html")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("<html><head><title>ERRORES</title>")
            f.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
            f.write('</head><body><div class="container text-center"><br><br>')
            f.write('<div class="jumbotron text-light bg-dark"><h1>Reporte de Errores</h1>')
            f.write('<p class="lead">Errores reconocidos por el AFD</p></div>')
            f.write('<table class="table"><thead><tr>')
            f.write('<th class="bg-danger">NO.</th><th class="bg-light">FILA</th><th class="bg-info">COLUMNA</th>')
            f.write('<th class="bg-warning">CARACTER</th><th class="text-light bg-dark">DESCRIPCION</th></tr></thead><tbody>')

            for idx, err in enumerate(lista_errores, 1):
                f.write(f"<tr><td>{idx}</td><td>{err[0]}</td><td>{err[1]}</td><td>{err[2]}</td><td>{err[3]}</td></tr>")

            f.write("</tbody></table><br><br></div></body></html>")

        webbrowser.open_new_tab(os.path.abspath(ruta))

    def generar_menu(self, menu_service, precio_limite=None):
        nombre_archivo = "menulimite.html" if precio_limite is not None else "menu.html"
        ruta = os.path.join(self.output_dir, nombre_archivo)

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("<html><head><title>Menu</title>")
            f.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
            f.write('</head><body><div class="container"><br><br>')
            f.write(f'<div class="jumbotron text-white bg-dark text-center"><h1 class="display-4">{menu_service.nombre_restaurante}</h1></div>')

            indice_valor = 0
            for index, seccion in enumerate(menu_service.lista_sec):
                f.write('<div class="jumbotron text-white bg-info"><div class="container">')
                f.write(f"<h1>{seccion}</h1><br>")
                cantidad_art = int(menu_service.lista_cantidad_producto[index])

                for _ in range(cantidad_art):
                    precio = float(menu_service.lista_pre[indice_valor])
                    nombre = menu_service.lista_nom[indice_valor]
                    descrp = menu_service.lista_des[indice_valor]

                    if precio_limite is None or precio <= precio_limite:
                        f.write(f"<h2>{nombre} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Q.{precio:.2f}</h2>")
                        f.write(f"<h3>{descrp}</h3><br>")

                    indice_valor += 1

                f.write("</div></div>")

            f.write("<br><br></div></body></html>")

        webbrowser.open_new_tab(os.path.abspath(ruta))

    def generar_factura(self, datos_factura, nombre_restaurante):
        today = date.today()
        ruta = os.path.join(self.output_dir, "factura.html")

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("<html><head><title>Factura</title>")
            f.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
            f.write('</head><body><div class="container"><br><br>')
            f.write('<div class="card text-white bg-dark"><div class="card-body">')
            f.write(f'<center><h1 class="card-title">{nombre_restaurante}</h1></center>')
            f.write(f'<center><h1 class="card-title">Factura No. {datos_factura["numero_factura"]}</h1></center>')
            f.write(f'<center><h1 class="card-title">Fecha {today.day}/{today.month}/{today.year}</h1></center><br>')
            f.write('<p class="card-text">Datos del Cliente</p>')
            f.write(f'<p class="card-text">Nombre: {datos_factura["cliente"]["nombre"]}</p>')
            f.write(f'<p class="card-text">Nit: {datos_factura["cliente"]["nit"]}</p>')
            f.write(f'<p class="card-text">Dirección: {datos_factura["cliente"]["direccion"]}</p><br>')
            f.write('Descripcion<table class="table text-white"><thead><tr>')
            f.write('<th scope="col">Cantidad</th><th scope="col">Concepto</th><th scope="col">Precio</th><th scope="col">Total</th></tr></thead><tbody>')

            for item in datos_factura["items"]:
                f.write(f'<tr><th scope="row">{item["cantidad"]}</th><td>{item["concepto"]}</td><td>Q{item["precio"]:.2f}</td><td>Q{item["total"]:.2f}</td></tr>')

            f.write(f'<hr><tr><th scope="row">Sub Total</th><td></td><td></td><td>Q{datos_factura["subtotal"]:.2f}</td></tr>')
            f.write(f'<tr><th scope="row">Propina ({datos_factura["cliente"]["propina_porcentaje"]}%)</th><td></td><td></td><td>Q{datos_factura["propina"]:.2f}</td></tr>')
            f.write(f'<hr><tr><th scope="row">Total</th><td></td><td></td><td>Q{datos_factura["total"]:.2f}</td></tr>')
            f.write("</tbody></table></div></div></div><br></body></html>")

        webbrowser.open_new_tab(os.path.abspath(ruta))