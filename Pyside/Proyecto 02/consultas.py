import email
import sys
from helpers import absPath
from PySide6.QtSql import QSqlDatabase,QSqlQuery

conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))

if not conexion.open():
    print("no se puede conectar a la base de datos")
    sys.exit(True)


consulta=QSqlQuery()
consulta.exec("DROP TABLE IF EXISTS contactos")
consulta.exec("""
                CREATE TABLE IF NOT EXISTS contactos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    nombre VARVCHAR(40) NOT NULL,
                    empleo VARCHAR(50),
                    telefono INTEGER(10) NOT NULL,
                    email VACHAR(40) NOT NULL
)""")

n,e,t,m="Andres","Jefe de desarrollo",3223052883,"andres@ejemplo.com"

consulta.exec(f"INSERT INTO contactos (nombre,empleo,telefono,email) VALUES ('{n}','{e}','{t}','{m}')") 

claves=["nombre","empleo","telefono",'email']

contactos = [
            ("Juan","Diseniador",3223052765,"juan@ejemplo.com"),
            ("Laura","Asesor",3223053412,"Laura@ejemplo.com"),
            ("Carlos","Sistemas",3102345283,"Carlos@ejemplo.com"),
            ("Luis","Programador",3223028543,"Luis@ejemplo.com")
]


consulta = QSqlQuery()
consulta.prepare("""
    INSERT INTO contactos (nombre, empleo,telefono, email) VALUES (?, ?, ?,?)
    """)

# usamos .addBindValue () para insertar datos
for nombre, empleo,telefono, email in contactos:
    consulta.addBindValue(nombre)
    consulta.addBindValue(empleo)
    consulta.addBindValue(telefono)
    consulta.addBindValue(email)
    consulta.exec()

consulta.exec("SELECT nombre,empleo,telefono,email FROM contactos")




# if consulta.first():
#     for clave in claves:
#         print(consulta.value(clave),end=" ")
    

while consulta.next():
    for clave in claves:
        print(consulta.value(clave),end=" ")
    print("")


conexion.close()
print("Conexion cerrada", not conexion.isOpen())