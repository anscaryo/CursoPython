enunciado = '''
    Ejercicio 2:
Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
teclado).
'''

print(enunciado)
print(f"Bienvenido alumno. Para abrir su ficha \nnecesito los siguentes datos personales:")
nombre = input("Nombre: ")
direccion = input("Dirección actual: ")
tlfno = input("Telefono de contacto: ")
alumno1 = [nombre, direccion, tlfno]

print("Los datos personales son: \nNombre:" + alumno1[0] + "\nDirección actual: " + alumno1[1] + "\nTelefono: " + alumno1[2])
