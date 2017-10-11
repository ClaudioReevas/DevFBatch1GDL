# dev.f
# crear una clase television con 5 atribustos
# metodos imprimir marca, tamanio y precio


class Television():
    cantidad = 0
    def __init__(self,marca,precio,tamanio,modelo,sku):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.tamanio = tamanio
        self.sku = sku
        Television.cantidad += 1

    def regresar_marca(self):
        return self.marca

    def regresar_tamanio(self):
        return self.tamanio

    def regresar_precio_sin_iva(self):
        return self.precio

    def regresar_precio_con_iva(self):
        return self.precio * 1.16


tv1 = Television("Samsung", 19.3, "20","PGC12345", "AKG123I5OAFN")
tv2 = Television("LG", 21.4, "35", "PGC13345", "GGG123I5OAFN")
tv3 = Television("Toshiba", 55.3, "50", "PGC13345", "GGG123I5OAFN")

print tv1.__dict__
print ("Precio con IVA ", tv1.regresar_precio_con_iva())
print tv2.__dict__
print ("Precio con IVA ", tv2.regresar_precio_con_iva())
print tv3.__dict__
print ("Precio con IVA ", tv3.regresar_precio_con_iva())

print ("Cantidad Televisiones: ", Television.cantidad)

