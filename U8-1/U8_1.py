
mängd=int(input("Hur många tal vill du mata in? "))
lista=[]
for i in range(1,mängd+1):
    lista.append(float(input("Ange tal "+ str(i) + ": ")))
for x in lista:
    print(x)
input()