from random import *
from turtle import *
from math import *

recurse=1
längd=300
bredd=210

def tavlan(längd,bredd):
    global recurse
    begin_fill()
    fd(längd)
    right(90)
    fd(bredd)
    right(90)
    fd(längd)
    right(90)
    fd(bredd)
    right(90)
    end_fill()
    if recurse>0:
        recurse-=1
        pu()
        fd(20)
        right(90)
        fd(20)
        left(90)
        pd()
        color("white")
        tavlan(längd-40,bredd-40)

def hus():

    #huset:
    pu()
    color("red")
    goto(-50,-85)
    pd()
    begin_fill()
    for i in range(4):
        fd(100)
        left(90)
    end_fill()
    fd(40)
    color("brown")

    #dörr:
    begin_fill()
    for i in range(2):
        fd(25)
        left(90)
        fd(40)
        left(90)
    end_fill()

    #dörrhandtag:
    fd(25)
    left(90)
    fd(20)
    left(90)
    fd(5)
    color("yellow")
    dot(5)

    #taket:
    color("black")
    pu()
    goto(-50,15)
    begin_fill()
    seth(0)
    left(21.8) #arctan ville inte funka
    pd()
    fd((sqrt(100*100+40*40))/2)
    right(43.6) #arctan ville inte funka 
    fd((sqrt(100*100+40*40))/2)
    end_fill()

def sol(): #ritar en röd cirkel i mitten av rutan som du klickade i
    color("yellow")
    pu()
    seth(90)
    goto(xclick+25, yclick)
    begin_fill()
    pd()
    circle(25)
    end_fill()
    pu()

def träd():

    #Själva stammen:
    global storlek
    color("brown")
    pu()
    goto(xclick, yclick)
    seth(90)
    pd()
    begin_fill()
    for i in range(2):
        fd(20)
        right(90)
        fd(10)
        right(90)
    end_fill()
    triangel()

def triangel():

    #Det gröna och sköna:
    seth(90)
    color("green")
    pu()
    goto(xclick+5,yclick+50)
    pd()
    begin_fill()
    right(150)
    for i in range(3):
        fd(34.64)
        right(120)
    end_fill()

def clickright(x, y): #läser av koordinaterna som du högerklickade på
    global xclick
    global yclick
    xclick = (x//1) 
    yclick = (y//1)
    sol()

def clickleft(x, y): #läser av koordinaterna som du högerklickade på
    global xclick
    global yclick
    xclick = (x//1) #Tar bort resten ur divisionen
    yclick = (y//1)
    träd()

setworldcoordinates(-200, -200, 200, 200)
pu() 
ht()
speed(0)
setpos(-150,105)
pd()
color("brown")
tavlan(längd,bredd)
hus()


listen() #under listen så kan man använda onscreenclick eftersom att skölpaddan lyssanr först då. Så man kan inte läsa av koordinaterna om man inte använder listen() innan
onscreenclick(clickleft, 1) #kollar om man vänsterklickar 
onscreenclick(clickright, 3) #kollar om du klickar högerklick

mainloop() #Loopar denna delen mellan listen och mainloop tills användaren stänger programmet.
input() #vet inte om den här behövs längre, men jag behåller den utifall att

#jag skulle kunna göra denna uppgiften mycket bättre om jag hade mer tid på mig. Men som det är nu så hann jag bara göra detta
