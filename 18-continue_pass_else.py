'''
Bucles con las instrucciones continue, pass y else.
'''
def funcion():
    pass#   se crea una función pero no se implementa en ese momento.


for letra in "Python": print(f"\tViendo la letra \"{letra}\"")

print(f"Eliminar la letra \"h\"")
for letra in "Python":
    if letra == "h":
        continue
    print(f"\tViendo la letra \"{letra}\"")

longitud = 0
nombre = "Pildoras informaticas"

for letra in nombre:

    if letra == " ":
        continue
    
    longitud += 1

print(f"El numero total de letras es: {longitud} pero su longitud real es {len(nombre)}.")

email = input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break

else:
    arroba = False

print(arroba)