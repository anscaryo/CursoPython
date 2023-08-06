'''
    Uso de Operadores logicos en condicionales if.
'''

def pideSueldo(n):  #   Defino una función para asignar el sueldo de los empleados.
    sueldos[lista_cargos[n]] = int(input("-->? "))


lista_cargos = ["Director General","Gerente","Responsable de Sección", "Administrativo"]
sueldos = {}
print("Asignamos el sueldo a los empleados de una empresa.")

for n in range(len(lista_cargos)):# por medio de un bucle for, asigno los sueldos a los emplados.
    print("Sueldo del " + lista_cargos[n] + "?")
    pideSueldo(n)

if sueldos[lista_cargos[0]] > sueldos[lista_cargos[1]] > sueldos[lista_cargos[2]] > sueldos[lista_cargos[3]]:
    print("\nLos sueldos se han asignado correctamente.")
    for n in range (len(sueldos)):# por medio de un bloque for, imprimo los sueldos de los empleados.
        print("\tEl suledo de " + lista_cargos[n] + " es: " + str(sueldos[lista_cargos[n]]) + "€")
else:
    print("\n\tAlgo no funciona bien en esta empresa.")

