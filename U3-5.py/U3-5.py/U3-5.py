#skapad av Viggo Hermansson
#här ger användaren variablerna värden
bensin=float(input("hur mycket bensin tankade du i liter? "))
pris=float(input("hur mycket kostar bensinen i kr per liter? "))
#här sker uträkningarna
total=float(bensin*pris)
#här printar datorn ut kvittot
print( "+---------------------------+")
print("| KVITTO                     |")
print("| Tankad volym:              |")
print("| ",bensin,"liter            |")
print("| Pris per liter:            |")
print("|     ",pris,"kr             |")
print("|                            |")
print("| Betalt kronor              |")
print("| ",total,"kr                |")
print("|                            |")
print("|                            |")
print("| Tack för besöket och       |")
print("| välkommen åter!            |")
print("+---------------------------+")
#här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
input()
