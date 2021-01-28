from math import *
from random import *
tal_i_area=0
försök=0
for i in range(1,10000000): #Den här kommer att ladda ett bra tag, så du kan gå på toa medans du väntar på den
    x=random()
    y=random()
    if sqrt((x*x)+(y*y)) < 1: #Här kollar jag om punkten som den slumpade ut är i eller utanför cirkeln
        tal_i_area+=1
    försök+=1 #Jag orkade inte räkna hur många nollor jag hade
ffaktor=(tal_i_area/försök) #om jag delar mängden punkter som kom inom arean med mängden repetitioner så får jag fram hur mycket av den totala arean som är täckt i procentform
#Jag behöver inte göra något med den förändringsfaktorn eftersom at den totala arean är 1 areaenhet i kvadrat. Så multiplicerar jag dem får jag samma svar
print(ffaktor*4) #Jag multiplicerar den arean med 4 för att det var en fjärdedels cikel. Får hela cirkelns area som är r^2*pi som är 1*1*pi som är pi
input()