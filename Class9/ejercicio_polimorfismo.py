class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Sublcass must implement abstract method")


class Cat(Animal):
    def talk(self):


# no existe la diferencia entre abstracto o interfaz en python

