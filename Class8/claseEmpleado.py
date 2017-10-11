


class Empleado(object):     # se indica "object" para que una clase hijo pueda heredar, de lo contrario marca error
    monto_para_aumento = 1.04
    numero_de_empleados = 0
    def __init__(self,nombre,apellido,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.email = self.nombre + "." + self.apellido + "@company.com"
        self.salario = salario
        Empleado.numero_de_empleados += 1

    def obtener_datos(self):
        return (self.nombre, self.apellido, self.email)

    def obtener_salario(self):
        return self.salario

    def aplicar_aumento(self):
        self.salario = int(self.salario * self.monto_para_aumento)
        return self.salario



class Developer(Empleado):

    monto_para_aumento = 1.10

    def __init__(self, nombre, apellido, salario,  prog_lang):
        super(Developer, self).__init__(nombre, apellido, salario)  # Se estan utilizando los metodos de la clase padre

                                                                    # Empleado mediante la palabra reservada super
                                                                    #
                                                                    # Se indica el objeto hijo Developer self de la
                                                                    # super clase y ejecuta el init de la clase padre
                                                                    # En python 2 debe definirse asi, en Python3 es
                                                                    # diferente

        self.prog_lang = prog_lang



print ("Antes de crear empleados: ", Empleado.numero_de_empleados)

empleado1 = Empleado("hugo", "mecalco", 90000)
empleado2 = Empleado("hugo", "renteria", 100000)
dev1 = Developer("claudio", "rivas", 80000, "python")

print ("Antes de crear empleados: ", Empleado.numero_de_empleados)
print empleado1.obtener_datos()
print empleado1.obtener_salario()
print empleado1.aplicar_aumento()

print empleado2 # al imprimir un objeto se imprime solo la referencia en memoria de la instancia

print Empleado.__dict__
print empleado1.__dict__
print dev1.__dict__
print dev1.rol

# output
# /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /Users/claudiorivas/PycharmProjects/Class8/claseEmpleado.py
# ('hugo', 'mecalco', 'hugo.mecalco@company.com')
# 90000
# <__main__.Empleado instance at 0x107116f38>
#Process finished with exit code 0