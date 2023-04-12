import tkinter as tk
from tkinter import filedialog
import os

class Editor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Editor de código")
        self.grid()

        self.crear_widgets()

        self.archivo_abierto = None

    def crear_widgets(self):
        self.editor = tk.Text(self)
        self.editor.grid(row=0, column=0, sticky="nsew")

        boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_archivo)
        boton_guardar.grid(row=1, column=0, sticky="e")

    def guardar_archivo(self):
        if self.archivo_abierto:
            archivo = self.archivo_abierto
        else:
            archivo = filedialog.asksaveasfilename(defaultextension=".txt")

        if archivo:
            with open(archivo, 'w') as f:
                contenido = self.editor.get('1.0', 'end')
                f.write(contenido)

            self.archivo_abierto = archivo
            print("Archivo guardado:", archivo)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            nombre_archivo = os.path.basename(archivo)
            nombre, extension = os.path.splitext(nombre_archivo)
            print("Nombre del archivo:", nombre)
            print("Extensión del archivo:", extension)

            with open(archivo, 'r') as f:
                contenido = f.read()
                self.editor.delete('1.0', 'end') # Limpiar el editor
                self.editor.insert('1.0', contenido)

            self.archivo_abierto = archivo
            print("Archivo abierto:", archivo)
    

root = tk.Tk()
editor = Editor(root)
editor.mainloop()
