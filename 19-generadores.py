'''
    Estruturas que extraen valores de una función y 
se almacenan en objetos iteranbles(que se pueden recorrer)
'''

def funcionPares(limite):#función.
    num = 1
    pares = []
    while num < limite:
        pares.append(num*2)
        num += 1
    
    return pares


print(funcionPares(10))


def generaPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1

print("\n")
devuelvePares = generaPares(10)

print(next(devuelvePares))

print("Lineas de codigo...")

print(next(devuelvePares))

print("Lineas de codigo...")

print(next(devuelvePares))

print("Lineas de codigo...")

# for i in devuelvePares:
#     print(i)