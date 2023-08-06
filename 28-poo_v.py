
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


    def arrancar(self,arrancamos, gasolina, aceite, puertas):
        
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            chequeo = self.__chequeo_previo(gasolina, aceite, puertas)

        if self.__enmarcha and chequeo:
            return "El coche esta en marcha."
        elif self.__enmarcha and chequeo == False:
            return "El chequeo previo no es favorable, no podemos arrancar."
        else:
            return "El coche esta parado."


    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas, Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis} cm de chasis.")


    def __chequeo_previo(self, gasolina, aceite, puertas):
        print(f"Realizando chequeo previo.")
        if gasolina:
            self.gasolina = "ok"
        else:
            self.gasolina = "No-ok"
        if aceite:
            self.aceite = "ok"
        else:
            self.aceite = "No-ok"
        if puertas:
            self.puertas = "Cerradas"
        else:
            self.puertas = "Abiertas"

        
        
        # self.gasolina = "ok"
        # self.aceite = "ok"
        # self.puertas = "Cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "Cerradas":
            return True
        else:
            return False
        

miCoche = Coche()
print(miCoche.arrancar(True, True, True, False))
miCoche.estado()

print("=============== Creación de un segundo objeto ===============")

miCoche1 = Coche()
print(miCoche1.arrancar(False, True, True, True))
miCoche1.estado()