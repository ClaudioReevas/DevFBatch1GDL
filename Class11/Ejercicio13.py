#Encoding
# -*- coding: utf-8 -*-

#Realizar un programa usando la librería "requests" para ejecutar una petición http|get a una API (Google Maps).
# Obtener laa respuesta y poder representar esa respuesta con clases Python.
# El programa debe pedir una latitud y longitud


import json
import requests




# Captura latitud y longitud

latitud = 0.0
longitud = 0.0

def validaNumero(numero, dato):
    #valida que el dato ingresado sea un número
    try:
        valor = float(numero)
        longitud_flotante = len(numero) - numero.find('.', 0, len(numero))
        if longitud_flotante < 3:
            print ("Debes ingresar un numero flotante de por lo menos DOS decimales ", dato)
            return False
        print longitud_flotante
        return True
    except ValueError:
        print ("Debes ingresar un numero flotante de por lo menos DOS decimales ", dato)  # indica al usuario que debe ingresar entero
        return False

num_valido = False                      # inicializa la variable num_valido a False para su uso en el bucle while
while num_valido == False:
    latitud = raw_input("Ingresa un numero flotante para la latitud: ") # solicita al usuario ingresar un numero entero
    num_valido = validaNumero(latitud, "latitud") # regresa un booleano indicando que el numero es un entero valido
    if num_valido:                    # si el numero es un entero valido rompe el bucle, de lo contrario continua
        break

num_valido = False                      # inicializa la variable num_valido a False para su uso en el bucle while
while num_valido == False:
    longitud = raw_input("Ingresa un numero flotante para la longitud: ") # solicita al usuario ingresar un numero entero
    num_valido = validaNumero(longitud, "longitud") # regresa un booleano indicando que el numero es un entero valido
    if num_valido:                    # si el numero es un entero valido rompe el bucle, de lo contrario continua
        break




