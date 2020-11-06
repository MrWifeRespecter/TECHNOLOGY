import math 
#Här har vi programmet för del 1 på uppgift 8
def del1():
    lista=[]
    första_tal=0
    andra_tal=1
    for i in range(1,41):
        lista.append(första_tal) 
        första_tal+=andra_tal
        lista.append(andra_tal)
        andra_tal+=första_tal
    print(lista, "\n")

#Här har vi programmet för del 2 på uppgift 8
def del2():
    #Vi kan bara återanvända grundstrukturen som jag hade i min förra upgift fast vi skkriver om den lite grann
    kvoter=[]
    första_tal=0
    andra_tal=1
    for i in range(1,41):
        kvoter.append(första_tal/andra_tal) 
        första_tal+=andra_tal
        kvoter.append(andra_tal/första_tal)
        andra_tal+=första_tal
    print(kvoter, "\n")

#Här har vi programmet för del 3 på uppgift 8
def del3():
    print((1+math.sqrt(5))/2, "\n")

#Här har vi programmet för del 4 på uppgift 8
def del4():
    #Det här kan vara en av de värst ställda frågorna jag någonsin skådat. Vi får inte veta vilket program vi ska skriva om. Vi får heller inte veta vilket det "önskade värdet" är. Är det önskade värdet kanske 3? Eller kanske är det någonting som användaren själv ska bestämma? Eller kanske är det önskade värdet helt enkelt slutet på fibonaccis talföljd? (SOM KAN VARA BARA LITE SVÅR ATT KOMMA TILL) 
    #Jag tolkar frågan som att man ska ta in ett värde som en användare knappar in och sedan berättar vilket talet är på den positionen utan att sätta in alla tal i en lista och att jag ska skriva om det första programmet.
    första_tal=0
    andra_tal=1
    temp=int(input("Vilken position ska ditt tal från Fibonaccis talföljd ha? "))
    repetitioner=int((temp+1)/2)
    for i in range(1,repetitioner):
        första_tal+=andra_tal
        andra_tal+=första_tal
    if temp%2==0:
        if temp!=0:
            print(andra_tal)
        else:
            print("Om du skulle ställa dig i ett led med andra människor. Vart skulle du stå om du stod på den nollte positionen i ledet? Hur kan en nollte position existera samtidigt som en första position? Vilken av dem kommer först? Och vilken är då egentligen först? Vem hamnar på den nollte platsen? Skulle inte den platsen då vara först igen? Fast då är den ju inte på den nollte platsen. Så då är den ju inte först, utan det andra talet är ju först. Fast då är ju först, och först och noll är inte samma sak. Så då är den inte först, utan är efter det andra talet som är på den nollte platsen som då blivit den första platsen igen. Kan det existera en nollte plats över huvud taget? Kan man bara hoppa över den första platsen om det nu skulle existera en nollte plats? Skulle inte det betyda att talet som är på den andra platsen då är först istället? Eller skulle det talet fortsätta vara det andra talet? Men vad händer då med den tomma första platsen? Existerar den platsen över huvud taget eller är den bara tom? Fast om den är tom så är det ju fortfarande en plats och därmed den första platsen. Hur skulle det se ut om det inte fanns några platser bakom den nollte platsen? Vad händer då med saken som tar upp den platsen? Skulle den kunna existera över huvud taget? Kan man vara säker på att den inte existerar? Kan man vara säker på att den gör det? Om den skulle kunna existera och inte samtidigt, vad skulle det betyda för oss människor? Skulle vi då kunna vara säkra på att vi existerar just nu? Hur beter sig någonting som existerar samtidigt som det inte gör det? Vilka frågor skulle man kunna besvara om vi visste mer om denna nollte position? Skriv en essä som besvarar dessa frågor. Utgå från de moment vi har jobbat med under lektioner och kunskap som du har med dig från tidigare. Deadline är den 30:de November 18:00. Skriv i Times New Roman typsnitt 12 och använd Oxfordmodellen vid eventuella citeringar och källhänvisningar. Ingen ordgräns, men håll dig till ämnet. Kom ihåg att detta kommer att påverka ditt betyg. Lycka till!")
    elif temp > 0:
        print(första_tal)

del1()
del2()
del3()
del4()
input()