import pickle

from utilidad.modulos import *

ficheroApertura = open("Los_Coches", "rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close
del (ficheroApertura)
for coche in misCoches:
    print(coche.estado())
