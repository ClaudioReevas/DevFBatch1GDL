#Enconding
# -*- coding: utf-8 -*-
# Kata #1
# Crea un programa que le pregunte al usuario su nombre y edad.
# Imprime un mensaje dirigido a él,
# que le diga el año en que cumplirá cien años
import time

def validaNumero(numero):
    #valida que el dato ingresado sea un número
    try:
        complex(numero)
        return True
    except ValueError:
        return False

def calcular100Anios(edad):
    # Calcula el año en la que cumplirá 100 años
    anio_actual = int(time.strftime("%Y")) # Obtener el año actual en formato de 4 dígitos YYYY
    cienanios = (anio_actual + 100) - edad
    return cienanios

# Captura de variables nombre y edad
nombre = raw_input("¿Cual es tu nombre? ")
edad = raw_input("¿Cual es tu edad? ")
edad_valida = validaNumero(edad)  #llama a la funcion para validar si se ingresó un valor numérico
while edad_valida == False:  # mientras que edad sea un valor numérico, edad_valida será true, caso contrario solicita
                             # nuevamente la entrada de edad
    print('la edad que ingresaste no es un numero, intenta de nuevo ')
    edad = raw_input("¿Cual es tu edad? ")
    edad_valida = validaNumero(edad)
    if edad_valida == True:  # si la edad es válida rompe el ciclo while
        break

# imprime las salidas de variables
print ('hola {}, actualmente tienes {} años y en el año {} cumplirás 100 años'
       .format(nombre, edad, calcular100Anios(int(edad))))