import tkinter as tk

root = tk.Tk()

miFrame = tk.Frame(root, width="600", height="300")
# para que fill, funcione en y, hay que añadir expand=True
miFrame.pack()
# miFrame.config(bg="blue", border=30, width="600", height="300", relief="sunken", cursor="pirate")

lblTitulo = tk.Label(miFrame, text="Formulario")
lblTitulo.grid(row=0, column=0, sticky="w", padx=4, pady=4)

lblNombre = tk.Label(miFrame, text="Nombre: ")
lblNombre.grid(
    row=2, column=2, sticky="w", padx=4, pady=4)

cuadroNombre = tk.Entry(miFrame)
cuadroNombre.grid(row=2, column=3, padx=4, pady=4)

lblApellido = tk.Label(miFrame, text="Apellidos: ")
lblApellido.grid(
    row=3, column=2, sticky="w", padx=4, pady=4)

cuadroApellido = tk.Entry(miFrame)
cuadroApellido.grid(row=3, column=3, padx=4, pady=4)

lblpassword = tk.Label(miFrame, text="Password: ")
lblpassword.grid(
    row=4, column=2, sticky="w", padx=4, pady=4)

cuadroPassword = tk.Entry(miFrame)
cuadroPassword.grid(row=4, column=3, padx=4, pady=4)
cuadroPassword.config(justify="center", show="·")

root.mainloop()
