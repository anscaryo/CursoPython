from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=250)
archivoMenu = Menu(barraMenu)
salirSub_menu = Menu(archivoMenu)
editarMenu = Menu(barraMenu)
toolsMenu = Menu(barraMenu)
ayudaMenu = Menu(barraMenu)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir...")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator(background="Green")
archivoMenu.add_command(label="Salir", command=quit)

barraMenu.add_cascade(label="Editar", menu=editarMenu)
editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Pegar")
editarMenu.add_command(label="Deshacer")
barraMenu.add_cascade(label="Herramientas", menu=toolsMenu)
toolsMenu.add_command(label="Exportar")
toolsMenu.add_command(label="Importar")
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label="ayuda       F1")
ayudaMenu.add_separator()
ayudaMenu.add_command(label="Acerca de...")


frame = Frame(root)
frame.config(width=300, height=150)
frame.pack()


root.mainloop()
