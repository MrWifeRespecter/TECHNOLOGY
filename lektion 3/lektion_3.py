# .format(x) gör så att man skriver in det man vill varje gång man skrivet {} i sin print. 
print("Här {} skriver vi lite text" .format("xxx"))

#exempel: här använder vi {:.3f} för att visa att vi vill att kosen ska skriva ut svaret som användaren ger som en float med 3 decimaler.
pris=float(input("skriv in pris "))
print("varan kostar {:.3f} " .format(pris))
print("varan kostar {0} kr {1}, {2} {3}".format(pris, "slut", "andra", "tredje", "fjärde"))
# {:.4s} ger en sträng med upptagande av mist 4 teckenpositioner
pris2=str(input("test "))
print("{:.4s} test".format(pris2))

#program för att addera tal.
while True:
    antal=int(input("hur många tal vill du addera? "))
    summa = 0 #till att börja med
    for i in range(1, antal+1):
        tal=float(input("ange tal " +str(i)+": "))
        summa+=tal 
    break
print(summa)
