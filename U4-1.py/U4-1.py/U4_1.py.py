#introduktion till programmet
print("det här proogrammet kommer att hjälpa dig att räkna ut medelpoängen på dina prov. ")
#användaren ger variablerna värden
prov1=float(input("skriv resultatet på ditt första prov här: "))
prov2=float(input("skriv resultatet på ditt andra prov här: "))
prov3=float(input("skriv resultatet på ditt tredje prov här: "))
#här sker uträkningarna
temp=(prov1+prov2+prov3)
medelvärde=(temp/3)
#här säger datorn någonting beroende på resultatet
if medelvärde > 90:
    print("grattis! ditt medelvärde är",medelvärde,"bra jobbat")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()
else:
    print("din medelpoäng är",medelvärde)
    print("om du skulle ha fått mer än 90 poäng skulle du ha varit en duktig elev")
    #här la jag till en tom input bara för att användaren inte kunne se svaret innan konsollen stängdes om man inte anvädner visual studio när man öppnar den.
    input()

