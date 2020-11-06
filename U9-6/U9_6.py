def räknare(x, y, z): #Här definierar jag en funktion som har tre parametrar som en använadre har satt i huvudprogrammet.
    if z=="/":
        return(x/y)
    if z=="*":
        return(x*y)
    if z=="+":
        return(x+y)
    if z=="-":
        return(x-y)
    else:
        return("Du har angivit fel symbol.")
#Här är huvudprogrammet
x=float(input("Skriv in tal 1: "))
y=float(input("Skriv in tal 2: "))
z=str(input("Vilket räknesätt vill du använda? Svara med + - / eller * "))
print(räknare(x, y, z))
input()