from tkinter import *

raiz = Tk()
raiz.title("Primera ventana")
raiz.resizable(1, 1)
icono_chico = Tkinter.PhotoImage(file="icon-16.png")
icono_grande = tk.PhotoImage(file="icon-32.png")
ventana.iconphoto(False, icono_grande, icono_chico)
raiz.iconbitmap(bitmap="pin_icon.ico")
raiz.mainloop()
