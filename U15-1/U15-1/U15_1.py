from random import *

lista=[]
it=1

for i in range(100):
    lista.append(randint(1,100))

print(lista)

def bubbleAHAHHAHAHAHAHAHAHAHAHAHA(lista):
    global it
    while True:
        change=0
        for j in range(len(lista)-it):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                change+=1
        if change==0:
            return
        it+=1

bubbleAHAHHAHAHAHAHAHAHAHAHAHA(lista)
print(lista)


input()
