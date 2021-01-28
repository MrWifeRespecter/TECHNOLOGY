from turtle import *
from random import *
from math import *
setworldcoordinates(-20, -20, 20, 20)
speed(0)
ht()

def draw(x,y):
    pu()
    setpos(x,0)
    pd()
    goto(0,y)

#Man gör bara förra uppgiften fast åt olika håll
#Första kvadrant
x=0
y=20
for i in range(21):
    draw(x,y)
    x+=1
    y-=1

#Andra kvadrant
x=0
y=20
for i in range(21):
    draw(x,y)
    x-=1
    y-=1

#Tredje kvadrant
x=0
y=-20
for i in range(21):
    draw(x,y)
    x-=1
    y+=1

#Fjärde kvadrant
x=0
y=-20
for i in range(21):
    draw(x,y)
    x+=1
    y+=1
exitonclick()
input()