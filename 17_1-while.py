def pideEdad():
    n = int(input("Que edad tienes?:"))
    return n

# edad = int(input("\tQue edad tienes?:"))
intentos = 2
edad = pideEdad()
contador = 0
while edad > 100 or edad < 0:
    print("\tHas introducido una edad negativa. Vuelve a intentarlo.")
    # edad = int(input("\tQue edad tienes?:"))
    if contador > intentos:
        print("Has realizado demasiados intentos.")
        break
    edad = pideEdad()
    contador +=1

print("\tGracias por colaborar, puedes continuar.")
print(f"\tEdad del aspirante: {edad} años.")