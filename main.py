import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from turtle import color
import webbrowser

class Myapp():
	def __init__(self):
		self.texto = ''
		# Creando ventana principal
		ventana = tk.Tk()
		ventana.title("Ventana principal")
		ventana.config(bg="dark orange")

		# Icono de la ventana
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath)  
		path = Directorio + r'/img/logo.png'	
		icon = PhotoImage(file=path)
		ventana.wm_iconphoto(True, icon)

		# Centrar la ventana...
		ancho_ventana = ventana.winfo_reqwidth()
		alto_ventana = ventana.winfo_reqheight()
		ancho_pantalla = ventana.winfo_screenwidth()
		alto_pantalla = ventana.winfo_screenheight()
		posicion_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
		posicion_y = (alto_pantalla // 2) - (alto_ventana // 2)
		ventana.geometry("+{}+{}".format(posicion_x, posicion_y))
		
  		# Creado menu desplegable
		
		menu = Menu(ventana)
		ventana.config(menu = menu)
		ventana.resizable(True, True)
		
  		# Objetos de la ventana principal
		# nombre del archivo con su respectiva extension en un label
		LabelEditor = Label(ventana,text="Name.extension")
		LabelEditor.grid(row=1, column=1,sticky="w",padx=10,pady=10)
		# Cuadro de edicion y muestra de archivo cargado a memoria
		self.CuadroEditor = tk.Text(ventana, width=60, height=20)
		self.CuadroEditor.grid(row=2, column=1,sticky="w",padx=10,pady=10)

		# Menu Archivo
		Archivo = Menu(menu, tearoff=0)
		Archivo.add_command(label="Nuevo", command=self.Nuevo)
		Archivo.add_command(label="Abrir", command=self.Abrir)
		Archivo.add_command(label="Guardar", command=self.Guardar)
		Archivo.add_command(label="Guardar Como", command=self.GuardarComo)
		Archivo.add_separator()		
		Archivo.add_command(label="Salir", command=ventana.destroy)
		
		# Menu Analizar
		Analizar = Menu(menu, tearoff=0)
		Analizar.add_command(label="Analizar", command=self.Analizar)
  
		# Menu Tokens
		Tokens = Menu(menu, tearoff=0)
		Tokens.add_command(label="Tokens", command=self.Tokens)
  
		# Menu Errores
		Errores = Menu(menu, tearoff=0)
		Errores.add_command(label="Tokens", command=self.Errores)
  
		menu.add_cascade(label="Archivo", menu=Archivo)
		menu.add_cascade(label="Analizar", menu=Analizar)
		menu.add_cascade(label="Tokens", menu=Tokens)
		menu.add_cascade(label="Errores", menu=Errores)
  
		ventana.mainloop()
	# Creacion de un nuevo archivo
	def Nuevo(self):
		pass
	
  	# Lectura del archivo
	def Abrir(self):  
		file = filedialog.askopenfilename(defaultextension=".json",
		filetypes=[("Archivos de texto", "*.json")])

		if file:
			with open(file, 'r') as archivo:
				# 2. Leer el contenido del archivo
				lineas = archivo.readlines()
				# 3. Cerrar el archivo
				archivo.close()
				self.CuadroEditor.delete(1.0, tk.END)
				for linea in lineas:
					self.CuadroEditor.insert(tk.END,linea)
					self.texto = self.texto + linea
				tkinter.messagebox.showinfo(title="Cargando archivo", message=("El archivo se cargo correctamente a memoria"))
		else:
			tkinter.messagebox.showinfo(title="Cargando archivo", message=("No seleccionaste ningun archivo"))  
			
	
	# Guardar archivo
	def Guardar(self):
		archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos de texto", "*.json")])
		if archivo:
			with open(archivo, 'w') as f:
				text = self.CuadroEditor.get('1.0', tk.END)
				f.write(text)
	# Guardar un archivo Como
	def GuardarComo(self):
		pass

	# Analizar el archivo de entrada
	def Analizar(self):
		if self.texto:
			self.texto = self.texto.strip("{}")
			self.analizar = Analizador(self.texto)
			self.analizar._compile()
			tkinter.messagebox.showinfo(title="Analizando el Texto", message=("El texto fue analizado correctamente"))	
		else:
			tkinter.messagebox.showinfo(title="Analizando el Texto", message=("No existe texto para analizar"))	
      
    # Tokens de entrada
	def Tokens(self):
		pass

	# Errores del ultimo archivo
	def Errores(self):
		self.analizar.GuardarErrores()
		self.texto = ''
	
# Llamada de la aplicacion
if __name__ == "__main__":
    Myapp()