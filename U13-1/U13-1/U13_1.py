from math import *
from random import *
from turtle import *
def countdown(x):
    if x == 0:
        print("woohoo")
    else:
       print(x)
       countdown(x-1)

x=int(input("skriv in ett tal: "))
countdown(x)
input()