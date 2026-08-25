import os
from PIL import Image

class GraphGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generar_arbol(self, menu_service):
        dot_path = os.path.join(self.output_dir, "arbol.dot")
        png_path = os.path.join(self.output_dir, "Menu.png")

        with open(dot_path, "w", encoding="utf-8") as f:
            f.write("digraph arbol{" + os.linesep)
            nodo_raiz = "Raiz"
            f.write(f'{nodo_raiz} [label="{menu_service.nombre_restaurante}"]' + os.linesep)

            for seccion in menu_service.lista_sec:
                f.write(f'{nodo_raiz} -> {seccion.replace(" ", "")};' + os.linesep)

            indice_valor = 0
            numero = 0
            for index, seccion in enumerate(menu_service.lista_sec):
                sec_id = seccion.replace(" ", "")
                f.write(f'{sec_id} [label="{seccion}"]' + os.linesep)
                cantidad_art = int(menu_service.lista_cantidad_producto[index])

                for _ in range(cantidad_art):
                    nombre = menu_service.lista_nom[indice_valor]
                    precio = float(menu_service.lista_pre[indice_valor])
                    descrp = menu_service.lista_des[indice_valor]
                    id_producto = f"menu{numero}"

                    f.write(f'{id_producto} [label="{nombre}     Q.{precio:.2f}\\n{descrp}"]' + os.linesep)
                    f.write(f'{sec_id} -> {id_producto};' + os.linesep)

                    numero += 1
                    indice_valor += 1

            f.write("}")

        # Ejecutar Graphviz y abrir imagen
        os.system(f'dot -Tpng "{dot_path}" -o "{png_path}"')
        if os.path.exists(png_path):
            imagen = Image.open(png_path)
            imagen.show()