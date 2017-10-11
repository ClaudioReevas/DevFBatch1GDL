#Encoding
# -*- coding: utf-8 -*-
# Kata #3
# Escribe un programa que tome una lista de números
# (por ejemplo, a = [5, 10, 15, 20, 25]) y haz dos nuevas listas.
# una que contenga sólo el primer y último número de la lista original
# y otra que contenga todos los números intermedios

# inicializa variables
lista = []
listasResultado = []
listaExtremos = []
listaMedios = []

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

def obtenerMediosYExtremos(lista = []):
    # obtiene los medios y extremos de la lista
    if len(lista) > 2: # existen los elementos extremo y uno o mas elementos medios
        extremos = [lista[0],lista[len(lista)-1]] # los medios son todos los elementos entre los extremos
        medios = lista[1:len(lista) - 1]  # los extremos son el primer y último elemento
        print ("Los extremos son: "), extremos
        print ("Los medios de la lista son: "), medios
    elif len(lista) == 2: # existen solo dos elementos en la lista, no hay medios
        extremos = [lista[0],lista[len(lista)-1]] # los medios son todos los elementos entre los extremos
        medios = []
        print "Sin elementos medios en la lista, existen solo dos elementos considerados como extremos: ", extremos
    elif len(lista) == 1:
        extremos = lista[0] # existe solo un elemento en la lista
        medios = []
        print "Solo se cuenta con un elemento en la lista {}".format(extremos)
    elif len(lista) == 0: # no existe ningún elemento en la lista
        print "Sin elementos en la lista, no ingresaste ningún elemento"

lista = capturaLista()
obtenerMediosYExtremos(lista)