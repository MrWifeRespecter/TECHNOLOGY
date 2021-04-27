from random import *
from turtle import *
from math import *


#jag vet inte hur jag skulle göra med den hör uppgiften.
#den sa att man skulle ha slumpade längd och vinkel mellan grenarna, 
#så jag gjorde det. trädet ser fult ut, men orkar inte fixa. 
#jag gjorde så som jag tolkade att uppgiften bad mig att göra.
speed(0)
ht()
seth(90)
pensize(1)
lista_of_awesomeness=[] #för att spara korrdinaterna där grenarna delades på ett bättre sätt.
grenar_i_längd=5
grenar_i_bredd=5
pd()
fd(50)

def hAHAHAHAH(): #main. den här står för allt ritande
    global lista_of_awesomeness
    global höjd_av_träd
    global grenar_i_längd
    global grenar_i_bredd
    pd()
    if grenar_i_bredd==0:
        det_som_blev_kvar()
        return
    for i in range(grenar_i_längd):
        z=randint(20,70) 
        å=randint(20,70)
        y=randint(20,40)
        left(z)
        fd(y)
        lista_of_awesomeness.append(pos()) 
        bk(y)
        seth(90)
        right(å)
        fd(y)
        seth(90)
    grenar()



def grenar(): #kontrollerar main så att den gör rätt sak vid rätt tillfälle
    global lista_of_awesomeness
    global höjd_av_träd
    global grenar_i_längd
    global grenar_i_bredd
    pu()
    setpos(lista_of_awesomeness[0])
    lista_of_awesomeness.pop(0)
    grenar_i_längd-=1
    if grenar_i_längd==0:
        grenar_i_bredd-=1
        grenar_i_längd=4
        hAHAHAHAH()
    pd()
    hAHAHAHAH()



def det_som_blev_kvar(): #lättare att ha den här än att skriva om all kod eftersom att mängden grenar ökar exponentiellt
    if len(lista_of_awesomeness)==0:
        return
    else:
        pu()
        setpos(lista_of_awesomeness[0])
        lista_of_awesomeness.pop(0)
        pd()
        z=randint(20,70) 
        å=randint(20,70)
        y=randint(20,40)
        right(z)
        fd(y)
        bk(y)
        seth(90)
        left(å)
        fd(y)
        seth(90)
        det_som_blev_kvar()

hAHAHAHAH()
input()