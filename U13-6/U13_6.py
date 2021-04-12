from random import *
from turtle import *
from math import *

speed(0)
ht()
pu()
seth(90)
recurse=0
pensize(1)
counter1=7
counter2=10
pd()
fd(50)
def hAHAHAHAH():
    global counter1
    global counter2
    pd()
    längd=randint(10,30)
    z=randint(5,70)
    left(z)
    högersväng=z*2
    if counter2==0:
        return
    else:
        counter1-=1
        läge1=position()
        if counter1>0:
            y=randint(10,45)
            fd(y)
            pos2=pos()
            bk(y)
            right(högersväng)
            fd(y)
            pos3=pos()
            pu()
            setpos(pos2)
            seth(90)
            print(counter1)
            hAHAHAHAH()
        else:
            counter2-=1
            counter1=3
            



hAHAHAHAH()
input()