from turtle import *
from random import *
def line(x1, y1, x2, y2):
    pu()
    goto(x1, y1)
    pd()
    goto(x2, y1)
    pu()
    goto(x1,y1)
    pd()
    goto(x1, y2)
x1=-10
x2=10
y1=-10
y2=10
setworldcoordinates(-10, -10, 10, 10)
ht()
speed(0)
for i in range(21):
   line(x1, y1, x2, y2)
   x1+=1
x1=-10
for j in range(21):
    line(x1, y1, x2, y2)
    y1+=1
exitonclick()
input()