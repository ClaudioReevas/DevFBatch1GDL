#Encoding
# -*- coding: utf-8 -*-

# chocolate 1 - 2.5
# soda      2 - 1.4
# gomitas   3 - 4
# papitas   5 - 1.2
# aceptar solo menor que 5

cantidad = 0
precio_producto = 0

# def iniciar():

def ingresar_cantidad():
    cantidad = raw_input("Ingrese la dinero (entre 1 y 5)")
    while (float(cantidad) >= 1 and float(cantidad)<=5):
        print (cantidad)
        break
    else:
        ingresar_cantidad()


def imprimirProductos():
    print(' --------------------------------------')
    print('| PRODUCTOS                            |')
    print(' --------------------------------------')
    print('|1 CHOCOLATE                       $2.5|')
    print('|2 SODA                            $1.4|')
    print('|3 GOMITAS                           $4|')
    print('|4 PAPITAS                         $1.2|')
    print(' --------------------------------------')

def eligeProducto():
    producto = raw_input('Elige tu producto (1-4')
    if producto == 1:
        precio_producto = 2.5
    elif producto == 2:
        precio_producto = 1.4
    elif producto == 3:
        precio_producto = 4
    elif producto == 4:
        precio_producto = 1.2
    else:
        eligeProducto()

def calcularVuelto():
    imprimirProductos()
    ingresar_cantidad()
    eligeProducto()
    vuelto = float(cantidad) - float(precio_producto)

calcularVuelto()
