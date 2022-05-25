from tkinter import *

def seleccionar():
	cadena = ""
	if (leche.get()):
		cadena += "Con leche"
	else:
		cadena += "Sin leche"

	if (azucar.get()):
		cadena += " y con azúcar"
	else:
		cadena += " y sin azúcar"

	monitor.config(text=cadena)

# Configuración de la raíz
root = Tk()
root.title("Cafetería")
root.config(bd=15)


leche = BooleanVar() 	# 1 si, 0 no
azucar = BooleanVar()	# 1 si, 0 no

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=True, offvalue=False, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=True, offvalue=False, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()


# Finalmente bucle de la apliación
root.mainloop()