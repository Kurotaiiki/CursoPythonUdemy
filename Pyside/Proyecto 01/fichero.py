import json


from helpers import absPath


datos=[]

contactos= [
    ("Luis", 3125562425, "Estudiante", "Luis@ejemplo.com"),
    ("Camilo", 3134592432, "Profesor", "Camilo@ejemplo.com"),
    ("Laura", 3124575757, "Asesora", "Laura@ejemplo.com"),
    ("Andres", 3102992854, "Gerente", "Andres@ejemplo.com")    
]


for nombre,telefono,empleo,email in contactos:
    datos.append({

        "Nombre":nombre,
        "Telefono":telefono,
        "Empleo": empleo,
        "Correo":email
    })


with open(absPath("contactos.json"),"w") as fichero:
    json.dump(datos,fichero)

datos=None

with open(absPath("contactos.json")) as fichero:
    datos=json.load(fichero)
    for contacto in datos:
        print(contacto["Nombre"],contacto["Telefono"],contacto["Empleo"],contacto["Correo"])




