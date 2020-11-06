def maximum(x, y):
    if x<y:
        return(y)
    if y<x:
        return(x)
x=float(input("Skriv in tal 1: "))
y=float(input("Skriv in tal 2: "))
print(maximum(x, y))
input()