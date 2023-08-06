'''
    calculo de raiz cuadrada de un numero.
'''
import math
print(f"Programa de cálculo de la raiz cuadrada.")
def pideNumero():
    return int(input("Introduce un número positivo, por favor: \n\t"))
intentos = 0

numero = pideNumero()

while numero < 0:
    print("No se puede hallar la raíz cuadrada de un número negativo.")

    if intentos == 2:
        print("Has consumado demasiados intentos, \nEl programa ha finalizado.")
        break
    
    intentos +=1
    numero = pideNumero()

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es: {math.sqrt(numero)}")
