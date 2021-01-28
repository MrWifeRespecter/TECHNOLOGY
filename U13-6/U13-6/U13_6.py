from turtle import *
#jag vet inte hur vi ska kunna lösa den här uppgiften bara med det som vi lärt oss. Jag tog hjälp från internet för annars så skulle jag aldrig bli klar. Jag förstår inte vad min kod gör, men den funkar. 
def snowflake(lengthSide, levels): 
    if levels == 0: 
        forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
    right(120) 
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 

if __name__ == "__main__": 
    speed(0)                    
    length = 300.0            
    penup()                      
    backward(length/2.0) 
    pendown()            
    for i in range(3):     
        snowflake(length, 4) 
        right(120) 
    mainloop()   
input()
#jag skulle inte kunna förklara vad koden gör 