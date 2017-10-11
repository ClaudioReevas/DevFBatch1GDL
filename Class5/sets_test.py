my_set={1,3}

def add_element_to_set():
    my_set.add(2)
    print('element',my_set)
    my_set.update([2,3,4])

    print('Elementos:',my_set)

    my_set.update([4,5],{1,6,8})

    print('Elem:',my_set)

    my_set2={1,3,4,5,6}
    print('set2',my_set2)

    my_set2.discard(4)
    print('set2', my_set2)

    my_set3=set('HelloWorld')
    #desordena la lista
    print(my_set3)

    #Pop random elementos
    my_set3.pop()
    print(my_set3)

    my_set3.clear()


    print(my_set3)
add_element_to_set()