lista=[] #till och börja med
lista2=[] #till och börja med
längd=len(lista)
mängd=int(input("Hur många tal vill du ha i listan? ")) #frågar hur många tal man vill ha i listan
for i in range(1,mängd+1): #jag börjar med 1 för att man den inte ska säga "tal 0", jag lade till 1 för att kompensera.
    lista.append(float(input("Ange tal " + str(i)+": "))) #säger vad du ska skriva in och samlar alla inputs i en lista
for j in range(len(lista),0,-1): #den här tar hänsyn till att längden av listan minskar med 1 efter varje loop
    xD=0 #sätter den här för att värdet på xD inte ska gå över längden av listan
    minsta=lista[xD] #till och börja med
    for k in lista: #den här loopen ska kolla alla delar av listan individuellt och se vilken del som är minst. Denna delen kommer den så att lägga in först i en ny lista. Den minsta delen sparas tills en ny lägsta hittas. När loopen är klar så läggs det minsta värdet in i en ny lista och den gamla tas bort.
        if minsta>lista[xD]:
            minsta=lista[xD]
        xD+=1 #här ökar xD med 1 för att jag ska kunna kolla på nästa tal i listan
    lista2.append(minsta) #lägger till det minsta värdet i en ny lista på sista platsen. Eftersom att det minsta värdet fått den sista platsen först så kommer de större värdena komma senare. Listan sorteras därför i storleksordning.
    lista.remove(minsta) #tar bort det minsta värdet ur den ursprungliga listan.
print(lista2) 