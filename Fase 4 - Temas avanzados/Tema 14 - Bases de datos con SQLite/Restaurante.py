from platform import platform
import sqlite3

from colorama import Cursor

def crear_bd():
	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE categoria(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nombre VARCHAR(100) UNIQUE NOT NULL)''')
	except sqlite3.OperationalError:
		print("La tabla de cagoria ya existe")	
	else:
		print('La tabla se ah creado correctamente')


	try:
		cursor.execute('''CREATE TABLE plato(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					nombre VARCHAR(100) UNIQUE NOT NULL, 
					categoria_id INTEGER NOT NULL,
					FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print("La tabla de Platos ya existe")	
	else:
		print('La tabla se ah creado correctamente')

	conexion.close()



def agregar_categoria():

	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()
	
	categoria=input("Ingrese el nombre de la cagoria nueva:.")
	try	:
		cursor.execute("INSERT INTO categoria VALUES (Null,'{}')".format(categoria))
	except sqlite3.IntegrityError:
		print("\nLa categoria {} ya existe".format(categoria))
	else:
		print("\nLa categoria {} fue creada ".format(categoria))


	conexion.commit()
	conexion.close()




def agregar_plato():

	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()


	categorias = cursor.execute("SELECT * FROM categoria").fetchall()


	print("\nEn que categoria desea agregar el plato?\n")
	for i,categoria in enumerate(categorias):
		print("[{}] {}".format(i+1,categoria[1]))
	categoria=int(input(".:"))


	plato=input('Cual es el nombre del plato?\n.:')


	try:
		cursor.execute("INSERT INTO plato VALUES (Null,'{}',{})".format(plato,categoria))
	except sqlite3.IntegrityError:
		print("El plato '{}' ya existe.".format(plato))
	else:
		print("Plato '{}' creado correctamente.".format(plato))


	conexion.commit()
	conexion.close()


def Mostrar_menu():

	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()


	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	
	for categoria in categorias:
		print(categoria[1])
		platos=cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0]))
		for plato in platos:
			print(plato)







crear_bd()


while True:
	print("\nBienvenido al gestor de restaurante!")
	opcion=input("\nIntroduce una opcion\n[1] Agregar una categoria\n[2] Agregar plato\n[3] Mostrar menu\n[4] Salir del programa\n.:")

	if opcion=='1':
		agregar_categoria()
	elif opcion=='2':
		agregar_plato()
	elif opcion=='3':
		Mostrar_menu()
	elif opcion=='4':
		break
	else: 
		print('Opcion incorrecta')