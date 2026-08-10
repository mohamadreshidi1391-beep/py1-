# Python program to draw a square
# using Turtle Programming
import turtle
skk = turtle.Turtle()
skk.pensize(3)
skk.shapesize(2,5,12)

# Change the color of both
skk.color("green", "blue")

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()