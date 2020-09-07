temp=-40
print("Celsius","\t","Farenheit")
while temp <= 40:
    farenheit=((32+temp*9)/5)
    print(temp,"\t",farenheit)
    temp+=1
input()