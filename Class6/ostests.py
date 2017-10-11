#Encoding
# -*- coding: utf-8 -*-

# requiere contar con la carpeta y archivos dentro de ella (los que sean) dentro de /prank y estar la carpeta
# al mismo nivel que el archivo de ostest.py∫
# pruebas de librería os

import os


directorio = os.getcwd()
print ("Estas en el directorio: ", directorio)
directorio = directorio + "/prank"
print ("Nuevo Directorio para cambiar: ", directorio)
os.chdir(directorio)
directorio = os.getcwd()
print ("Cambiaste al directorio: ", directorio)
print ("")
print ("Contenido del directorio: ")
listaArchivos = os.listdir(directorio)
print (str(listaArchivos))
