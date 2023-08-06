import pickle


fichero_binario = open("familia", "rb")
lista_familia = pickle.load(fichero_binario)

for i in lista_familia:
    print(i)
