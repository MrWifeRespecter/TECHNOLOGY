from turtle import *
from random import *
from math import *

speed(0)
ht()
hörn=randint(3,6) #bestämmer hur många hörn som ska finnas
sidlängd=randint(100,300) #bestämmer sidlängd

def färg(): #Här skapar jag en färg med en slumpad färgkod. Denna är jag stolt över eftersom att jag slumpar ut en helt och hållet ranfom färgkod. Simpel men rolig. :)
    r=random()
    b=random()
    g=random()
    färg=(r, g, b)
    return(färg)

def rita(hörn, sidlängd): #här ritas månghörningen upp beroende på hur många sidor den ska ha och hur långa sidorna ska vara.
    begin_fill() 
    for i in range(hörn): #loopar beroende på hur många sidor som ska skapas
        right(360/hörn) 
        fd(sidlängd)
    end_fill()

color(färg())
rita(hörn, sidlängd)
input()