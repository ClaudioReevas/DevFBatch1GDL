#Enconding
# -*- coding: utf-8 -*-
# Kata #2
# Pídele un número al usuario.
# Dependiendo de si el número es par o impar,
# imprime el mensaje apropiado al usuario

def validaNumero(numero):
    #valida que el dato ingresado sea un número
    try:
        valor = int(numero)
        return True
    except ValueError:
        print ("Debes ingresar un número entero. ")  # indica al usuario que debe ingresar entero
        return False

num_valido = False                      # inicializa la variable num_valido a False para su uso en el bucle while
while num_valido == False:
    numero = raw_input("Ingresa un numero entero: ") # solicita al usuario ingresar un numero entero
    num_valido = validaNumero(numero) # regresa un booleano indicando que el numero es un entero valido
    if num_valido:                    # si el numero es un entero valido rompe el bucle, de lo contrario continua
        break

if int(numero) == 0:                    # si es 0 no es par ni inpar
    print ("Ingresaste 0, no es par ni inpar")
elif int(numero)%2 == 0:                # si es divisible entre 2 es par
    print ("Ingresaste un número par")
else:                                   # si no es divisible entre 2 es impar
    print ("Ingresaste un número impar (non)")
