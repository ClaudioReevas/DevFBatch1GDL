# Variables de clase
# son variables que son compartidas todas las instancias de una clase. son las mismas para cada instancia
class Empleado:
	# variable de clase
	# Constantes para todas las instancias
	monto_para_aumento = 1.04
	numero_de_empleados = 0
	
	# metodo init va a correr automaticamente cada que creamos una nueva instancia
	def __init__(self, nombre, apellido, salario):
		# self -> current instance
		self.nombre = nombre
		self.apellido = apellido
		self.email = nombre + "." + apellido + "@company.com"
		self.salario = salario

		Empleado.numero_de_empleados += 1

	#  no olvidar escribir self cada que definamos un nuevo metodo
	def nombre_completo(self):
		return '{} {}'.format(self.nombre, self.apellido)

	def obtener_salario(self):
		return self.salario

	def aplicar_aumento(self):
		self.salario = int(self.salario * self.monto_para_aumento)

print Empleado.numero_de_empleados

# self es pasado automaticamente por python, atributos son pasados en orden
empleado_1 = Empleado("hugo", "Mecalco", 90000)
empleado_2 = Empleado("Test", "User", 80000)

print Empleado.numero_de_empleados

Empleado.monto_para_aumento = 1.05

# print Empleado.__dict__
# print empleado_1.__dict__

print empleado_1.salario
empleado_1.aplicar_aumento()
print empleado_1.salario

print Empleado.monto_para_aumento
print empleado_1.monto_para_aumento
print empleado_2.monto_para_aumento