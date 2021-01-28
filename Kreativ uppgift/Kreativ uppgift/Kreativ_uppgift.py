from turtle import * #turtle racing i real-time 
from math import *
from random import *
pos1=0
pos2=0
pos3=0
pos4=0
ht()
speed(0)
pu()
goto(-140, 140)
for i in range(20): #ritar upp banan
    write(i, align="center")
    right(90)
    forward(10)
    pd()
    forward(150)
    pu()
    backward(160)
    left(90)
    forward(20)

padda1=Turtle() #här fixar jag alla paddor
padda1.color("blue")
padda1.shape("turtle")
padda1.speed(0)
for j in range(72):
    padda1.right(5)
padda1.pu()
padda1.goto(-160, 100)
padda1.pd()
padda2=Turtle()
padda2.color("red")
padda2.shape("turtle")
padda2.speed(0)
for k in range(72):
    padda2.right(5)
padda2.pu()
padda2.goto(-160, 70)
padda2.pd()
padda3=Turtle()
padda3.color("green")
padda3.shape("turtle")
padda3.speed(0)
for l in range(72):
    padda3.right(5)
padda3.pu()
padda3.goto(-160, 40)
padda3.pd()
padda4=Turtle()
padda4.color("black")
padda4.shape("turtle")
padda4.speed(0)
for m in range(72):
    padda4.right(5)
padda4.pu()
padda4.goto(-160, 10)
padda4.pd()

def clickleft(x, y): #läser av koordinaterna som du högerklickade på
    global xclick
    global yclick
    xclick = (x//1) #Tar bort resten ur divisionen
    yclick = (y//1)
    whichturtle()

def whichturtle(): #vilken padda som man klickade på
    global chosen
    all_y=[100, 70, 40, 10]
    chosen=min(all_y, key=lambda x:abs(x-yclick))
    if chosen==100:
        chosen="blå"
    if chosen==70:
        chosen="röd"
    if chosen==40:
        chosen="grön"
    if chosen==10:
        chosen="svart"
    print("du valde", chosen)
    start_race()

def start_race(): #startar race
     for m in range(500):
        global pos1
        global pos2
        global pos3
        global pos4
        x1=random()
        x2=random()
        x3=random()
        x4=random()
        pos1+=x1
        pos2+=x2
        pos3+=x3
        pos4+=x4
        padda1.forward(x1)
        padda2.forward(x2)
        padda3.forward(x3)
        padda4.forward(x4)
     winner_winner_chicken_dinner_maybe()
def type(): #vet inte varför jag har den
    pu()
    goto(-250, -150)
    write("Klicka på den sköldpaddan som du vill satsa 100000000000000000000000000000000000000000000000000000000000000000000000kr på")

def winner_winner_chicken_dinner_maybe(): #kollar om du vann eller förlorade baserat på vilken av paddorna som du valde och hur de placerade i loppet
    lista=[pos1, pos2, pos3, pos4]
    lista.sort()
    if lista[3] == pos1:
        if chosen=="blå":
            winner_winner_chicken_dinner()
        else:
            loser_loser_alarmclock_snoozer()
    if lista[3] == pos2:
                if chosen=="röd":
                    winner_winner_chicken_dinner()
                else:
                    loser_loser_alarmclock_snoozer()
    if lista[3] == pos3:
        if chosen=="grön":
            winner_winner_chicken_dinner()
        else:
            loser_loser_alarmclock_snoozer()
        if lista[3] == pos4:
            if chosen=="svart":
                winner_winner_chicken_dinner()
        else:
            loser_loser_alarmclock_snoozer()
def winner_winner_chicken_dinner(): #du vann
    clear()
    write("yay du vann peng")
def loser_loser_alarmclock_snoozer():#  du vann inte 
    clear()
    write("du har fel och du valde fel och du fick inte rätt och nu är du dålig och förlorara peng :(((((((((((((((((((((((((((")
type()
listen()
onscreenclick(clickleft, 1)
mainloop()
input()