def maximum(x, y, z):
    if x<y:
        if z<y:
            return(y)
    if y<x:
        if z<x:
            return(x)
    if x<z:
        if y<z:
            return(z)
x=float(input("Skriv in tal 1: "))
y=float(input("Skriv in tal 2: "))
z=float(input("Skriv in tal 3: "))
print(maximum(x, y, z))
input()