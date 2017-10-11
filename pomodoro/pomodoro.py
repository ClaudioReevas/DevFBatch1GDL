#Encoding
# -*- coding: utf-8 -*-

# Se agregan las dos primeras líneas para aceptar ñ y acentos como parte del encoding
# dev.f GDL Badge 1 Red Belt
# Sensei: Hugo Mecalco
# Deshi:  Claudio Rivas
# Requiere que Firefox sea tu navegador predeterminado



import webbrowser
import time
import os

print "Este es el dev.f_doro"
print "La hora exacta es: ", time.ctime()
print "Vas a rickrolear 60 segundos cada 20 segundos durante 3 veces"
Segs = 0

for x in range (0, 3):
    while Segs < 20:
        Segs += 1
        print (Segs, " segundos")
        time.sleep(1)
    else:
        Segs = 0 # reinicio de contador de segundos

        print("Ahora RickRollea 60 segundos")
        browser = None
        browsers = ("google-chrome","chrome","firefox", "opera", "mosaic", None)
        linkweb = "https://www.youtube.com/watch?v=oHg5SJYRHA0"
        for wb in browsers:
            try:
                browser = webbrowser.get(wb)

                if wb != None:
                    print ("-----------------------------------------")
                    print ("# Navegador predeterminado encontrado #")
                    print ("valor de browser: %s " % browser)
                    print ("valor de wb: %s " % wb)
                    # print ("Valor de browsers ", browsers)
                    print ("-----------------------------------------")
                    print ("]  Abriendo Navegador para RickRollear  [")
                    print ("-----------------------------------------")
                    webbrowser.get(wb).open_new(linkweb)
                    print ("link: %s " % linkweb)
                    print ("-----------------------------------------")
                    break

            except webbrowser.Error:
                if wb is None:
                    print("No hay navegador registrado.")
                else:
                    print("No se ha encontrado '%s'." % wb)
            else:
                if wb is None:
                    print("Se intenta utilizar navegador por defecto.")
                    webbrowser.get(wb).open_new(linkweb)
                else:
                    print("Navegador '%s'." % wb)
        while Segs <= 60:
            Segs += 1
            print (Segs, " segundos")
            time.sleep(1)
        else:
            Segs = 0
            browserExe = "firefox"
            os.system("pkill " + browserExe)

# webbrowser.open_new_tab("https://www.48seeds.com/")

# try:
#    webbrowser.get("chrome").open_new("http://www.recursospython.com/")
# except webbrowser.Error:
#   print "No se ha encontrado Chrome."
