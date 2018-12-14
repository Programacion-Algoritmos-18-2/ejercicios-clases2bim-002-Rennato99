import codecs
import sys

class MiArchivo:

	# Constructor
	def __init__(self):
		self.archivo = codecs.open("data/demo_notas.csv", "r")

	# Metodo que retorna una lista cuyos elementos son cada linea
	def obtener_informacion(self):
		return self.archivo.readlines()

	# Metodo para cerrar el archivo
	def cerrar_archivo(self):
		self.archivo.close()


class MiArchivoEscribir:

	# Constructor
	def __init__(self):
		self.archivo = codecs.open("data/demo2.csv", "a")

	# Metodo para agregar informacion
	def agregar_informacion(self, p):
		self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
				p.edad, p.codigo))

	# Metodo para cerrar el archivo
	def cerrar_archivo(self):
		self.archivo.close()
