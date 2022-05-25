import enum
import math
import random


def leer_numero(ini,fin,mensaje):

    while True:

        try:
            num=float(input (mensaje))

            if num<=fin  and num >= ini:
                return num
            else:
                print("El numero se encuentra fuera del rango")
        except ValueError:
            print("Debe ingresar un numero")

            
        
def generador():
    numeros=int(leer_numero(1,20,"Cuantos numeros quiere generar? [1-20]:"))
    modo=leer_numero(1,3,"Como quieres redondear los numeros? [1]Al azar [2]A la baja [3]Normal:")
    l=[]

    
    for i in range(numeros):
            l.insert(i,random.uniform(0,100))



    if modo==1:
        for i in  range(numeros):
            print("[{}]. {}".format(i+1,l[i]))

    elif modo==2:
        for i in  range(numeros):
            print("[{}]. {} --- {} ".format(i+1,math.floor(l[i]),l[i]))
            l.insert(i,math.floor(l[i]))


    elif modo==3:
        for i in  range(numeros):
           
            print("[{}]. {} --- {} ".format(i+1,math.ceil(l[i]),l[i]))
            l.insert(i,math.ceil(l[i]))





generador()