nombre = "oscar flores"

for i in range(len(nombre)):
    if nombre[i] == " ":
        print(f"Tiene un espacio {nombre[i]}.")
    else:
        print(f"{nombre[i]}")