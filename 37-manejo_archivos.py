from io import open
'''Crear y escribir en un archivo.'''
archivo_texto = open("prueba.txt", "w")

frase = "Estupendo día para aprender python\n\tse acaban las vacaciones."

archivo_texto.write(frase)
archivo_texto.close

'''Leer el contenido de un archivo'''
archivo_texto = open("prueba.txt", "r")
texto = archivo_texto.read()
archivo_texto.close()

print(texto)


archivo_texto = open("prueba.txt", "r")
lineas_texto = archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)
for i in lineas_texto:
    print(i)
archivo_texto.close

archivo_texto = open("prueba.txt", "a")

archivo_texto.write("\nSiempre es una buean ocasión para aprender.")
archivo_texto.close()
