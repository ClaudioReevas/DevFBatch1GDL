
class persona:
    def get_name(self):    # < - - - Las funciones en una class se llaman metodos
        return self.name

 #   pass # es para definir una clase vacia que no truene

class Hidalgo(persona): # < - - - hereda Hidalgo de la clase persona
    def get_age(self):
        return self.age
 #   pass

h = Hidalgo()
age = Hidalgo.get_age()