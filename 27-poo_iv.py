
''' ------ Clase Coche ------ '''
class Coche():

    def __init__(self):
        '''Para encapsular variables, se añade dos guiones bajos
        delante del nombre de la variable.'''
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    ''' --- Metodos --- '''


    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            return "El coche esta en marcha."
        else:
            return "El coche esta parado."


    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas, Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis} cm de chasis.")


miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.__ruedas=3
miCoche.estado()

print("=============== Creación de un segundo objeto ===============")

miCoche1 = Coche()
print(miCoche1.arrancar(False))
miCoche1.estado()