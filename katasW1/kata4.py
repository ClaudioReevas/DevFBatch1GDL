#Encoding
# -*- coding: utf-8 -*-
# Kata #4
# Escribe una función que tome una lista de números y un número.
# La función debe checar si el número pertenece a la lista y devolver
# el booleano correspondiente

def validaNumero(numero):
    #valida que el dato ingresado sea un número
    if numero == "":
        return True
    else:
        try:
            valor = int(numero)
            return True
        except ValueError:
            print ("Debes ingresar un número entero. Intenta de nuevo")  # indica al usuario que debe ingresar entero
            return False

def capturarLista():
    lista = []
    elemento = "vacio"
    while elemento != "":
        num_valido = False
        while num_valido == False:
            elemento = raw_input("Ingresa el elemento a la lista, para finalizar presiona [Enter]: ")  # solicita al usuario ingresar un numero entero
            num_valido = validaNumero(elemento)  # regresa un booleano indicando que el numero es un entero valido
            if num_valido == True:  # si el numero es un entero valido rompe el bucle, de lo contrario continua
                break
        if elemento != "":
            lista.append(elemento)
        else:
            return lista
    else:
        return lista

def compararNumeroConLista(lista, numero):
    # Compara numero ingresado versus la lista dada por el usuario
    for x in range (0,len(lista)):
        if numero == lista[x]:
            # Coincidencia encontrada
            print ("Coincidencia encontrada {} en posición de lista {}".format((lista[x]), x))
            return lista[x]


lista = capturarLista()
if len(lista) <= 1:
    print ("No existen elementos en la lista para comparar.")
else:
    num_valido = False
    while num_valido == False:
        numero = raw_input("Ingresa un numero entero para comparar con la lista: ")  # solicita al usuario ingresar un numero entero
        num_valido = validaNumero(numero)  # regresa un booleano indicando que el numero es un entero valido
        if num_valido:  # si el numero es un entero valido rompe el bucle, de lo contrario continua
            break
    compararNumeroConLista(lista,numero)