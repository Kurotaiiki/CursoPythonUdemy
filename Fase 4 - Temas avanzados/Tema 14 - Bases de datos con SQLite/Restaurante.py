import sqlite3

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

	categoria=input("Ingrese el nombre de la cagoria nueva")
	cursor.execute('INSERT INTO categoria VALUES (Null,{}'))



crear_bd()