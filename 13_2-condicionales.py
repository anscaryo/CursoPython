print("Asinaturas Optativas Año 2023")
asignaturas = ["informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"]
print("Asignaturas Optativas: Informatica gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in asignaturas:
    print("Asignatura elegida: "+ asignatura)

else:
    print("La asignatura escogida no esta contemplada.")

if asignatura in ("informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: "+ asignatura)

else:
    print("La asignatura escogida no esta contemplada.")