#temp=10
#blank=""
#for i in range(1,11):
#    for j in range(0,temp):
#        print(blank, j, end=" ")
#        for k in range(0,j):
#            blank+=" "  
#    print("\n")
#    temp=10-i










temp=10
blanksteg=" "
for x in range(1,11):
        print(blanksteg, end="")
        blanksteg+="  "
        for j in range(0,temp):
            print(j, end=(" "))
            temp=10-x
        print("")
input()
    