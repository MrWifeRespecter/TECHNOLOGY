bokstäver=list("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ")
print(bokstäver)
namn = ['ÅBERG', 'ÖBERG', 'VIKLUND', 'ANDERSSON', 'ANDERBERG', 'ÄRLESKOG', 'STRÄNG', "STRÅBY", "VIKLANDER"] #.capitalize() funkar inte på en lista, så jag skrev om alltig till stora bokstäver, 
                                                                                                            #men detta man kan slippa om man inte hade hårdprogrammerat det så att listan alltid 
                                                                                                            #var likadan

def sortering(bokstäver, namn): #Jag kom på detta aldeles själv :)

        while True: #sorterar de första bokstäverna
            change=0
            for k in range(len(namn)-1):
                if bokstäver.index(list(namn[k])[0]) > bokstäver.index(list(namn[1+k])[0]): #Denna är jag stolt över, jag kollar så att bokstaven som finns i första positionen i de olika namnen i 
                                                                                            #listan får ett värde baserat på dess index i listan som jag gjorde med alla bokstäverna i det svenska 
                                                                                            #alfabetet, därefter kollar den vilken av de värdena som är störst
                    namn[k], namn[1+k] = namn[1+k], namn[k]
                    change+=1
            if change == 0:
                break

        for k in range(len(namn)-1): #Denna delen fixar så att om två namn börjar på samma bokstav så kommer den första som har en bokstav längre ner i namnet som är större än den 
                                     #andras vid respektive position att flyttas upp
            if bokstäver.index(list(namn[k])[0]) == bokstäver.index(list(namn[1+k])[0]):
                if len(list(namn[k]))<len(list(namn[k+1])): #Dessa ser till så att man inte kan kalla på ett index som står utanför ett av namnens gränser
                    minsta=len(list(namn[k]))               #|
                if len(list(namn[k]))>len(list(namn[k+1])): #|
                    minsta=len(list(namn[k+1]))             #|
                if len(list(namn[k]))==len(list(namn[k+1])):#|
                    minsta=len(list(namn[k]))               #|
                for l in range(1, minsta-1): #Denna kollar vilken av de som först har en avvikande bokstav och placerar därefter det namnet med den större bokstaven bakom det andra
                    if bokstäver.index(list(namn[k])[l]) > bokstäver.index(list(namn[1+k])[l]):
                        namn[k], namn[1+k] = namn[1+k], namn[k]
                        break #Så att de bokstäverna bakom det första som skiljer sig inte spelar roll

        print(namn)

sortering(bokstäver, namn)
input()