from random import *
from math import *
from webbrowser import *
from time import *

websites=["https://www.youtube.com/watch?v=kYChcl_6rvs", "https://www.youtube.com/watch?v=_VUwVS9cddg", "https://www.youtube.com/watch?v=qiSUmKzGpPM", "https://www.youtube.com/watch?v=OiwsGLsfJwM", "https://www.youtube.com/watch?v=skeC80CGejI", "https://www.youtube.com/watch?v=fc_u4GFICZ4", "https://www.youtube.com/watch?v=k0aYG-YgbUI", "https://www.youtube.com/watch?v=-TGFqNK8czE", "https://www.youtube.com/watch?v=RoUJ7TI9MgA", "https://www.youtube.com/watch?v=EQqXGDw12fY", "https://www.youtube.com/watch?v=e7VK3pne8N4", "https://www.youtube.com/watch?v=2tmKG1fCn-o", "https://www.youtube.com/watch?v=LQ_eazT56FA", "https://www.youtube.com/watch?v=xvRR_Kqlh48", "https://www.youtube.com/watch?v=AdP8Fk0fofk", "https://www.youtube.com/watch?v=vC8hK8JOqhI", "https://www.youtube.com/watch?v=O-YFUFPXGqo", "https://www.youtube.com/watch?v=5QVSs6DsMKE", "https://www.youtube.com/watch?v=4dfP0_j2Tug", "https://www.youtube.com/watch?v=ctWFZb9FM1M", "https://www.youtube.com/watch?v=_5DUrOyIvm0", "https://www.youtube.com/watch?v=E0KfQ1o43R8", "https://www.youtube.com/watch?v=qzQCVSYqnu0", "https://www.youtube.com/watch?v=VT6w7f3N8Hw", "https://www.youtube.com/watch?v=AT1Q9F_-c0g", "https://www.youtube.com/watch?v=dehZYbJt_Wg", "https://www.youtube.com/watch?v=XLufvfM7WJ8", "https://www.youtube.com/watch?v=cB4dYfFgaME", "https://www.youtube.com/watch?v=VAaMXR0tMQ8", "https://www.youtube.com/watch?v=pGZzJ5mguBQ", "https://www.youtube.com/watch?v=WiD5WunwTvQ", "https://www.youtube.com/watch?v=Zg1pDweZ0W8", "https://www.youtube.com/watch?v=YwfVFXkT_tM", "https://www.minecraft.net/en-us/download/"," https://twitter.com/Riot_Kassadin", "https://www.jw.org/en/"]

def straff(): #Jag ber om ursäkt...

    tabs=choice(websites)
    open(tabs,new=1)
    sleep(1)

minsta=int(input("Vilket är det minsta talet i ditt intervall som du tänker på? "))
största=int(input("Vilket är det största talet i ditt intervall som du tänker på? "))
gissningar=0

while True:
    gissningar+=1
    gissning=minsta+((största-minsta)//2)
    print("jag gissar på",gissning)
    print("\n")
    svar=str(input("Var det korrekt? Svara med J eller N: "))
    svar=svar.capitalize()
    if svar=='J':
        print("Haha jag vann och du förlorade. ")
        print("\n")
        print("Jag behövde bara",gissningar,"försök på mig. ")
        break
    if svar=="N":
        while True: 
            if minsta==största:
                print("Nu har du ljugit för mig någonstans. ")
                for i in range(25):
                    straff()
                break
            mm=str(input("Nähä var det mer eller mindre än ditt tal? Svara med Mer eller Mindre: "))
            mm=mm.capitalize()
            if mm=="Mer":
                a=största
                största-=a-gissning
                break
            if mm=="Mindre":
                minsta=gissning
                break
            else:
                print("Svara med Mer eller Mindre")
                print("\n")
    else:
        print("Du ska skriva in en bokstav hur svårt kan det vara?")
        print("\n")
input()