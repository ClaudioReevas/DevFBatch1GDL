#Encoding
# -*- coding: utf-8 -*-

import math

vector1 = [0,0]
vector2 = [0,0]
distancia = 0

def captura():
    lista = []
    for i in range (2):
        lista.append(raw_input('Ingresa elemento {} : '))
    return lista



def calculaDistancia():

    vector1 = captura()
    print vector1
    vector2 = captura()
    print vector2

    Distancia = math.sqrt((int(vector2[0])-int(vector1[0]))) ** 2 + ((int(vector2[1])-int(vector1[1])) ** 2)
    print Distancia

calculaDistancia()









