from turtle import *


#we want to paint a house

#setp 1: draw a square

width(5) #sisqe
speed(10)
color("purple")
begin_fill()
forward(200)
left(90) #Radius/Gradusi

forward(200)
left(90)

forward(200)
left(90) #Radius/Gradusi

forward(200)
left(90)
end_fill()

forward(70)
color("yellow")
begin_fill
left(90)
forward(120)   #height
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(0, 100)
pendown()

right(240)
penup()
forward(15)
pendown()

color("blue")
begin_fill()
forward(35)
right(90)

forward(35)
right(90)

forward(35)
right(90)

forward(35)
right(90)
end_fill()


penup()
goto(200, 100)
right(180)
forward(10)
pendown()

begin_fill()
forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)
end_fill()

penup()
goto(0, 0)

exitonclick()

