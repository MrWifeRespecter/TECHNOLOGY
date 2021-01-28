from random import *
vinst_med_byte=0 #för att kolla hur många man får
förlust_med_byte=0 #för att kolla hur många man får
vinst_utan_byte=0 #för att kolla hur många man får
förlust_utan_byte=0 #för att kolla hur många man får
for i in range(1,1001): #1000 försök    
    dörr=randint(1,3) #Rätt dörr slumpas ut
    valdörr=randint(1,3) #Valdörren slumpas ut
    if valdörr!=dörr: #om man har valt fel dörr så kommer man att vinna om man byter dörr.
        ändra_dörr=randint(1,2)
        if ändra_dörr==1: #Här  byter man
            vinst_med_byte+=1
        if ändra_dörr==2: #Här byter man inte man
            förlust_utan_byte+=1
    else: #Om man har valt rätt dörr så vinner man om man inte byter.
        ändra_dörr=randint(1,2)
        if ändra_dörr==1: #Här byter man
            förlust_med_byte+=1
        if ändra_dörr==2: #Här byter man inte
            vinst_utan_byte+=1
print(vinst_med_byte,"vinster med byte",förlust_med_byte,"förluster med byte",vinst_utan_byte,"vinster utan byte",förlust_utan_byte,"förluster utan byte")
input()