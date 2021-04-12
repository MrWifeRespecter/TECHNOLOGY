import os 


f = open("./test.txt", "w+") #Öppnar filen så att man kan både skriva och läsa den samtidigt
rad = input("skriv en rad (tom rad avslutar programmet): ")
while rad: #skriver man in en tom rad så räknas det som False
    f.write(rad+"\n") #gör det prydligt i själva dokumentet.
    rad=input("Skriv en rad (tom rad avslutar programmet): ")

f.seek(0) #sätter pointern till första raden
rad = f.readline()
while rad: #Runnar tills det inte längre finns några rader att läsa, värdet blir då False
    print(rad.strip()) #tar bort tomma rader.
    rad= f.readline()
f.close()


input()


