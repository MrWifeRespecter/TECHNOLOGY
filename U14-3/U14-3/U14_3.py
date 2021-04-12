from random import *
from math import *

rätt=randint(1,99)
gissningar=1

while True:
    gissning=int(input("Jag tänker på ett tal mellan 1 och 99, gissa vilket: "))
    if gissning==rätt:
        print("Grattis du gissade rätt!")
        print("Det tog dig",gissningar,"försök")
        break
    else:
        if gissning<rätt:
            print("För lågt... Gissa igen")
        if gissning>rätt:
            print("För högt... Gissa igen")
        gissningar+=1
input()