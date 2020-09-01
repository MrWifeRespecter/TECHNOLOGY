#här frågar jag efter bensinpris och ger en variable det värdet.
pris=float(input("Hur mycket kostar en liter bensin? "))
#här skriver jag if-satserna


if pris<10:
    print("Det var billigt!")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()
elif 10<pris<15:
    print("Tanka full tank")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()
elif 15<pris<20:
    print("Tanka tio liter")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()
elif pris>20:
    print("Nu säljer jag bilen och cyklar istället")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()
else:
    print("svarade du rätt?")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()

