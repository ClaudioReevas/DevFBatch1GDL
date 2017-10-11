#Encoding
# -.- coding = utf-8 -.-

# Clase padre que se llame figura
# Crear tres clases hijas que cuadrado triangulo y circulo
# Deben tener un metodo que regrese el area de las figurase

import math


class Figura():
    def __init__(self):
        self.__area = 0

    def return_area(self):
        raise NotImplementedError("Sublcass must implement abstract method") # Se obliga a ejecutar una excepción

class Cuadrilatero(Figura):
    def __init__(self, area, basee, altura):
        self.__base = basee
        self.__altura = altura
        self.__area = area

    def return_area(self):
        self.__area = (self.__base * self.__altura)
        return self.__area


class Triangulo(Cuadrilatero):
    def __init__(self, area, basee, altura):
        self.__base = basee
        self.__altura = altura
        self.__area = area

    def return_area(self):
        self.__area = (self.__base * self.__altura) / 2
        return self.__area


class Circulo(Figura):
    def __init__(self, area, radio):
        self.__radio = radio
        self.__area = area

    def return_area(self):
        self.__area = math.sqrt(self.__radio * 3.141516)
        return self.__area

class Paralepipedo(Figura):
    def __init__(self):
        self.__area = 0


cuadrilatero1 = Cuadrilatero(0, 3, 3)
print cuadrilatero1.return_area()
triangulo1 = Triangulo(0, 3, 3)
print triangulo1.return_area()
circulo1 = Circulo(0, 3)
print circulo1.return_area()

input("ahora vamos a ejecutar un metodo de area de figura el cual tiene excepcion, preciona [enter] para continuar")
paralepipedo = Paralepipedo()
print paralepipedo.return_area()



