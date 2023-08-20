import tkinter as tk

root = tk.Tk()
root.title("Ejemplo CheckButton")
playa = tk.IntVar()
montagna = tk.IntVar()
rural = tk.IntVar()


def opcionesViajes():
    opcionesElegidas = ""
    if playa.get() == 1:
        opcionesElegidas += " playa"

    if montagna.get() == 1:
        opcionesElegidas += " montaña"

    if rural.get() == 1:
        opcionesElegidas += " Turismo Rural"

    mensajeFinal.config(text=opcionesElegidas)


frame1 = tk.Frame(root)
frame1.pack()
foto = tk.PhotoImage(file="graficos/x-wing2.png")
label1 = tk.Label(frame1, image=foto).pack()
# label1.grid(row=0, column=0)
label2 = tk.Label(frame1, text="Que prefieres?", width=50).pack()
# label2.grid(row=1, column=0)
check1 = tk.Checkbutton(frame1, text="Playa",
                        variable=playa, onvalue=1, offvalue=0, command=opcionesViajes).pack()
# check1.grid(row=2, column=0)
# check1.config(justify="right")
check2 = tk.Checkbutton(frame1, text="Montaña",
                        variable=montagna, onvalue=1, offvalue=0, command=opcionesViajes).pack()
# check2.grid(row=3, column=0)
# check2.config(justify="right")
check3 = tk.Checkbutton(frame1, text="Turismo Rural",
                        variable=rural, onvalue=1, offvalue=0, command=opcionesViajes).pack()
# check3.grid(row=4, column=0)
# check3.config(justify="right")


mensajeFinal = tk.Label(frame1)
mensajeFinal.pack()
root.mainloop()
