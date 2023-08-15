'''
texto de prueba
'''
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x250")
ventana.title("Mi primera ventana")
etiqueta = tk.Label(ventana, text="Primera ventana", bg="green")
# etiqueta.pack(side=tk.BOTTOM)
etiqueta.pack(fill=tk.X, side="bottom")
# etiqueta.pack(fill=tk.Y, expand=True)

# etiqueta.pack(fill=tk.BOTH, expand=True)

ventana.mainloop()
