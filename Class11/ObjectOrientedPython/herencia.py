# Herencia - Creacion de subclases
# Reusar codigo
# Developers y PMs
# Clases python heredan de object
class Empleado(object):
	monto_para_aumento = 1.04

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

	def aplicar_aumento(self):
		self.salario = int(self.salario * self.monto_para_aumento)


class Developer(Empleado):
	monto_para_aumento = 1.10

	def __init__(self, nombre, apellido, salario, prog_lang):
		super(Developer, self).__init__(nombre, apellido, salario)
		self.prog_lang = prog_lang

# empleado_1 = Empleado("hugo", "Mecalco", 90000)
# empleado_2 = Empleado("Test", "User", 80000)

dev_1 = Empleado("hugo", "Mecalco", 90000)
dev_2 = Developer("Prueba", "Empleado", 80000, "python")


# print dev_1.salario
# dev_1.aplicar_aumento()
# print dev_1.salario

# print help(Developer)

print dev_1.email
print dev_2.prog_lang
print dev_2.email

