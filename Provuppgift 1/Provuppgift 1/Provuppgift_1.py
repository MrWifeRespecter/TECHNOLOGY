from turtle import *
speed(0)
ht()
#blå bakgrund
color("blue")
begin_fill()
fd(200)
right(90)
fd(120)
right(90)
fd(200)
right(90)
fd(120)
end_fill()

#Första sträcket
color("yellow")
begin_fill()
pu()
bk(50)
right(90)
pd()
fd(200)
right(90)
fd(20)
right(90)
fd(200)
right(90)
fd(20)
end_fill()

#andra sträcket
pu()
bk(70)
right(90)
fd(50)
begin_fill()
pd()
fd(20)
left(90)
fd(120)
left(90)
fd(20)
left(90)
fd(120)
left(90)
fd(20)
end_fill()
input()