
for i in range(1,10):
    for j in range(1,10):
        x=j*i
        if x<10:
            print("   ",x, end=(""))
        else:
            print("  ",x, end=(""))
    print("\n")
input()