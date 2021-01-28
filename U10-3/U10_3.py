from random import *
störst=0
minst=1001
total=0
for k in range(1,101):
    x=randint(1,1000)
    if x < minst:
        minst=x
    if x > störst:
        störst=x
    total+=x
print("Det största värdet var", störst, "Det minsta värdet var", minst, "Medelvärdet var", (total/100))
input()
