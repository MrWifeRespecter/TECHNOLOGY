from turtle import *
from random import *
from math import *
side=float(input("Hur stor sida ska din kvadrat ha? "))

#Kolla... Om det ser dumt ut, fast det funkar. Då är det inte dumt. 
side2=side+(side/2) 
setworldcoordinates(0, 0, side2, side2)

speed(0)
ht()
def shape(side):
    pu()
    setpos(side/4, side*1.25) # Det funkar iallafall. Jag ville att kvadraten skulle bli centrerad och alltid få plats.
    pd()
    begin_fill()
    for i in range(4):
        forward(side)
        right(90)
    end_fill()

shape(side)
exitonclick()
input()