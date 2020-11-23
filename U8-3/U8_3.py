mängd=int(input("Hur många tal vill du mata in? "))
lista=[]
summa=0
for i in range(1,mängd+1):
    lista.append(float(input("Ange tal "+ str(i) + ": ")))
for x in lista:
    summa+=x
medel=summa/mängd
print(summa)
print(medel)
input()