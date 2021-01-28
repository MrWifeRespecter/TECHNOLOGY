from turtle import *
from math import *
from random import *
radie=float(input("Hur stor radie ska din cirkel ha? "))
setworldcoordinates(0,0,radie*4,radie*4)

speed(0)
ht()
def drawcircle(radie):
    pu()
    goto(radie*2,radie*2)
    forward(radie)
    right(270)
    pd()
    circle(radie)
    pu()
    left(90)
    forward(radie)
    pd()
    dot(radie/(radie/10))
drawcircle(radie)
exitonclick()
input()