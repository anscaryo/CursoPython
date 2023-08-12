'''

'''

import tkinter as tk

raiz = tk.Tk()
raiz.title("Primera ventana")
raiz.resizable(1, 1)
icono_chico = tk.PhotoImage(file="icon-16.png")
# icono_grande = tk.PhotoImage(file="icon-32.png")
# raiz.iconphoto(False, icono_grande, icono_chico)
#raiz.iconbitmap(bitmap="icon-16.ico")
raiz.mainloop()
