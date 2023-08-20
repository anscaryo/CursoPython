
''' Ejercicio realizado en las clases 47, 48, 49
del curso de Python de pildoras informaticas '''

from tkinter import *
import modulos.operaciones as Op

root = Tk()
miFrame = Frame(root)
miFrame.pack()

''' Creando los botones y la pantalla.'''

# ------------------ pantalla --------------------#
numPantalla = StringVar()  # Creamos la variable y la asociamos a la pantalla.
operacion = ""  # Variable que almacenara la operación a ralizar.
pantalla = Entry(miFrame, textvariable=numPantalla)
pantalla.grid(row=1, column=1,
              padx=1, pady=10,
              columnspan=4)
pantalla.config(background="black", fg="#00FF27", justify="right")


# ---------------- Funciones ---------------------#

def numPulsado(num):
    global operacion
    if operacion != "":
        numPantalla.set(num)

    else:
        numPantalla.set(numPantalla.get() + num)


def botonOp(boton):
    global operacion
    if boton == "suma":
        operacion = "suma"
    elif boton == "resta":
        operacion = "resta"
    elif boton == "multip":
        operacion = "multip"
    elif boton == "divid":
        operacion = "divid"
    elif boton == "resultado":
        operacion = "resultado"


# -------- Linea de botones funciones ------------#


# --------- Primeria linea de botones ------------#

boton7 = Button(miFrame, text="7", width=3,
                command=lambda: numPulsado("7"))
boton7.grid(row=2, column=1,
            padx=1, pady=3)
boton8 = Button(miFrame, text="8", width=3,
                command=lambda: numPulsado("8"))
boton8.grid(row=2, column=2,
            padx=1, pady=3)
boton9 = Button(miFrame, text="9", width=3,
                command=lambda: numPulsado("9"))
boton9.grid(row=2, column=3,
            padx=1, pady=3)
botonDiv = Button(miFrame, text="/", width=3, command=lambda: botonOp("divid"))
botonDiv.grid(row=2, column=4,
              padx=1, pady=3)

# -------- Segunda linea de botones ------------#

boton4 = Button(miFrame, text="4", width=3,
                command=lambda: numPulsado("4"))
boton4.grid(row=3, column=1,
            padx=1, pady=3)
boton5 = Button(miFrame, text="5", width=3,
                command=lambda: numPulsado("5"))
boton5.grid(row=3, column=2,
            padx=1, pady=3)
boton6 = Button(miFrame, text="6", width=3,
                command=lambda: numPulsado("6"))
boton6.grid(row=3, column=3,
            padx=1, pady=3)
botonPor = Button(miFrame, text="X", width=3,
                  command=lambda: botonOp("multip"))
botonPor.grid(row=3, column=4,
              padx=1, pady=3)

# -------- Tercera linea de botones ------------#

boton1 = Button(miFrame, text="1", width=3,
                command=lambda: numPulsado("1"))
boton1.grid(row=4, column=1,
            padx=1, pady=3)
boton2 = Button(miFrame, text="2", width=3,
                command=lambda: numPulsado("2"))
boton2.grid(row=4, column=2,
            padx=1, pady=3)
boton3 = Button(miFrame, text="3", width=3,
                command=lambda: numPulsado("3"))
boton3.grid(row=4, column=3,
            padx=1, pady=3)
botonMenos = Button(miFrame, text="-", width=3,
                    command=lambda: botonOp("resta"))
botonMenos.grid(row=4, column=4,
                padx=1, pady=3)

# -------- Cuarta linea de botones ------------#

boton0 = Button(miFrame, text="0", width=3,
                command=lambda: numPulsado("0"))
boton0.grid(row=6, column=1,
            padx=1, pady=3)

botonComma = Button(miFrame, text=".", width=3,
                    command=lambda: numPulsado("."))
botonComma.grid(row=6, column=2,
                padx=1, pady=3)


botonMas = Button(miFrame, text="+", width=3, command=lambda: botonOp("suma"))
botonMas.grid(row=6, column=3,
              padx=1, pady=3)

botonIgual = Button(miFrame, text="=", width=3,
                    command=lambda: botonOp("resultado"))
botonIgual.grid(row=6, column=4,
                padx=1, pady=3)

root.mainloop()
