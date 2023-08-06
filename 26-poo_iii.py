
''' ------ Clase Coche ------ '''
class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    ''' --- Metodos --- '''

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:
            return "El coche esta en marcha."
        else:
            return "El coche esta parado."

miCoche = Coche()

print(f"El largo del chasis es: {miCoche.largoChasis} cm")
print(f"El ancho del chasis es: {miCoche.anchoChasis} cm")
print(f"El Coche tiene: {miCoche.ruedas} ruedas")
miCoche.arrancar()

print(f"El el coche esta { miCoche.estado()}")