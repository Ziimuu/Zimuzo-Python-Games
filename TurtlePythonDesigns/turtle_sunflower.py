import turtle
import math

zimu = turtle.getscreen()
zimu = turtle.Turtle()
zimu.color("red", "yellow")
zimu.bgcolor('black')
zimu.speed(10)

zimu.begin_fill()
for i in range(100):
    zimu.forward(300)
    zimu.left(168.5)

zimu.end_fill()

turtle.done()