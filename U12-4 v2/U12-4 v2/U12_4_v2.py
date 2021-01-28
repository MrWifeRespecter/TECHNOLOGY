from turtle import *
from random import *
from math import *

def line(x1, y1, x2, y2): #ritar upp nätet med hjälp av sernare kod
    pu()
    goto(x1, y1)
    pd()
    goto(x2, y1)
    pu()
    goto(x1,y1)
    pd()
    goto(x1, y2)

def clickright(x, y): #läser av koordinaterna som du högerklickade på
    global xclick
    global yclick
    xclick = (x//1) #Tar bort resten ur divisionen
    yclick = (y//1)
    drawcircle()

def clickleft(x, y): #Läser av korrdinaterna som du vänsterklickade på
    global xclick
    global yclick
    xclick = (x//1) #tar bort restsumman ur divisionen. Denna är konsekvent eftersom att vi ibland har negativa x och y värden. Därför kan vi inte göra om x eller y till en int och nöja oss där
    yclick = (y//1)
    paint()

def paint(): #fyller i en ruta som du klickat i
    color("green")
    pu()
    goto(xclick, yclick)
    begin_fill()
    pd()
    goto(xclick+1, yclick)
    goto(xclick+1, yclick+1)
    goto(xclick, yclick+1)
    goto(xclick, yclick)
    end_fill()

def drawcircle(): #ritar en röd cirkel i mitten av rutan som du klickade i
    color("red")
    pu()
    width(5)
    goto(xclick, yclick)
    goto(xclick+0.5, yclick+0.5)
    right(90)
    forward(0.25)
    left(90)
    pd()
    circle(0.25)
    width(1)
speed(0)
x1=-10
x2=11
y1=-10
y2=11
setworldcoordinates(-10, -10, 11, 11)
ht()
speed(0)
for i in range(22):
   line(x1, y1, x2, y2)
   x1+=1
x1=-10
for j in range(22):
    line(x1, y1, x2, y2)
    y1+=1
listen() #under listen så kan man använda onscreenclick eftersom att skölpaddan lyssanr först då. Så man kan inte läsa av koordinaterna om man inte använder listen() innan
onscreenclick(clickleft, 1)
onscreenclick(clickright, 3)
mainloop() #Loopar denna delen mellan listen och mainloop tills användaren stänger programmet.
input() #vet inte om den här behövs längre. men om den gö det så behåller jag den utifall att