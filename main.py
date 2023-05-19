import sys
from DiseñoUi import *
from conexionBD import*
from PyQt5.QtWidgets import QTableWidgetItem
from tkinter import ttk
from tkinter import *
from tkinter import messagebox, simpledialog

class Registro:
    def __init__(self, root):
        self.wind = root
        self.wind.title("Videojuegos")
        self.wind.geometry("850x600")
        self.wind.config(bg="springgreen")

        self.credenciales_permitidas = {"Usu1": "Cont1", "Usu2": "Cont2"}

        usuario = simpledialog.askstring("Inicio de sesión", "Ingrese su nombre de usuario")
        contrasena = simpledialog.askstring("Inicio de sesión", "Ingrese su contraseña", show="*")

        if usuario not in self.credenciales_permitidas or self.credenciales_permitidas[usuario] != contrasena:
            messagebox.showerror("Error", "Credenciales incorrectas. El programa se cerrará.")
            self.wind.destroy() 
            return

class Thegame(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form() 
		self.ui.setupUi(self)

		self.datosTotal = Registro_Juego()
		self.ui.bt_refrescar.clicked.connect(self.e_juegos)
		self.ui.bt_agregar.clicked.connect(self.poner_juegos)
		self.ui.bt_buscar.clicked.connect(self.buscar_juego)
		self.ui.bt_borrar.clicked.connect(self.eliminar_juego)
		self.ui.bt_actualizar.clicked.connect(self.modificar_juegos)
		
		self.ui.tabla_juegos.setColumnWidth(0,98)
		self.ui.tabla_juegos.setColumnWidth(1,100)
		self.ui.tabla_juegos.setColumnWidth(2,98)
		self.ui.tabla_juegos.setColumnWidth(3,98)
		self.ui.tabla_juegos.setColumnWidth(4,98)

		self.ui.tabla_borrar.setColumnWidth(0,98)
		self.ui.tabla_borrar.setColumnWidth(1,100)
		self.ui.tabla_borrar.setColumnWidth(2,98)
		self.ui.tabla_borrar.setColumnWidth(3,98)
		self.ui.tabla_borrar.setColumnWidth(4,98)

		self.ui.tabla_buscar.setColumnWidth(0,98)
		self.ui.tabla_buscar.setColumnWidth(1,100)
		self.ui.tabla_buscar.setColumnWidth(2,98)
		self.ui.tabla_buscar.setColumnWidth(3,98)
		self.ui.tabla_buscar.setColumnWidth(4,98)

	def e_juegos(self):	
		datos = self.datosTotal.buscar_juegos()
		i = len(datos)

		self.ui.tabla_juegos.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_juegos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_juegos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_juegos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_juegos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_juegos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			tablerow +=1
	def poner_juegos(self):
		codigo = self.ui.codigoA.text() 
		nombre = self.ui.nombreA.text()
		plataforma = self.ui.plataformaA.text()
		precio = self.ui.precioA.text()
		estrellas = self.ui.estrellasA.text()

		self.datosTotal.inserta_juego(codigo, nombre, plataforma, precio, estrellas)
		self.ui.codigoA.clear()
		self.ui.nombreA.clear()
		self.ui.plataformaA.clear()
		self.ui.precioA.clear()
		self.ui.estrellasA.clear()

	def modificar_juegos(self):
		id_producto = self.ui.id_juego.text() 
		id_producto = str("'" + id_producto + "'")
		nombreXX = self.datosTotal.busca_juego(id_producto)

		if nombreXX != None:
			self.ui.id_buscar.setText("ACTUALIZAR")
			codigoM = self.ui.codigo_actualizar.text() 
			nombreM = self.ui.nombre_actualizar.text()
			plataformaM = self.ui.plataforma_actualizar.text()
			precioM = self.ui.precio_actualizar.text()
			estrellasM = self.ui.estrellas_actualizar.text()
			act = self.datosTotal.actualiza_juegos(codigoM,nombreM , plataformaM, precioM, estrellasM)
			if act == 1:
				self.ui.id_buscar.setText("ACTUALIZADO")				
				self.ui.codigo_actualizar.clear()
				self.ui.nombre_actualizar.clear()
				self.ui.plataforma_actualizar.clear()
				self.ui.precio_actualizar.clear()
				self.ui.estrellas_actualizar.clear()
				self.ui.id_juego.clear()
			elif act == 0:
				self.ui.id_buscar.setText("ERROR")
			else:
				self.ui.id_buscar.setText("INCORRECTO")		
		else:
			self.ui.id_buscar.setText("NO EXISTE")

	def buscar_juego(self):
		nombre_producto = self.ui.codigoB.text()
		nombre_producto = str("'" + nombre_producto + "'")

		datosB = self.datosTotal.busca_juego(nombre_producto)
		i = len(datosB)

		self.ui.tabla_buscar.setRowCount(i)
		tablerow = 0
		for row in datosB:
			self.ui.tabla_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			tablerow +=1

	def eliminar_juego(self):
		eliminar = self.ui.codigo_borrar.text()
		eliminar = str("'"+ eliminar + "'")
		resp = (self.datosTotal.elimina_juegos(eliminar))
		datos = self.datosTotal.buscar_juegos()
		i = len(datos)
		self.ui.tabla_borrar.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			tablerow +=1
		if resp == None:
			self.ui.borrar_ok.setText("NO EXISTE")
		elif resp == 0:
			self.ui.borrar_ok.setText("NO EXISTE")
		else:
			self.ui.borrar_ok.setText("SE ELIMINO")

if __name__ == "__main__":
     aña = QtWidgets.QApplication(sys.argv)
     mi_game = Thegame()
     mi_game.show()
     sys.exit(aña.exec_())	