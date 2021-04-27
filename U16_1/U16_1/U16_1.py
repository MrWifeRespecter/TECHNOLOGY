from random import *
from math import *
from sys import *
from time import *
from webbrowser import *

dict = {}

def lägg(): #Här är koden som körs om man vill lägga till en adress:
    ep=input("Skriv in adressen som du ska lägga in: ")
    if "@" in ep and "." in ep:  #Kollar om det finns med en punkt och ett @ i adressen. Man kan skriva in adressen ".@", men jag orkar inte fixa fler villkor. Om man vill vara muppig så får man vara det 
        namn=str(input("Skriv in namnet på den personen som adressen tillhör: ")).capitalize()
        if namn in dict or any(ep in i for i in dict.values()): #Kollar om namnet eller adressen redan finns med i registret. Namnet var enkelt att kolla eftersom att den är en key. Men adressen är en value så då itererade jag igenom dictionaryts värden för att se om något av de stämde överens med den inmatade adressen. 
            print("Personen eller adressen finns redan med i registret. Du kan ta bort personen eller adressens ägare om du vill uppdatera informationen genom att välja alternativ 3 på startskärmen: ")
            print("\n")
            start()
        else: #Lägger in namnet på personen som en nyckel och binder adressen till den. 
            dict[namn]=ep 
            print(dict)
            print("\n")
    else: #Här kollar jag om man är säker på om adressen är korrekt skriven:
        print("Är du säker på att du skrivit in adressen rätt? ")
        svar2 = input("Svara med J eller N: ").capitalize()
        if svar2=="J":
            namn=str(input("Skriv in namnet på den personen som adressen tillhör: ")).capitalize()
            dict[namn]=ep
            print(dict)
            print("\n")
        if svar2=="N":
            print("Nähä men skriv in rätt då. ")
            print("\n")
            lägg()
def sök(): #Här söker man efter en adress:
    leta=str(input("Skriv in namnet på den personen som du vill söka: ")).capitalize()
    if leta in dict:
        print("\n")
        print(leta, "har adressen:", dict[leta])
        print("\n")
    else: 
        print("Namnet finns inte med i registret. ")
        print("\n")

def bort(): #Här tar man bort en adress ur registret:
    sjas = str(input("Skriv in namnet på den personen som du vill ta bort från registret: ")).capitalize()
    if sjas in dict:
        del dict[sjas]
        print("Ok nu är den borta")
        print("\n")
    else:
        print("Namnet finns inte med i registret")
        print("\n")

def visa(): #Här visar jag dictionaryn: 
    print(dict)
    print("\n")

def start(): #Det här kommer att loopa tills användaren är nöjd
    global svar
    print("Vad vill du göra?")
    print("=================")
    print("1. lägga till eller ändra en adress")
    print("2. söka en adress")
    print("3. ta bort en adress ur registret")
    print("4. visa hela registret")
    print("0. avsluta")
    svar = str(input("Skriv in ditt svar: "))
    print("\n")

def nyaa(): #YOU FOOL! YOU FELL FOR THE OLDEST TRICK IN THE BOOK! THUNDERU CROSSU SPURITU ATTACKU!
    websites=["https://www.youtube.com/watch?v=kYChcl_6rvs", "https://www.youtube.com/watch?v=_VUwVS9cddg", "https://www.youtube.com/watch?v=qiSUmKzGpPM", "https://www.youtube.com/watch?v=OiwsGLsfJwM", "https://www.youtube.com/watch?v=skeC80CGejI", "https://www.youtube.com/watch?v=fc_u4GFICZ4", "https://www.youtube.com/watch?v=k0aYG-YgbUI", "https://www.youtube.com/watch?v=-TGFqNK8czE", "https://www.youtube.com/watch?v=RoUJ7TI9MgA", "https://www.youtube.com/watch?v=EQqXGDw12fY", "https://www.youtube.com/watch?v=e7VK3pne8N4", "https://www.youtube.com/watch?v=2tmKG1fCn-o", "https://www.youtube.com/watch?v=LQ_eazT56FA", "https://www.youtube.com/watch?v=xvRR_Kqlh48", "https://www.youtube.com/watch?v=AdP8Fk0fofk", "https://www.youtube.com/watch?v=vC8hK8JOqhI", "https://www.youtube.com/watch?v=O-YFUFPXGqo", "https://www.youtube.com/watch?v=5QVSs6DsMKE", "https://www.youtube.com/watch?v=4dfP0_j2Tug", "https://www.youtube.com/watch?v=ctWFZb9FM1M", "https://www.youtube.com/watch?v=_5DUrOyIvm0", "https://www.youtube.com/watch?v=E0KfQ1o43R8", "https://www.youtube.com/watch?v=qzQCVSYqnu0", "https://www.youtube.com/watch?v=VT6w7f3N8Hw", "https://www.youtube.com/watch?v=AT1Q9F_-c0g", "https://www.youtube.com/watch?v=dehZYbJt_Wg", "https://www.youtube.com/watch?v=XLufvfM7WJ8", "https://www.youtube.com/watch?v=cB4dYfFgaME", "https://www.youtube.com/watch?v=VAaMXR0tMQ8", "https://www.youtube.com/watch?v=pGZzJ5mguBQ", "https://www.youtube.com/watch?v=WiD5WunwTvQ", "https://www.youtube.com/watch?v=YwfVFXkT_tM", "https://www.minecraft.net/en-us/download/"," https://twitter.com/Riot_Kassadin", "https://www.jw.org/en/"]
    for i in range(20):
        tabs=choice(websites)
        open(tabs,new=1)
        sleep(3)



while True:
    start()
    if svar == "1":
        lägg()
    if svar == "2":
        sök()
    if svar == "3":
        bort()
    if svar == "4":
        visa()
    if svar == "0":
        exit()
    else:
        print("Ditt alternativ finns inte med på listan... Håll dig till vad som står på den... Nu blir du bestraffad! ")
        print("\n")
        nyaa() #Uh oh...

