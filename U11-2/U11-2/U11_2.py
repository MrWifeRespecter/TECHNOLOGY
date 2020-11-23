def isint(str): #Jag hade svårt att tolka den här uppgiften, men jag är rätt säker på att detta var vad jag skulle göra. Vilket är exakt vad .isdecimal() redan gör.
    try:
        str=int(input("Skriv in en sträng som kan göras om till ett heltal: "))
    except:
        return(True)
    else:
        return(False)
while isint(str) == True:
    print("Din sträng kan inte göras om till ett heltal. ")
print("Din sträng kan göras om till ett heltal. ")
input()