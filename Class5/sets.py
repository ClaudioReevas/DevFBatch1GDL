def delete_sets_elements():
    #initialize my_set
    my_set = {1, 2 ,3, 4, 5, 6}
    print (my_set)

    #discard an element
    my_set.discard(4) # no es necesario que elemento se encuentre en la lista
    print (my_set)

    #remove an element
    my_set.remove(6) # cuidar que elemento exista al hacer remove
    print (my_set)


delete_sets_elements()
