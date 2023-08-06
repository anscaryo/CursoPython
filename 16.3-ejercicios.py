enunciado = '''
\tEjercicio 3:

Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
correcta si solo tiene una “@” y si tiene uno o más “.”
'''

print(f"{enunciado}")

email = False
arroba = 0
punto = 0

correo = input("Dime un correo Electrónico: ")

for i in correo:
    if i == "@":
        arroba += 1
    if i == ".":
        punto += 1

if arroba != 1 or punto < 1:
    print(f"El Email: {correo} es incorrecto.")
else:
    print(f"El Email: {correo} es correcto.")
