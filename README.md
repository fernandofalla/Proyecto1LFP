# 🍽️ Proyecto 1 - Analizador Léxico de Restaurante (LFP)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Graphviz](https://img.shields.io/badge/Graphviz-Dot-red)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.5-purple?logo=bootstrap&logoColor=white)

Sistema de análisis léxico y procesamiento de órdenes para un restaurante utilizando **Autómatas Finitos Deterministas (AFD)** implementados desde cero en Python. Desarrollado para el curso de **Lenguajes Formales y de Programación (USAC)**.

---

## 👨‍💻 Datos del Estudiante
* **Nombre:** Luis Fernando Falla Guzmán
* **Carné:** 201700700
* **Curso:** Lenguajes Formales y de Programación - Sección A+
* **Universidad:** Universidad de San Carlos de Guatemala (USAC)

---

## ✨ Características Principales

* 📖 **Carga y Análisis de Menú:** Lectura de archivos `.txt` con sintaxis personalizada para definir secciones, platillos, precios y descripciones mediante un AFD.
* 🧾 **Procesamiento de Facturación:** Reconocimiento y cálculo automático de órdenes, datos del cliente, subtotales, propina y total final.
* 📊 **Generación de Reportes en HTML:**
  * Reporte de **Tokens** reconocidos con número, fila, columna y lexema.
  * Reporte de **Errores Léxicos** con detalle de caracteres no reconocidos.
  * Visualización del **Menú** interactivo (con opción de filtrar por precio límite).
  * Generación de **Factura** formateada con Bootstrap.
* 🌳 **Visualización con Graphviz:** Creación automática de árboles jerárquicos del menú en formato `.dot` y renderizado a imagen `.png`.

---

## 📁 Estructura del Proyecto

* **samples/**: Archivos de prueba (`menu.txt`, `factura.txt`).
* **output/**: Archivos generados dinámicamente (`.html`, `.dot`, `.png`).
* **src/models/**: Clases del modelo (`Token`, `Error`).
* **src/analyzer/**: Autómatas AFDs (`AFDMenu`, `AFDFactura`).
* **src/services/**: Lógica de negocio y procesamiento de datos.
* **src/generators/**: Generadores de reportes HTML y árboles Graphviz.
* **src/ui/**: Menú de consola y selector de archivos.
* **main.py**: Punto de entrada de la aplicación.
* **requirements.txt**: Librerías necesarias (`Pillow`).

---

## ⚙️ Requisitos Previos

1. **Python 3.8 o superior** instalado en el sistema.
2. **Graphviz** instalado y agregado a las variables de entorno (PATH).

---

## 🚀 Instalación y Ejecución

1. Clonar el repositorio:
   git clone https://github.com/fernandofalla/Proyecto1LFP.git

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar la aplicación:
   python main.py

---

## 🖥️ Opciones del Menú Principal

* **1. Cargar menú:** Abre el explorador para seleccionar el archivo del menú.
* **2. Cargar orden:** Abre el explorador para seleccionar el archivo de la orden.
* **3. Generar menú:** Genera el menú HTML (completo o con límite de precio) y el reporte de tokens.
* **4. Generar factura:** Calcula subtotales, propina y muestra la factura formateada en HTML.
* **5. Generar árbol:** Crea el grafo en Graphviz y muestra la imagen del menú.
* **6. Salir:** Cierra la aplicación.