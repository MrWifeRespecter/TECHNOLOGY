mening=str(input("vad är din mening som du vill göra om till rövarspråk? "))
temp=mening.lower()
konsonanter="bcdfghjklmnpqrstvwxz"
mening2=""
j=0
for i in range(len(temp)):
    bokstav=temp[j]
    if bokstav in konsonanter:
        mening2+=bokstav+"o"+bokstav
    if bokstav not in konsonanter:
        mening2+=bokstav
    j+=1
mening2=mening2.capitalize()
print(mening2)
input()