#Encoding
# -*- coding: utf-8 -*-

def capturaHora():
    hora = raw_input('Captura horas en formato XX:XX :')
    return hora

def validaHora(hora, x):
    print len(hora)
    if len(hora) > 5:
        print "d"
        hora = 'error'
        print hora
    else:
        if int(x) == -1:
            hora = 'error'
        else:
            hora = hora
    return hora

def cambiaFormato():
    hora = capturaHora()
    x = hora.find(":")
    validaHora(hora,x)
    print len(hora), x, hora
    raw_input('seguir')
    m = ""
    horas = int(hora[:x])
    if horas > 23:
        print ("Hora mayor que 24")
        return
    minutos = hora[x + 1:]
    if int(minutos) > 59:
        print ("Minutos mayor que 59")
        return

    print horas
    print minutos

    if horas > 12:
        horas = int(horas) - 12
        m = "pm"
    else:
        horas = int(horas)
        m = "am"

    print ("LA hora es: {}:{} {}".format(horas, minutos,m))

cambiaFormato()