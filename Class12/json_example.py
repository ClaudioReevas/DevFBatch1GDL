
midiccionario = {"llave":"valor"}
print midiccionario ['llave']
midiccionario2 = {"llave2":{"llave3":{"llave4":"hola"}}}
print midiccionario2["llave2"]["llave3"]["llave4"]


midiccionario3 = {"llave2":{"llave3":{"llave4":[1,2,3,4,5,6]}}}
print midiccionario3["llave2"]["llave3"]["llave4"][0:5]
print midiccionario3["llave2"]["llave3"]["llave4"][0:11]

# para el caso midiccionario3:
# cuando entras a llave 2 te un otro diccionario, cuando entres a llave 3
# te regresa otro diccionario, mismo caso para llave 4 y luego  puedes acedeer una lista




