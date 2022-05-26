from tkinter import *
from tkinter import filedialog as Filledialog
from io import open	
ruta="" #ruta de un fichero

def nuevo():
	global ruta
	mensaje.set("Nuevo Fichero creado")
	ruta=""
	texto.delete(1.0,"end")
	root.title("Mi editor")


def abrir():
	global ruta
	mensaje.set("Se abrio un fichero nuevo")
	ruta=Filledialog.askopenfilename(initialdir=".",filetypes=(("Ficheros de texto","*.txt"),),title=" Abrir un fichero de texto")

	if ruta!="":
		fichero=open(ruta,"r")
		contenido=fichero.read()
		texto.delete(1.0,"end")
		texto.insert("insert",contenido)
		fichero.close()
		root.title(ruta+" - Mi editor")

def guardar():
	global ruta
	if ruta != "":
		contenido=texto.get(1.0,"end-1c")
		fichero=open(ruta,"w+")
		fichero.write(contenido)
		fichero.close
		mensaje.set("Fichero guardado correctamente")
	else:
		guardar_como()


def guardar_como():
	global ruta
	mensaje.set("Se guardo un fichero  nuevo")
	fichero=Filledialog.asksaveasfile(title="Guardar  fichero",mode="w",defaultextension=".txt")
	if fichero is not  None:
		ruta=fichero.name
		contenido=texto.get(1.0,"end-1c")
		fichero=open(ruta,"w+")
		fichero.write(contenido)
		fichero.close
		mensaje.set("Fichero guardado correctamente")
	else:
		mensaje.set("Guardado Cancelado")
		ruta==0

#Configuracion de  la raiz
root=Tk()
root.title("Mi editor")

#menu superior
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_cascade(label="Nuevo",command=nuevo)
filemenu.add_cascade(label="Abrir",command=abrir)
filemenu.add_cascade(label="Guardar",command=guardar)
filemenu.add_cascade(label="Guardar como...",command=guardar_como)
filemenu.add_separator()
filemenu.add_cascade(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu,label=" Archivo")


#caja de  texto  central
texto=Text(root)
texto.pack(fill=BOTH,expand=1)
texto.config(bd=5,padx=6,pady=4,font=("consolas",12))


#Monitor inferior
mensaje=StringVar()
mensaje.set("re loco papi re loco!!!")
monitor=Label(root,textvariable=mensaje,justify="left").pack(side="left")
monitor2=Label(root,text="By Andres Vargas",justify="right").pack(side="right")





















root.config(menu=menubar)
#bucle app
root.mainloop()