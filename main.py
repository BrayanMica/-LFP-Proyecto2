import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from Analizador import Analizador

# Frontend de Aplicacion
class Myapp():
	def __init__(self):
		self.analizar = Analizador('')
		self.Estado_Archivo = False
		self.archivo = None
		self.texto = ''
		self.nombre = 'NombreArchivo'
		self.extension = 'Extension'
		
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
		
  		# Creando la barra de menu
		menus = Menu(ventana)
		ventana.config(menu = menus)
		ventana.resizable(True, True)
		
  		# Objetos de la ventana principal
		# nombre del archivo con su respectiva extension en un label
		self.LabelEditor = Label(ventana,text="Edicion")
		self.LabelEditor.grid(row=1, column=1,sticky="w",padx=10,pady=10)
		self.LabelDatos = Label(ventana,text="Datos")
		self.LabelDatos.grid(row=1, column=2,sticky="w",padx=10,pady=10)
		self.LabelPosicion = Label(ventana,text="", bg="black", fg="yellow")
		self.LabelPosicion.grid(row=3, column=1,sticky="w",padx=10,pady=10)
		# Creando evento de posixionamiento del cursor x,y
		def actualizar_posicion(event):
			pos_actual = self.CuadroEditor.index(tk.INSERT)
			linea, columna = pos_actual.split('.')
			self.LabelPosicion.config(text=f"Posición del cursor: lín. {linea}, col. {columna}")

  		# Cuadro de edicion y muestra de archivo cargado a memoria
		self.CuadroEditor = tk.Text(ventana, width=40, height=20)
		self.CuadroEditor.grid(row=2, column=1,sticky="w",padx=10,pady=10)
		self.CuadroTokens = tk.Text(ventana, width=40, height=20)
		self.CuadroTokens.grid(row=2, column=2,sticky="w",padx=10,pady=10)

		# vincular el evento de clic con la función actualizar_posicion_cursor
		self.CuadroEditor.bind("<KeyRelease>", actualizar_posicion)

		# Menu Archivo
		Archivo = Menu(menus, tearoff=0)
		menus.add_cascade(label="Archivo", menu=Archivo, font=("green",10))		
		Archivo.add_command(label="Nuevo", command=self.preguntar_guardar)
		Archivo.add_command(label="Abrir", command=self.Abrir)
		Archivo.add_command(label="Guardar", command=self.Guardar)
		Archivo.add_command(label="Guardar Como", command=self.GuardarComo)
		Archivo.add_separator()		
		Archivo.add_command(label="Salir", command=ventana.destroy)
		
		# Menu Analizar
		menus.add_command(label="Analizar", command=self.Analizar, font=("green",10))
		# Menu Tokens
		menus.add_command(label="Tokens", command=self.Tokens, font=("green",10))
  
		# Menu Errores
		menus.add_command(label="Errores", command=self.Errores, font=("green",10))
		ventana.mainloop()
	# Creacion de un nuevo archivo
	def limpiar_editor(self):
		self.CuadroEditor.delete("1.0", "end")
		self.CuadroTokens.delete('1.0', 'end')
		self.analizar.Limpiar_ListaTokens
	def preguntar_guardar(self):

		if tkinter.messagebox.askyesno("Guardar cambios", "¿Desea guardar los cambios antes de limpiar el editor?"):
			archivo = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
			if archivo:
				with open(archivo, "w") as f:
					f.write(self.CuadroEditor.get("1.0", "end-1c"))
				self.limpiar_editor()
				self.archivo = None
				self.Estado_Archivo = False
		else:
			self.limpiar_editor()
			self.archivo = None
			self.Estado_Archivo = False
	# Lectura del archivo
	def Abrir(self):  
		self.archivo = filedialog.askopenfilename()
		if self.archivo:
			self.analizar.Limpiar_ListaTokens()
			self.CuadroTokens.delete('1.0', 'end')
			self.LabelEditor.tk_focusNext = "Archivo"
			self.nombre_archivo = os.path.basename(self.archivo)
			self.nombre, self.extension = os.path.splitext(self.nombre_archivo)
			# print("Nombre del archivo: ", nombre)
			# print("Extension del archivo: ", extension)

			with open(self.archivo, 'r') as f:
				contenido = f.read()
				self.CuadroEditor.delete('1.0', 'end')
				self.CuadroEditor.insert('1.0', contenido)
			self.Estado_Archivo = True
		else:
			self.Estado_Archivo = False
	# Guardar archivo
	def Guardar(self):
		if self.Estado_Archivo:
			with open(self.archivo, 'w') as f:
				contenido = self.CuadroEditor.get('1.0', 'end')
				f.write(contenido)
			tkinter.messagebox.showinfo("Guardar", "El archivo fue guardado correctamente")
		elif self.Estado_Archivo == False:
			self.archivo = filedialog.asksaveasfilename(defaultextension=".txt")
			if self.archivo:
				with open(self.archivo, 'w') as f:
					contenido = self.CuadroEditor.get('1.0', 'end')
					f.write(contenido)
				self.Estado_Archivo = True	
	# Guardar un archivo Como
	def GuardarComo(self):
		self.archivo = filedialog.asksaveasfilename(defaultextension=".txt")
		if self.archivo:
			with open(self.archivo, 'w') as f:
				contenido = self.CuadroEditor.get('1.0', 'end')
				f.write(contenido)
			self.Estado_Archivo = True
	# Analizar el archivo de entrada
	def Analizar(self):
		print("Funcion Analizar")
		texto = self.CuadroEditor.get("1.0", "end-1c")
		if texto:
			#print(f"El texto es: {texto}")
			os.system("clear")
			self.analizar = Analizador(texto)
			self.analizar._compile()
			tkinter.messagebox.showinfo("Analisis de datos","Datos analizados")
		else:
			tkinter.messagebox.showinfo("Analisis de datos","No hay datos en el cuadro\nde texto para analizar")	
    # Tokens de entrada
	def Tokens(self):
		Lista_aux = []
		if self.analizar:
			print("Funcion Tokens")
			self.CuadroTokens.delete('1.0', 'end')
			self.CuadroTokens.insert('1.0', '--------- Lista de Tokens -----------')
			Lista_aux = self.analizar.get_ListaTokens()
			fila=1
			for valor in Lista_aux:
				self.CuadroTokens.insert(''+str(fila+1)+'.0', '\n')
				self.CuadroTokens.insert(''+str(fila+1)+'.0', 'Token -> '+valor)
				fila = fila +1
		else:
			tkinter.messagebox.showinfo("Analisis Tokens","No existe datos\nPara")
		
		for i in Lista_aux:
			print(i)
		
	# Errores del ultimo archivo
	def Errores(self):
		print("Funcion Errores")
# Llamada de la aplicacion
if __name__ == "__main__":
    Myapp()