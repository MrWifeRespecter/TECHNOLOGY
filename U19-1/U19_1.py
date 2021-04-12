from random import *
from time import *
from math import *

listamednamn=[]

class Maträtt:

    def __init__(self, namn, pris, vegetarisk, är_god):
        self.namn = namn
        self.pris = pris
        self.vegetarisk = vegetarisk
        self.är_god = är_god

    def info(self):
        print("Namn: ", self.namn)
        print("Pris: ", self.pris, "kr")
        print("Vegetarisk: ", self.vegetarisk)
        print("Maten är god: ", self.är_god)

def billigaste(x, y):
    if x.pris < y.pris:
        print(x.namn, " kostar mindre. ", x.pris, "kr")

    if y.pris < x.pris:
        print(y.namn, " kostar mindre.", y.pris, "kr")

def rätter():
    namn=str(input("Vad heter din maträtt? ")).capitalize()
    pris=int(input("Hur mycket kostar den? "))
    vegetarisk = str(input("Är rätten vegetarisk? ")).capitalize()
    är_god = str(input("Är maten god? ")).capitalize()
    listamednamn.append(namn)
    print("\n") 
    namn = Maträtt(namn, pris, vegetarisk, är_god)       

def vilka_rätter():
    namn=str(input("Vilka rätter vill du jämföra? Skriv in första rätten: ")).capitalize()
    if namn in listamednamn:
        x=namn
        namn=str(input("Vilka rätter vill du jämföra? Skriv in andra rätten: ")).capitalize()
        if namn in listamednamn:
            y=namn
    else:
        print("Någonting gick fel... Försök igen. ")
        print("Här är namnen på de rätter som finns")
        print(listamednamn)
        print("\n")
        vilka_rätter()
    billigaste(x,y)


while True:
    rätter()
    fortsätt = input("Vill du skriva in fler rätter? Svara med J eller N: ").capitalize()
    if fortsätt=="N":
        break


vilka_rätter()
input()

