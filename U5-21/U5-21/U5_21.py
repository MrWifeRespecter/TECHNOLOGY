tal1=int(input("Ange första talet: "))
tal2=int(input("Ange andra talet: "))
if tal1<tal2:
    for i in range(tal1, tal2+1):
        print(i, end=(" "))
if tal2<tal1:
    for j in range(tal1, tal2-1, -1):
        print(j, end=(" "))
elif tal1==tal2:
    print(tal1)
input()