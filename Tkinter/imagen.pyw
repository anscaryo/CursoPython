import tkinter as tk

root = tk.Tk()
root.title("imagen avión")
foto = tk.PhotoImage(file="Tkinter/x-wing.png")
tk.Label(root, image=foto).pack()

root.mainloop()
