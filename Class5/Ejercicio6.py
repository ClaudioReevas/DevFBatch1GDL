# Hacere unión e intersección con los siguientes sets
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}


def interseccion_A_B():
    A =  {1, 2, 3, 4, 5}
    B =  {4, 5, 6, 7, 8}
    print ("La union de A y B es: ", A | B)
    print ("La interseccion de A y B es: ", A & B)
    print (A.intersection(B)) # un método para intersección
    print(A.union(B)) # un método para unión
interseccion_A_B()