#Encoding
# -.- coding: utf-8 -*-

# Guardar en lista los números divisibles entre 7 pero no multiplicable entre 5 desde 2000 : 3200
# Imprimir lista separada por comas


def encuentra_numero():

    lista = []

    for valor in range (2000, 3200):
        if (valor%7 == 0) and (valor%5 == 0):
            lista.append(valor)

    print (lista)
encuentra_numero()

