from random import *
from math import *

tal = [3,7,14,19,21,40,47,47,69,72,83,87,94,101] 
leta=int(input("Skriv in det talet som du vill leta efter: "))

while True:
    if leta<tal[(len(tal)//2)]:
        for i in range((len(tal)//2)):
            tal.pop((len(tal)-1))
    if leta>tal[(len(tal)//2)]:
        for i in range((len(tal)//2)):
            tal.pop(0)
    if leta==tal[(len(tal)//2)]:
        riktig=tal[(len(tal)//2)]
        tal = [3,7,14,19,21,40,47,47,69,72,83,87,94,101] 
        print("talet finns på plats", tal.index(riktig)+1)
        break
    elif len(tal)==1:
        print("nej den finns inte")
        break
input()