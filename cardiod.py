import turtle as tu
import math

R=200
n=2
n=n-1
tu.bgcolor("black")
tu.pensize(1)
tu.speed(0)

tu.color("black")
tu.circle(R)
tu.color("yellow")
tu.penup()

for i in range(360):
    tu.circle(R,i)
    angle=n*i*0.5
    length=2*R*math.sin(math.pi*angle/180)
    tu.left(angle)
    tu.pendown()
    tu.forward(length)
    tu.penup()
    tu.forward(-length)
    tu.right(angle)
    tu.circle(R,-i)

tu.hideturtle()
tu.done()