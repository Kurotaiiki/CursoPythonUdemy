import  sqlite3

conexion=sqlite3.connect("ejemplo.db")

cursor= conexion.cursor()

##region comentarios
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100),edad  INTEGER,email VARCHAR(100))")

# cursor.execute("INSERT INTO  usuarios VALUES ('Felipe',25,'pipe@ejemplo.com')")

# cursor.execute ("SELECT  *  FROM usuarios")
# usuario=cursor.fetchone()

# usuarios=[

#     ('Mario',54,'mario@ejemplo.com'),
#     ('Luis',30,'luis@ejemplo.com'),
#     ('Sergio',20,'sergio@ejemplo.com')
# ]

# cursor.executemany('INSERT INTO usuarios VALUES (?,?,?)',usuarios)

##endregion comentarios

cursor.execute('SELECT * FROM usuarios ')

usuarios=cursor.fetchall()

for usuario in usuarios:
	print('Nombre',usuario[0],'Email',usuario[1])

print(usuarios)

conexion.commit()
conexion.close()


