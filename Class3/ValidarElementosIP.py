#Encoding
# -*- coding: utf-8 -*-

# 192.168.1.1


def validaOcteto(octetos):

    for octeto in range(octetos):
        if octeto.isdigit():
            #es digito
            if (octeto >= 0) and (octeto <=255):
                # es un octeto correcto
                print "false"
                a = "true"
            else:
                a = "false1"
                print a
                # es octeto pero incorrecto
        else:
            a = "false2"
            print a
            # no es octeto

def romperEnOctetos(stringIP):
    octetos = [192,168,1,1]
    octetos = stringIP.split(".")
    print ("Separando IP en octetos mediante '.'", octetos)
    return octetos


def capturaIP():
    stringIP = raw_input("Dame tu IP: ")
    validaOcteto(romperEnOctetos(stringIP))


    # stringIP = raw_input("Dame una direccion IP en cadena: ")


capturaIP()
