#Encoding
# -.- coding: utf-8 -*-

# Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista



def capturaLista():
    # Captura la lista hasta recibir un elemento vacío mediante la tecla [Enter]
    elemento = "vacio"
    lista = []
    while elemento != "": # mientras que elemento sea distinto de vacío continua capturando elementos para la lista
        elemento = raw_input("Ingresa el elemento a agregar a la lista, para terminar presiona [Enter]: ")
        if elemento != "": # si el elemento es vacío termina bucle y regresa la lista
            lista.append(elemento)
        else:
             return lista
    else:
        # no capturar mas elementos
        return lista

lista = capturaLista()

palabra = raw_input("Ingresa una palabra:")
x= 0
contador= 0
longitud_lista = len(lista)
print longitud_lista
while x in range(0,longitud_lista):
    if palabra == lista[x]:
        contador = contador + 1
    x = x + 1

print ("La palabra '{}' aparece '{}' veces.".format(palabra, contador))

