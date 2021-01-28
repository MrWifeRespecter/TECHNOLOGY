from math import *
from random import *
def fib(x):
    if x<=2:
        return(1)
    else:
        return(fib(x-2)+fib(x-1)) # uppgiften sa att man skulle göra såhär jag vet inte varför det funkar med det gör det??

print("fib nummer".rjust(6), "fib tal".rjust(10))
for i in range(40):
    print(i, "           ", fib(i)) #jag vet inte hur jag ska formatera om en int, när jag försker göra det så gnäller den och jag orkaar inte fixa. 
input()