import tkinter as tk


def pasaTexto():
    mensaje = cajaTexto.get()
    print(mensaje)
    etiqueta["text"] = mensaje


ventana = tk.Tk()
ventana.geometry("300x250")
ventana.title("Tercera Ventana")
cajaTexto = tk.Entry(ventana, font="Helvetica 20")
cajaTexto.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

boton1 = tk.Button(ventana, text="Texto", command=pasaTexto)
boton1.pack()

ventana.mainloop()
