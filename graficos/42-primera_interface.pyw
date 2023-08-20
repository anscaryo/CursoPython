'''

'''

import tkinter as tk

raiz = tk.Tk()
raiz.title("42-Primera ventana")
raiz.geometry("600x300")
raiz.resizable(True, True)
raiz.config(bg="orange")
icono_chico = tk.PhotoImage(file="graficos/icon-16.png")
icono_grande = tk.PhotoImage(file="graficos/icon-32.png")
raiz.iconphoto(False, icono_grande, icono_chico)
# raiz.iconbitmap(bitmap="icon-16.ico")
raiz.mainloop()
