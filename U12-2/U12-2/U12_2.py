from turtle import *
from random import *
def färg(): #Här skapar jag en färg med en slumpad färgkod
    r=random()
    b=random()
    g=random()
    färg=(r, g, b)
    return(färg)
setworldcoordinates(-200, -200, 200, 200) 
ht() #för att den ska bli snabb
speed(0) #för att den ska bli snabb
for i in range(100): #Slumpar ut en position och sätter ut en punkt där med en slumpad färg
    x=randint(-100,100)
    y=randint(-100,100)
    storlek=randint(1,100)
    pu()
    setpos(x,y)
    dot(storlek,färg())
exitonclick() #För att man ska kunna beundra sitt mästerverk.
input()