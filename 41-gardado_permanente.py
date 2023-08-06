import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad

    def __str__(self):
        return "{} {} {}".format(self.__nombre, self.__genero, self.__edad)


p1 = Persona("Oscar", "Masculino", "50")
