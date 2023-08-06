enunciado = '''
\tEjercicio 2:
Crea un programa que pida por teclado introducir una contraseña. La contraseña no
podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
errónea”
'''

print(enunciado)
espacio = False

contraseña = input("Introduce una contraseña, \n\tdebe tener almenos 8 caracteres \n\tno puede tener espacios en blanco: ")
longitud = len(contraseña)
for i in range(len(contraseña)):
    if contraseña[i] == " ":
        espacio = True

if longitud < 8 or espacio:
    print("\nContraseña errónea")
else:
    print("\nContraseña Ok")