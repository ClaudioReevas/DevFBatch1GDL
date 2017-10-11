#Encoding
# -*- coding: utf-8 -*-

lista = ['fisica','quimica','matematicas']
lista2 = [1,3,'fisica','quimica','matematicas']
print('imprime elemento 1 de lista', lista[1])
print('imprime elemento 0 de lista2', lista2[0])
print('imprime el ultimo elemento de la de lista2', lista2[-1])
print('imprime rango de elemntos 2 al 4 de lista2', lista2[2:4])
print('imprime todo el rango de elementos', lista2[:])
print('imprime longitud de lista', len(lista))

# por cada elemento imprime el elemento
for x in [1, 2, 3]: print x,





myList = [1, 2, 3, 4, 5, 6]
def recorrer_lista(lista):
    m = 0
    for i in range(len(lista)):
        if m > myList[i]:
            m = myList[i]
        print i, m



recorrer_lista(myList)




# Otra forma de recorrer un for

for elemento in lista:
    print (elemento)


# Agregar elemento a final de a la lista

lista.append('civismo')
print (lista)

# Agregar elemento en una posición
lista.insert(2,"filosofia")
print (lista)


# Sacar el último elemento de una lista, se puede indicar el índice para sacar el elemento
lista.pop()
print lista

# Sacar el elemento por su nombre
lista.remove('fisica')
print lista
