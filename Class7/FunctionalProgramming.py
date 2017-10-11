def f(x): return x%3==0 or x%5==0
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def filtrar():
    print filter(f, range(1,15))
    print filter(f, lista[:])
    print (map (f, range(1,15)))



filtrar()


def cubo(x): return x * x * x
print (map (cubo, range(1,11)))