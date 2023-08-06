for i in ["Pildoras","Informáticas", 3]:
    print("hola")

for i in ["Pildoras","Informáticas", 3]:
    print("hola", end="")

email = False
arroba = False
punto = False

correo = input("Dime un correo Electrónico: ")

for i in correo:
    if i=="@":
        arroba=True
    if i == ".":
        punto = True
    
if arroba and punto:
    email = True
    

if email:
    print("\nEl Email es correcto")
else:
    print("\nEl Email es incorrecto")