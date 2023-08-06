'''
Instrucción yield from, simplificamos el codigo del generador
al usar bucles anidados dentro de un generador.'''


def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento
        # yield elemento

    
andalucia = devuelve_ciudades("Cadiz", "Huelva", "Cordoba", "Jaen", "Malaga", "Almeria", "Granada", "Sevilla")
# prov_Andalucia = ["Cadiz", "Huelva", "Cordoba", "Jaen", "Malaga", "Almeria", "Granada", "Sevilla"]

print(next(andalucia))
print(next(andalucia))
print(next(andalucia))