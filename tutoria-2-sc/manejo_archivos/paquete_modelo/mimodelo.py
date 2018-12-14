"""
	creación de clases
"""

class Persona(object):
	# Constructor
	def __init__(self, nombre, apellido, edad, codigo, nota1, nota2):
		self.agregar_nombre(nombre)
		self.agregar_apellido(apellido)
		self.agregar_edad(edad)
		self.agregar_codigo(codigo)
		self.agregar_nota1(nota1)
		self.agregar_nota2(nota2)

	# Metodos set
	def agregar_nombre(self, n):
		self.nombre = n

	def agregar_edad(self, n):
		self.edad = int(n)
	
	def agregar_codigo(self, n):
		self.codigo = int(n)

	def agregar_apellido(self, n):
		self.apellido = n
	
	def agregar_nota1(self, n):
		self.nota1 = int(n)

	def agregar_nota2(self, n):
		self.nota2 = int(n)

	# Metodos get
	def obtener_nombre(self):
		return self.nombre

	def obtener_edad(self):
		return self.edad

	def obtener_codigo(self):
		return self.codigo

	def obtener_apellido(self):
		return self.apellido

	def obtener_nota1(self):
		return self.nota1

	def obtener_nota2(self):
		return self.nota2

	# Modificamos el str
	def __str__(self):
		return " %s - %s - %d - %d - %d - %d" % (self.obtener_nombre(), self.obtener_apellido(),\
				self.obtener_edad(), self.obtener_codigo(), self.obtener_nota1(), self.obtener_nota2())


# Creando la clase OperacionesPersona
class OperacionesPersona(object):
	
	# Constructor
	def __init__(self, listado):
		self.listado_personas = listado

	# Modificamos el str
	def __str__(self):
		cadena = "\nListado de todas las personas:\n"
		for n in self.listado_personas:
			cadena = ("%s\tNombre: %s %s\n" %(cadena, n.obtener_nombre(), n.obtener_apellido()))
		return cadena

	# Metodo para obtener el promedio de las notas 1
	def obtener_promedio_n1(self):
		suma = 0 # Inicializamos suma
		for n in self.listado_personas: # Recorremos el listado de personas
			suma += n.obtener_nota1()  # Actualizamos suma
		promedio = suma / len(self.listado_personas)  # Calculamos el promedio
		return promedio # Retornamos el promedio

	# Metodo para obtener el promedio de las notas 2
	def obtener_promedio_n2(self):
		suma = 0 # Inicializamos suma
		for n in self.listado_personas:  # Recorremos el listado de personas
			suma += n.obtener_nota2()  # Actualizamos suma
		promedio = suma / len(self.listado_personas)  # Calculamos el promedio
		return promedio  # Retornamos el promedio

	# Metodo que retorne los personas con notas1 menores que 15
	def obtener_listado_n1(self):
		cadena = "Personas con nota 1 menores que 15:\n" # Encabezado
		
		for n in self.listado_personas: # Recorremos el listado de personas
			
			if (n.obtener_nota1() < 15): # Verificamos si es menor que 15
				cadena = ("%s\tNombre: %s %s; Nota %d\n" %(cadena, n.obtener_nombre(), n.obtener_apellido(), n.obtener_nota1())) # Formateo de cadena
		
		return cadena  # Retornamos la cadena

	# Metodo que retorne los personas con notas2 menores que 15
	def obtener_listado_n2(self):
		cadena = "Personas con nota 2 menores que 15:\n" # Encabezado
		
		for n in self.listado_personas: # Recorremos el listado de personas
			
			if (n.obtener_nota2() < 15): # Verificamos si es menor que 15
				cadena = ("%s\tNombre: %s %s; Nota: %d\n" %(cadena, n.obtener_nombre(), n.obtener_apellido(), n.obtener_nota2())) # Formateo de cadena
		
		return cadena  # Retornamos la cadena


	# Metodo que retorna el listado de personas cuyo nombre empieza con dos letras específicas
	def obtener_listado_personas(self, primeraLetra, segundaLetra):
		cadena = "Personas con las iniciales especificadas:\n" # Encabezado
		
		for n in self.listado_personas: # Recorremos el listado de personas
			
			if (n.obtener_nombre()[0] == primeraLetra or n.obtener_nombre()[0] == segundaLetra): # Verificamos si la primera letra del nombre empieza con las letras especificadas
				cadena = ("%s\tNombre: %s %s\n" %(cadena, n.obtener_nombre(), n.obtener_apellido())) # Formateo de cadena
		
		return cadena  # Retornamos la cadena