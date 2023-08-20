import tkinter as tk


root = tk.Tk()
miFrame = tk.Frame(root, width=600, height=400)
miFrame.pack()

'''
Utilizo el codigo del programa anterior para este.
'''

lblTitulo = tk.Label(miFrame, text="Formulario")
lblTitulo.grid(row=0, column=0,
               sticky="w",
               padx=4, pady=4)

lblNombre = tk.Label(miFrame, text="Nombre: ")
lblNombre.grid(row=2, column=2,
               sticky="w",
               padx=4, pady=4)

cuadroNombre = tk.Entry(miFrame)
cuadroNombre.grid(row=2, column=3,
                  padx=4, pady=4)

lblApellido = tk.Label(miFrame, text="Apellidos: ")
lblApellido.grid(
    row=3, column=2,
    sticky="w",
    padx=4, pady=4)

cuadroApellido = tk.Entry(miFrame)
cuadroApellido.grid(row=3, column=3,
                    padx=4, pady=4)

lblpassword = tk.Label(miFrame, text="Password: ")
lblpassword.grid(
    row=4, column=2,
    sticky="w",
    padx=4, pady=4)

cuadroPassword = tk.Entry(miFrame)
cuadroPassword.grid(row=4, column=3,
                    padx=4, pady=4)
cuadroPassword.config(justify="center", show="·")

lblComentarios = tk.Label(miFrame, text="Comentarios")
lblComentarios.grid(row=5, column=2,
                    padx=4, pady=4)

cuadroText = tk.Text(miFrame, width=26, height=5)
cuadroText.grid(row=5, column=3,
                padx=4, pady=4)

scrollVert = tk.Scrollbar(miFrame, command=cuadroText.yview)
scrollVert.grid(row=5, column=4,
                sticky="nsew")

cuadroText.config(yscrollcommand=scrollVert.set)

botonEnvio = tk.Button(root, text="Enviar")
botonEnvio.pack()
botonCerrar = tk.Button(root, text="Cancelar", command=quit)
botonCerrar.pack()

root.mainloop()
