#Encoding
# -*- coding: utf-8 -*-

# poder leer el contenido de una carpeta
# extraer el nombre de los archivos
# obtener lista de nombre de archivos de la carpeta
# modificar el nombre de cada archivo para que no contenga los números

import os
import re

def extraerArchivos():
    # obtener lista de nombres

    directorio = "/Users/claudiorivas/PycharmProjects/Class6/prank/"
    os.getcwd()
    #os.chdir("/prank")
    listaArchivos = os.listdir(directorio)
    print (listaArchivos)
    x = 0
    for x in range (1,len(listaArchivos)):
        nuevoNombreArchivoString = ""
        print listaArchivos[x]
        rutaOriginal = (directorio + listaArchivos[x])
        nombreArchivo = listaArchivos[x]
        nuevoNombreArchivo = []
        for y in range (0, len(nombreArchivo)):
            if nombreArchivo[y].isdigit() == False:
                nuevoNombreArchivo.append(nombreArchivo[y])

        #print nuevoNombreArchivo
        nuevoNombreArchivoString = "".join(nuevoNombreArchivo)
        rutaNueva = directorio + nuevoNombreArchivoString
        #print rutaNueva
        os.rename(rutaOriginal, rutaNueva)


extraerArchivos()





