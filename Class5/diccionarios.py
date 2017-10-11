#Encoding
# -.- coding: utf-8 -*-

# Un diccionario es una colección no ordenada de elementos mientras otras estructuras de datos contienen
# solo un valor como elemento, un diccionario tiene pares de llave y valor.

def crear_diccionario():
    # empty dictionario
    my_dict = {}

    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict = {'name': "John", 1: [2, 4, 3]}

    # using dictionary
    my_dict = dict({1: 'apple', 2: 'ball'})

    # from sequence having each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])

def accesar_elementos():
    my_dict = {'name': 'Jack', 'age': 26, 'address': 'Marmol 2971'}

    # output: Jack
    print(my_dict['name'])

    # output: 26
    print(my_dict.get('age')) # A diferencia de la linea 27 con el método get regresa el elemento como "None"
                              # en lugar de tronar el programa

    print(my_dict.get('address'))


accesar_elementos()

def cambiar_agregar_elementos():
    my_dict = {'name': 'hugo', 'age': 26}

    # update value
    my_dict['age'] = 27

    print (my_dict)

    # add item
    new_value = my_dict['address'] = 'zapopan'

    print (my_dict)

cambiar_agregar_elementos()



def eliminar_elementos():
    # create a dictionary
    squares = {1: 1, 2: 4, 3: }

