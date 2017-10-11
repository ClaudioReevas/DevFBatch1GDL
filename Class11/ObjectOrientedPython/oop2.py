# Variables de instancia (atributos de objetos)
class Empleado:
	
	# metodo init va a correr automaticamente 
	def __init__(self, nombre, apellido, salario):
		# self -> current instance
		self.nombre = nombre
		self.apellido = apellido
		self.email = nombre + "." + apellido + "@company.com"
		self.salario = salario

	#  no olvidar escribir self cada que definamos un nuevo metodo
	def nombre_completo(self):
		return '{} {}'.format(self.nombre, self.apellido)

	def obtener_salario(self):
		return self.salario


# self es pasado automaticamente por python, atributos son pasados en orden
empleado_1 = Empleado("hugo", "Mecalco", 90000)
empleado_2 = Empleado("Test", "User", 80000)

# print empleado_1
# print empleado_2

print empleado_1.email
print str(empleado_1.obtener_salario())
# print empleado_2.email

print empleado_1.nombre_completo()
print Empleado.nombre_completo(empleado_1)