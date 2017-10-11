#Encoding
# -.- coding: utf-8 -.-
class Persona:

    # Las variables privadas se definen con "__" a fin de que estas solo puedan ser utilizados por los métodos de la clase

    def __init__(self, nombre, email, age):
        self.nombre = nombre
        self.__email = email
        self.__age = age

    def update_email(self, new_email):
        self.__email = new_email

    def email(self):
        return self.__email

    def __show_age(self):
        return self.__age

    def show_age(self):
        return self.__get_age()

    def __get_age(self):
        return self.__age

    # Sobrecarga de metodos, es definir un segundo método, pero como en el ejemplo de abajo que se encuentra ya definido
    # aunque sobreargandolo para recibir mas variables en el mismo metodo

    def update_email(self, new_email, algo_mas):
        self.__email = new_email + algo_mas

class ninio(Persona):
    def __init__(self, nombre, email, age, school):
        self.nombre = nombre
        self.__email = email
        self.__age = age
        self.__school = school

    # Este es un método sobreescrito, ya que se requiere que haga algo diferente en lugar de hacer lo preestablecido
    # por herencia del objeto padre
    def show_age(self):
        # Hide age
        return "age not allowed to display"

tk = Persona('TK', 'tk@mail.com', 25)
#print tk.__email   # Si trato de imprimir la variable de forma diracta  indica que no tiene el atributo porque es privado
# Traceback (most recent call last):
#  File "/Users/claudiorivas/PycharmProjects/Class9/encapsulacion.py", line 35, in <module>
#    print tk.__email
# AttributeError: Persona instance has no attribute '__email'


tk = Persona('TK', 'tk@mail.com', 25)
print tk.email()
# en este segundo print estoy regresando la variable a través de un metodo público, por eso es accesible


ninio = ninio('TK', 'tk@mail.com', 10, 'Elementary JFK')
print ninio.show_age()