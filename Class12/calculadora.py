class Calculadora(object):
    def __init__(self, marca_param):
        self.marca = marca_param

    def sumar (self, a, b):
        resultado = a + b
        return resultado

    def restar (self, a, b):
        resultado = a - b
        return resultado

    def multiplicar (self, a, b):
        resultado = a * b
        return resultado

    def dividir (self, a, b):
        resultado = float(a / b)
        return resultado

calculadora = Calculadora("Casio")

print calculadora.sumar(7,5)
print calculadora.restar(7,5)
print calculadora.multiplicar(7,5)
print calculadora.dividir(7,5)