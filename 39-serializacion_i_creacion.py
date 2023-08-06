import pickle

familia = ["Oscar", "Manen", "Pablo", "Jaime"]
familia.append("Jäger")

fichero_binario = open("familia", "wb")

pickle.dump(familia, fichero_binario)

fichero_binario.close()

del (fichero_binario)
