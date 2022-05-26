import sqlite3

conexion=sqlite3.connect('usuarios_autoincremental.db')
cursor=conexion.cursor()

cursor.execute("DELETE FROM usuarios")

usuarios = cursor.fetchall()
print(usuarios)


conexion.commit()
conexion.close()