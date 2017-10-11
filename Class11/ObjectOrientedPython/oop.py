
"""Simple clase vacia"""
class Empleado:
	pass

empleado_1 = Empleado()
empleado_2 = Empleado()

print empleado_1
print empleado_2

empleado_1.nombre = "hugo"
empleado_1.apellido = "Mecalco"
empleado_1.email = "hugo.mecalco@company.com"
empleado_1.salario = 90000

empleado_2.nombre = "Test"
empleado_2.apellido = "User"
empleado_2.email = "test.user@company.com"
empleado_2.salario = 80000

print empleado_1.email
print empleado_2.email