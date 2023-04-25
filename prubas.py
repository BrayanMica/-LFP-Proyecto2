import tkinter as tk
from tkinter import Label

class VentanaEditor:
    def __init__(self, ventana, nombre_archivo, extension):
        self.nombre = nombre_archivo
        self.extension = extension
        
        # crear el cuadro de texto
        self.CuadroEditor = tk.Text(ventana, width=60, height=20)
        self.CuadroEditor.grid(row=2, column=1, sticky="w", padx=10, pady=10) 
        
        # vincular el evento de clic con la función actualizar_posicion_cursor
        self.CuadroEditor.bind("<Button-1>", self.actualizar_posicion_cursor)
        
        # crear el LabelEditor
        self.LabelEditor = Label(ventana, text="{}{}".format(self.nombre, self.extension))
        self.LabelEditor.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        
        # crear el LabelEditorPosicion
        self.LabelEditorPosicion = tk.Label(ventana, text="")
        self.LabelEditorPosicion.grid(row=3, column=1, sticky="w", padx=10, pady=10)

    def actualizar_posicion_cursor(self, event):
        # obtener la ubicación x e y del cursor
        pos_x = self.CuadroEditor.winfo_pointerx() - self.CuadroEditor.winfo_rootx()
        pos_y = self.CuadroEditor.winfo_pointery() - self.CuadroEditor.winfo_rooty()
        
        # obtener la posición actual del cursor dentro del widget de texto
        pos = self.CuadroEditor.index("@{}h,{}c".format(pos_y, pos_x))
        
        # actualizar el texto del LabelEditorPosicion
        self.LabelEditorPosicion.config(text="Posición del cursor: " + pos)

        # actualizar el texto del LabelEditor con la nueva información
        self.LabelEditor.config(text="{}{}    {}".format(self.nombre, self.extension, pos))

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    editor = VentanaEditor(ventana_principal, "archivo", ".txt")
    ventana_principal.mainloop()
