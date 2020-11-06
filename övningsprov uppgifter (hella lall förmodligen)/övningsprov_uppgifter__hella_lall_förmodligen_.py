#del 1:
name=input("Dein Name mein Herr: ")
print("Grüss dich",name)
print("\n")
#del 2:
for i in range(100,0,-1):
    print(i, end=" ")
print("\n")

#del 3:
preis=int(input("Wie viel kostet dein Pulli mein Herr? "))
if preis<200:
    print("Aber das ist ein wunderbar Preis! Ich will dass kaufen.")
if 401>preis>199:
    print("Ich will dass überdenken.")
if preis>400:
    print("Zu teuer, geh weg und finde Jemanden andre, der betrügen du Hurensohn.")
print("\n")
#del 4:
for j in range(1,13):
    for k in range(1,11):
        print(j*k, end=" ")
    print("\n")

#del 5:
for l in range(1,31):
    print(l)
print("\n")

#del 6:
fünfundsiebzig=int(75)
zahl=float(input("Schreib ein Zahl: "))
if zahl>fünfundsiebzig:
    print("Dein Zahl ist grösser als 75.")
if zahl==fünfundsiebzig:
    print("Dein Zahl ist 75")
if zahl<fünfundsiebzig:
    print("Dein Zahl ist kleiner als 75.")
print("\n")