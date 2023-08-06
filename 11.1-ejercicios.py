enunciado = """
    Ejercicio 1:
Crea un programa que pida dos números por teclado. El programa tendrá una función
llamada “DevuelveMax” encargada de devolver el número más alto de los dos
introducidos.
"""

def DevuelveMax(num1, num2):
    if num1 > num2:
        print(f"\n\tEl número \"{num1}\" es el mayor.")
    elif num2 > num1:
        print(f"\n\tEl número \"{num2}\" es el mayor.")
    else:
        print("Son iguales.")


print(enunciado)
try:
    n1 = input("Dame el primer número: ")
    n2 = input("Dame el segundo número: ")
    n1 = int(n1)
    n2 = int(n2)
    DevuelveMax(n1,n2)
except:
    print("Valores no validos.")