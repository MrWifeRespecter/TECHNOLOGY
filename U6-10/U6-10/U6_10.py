mening=str(input("Vad är din mening som du vill göra om till Svenska? ")) #här frågar jag om meningen som användaren ska skriva in
temp=mening.lower() #här gör jag temporärt om meningen till lowercase så att jag inte behöver ta hänsyn till stora bokstäver
konsonanter="bcdfghjklmnpqrstvwxz" #här sätter jag in alla konsonanter så att jag senare snabbt kan kolla om en bokstav på en viss position i meningen är e konsonant eller inte
mening2="" #Det här är den översatta meningen som jag till en början lämnar blank.
längd=len(temp) #för att jag ska slippa skriva in len(temp) så många gånger och för att koden ska bli lättare att förstå
j=0 #Ska kolla om första bokstaven i ett segment är en konsonant.
k=1 #för att jag ska kunna läsa av den inmatade meningen i större segment. Denna läser av om den andra bokstaven i ett segment med en konsonant i början är ett o.
l=2 #Samma anledning som den innan. Denna läser av om den tredje bokstaven i ett segment efter ett o är samma som den första konsonanten i segmentet.
for i in range(längd): #hur många gånger som man ska loopa koden. Denna är viktig för att man ska få ett svar oavsett längd på mening.
    bokstav=temp[j] #kollar vilken bokstav är den första i ett segment
    if bokstav in konsonanter: #kollar om den bokstaven är en konsonant
        O_Check=temp[k] #ska kolla om den andra bokstaven i segmentet är ett o
        if O_Check=="o": #Kollar om bokstaven faktiskt är o
            bokstav2=temp[l] #kollar vilken bokstav den tredje i segmentet är
            if bokstav2==bokstav: #kollar om den bokstaven är densamma som den första i segmentet
                    mening2+=bokstav #lägger till bokstaven utifall att alla kraven är uppfyllda
                    j+=3 #om vi gick igenom hela segmentet utan problem så behöver vi lägga till 3 på j k och l för annars kommer fel bokstäver att checkas nästa loop
                    k+=3 
                    l+=3
                    if j==längd: #om värdena på j och längd är samma så måste vi stoppa loopen, annars blir värdet j större än mängden tecken i meningen. Då går koden sönder :( 
                        break
            if bokstav2!=bokstav: #om den tredje bokstaven i segmentet inte är detsamma som det första är meningen inte skriven på korrekt rövarspråk
                print("Din mening är inte på korrekt rövarspråk.") 
                break #är meningen inte skriven på korrekt rövarspråk så stannar koden.
        if O_Check!="o": #om den andra bokstaven inte är o när en konsonant är hittad så är meningen inte skriven på korrekt rövarspråk
            print("Din mening är inte på korrekt rövarspråk.")
            break
    if bokstav not in konsonanter: #är bokstaven som vi tittar på inte en konsonant så lägger vi bara till den i den nya meningen.  
        mening2+=bokstav
        j+=1 #här lägger vi bara till ett på j k och l eftersom att vi bara tittade på en bokstav här istället för ett helt segment. 
        k+=1
        l+=1
        if j==längd: #om värdena j och längs är lika stora så bryts koden annars går den boom.
            break
mening2=mening2.capitalize() #för att göra den lite finare
print("Din mening betyder:", mening2) #för att göra det tydligare vad koden gjorde.
input() #en tom input för att mans ka kunna se koden om man inte använder visual studio 2019
    