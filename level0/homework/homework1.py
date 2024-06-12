from turtle import *
speed(3)

#we want to paint a house

#steo 1 draw a square
color("green")
width(7)
forward(200)
left(90)


forward(200)


left(90)
forward(200)

left(90)
forward(200)
#end of square

#drawing a door

left(90)

forward(80)
color("dark blue")

left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
#end of door

penup()
goto(200,200)

pendown()
color("dark green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()
