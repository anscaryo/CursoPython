from io import open

archivo = open("prueba.txt", "r+")

print(archivo.read())
archivo.seek(10)  # mueve el cursor en un punto en concreto.
print(archivo.read())
archivo.seek(0)
print(archivo.read(10))
print(archivo.read())
archivo.seek(0)
archivo.seek(len(archivo.read())/2)
print(archivo.read())
archivo.seek(0)
archivo.seek(len(archivo.readline()))
archivo.write("\nOtro texto más.")

print(archivo.readline())
archivo.close()

archivo = open("prueba.txt", "r+")

lista_textos = archivo.readlines()
lista_textos[1] = "\nEsta linea a sido añadida como elemento de una lista."
archivo.seek(0)
archivo.writelines(lista_textos)
archivo.close()
