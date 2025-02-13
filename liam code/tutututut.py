import turtle, math

pen = turtle.Turtle()
pen.speed(10)
turtle.bgcolor("black") 
pen.pensize(2)
pen.color("white")

turtle.Screen()

pen.up()
pen.left(180)
pen.forward(200)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.down()

for j in range(300):
    pen.down()
    pen.forward(20)
    pen.left(10-j)