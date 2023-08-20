import tkinter as tk

root = tk.Tk()
root.title("44 - Practicando con Label")
root.config(bg="orange", border=1, relief="raised")
icono_chico = tk.PhotoImage(file="graficos/icon-16.png")
icono_grande = tk.PhotoImage(file="graficos/icon-32.png")
miFrame = tk.Frame(root, width="600", height="450", cursor="hand")
miFrame.pack()
lblImagen = tk.PhotoImage(file="graficos/giphy.gif")
lblLabel = tk.Label(miFrame, text="MI primer label.")
lblLabel.place(x=100, y=200)

tk.Label(miFrame,
         text="Label directo.", fg="red", font=("Comic Sans Ms", 18)).place(x=100, y=150)
tk.Label(miFrame, image=lblImagen).place(x=0, y=0)

root.mainloop()
