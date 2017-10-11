#Encoding
# -*- coding: utf-8 -*-

lista = []
cantidad = int(raw_input('Indica la cantidad de elementos de la lista: '))

def captura_elementos(numero):
    elemento = raw_input('Ingresa elemento {} : '.format(numero))
    return elemento

for x in range(cantidad):
    lista.append(captura_elementos(x))

print lista