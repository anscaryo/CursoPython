'''

'''

import tkinter as tk

raiz = tk.Tk()
raiz.title("43-Frames")
# raiz.geometry("600x300")
raiz.resizable(True, True)
raiz.config(bg="orange", border=30, relief="raised", cursor="hand")
icono_chico = tk.PhotoImage(file="graficos/icon-16.png")
icono_grande = tk.PhotoImage(file="graficos/icon-32.png")
raiz.iconphoto(False, icono_grande, icono_chico)

miFrame = tk.Frame()
# para que fill, funcione en y, hay que añadir expand=True
miFrame.pack()
# miFrame.pack(fill="both", expand=True)
miFrame.config(bg="blue", border=30, width="600", height="300",
               relief="sunken", cursor="pirate")

# raiz.iconbitmap(bitmap="icon-16.ico")
raiz.mainloop()
