#Här presenterar jag programmet och dess uppgift:
print("Hej, detta program kommer att hjälpa dig lösa ut hypotenusan ur en rätvinklig triangel.")
#Här ger användaren variablerna värden:
enhet=input("Vilken längdenhet används? ")
katet=float(input("Skriv in värdet på din katet: "))
bas=float(input("Skriv in värdet på din bas: "))
#Här löser programmet problemet:
temp=(katet**2 + bas**2) #a^2+b^2=c^2
hypotenusa=(temp**0.5) #(c^2)^0,5=c
#Här skriver jag vad jag vill att konsolen ska säga när den ger svaret: 
print("En rätvinklig triangel med kateten",katet,enhet,"och basen",bas,enhet,"har en hypotenusa som är",hypotenusa,enhet,"lång")

