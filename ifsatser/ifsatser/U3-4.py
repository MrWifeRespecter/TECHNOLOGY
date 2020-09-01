#här ger användaren variablerna värden
pris=float(input("hur mycket kostar din vara? "))
rabatt=float(input("hur stor är rabatten? "))
#här räknar datorn ut problemet
temp=float(rabatt*0.01) 
nytt_pris=float(pris*temp)
#här är vi klara
print("din vara kostar",nytt_pris,"kr",)
#här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
input()