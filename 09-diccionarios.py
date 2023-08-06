midiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["España"])
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)

miTupla = ("España", "Francia", "Alemania", "Italia")
diccionarioPaises = {miTupla[0]:midiccionario[miTupla[0]],miTupla[1]:midiccionario[miTupla[1]],miTupla[2]:midiccionario[miTupla[2]],miTupla[3]:midiccionario[miTupla[3]],}
print(diccionarioPaises)

michale_jordan = {"Apellido":"Jordan", "Nombre":"Michael", "Número":23, "Equipo":"Chicago Bulls", "Anillos":[1991,1992,1993,1996,1997, 1998]}
print(michale_jordan)
print(michale_jordan["Anillos"])

print(midiccionario.keys())
print(midiccionario.values())