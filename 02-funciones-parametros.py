'''
    Programa con el que trabajamos con funciones
    pasandole parametros.
'''

def suma(a,b):
    return a + b

n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
print(f"El resultado de la suma del {n1} y el {n2} es: {suma(n1,n2)}")

print(suma(n1, suma(n1,n2)))

