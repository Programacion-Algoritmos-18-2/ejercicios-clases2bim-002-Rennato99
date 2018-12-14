from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona


m = MiArchivo()     					 # Creamos un objeto MiArchivo
lista = m.obtener_informacion()			 # Obtenemos la lista de lineas del file
lista = [l.split("|") for l in lista]	 # Dividimos cada linea en otra lista


lista = lista[1:]		# Desechamos el primer elemento que es el encabezado
lista_personas = []     # Creamos otra lista vacia


for d in lista:   # Recorremos la lista
	
	p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])     # Creamos un objeto persona por cada elemento de la lista
	lista_personas.append(p)   							# Agregamos el objeto a la lista_personas

operaciones = OperacionesPersona(lista_personas)  # Creamos el objeto operaciones

print(operaciones)     # Imprima todos los elementos
print("Promedio de notas 1:\n\t%d\n"% (operaciones.obtener_promedio_n1()))  # Imprime el promedio de notas 1
print("Promedio de notas 2:\n\t%d\n"% (operaciones.obtener_promedio_n2()))  # Imprime el promedio de notas 2
print(operaciones.obtener_listado_n1())	  # Imprime las personas con notas 1 menores que 15
print(operaciones.obtener_listado_n2())   # Imprime las personas con notas 2 menores que 15
print(operaciones.obtener_listado_personas("R", "J"))  # Imprime las personas cuyo nombre empiece con R o J