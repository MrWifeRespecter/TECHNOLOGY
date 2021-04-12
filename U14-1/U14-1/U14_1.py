from random import *
from math import *

a=0
lista=[]
for i in range(20):
    lista.append(randint(1,100))
print(lista)
sökt=int(input("Skriv in ett tal som du ska söka efter i listan: "))

for j in range(0,20):
    a+=1
    if sökt==lista[j]:
        print("Talet",sökt,"ligger på plats",j+1, "i listan." )
        break
    if a==20:
        print("Sorry, ditt sökta tal finns inte med i listan. ")
input()