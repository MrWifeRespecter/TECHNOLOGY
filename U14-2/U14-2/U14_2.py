from random import *
from math import *
lista=[]
for i in range(20):
    lista.append(randint(1,101))
print(lista)
tal=int(input("Vilket tal vill du leta efter? "))

def hitta(lista, tal):
    for j in range(len(lista)):
        if tal == lista[j]:
            print("Talet", tal, "finns på index", j, "i listan. ")
            return
    print("Talet", tal, "finns inte med i listan. ")

hitta(lista, tal)
     
input()