'''
Equivalente a arrays y vectores en otros lenguajes.
'''
def busca_lista(nomb, lista):
    if nomb in lista:
        return True
    

familia = ["Oscar", "Manen", "Pablo", "Jaime"]
armas_oscar = ["SPS", "Glock 17", "Walther GSP-Expert", "Norinco 45 ACP", "Walter PDP"]
print(armas_oscar)
armas_mamen = ["Walther Q5", "Walter GSP500"]
print(armas_mamen)
armas_oscar.extend(["Escopeta Reminton", "Carabina AR15"])
print(armas_oscar)
armas_oscar.pop()   #   Elimina el ultimo elemento de una lista.
armas = armas_oscar + armas_mamen

print(armas)
print(familia[0:2])
print(familia[:2])
print(familia)

familia.append("Jäguer")

print(familia)


familia.insert(4,"Clarita")
print(familia)
familia.insert(5,"Mafalda")
print(familia)

if busca_lista("Jäguer", familia):
    print(f"Jäguer se encuentra en la lista familia.")
else:
    print(f"El mienbro buscado aun no pertenece a la familia.")
