from turtle import *
from random import *
from math import *
x=0
y=20
setworldcoordinates(0, 0, 20, 20)
speed(0)
def draw(x,y):
    pu()
    setpos(x,0)
    pd()
    goto(0,y)
for i in range(21):
    draw(x,y)
    x+=1
    y-=1
exitonclick()
input()