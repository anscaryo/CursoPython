'''
    programa que Evalua la beca a un estudiante.
'''

print("Programa de Becas 2023")
salario_tope = 20000
hermanos = 2
distancia = 40
alumno = {}

distancia_escuela = int(input("Distancia de la vivienda a la escuela en km? "))
alumno["distancia_escuela"] = distancia_escuela

n_hermanos = int(input("Números de hermanos en el centro? "))
alumno["n_hermanos"] = n_hermanos

salario_familiar = int(input("Salario anula bruto de la familia? "))
alumno["salario_familiar"] = salario_familiar

print("\nCaso con tres \"and\"")
if alumno["distancia_escuela"] > distancia and alumno["n_hermanos"] > hermanos and alumno["salario_familiar"]<= salario_tope:
    print("\tTienes derecho a Beca.")
else:
    print("\tNo tienes derecho a Beca.")
print("\nCaso con dos \"and\" y un \"or\"")

if alumno["distancia_escuela"] > distancia and alumno["n_hermanos"] > hermanos or alumno["salario_familiar"]<= salario_tope:
    print("\tTienes derecho a Beca.")
else:
    print("\tNo tienes derecho a Beca.")
