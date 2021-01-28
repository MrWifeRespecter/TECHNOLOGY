from random import *
#Uppgift 1
for i in range(1,14):
    tecken=randint(1,3)
    if tecken == 1:
        print("1")
    if tecken == 2:
        print(" x")
    if tecken == 3:
        print("  2")
print("\n")
#Uppgift 2
for j in range(1,14):
    tal=random()
    if tal < 0.5:
        print("1")
    if tal > 0.5:
        if tal < 0.75:
            print(" x")
        elif tal > 0.75:
            print("  2")
input()
