def nettopris(x):
    if x < 500:
        return(x)
    if x > 499:
        if x < 1000:
            return(x*0.98)
        if x > 999:
            return(x*0.95)
x=int(input("Hur stort är bruttobeloppet på din vara? "))
print("Din vara kostar", nettopris(x), "kr")
input()
