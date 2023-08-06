import pickle
from utilidad.modulos import *

coche1 = Vehiculos("Mazda", "MX5")
coche2 = Vehiculos("Seat", "Leon")
coche3 = Vehiculos("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("Los_Coches", "wb")
pickle.dump(coches, fichero)

fichero.close
del (fichero)
print(f"El fichero se ha creado correctamente.")

# ficheroApertura = open("Los_Coches", "rb")
# misCoches = pickle.load(ficheroApertura)
# ficheroApertura.close
# del (ficheroApertura)
# for coche in misCoches:
#     print(coche.estado())
