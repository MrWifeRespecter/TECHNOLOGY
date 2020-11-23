def isfloat(str):
    try:
        str=str(input("Skriv in en sträng som kan göras om till ett flyttal: "))
        float(str)
    except:
        return(False)
    else:
        return(True)
while isfloat(str) == True:
    print("Din sträng kan göras om till ett flyttal. ")
print("Nu skrev du in en sträng som inte kan göras om till ett flyttal. Vilken rebell. ")
input()