import tkinter as tk


# def pasaTexto():
#     mensaje = cajaTexto.get()
#     print(mensaje)
#     etiqueta["text"] = mensaje


ventana = tk.Tk()
ventana.geometry("300x250")
ventana.title("Cuarta Ventana")

boton1 = tk.Button(ventana, text="Boton1", width=5, height=5)

boton2 = tk.Button(ventana, text="Boton2", width=5, height=5)

boton3 = tk.Button(ventana, text="Boton3", width=5, height=5)

boton1.grid(row=0, column=0)
boton2.grid(row=1, column=1)
boton3.grid(row=2, column=2)

# boton1.pack()
# boton2.pack()
# boton3.pack()
ventana.mainloop()
