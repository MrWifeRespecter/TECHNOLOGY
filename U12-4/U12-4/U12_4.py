from turtle import *
from random import *
xclick = 0
yclick = 0
def getcoordinates():
    onscreenclick(modifyglobalvariables())
def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print(xclick)
    print(yclick)
getcoordinates()
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
def koordinater(x, y): 
    color("green")
    int(x)
    int(y)
    pu()
    setpos(x, y)
    pd()
    begin_fill()
    goto(x+1,y)
    goto(x, y)
    goto(x, y+1)
    goto(x+1, y+1)
    goto(x+1,y)
    end_fill()
for i in range(20):
    onscreenclick(koordinater(x, y), btn=1, add=None)
    print(x)
    print(y)
exitonclick()
input()