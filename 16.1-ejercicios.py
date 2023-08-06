enunciado = '''\tEjercicio 1:
Crea un programa que muestre los números impares del 1 al 100. Los números deberán
aparecer una al lado del otro sin salto de línea.
'''

print(enunciado)

for i in range(0,100):
    if (i%2!=0):
        print(i,end=" ")#   añado un espacio para que sea legible.
print("\nOtra forma.")
for i in range(1,100,2):
    print(i,end=" ")#   añado un espacio para que sea legible.