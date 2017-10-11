#Encoding
# -*- coding: utf-8 -*-

# Sentencia condicional IF / ELSE
def if_else_control():
    numero1 = 4
    numero2 = 9

    if numero1 > numero2:
        print "{} mayor a {}".format(numero1, numero2)
    elif numero2 <= numero1:
        print "{} igual a {}".format(numero1, numero2)
    else:
        print "error"

if_else_control()

un_string ="hola mundo"
def tamano_de_string (string_size):
    if string_size > 9:
        print "es muy grande, mide {}".format(string_size)
    else:
        print "nice!, mide {}".format(string_size)

tamano_de_string(len(un_string))

count = 0
while count <= 5:
    print count, " is less than 5"
    count = count + 1
    # break <- rompe el ciclo
else:
    print count, " is not less than 5"


for x in range (0, 3):
    print "We're on time %d" % (x)


for x in range(1,10,6):
    print x

def recursiva(intento=1):
    respuesta = raw_input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print "\nFallaste! Inténtalo de nuevo"
            intento += 1
            recursiva(intento) #llamada recursiva
        else:
            print "\Perdiste!"
    else:
        print"\nGanaste"

#recursividad
recursiva()

def saludar(nombre, mensaje="hola "):
    print(mensaje,nombre)

saludar("hugo")
saludar("hugo","sup");
saludar(mensaje="Buen día ", nombre="hugol")



#Asignación Múltiple
def printing():
    a, b, c = 'string', 15, True
    mi_tupla = ('hola mundo', 2014)
    texto, anio = mi_tupla # asigna los valores de la tupla a la variable text y anio, ingresando "hola mundo" en texto y 2014 en anio
    print str(a)
    print str(b)
    print str(c)
    print str(texto) # imprime la primera parte de la tupla
    print str(anio) # imprime la segunda parte de la tupla

printing()


# While
def the_while():
    while True:
        nombre = raw_input("Indique su nombre: ")
        if nombre:
            print nombre
            break

the_while()

# For continuo
def the_for():
    mi_lista = ['Juan','antonio','pedro','herminio']
    for nombre in mi_lista:
        print nombre
    mi_tupla = ('rosa','verde','celeste','amarillo')
    for color in mi_tupla:
        print color
    for anio in range(2001, 2013):
        print "Informes del Año ", str(anio)

the_for()


#librería de time
#librería de web browser
#esperar x tiempo, dormir el programa abrir el explorador y correr el video
