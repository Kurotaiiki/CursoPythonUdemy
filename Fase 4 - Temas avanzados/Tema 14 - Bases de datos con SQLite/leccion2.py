import sqlite3


conexion=sqlite3.connect('usuarios_autoincremental.db')
cursor=conexion.cursor()

#region comentario

# cursor.execute(''' 
# 	CREATE TABLE usuarios ( 
# 			dni VARCHAR(9) PRIMARY KEY,
# 			nombre VARCHAR(100),
# 			edad INTEGER,
# 			email VARCHAR(100)


# 	)
# 	''')

# usuarios=[		('11111111A','Mario',54,'mario@ejemplo.com'),
# 				('22222222B','Luis',30,'luis@ejemplo.com'),
# 				('3peoridus','Sergio',20,'sergio@ejemplo.com'),
# 				('4peoridus','Hector',25,'hector@ejemplo.com'),]


# cursor.executemany('INSERT INTO usuarios VALUES (?,?,?,?)', usuarios)

#endregion



# cursor.execute('''
# 	CREATE TABLE productos(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		nombre VARCHAR(100) NOT NULL,
# 		marca VARCHAR(100) NOT NULL,
# 		precio FLOAT NOT NULL
# 	)
# 	''')

# productos=[
# 	('Teclado','Logitech',19.95),
# 	('Pantalla 19"','LG',19.95),
# 	('Mouse','Logitech',19.95)

# ]

# cursor.executemany('INSERT INTO productos VALUES (null,?,?,?)',productos)


# cursor.execute('SELECT * FROM productos')

# productos=cursor.fetchall()
# for producto in productos:
# 	print(producto)


# cursor.execute('''
# 	CREATE TABLE usuarios(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		dn1 VARCHAR(9) UNIQUE,
# 		nombr VARCHAR(100),
# 		edad INTEGER,
# 		email VARCHAR(100)
# 	)
# 	''')


usuarios=[		('11111111A','Mario',54,'mario@ejemplo.com'),
				('22222222B','Luis',30,'luis@ejemplo.com'),
				('3peoridus','Sergio',20,'sergio@ejemplo.com'),
				('4peoridus','Hector',25,'hector@ejemplo.com'),]


cursor.executemany('INSERT INTO usuarios VALUES (null,?,?,?,?)',usuarios)


conexion.commit()
conexion.close()
