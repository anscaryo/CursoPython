import tkinter as tk


def saludo(nombre):
    print("Hola {}".format(nombre))


ventana = tk.Tk()
ventana.geometry("300x250")
ventana.title("Segunda Ventana")
boton1 = tk.Button(ventana, text="OK", padx=8, pady=5,
                   command=lambda: saludo("Óscar"))
boton1.pack()
ventana.mainloop()
