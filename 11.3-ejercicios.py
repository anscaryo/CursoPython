enunciado='''
    Ejercicio 3:
Crea un programa que pida tres números por teclado. El programa imprime en consola
la media aritmética de los números introducidos.
'''

def media_aritmetica(num1, num2, num3):
    return (num1 + num2 +num3)/3

print(enunciado)

print("Calculo de la media aritmética de tres números.")
try:
    n1 = int(input("Dame el primer numero: "))
    n2 = int(input("Dame el segundo numero: "))
    n3 = int(input("Dame el tercer numero: "))
    print(f"{media_aritmetica(n1, n2, n3)}")
except:
    print("Los datos introducidos no son correctos.")