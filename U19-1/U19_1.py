from random import *
from time import *
from math import *
from sys import *
import pickle # <-- jag hatar den här 

d = {}

class Maträtt:

    def __init__(self, namn, pris, vegetarisk, är_god): #här ser man vilka egenskaper som klassen kan ha
        self.namn = namn
        self.pris = pris
        self.vegetarisk = vegetarisk
        self.är_god = är_god

    def info(self): #Den här kan komma att användas senare
        print("Namn: ", self.namn)
        print("Pris: ", self.pris, "kr")
        print("Vegetarisk: ", self.vegetarisk)
        print("Maten är god: ", self.är_god)

def billigaste(namn1, namn2): #Kollar vilken av de inmatade rätterna som är billigast eller om de är lika dyra. Returnerar false till en loop så att den inte körs igen
    if d[namn1].pris < d[namn2].pris:
        print(d[namn1].namn, " kostar mindre. ", d[namn1].pris, "kr")

    if d[namn2].pris < d[namn1].pris:
        print(d[namn2].namn, " kostar mindre.", d[namn2].pris, "kr")

    if d[namn1].pris == d[namn2].pris:
        print("De kostar båda", d[namn1].pris, "kr")
    return False

def rätter(): #Frågar frågor om vilka egenskaper maträtten har och gör en klass med de egenskaperna
    namn=str(input("Vad heter din maträtt? ")).capitalize()
    pris=int(input("Hur mycket kostar den? "))
    vegetarisk = str(input("Är rätten vegetarisk? ")).capitalize()
    är_god = str(input("Är maten god? ")).capitalize()
    print("\n") 
    rätt = Maträtt(namn, pris, vegetarisk, är_god)
    placeholderDict = {namn:rätt} # kunde inte lösa det på något finare sätt, koden var muppig om jag skippade denna delen tror jag
    d.update(placeholderDict) #Updatear ett existerande dictionary med placeholderDict

def vilka_rätter(): #kollar vilka rätter som användaren vill jämföra
    namn1=str(input("Vilka rätter vill du jämföra? Skriv in första rätten: ")).capitalize()
    if namn1 in d: #Finns namnet som användaren skrev in i dictionaryt så körs denna del
        pris1=d[namn1].pris
        print(namn1)
        namn2=str(input("Vilka rätter vill du jämföra? Skriv in andra rätten: ")).capitalize()
        if namn2 in d:
            pris2=d[namn2].pris
            print(namn2)
        else: #om namnet inte finns med i dictionaryn
            print("Någonting gick fel... Försök igen. ")
            print("Här är namnen på de rätter som finns")
            print(d)
            print("\n")
            return True
    else: #om namnet inte finns med i dictionaryn
        print("Någonting gick fel... Försök igen. ")
        print("Här är namnen på de rätter som finns")
        print(d)
        print("\n")
        return True
    return billigaste(namn1, namn2) #returnerar alltid False, men jag behöver den för att koden ska stanna om alla kraven uppfylls.
    

while True: #Den här låter användaren skriva in rätter tills hen är nöjd
    rätter()
    if input("Vill du skriva in fler rätter? Svara med J eller N: ").capitalize()=="N": #Den här täcker inte felinmatningar som typ "sjied". Men jag orkar inte bry mig om det. 
        break

while True: #Den här är tänkt att loopa tills användaren skriven in två rätter som kan jämföras.
    if vilka_rätter() == False:
        break

input()