from cmath import rect
from msilib.schema import RadioButton
import turtle as t

t.setup(500,500)

t.shape("turtle")
t.color("green")

def rectangulo(px,py,ancho,alto):
    t.penup()
    t.goto(px+ancho/2,py+alto/2)
    t.left(180)
    t.pendown()
    for i in range(2):
        t.forward(ancho)
        t.left(90)
        t.forward(alto)
        t.left(90)


def poligono_regular(px,py,radio,lados):
    t.penup()
    t.goto(px,py-radio)
    t.pendown()
    t.circle(radio)
    angulo=360/lados
    vertices=[]

    for i in range(lados):
        t.penup()
        t.goto(0,0)
        t.seth(angulo*i+1)
        t.forward(radio)
        vertices.append(t.pos())

    t.penup()
    t.goto(vertices[-1])
    t.pendown()

    for i in range(lados):
        t.goto(vertices[i])
        t.pendown()

    

        





poligono_regular(0,0,100,4)



#rectangulo(0,0,400,300)





t.done()
t.bye