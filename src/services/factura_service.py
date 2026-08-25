class FacturaService:
    def __init__(self):
        self.numero_factura = 1

    def validar_propina(self, lista_tokens_factura):
        valor_propina = "0"
        for token in lista_tokens_factura:
            if token[0] == "TK_PROPINA":
                valor_propina = token[1]
                break

        sin_porcentaje = valor_propina.replace("%", "").strip()
        try:
            prop = float(sin_porcentaje)
            return 0 <= prop <= 100
        except:
            return False

    def calcular_factura(self, lista_tokens_factura, tokens_factura_ids, menu_service):
        # 1. Extraer datos del cliente y propina
        cliente = {"nombre": "", "nit": "", "direccion": "", "propina_porcentaje": 0.0}
        cantidades = []
        ids_pedidos = []

        for token in lista_tokens_factura:
            tipo = token[0]
            lexema = token[1]

            if tipo == "TK_NOMBRE_CLIENTE":
                cliente["nombre"] = lexema
            elif tipo == "TK_NIT":
                cliente["nit"] = lexema
            elif tipo == "TK_DIRECCION":
                cliente["direccion"] = lexema
            elif tipo == "TK_PROPINA":
                cliente["propina_porcentaje"] = float(lexema.replace("%", "").strip())
            elif tipo == "TK_CANTIDAD_COMIDA":
                cantidades.append(int(lexema))

        for token in tokens_factura_ids:
            if token[0] == "TK_IDENTIFICADOR":
                ids_pedidos.append(token[1])

        # 2. Calcular líneas de la factura
        items_factura = []
        subtotal = 0.0

        for i in range(len(ids_pedidos)):
            id_pedido = ids_pedidos[i]
            cantidad = cantidades[i]

            if id_pedido in menu_service.lista_ide:
                indice_menu = menu_service.lista_ide.index(id_pedido)
                concepto = menu_service.lista_nom[indice_menu]
                precio_unitario = float(menu_service.lista_pre[indice_menu])
                total_linea = cantidad * precio_unitario
                subtotal += total_linea

                items_factura.append({
                    "cantidad": cantidad,
                    "concepto": concepto,
                    "precio": precio_unitario,
                    "total": total_linea
                })

        total_propina = (cliente["propina_porcentaje"] / 100.0) * subtotal
        total_final = subtotal + total_propina

        resultado = {
            "numero_factura": self.numero_factura,
            "cliente": cliente,
            "items": items_factura,
            "subtotal": subtotal,
            "propina": total_propina,
            "total": total_final
        }

        self.numero_factura += 1
        return resultado