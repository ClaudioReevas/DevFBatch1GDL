


class Empleado(object):
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


class Rol(object):
    def __init__(self, rol):
        self.rol = rol

    def regresar_rol(self):
        return self.rol


class Developer(Empleado, Rol):

    monto_para_aumento = 1.10

    def __init__(self, nombre, apellido, salario, rol,  prog_lang):
        Empleado.__init__(self, nombre, apellido, salario)
        Rol.__init__(self, rol)                             # Dudas: Pq tuve que pasar "self" aqui?

        self.prog_lang = prog_lang



print ("Antes de crear empleados: ", Empleado.numero_de_empleados)

empleado1 = Empleado("hugo", "mecalco", 90000)
empleado2 = Empleado("hugo", "renteria", 100000)
dev1 = Developer("claudio", "rivas", 80000, "Brigada Prevencion Civil", "python")

print ("Antes de crear empleados: ", Empleado.numero_de_empleados)
print empleado1.obtener_datos()
print empleado1.obtener_salario()
print empleado1.aplicar_aumento()

print empleado2 # al imprimir un objeto se imprime solo la referencia en memoria de la instancia

print Empleado.__dict__
print empleado1.__dict__
print dev1.__dict__
print dev1.rol