import math

# def evaluaEdad(edad):

#     if edad < 0:
#         raise TypeError("La edad no puede ser menor de 0.") #El programa se para.
    
#     if edad < 20:
#         return "Eres muy joven"
#     elif edad < 40:
#         return "Eres joven"
#     elif edad < 65:
#         return "Eres maduro"
#     elif edad < 100:
#         return "Cuidate ..."
#     else:
#         return "Matusalen ... :-)"
    


# print(evaluaEdad(18))
# print(evaluaEdad(38))
# print(evaluaEdad(58))
# print(evaluaEdad(68))
# print(evaluaEdad(108))
# print(evaluaEdad(-5))

def raizNumero(num1):
    
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo.")
    else:
        return math.sqrt(num1)
    

num = int(input("Dame un número y te doy su raiz cuadrada: "))
try:
    print(f"La raiz es: {raizNumero(num)}")
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado.")