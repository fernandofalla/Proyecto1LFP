from tkinter.filedialog import askopenfilename
import tkinter as tk

def seleccionar_archivo():
    # Ocultar la ventana principal gris de Tkinter
    root = tk.Tk()
    root.withdraw()

    ruta = askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    root.destroy()

    if not ruta:
        return None

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except:
        print(">> Error al leer el archivo seleccionado.")
        return None