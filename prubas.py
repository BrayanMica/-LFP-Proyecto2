import tkinter as tk

# Función a ejecutar al hacer clic en el elemento del menú "Archivo"
def nueva_accion():
    print("¡Hola desde la acción del menú 'Archivo'!")

# Creación de la ventana principal
ventana = tk.Tk()

# Creación de la barra de menú
barra_menu = tk.Menu(ventana)

# Agregación del elemento "Archivo" a la barra de menú
barra_menu.add_command(label="Archivo", command=nueva_accion)

# Asociación de la barra de menú a la ventana principal
ventana.config(menu=barra_menu)

# Inicio del loop principal de la aplicación
ventana.mainloop()
