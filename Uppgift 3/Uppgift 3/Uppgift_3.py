from math import *
from random import *

def mul(x,y):
    if x<1: #annars kommer en fatal error att förekomma
        return(0)
    if y<1: #ditto
        return(0)
    if x == 1:
        return(y)
    if y == 1:
        return(x)
    else:
        return(x+mul(x,y-1))

x=int(input("skriv in ett tal: "))
y=int(input("skriv in ett tal: "))
print(mul(x,y))
input()