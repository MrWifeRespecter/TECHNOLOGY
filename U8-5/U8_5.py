lista=[] #till och börja med
xD=0 #till och börja med
mängd=int(input("Hur många tal vill du ha i listan? ")) #frågar hur många tal man vill ha i listan
for i in range(1,mängd+1): #jag börjar med 1 för att man den inte ska säga "tal 0", jag lade till 1 för att kompensera.
    lista.append(float(input("Ange tal " + str(i)+": "))) #säger vad du ska skriva in och samlar alla inputs i en lista
minsta=lista[0] #till och börja med
for j in lista:
    if minsta>lista[xD]: #om värdet på det innan minsta värdet så byter vi ut den med det nya minsta värdet.
        minsta=lista[xD] 
        position=xD+1
    xD+=1
print(minsta, "är den minsta variabeln, och den fanns på plats ", position, " i listan.")
input()