psw=input("Skriv ditt lösenord här: ")
test=input("Vad är ditt lösenord? (tryck enter för att avbryta) ")
while test!=psw: 
    if test =="":
        print("inloggning avbruten")
        break
    else:
        print("Fel lösenord. ")
        test=input("Vad är ditt lösenord? ")
if test !="":
    print("Lösenord OK")
    input()
