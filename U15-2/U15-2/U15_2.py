from random import *


lista=[]
req=0

for i in range(100):
    lista.append(randint(1,100))
print(lista)

def combsort(lista):
    global req
    gap=len(lista)
    bytt=True
    while gap>1 or bytt==True:
        gap=int(gap/1.3)
        if gap < 1:
            gap=1
        i=0
        bytt=False
        while i+gap < len(lista):
            req+=1
            if lista[i] > lista[i+gap]:
                lista[i], lista[i+gap] = lista[i+gap], lista[i]
                bytt=True
            i+=1

combsort(lista)
print(lista)
print(req)

