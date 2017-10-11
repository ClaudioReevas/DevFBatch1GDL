def creando_tuplas():
    #empty tuple
    my_tuple = ()

    #nested tuple
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print (my_tuple)

    # tuple can be created without parentheses
    # also called tuple packing

    my_tuple = 3, 4.6, "dog"
    print (my_tuple)

    # tuple unpacking is also posible
    a, b, c = my_tuple
    print (a)
    print (b)
    print (c)

creando_tuplas()



def cambiando_elementos():
    my_tuple = (4, 2, 3, [6, 5])
    # we cannot change an element
    # TypeError 'tuple' object does not support item assignment
    # my_tuple [0] = 9
    my_tuple[3][0] = 9 # solo se cambia el elemnto de lista dentro de la tupla, en este caso el 6 por el 9

cambiando_elementos()