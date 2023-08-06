'''
trabajando con tuplas, son como las listas
pero no se pueden modificar ni indexar.
'''
import math


def busca_lista(nomb, lista):
    if nomb in lista:
        return True


familia = ("Oscar", "Mamen", "Pablo", "Jaime", "Jäguer")
armas_oscar = ("SPS", "Glock 17", "Walther GSP-Expert", "Norinco 45 ACP", "Walter PDP")
numeros = (math.pi, math.e)

print(numeros[0])
print(numeros[1])

lista_familia = list(familia)
print(lista_familia)

lista_familia.insert(4,"Clarita")
print(lista_familia)
lista_familia.insert(5,"Mafalda")
print(lista_familia)
familia = tuple(lista_familia)
print(familia)

nombre = input("Que nombre quieres buscar en \"familia\"?")
if busca_lista(nombre, familia):
    print(f"El nombre buscado esta en la tupla familia")
else:
    print("El nombre buscado no esta en la tupla familia")

print(f"hay {len(familia)}, miembros en la familia")

armas = "SPS", "Glock 17", "Walther GSP-Expert", "Norinco 45 ACP", "Walter PDP"

print(armas)

miTupla = ("Óscar", 6, 10,  1972)
nombre, dia, mes, agno = miTupla
print(f"Mi nombre es {nombre}, naci en el año {agno}, el {dia} del {mes} mes.")

print(familia[2])