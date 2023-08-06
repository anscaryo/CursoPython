def evaluacion(nota):
    valoracion = "Sin Calificar"
    try:
        if nota < 5:
            valoracion = "No-Apto"
        else:
            valoracion = "Apto"
    except:
        print("valor introducido no es valido.")
    return valoracion

print(f"El alumno que ha optenido una nota de 4, es {evaluacion(4)}")
print(f"El alumno que ha optenido una nota de 5 o más, es {evaluacion(5)}")
calificacion = input("Que nota as optenido?: ")
try:
    calificacion = int(calificacion)
except:
    print(f"El valor introducido, no es valido.")

print(f"Has resultado \"{evaluacion(calificacion)}\"")