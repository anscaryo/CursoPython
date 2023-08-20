import tkinter as tk

root = tk.Tk()
varOption = tk.IntVar()


def imprimir():
  # Función para mostrar la opción seleccionada.
    if varOption.get() == 1:
        etiqueta.config(text="Masculino")

        # print("Masculino")

    elif varOption.get() == 2:
        etiqueta.config(text="Femenino")
        # print("Femenino")


frame = tk.Frame(root, width=60, height=50)
frame.pack()
tk.Label(frame, text="Genero: ").pack()
tk.Radiobutton(frame, text="Masculino", variable=varOption,
               value=1, command=lambda: imprimir()).pack()
tk.Radiobutton(frame, text="Femenino", variable=varOption,
               value=2, command=lambda: imprimir()).pack()
etiqueta = tk.Label(frame)
etiqueta.pack()

root.mainloop()
