#här börjar jag med att kolla om användaren är 18 år eller äldre.
ålder=int(input("hur gammal är du? "))
#här skriver jag vad som händer om du är 18 eller äldre.
if ålder>=18:
    print("ok bra")
    #härfrågar jag hur hög din bruttoårsinkomst är och skriver vad som ska hända beroende på svar
    inkomst=float(input("hur hög är din bruttoårsinkomst? "))
    if inkomst>=120000:
        print("ok bra")
        #här kollar jag om personen har några betalningsanmärkningar och skriver vad som ska hända beroende på svaret
        anmärkningar=input("har du några betalningsanmärkningar? ")
        if anmärkningar=="nej":
            print("Fakturaavbetalning beviljad")
            #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
            input()
        else:
            print("tyvärr kan vi inte bevilja fakturabetalning")
            #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
            input()
    else: 
        print("tyvärr kan vi inte bevilja fakturabetalning")
        #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
        input()
else:
    print("tyvärr kan vi inte bevilja fakturabetalning")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()