from math import *
from random import *
def s(x): #bara för att jag inte orkade skriva försök så mycket. Min kod ser mer fancy ut nu dessutom
    return(x/försök)
def p(x): #Ibland kan den här skicka iväg antingen 59 eller 61 asterisker. Men det händer inte ofta och det är ett så litet problem så jag skiter i det.
    mängd=round(60*((x/försök)))
    stapel=("*"*mängd)
    return(stapel)
försök=0
frek2=0 #Här är frekvensen som summorna förekommer med
frek3=0
frek4=0
frek5=0
frek6=0
frek7=0
frek8=0
frek9=0
frek10=0
frek11=0
frek12=0
for i in range(1,10001):
    x=randrange(1,7)
    y=randrange(1,7)
    temp_summa=(x+y)
    if temp_summa==2:
        frek2+=1
    if temp_summa==3:
        frek3+=1
    if temp_summa==4:
        frek4+=1
    if temp_summa==5:
        frek5+=1
    if temp_summa==6:
        frek6+=1
    if temp_summa==7:
        frek7+=1
    if temp_summa==8:
        frek8+=1
    if temp_summa==9:
        frek9+=1
    if temp_summa==10:
        frek10+=1
    if temp_summa==11:
        frek11+=1
    if temp_summa==12:
        frek12+=1
    försök+=1
print("Med vilken frekvens förekom de olika summorna? ")
print(" 2|", s(frek2))
print(" 3|", s(frek3))
print(" 4|", s(frek4))
print(" 5|", s(frek5))
print(" 6|", s(frek6))
print(" 7|", s(frek7))
print(" 8|", s(frek8))
print(" 9|", s(frek9))
print("10|", s(frek10))
print("11|", s(frek11))
print("12|", s(frek12))
print("\n")
print("Stapeldiagrammet skulle se ut såhär: ")
print(" 2|", p(frek2))
print(" 3|", p(frek3))
print(" 4|", p(frek4))
print(" 5|", p(frek5))
print(" 6|", p(frek6))
print(" 7|", p(frek7))
print(" 8|", p(frek8))
print(" 9|", p(frek9))
print("10|", p(frek10))
print("11|", p(frek11))
print("12|", p(frek12))    