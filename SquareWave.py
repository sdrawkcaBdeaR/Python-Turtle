import turtle as tu
import math

delta=0.1
scale=30
scaleh=5
X=300
Y=600
n=20
tu.penup()
tu.goto(-400,-100)
tu.pendown()

tu.bgcolor("black")
tu.color("white")
tu.speed(0)
for i in range(10000):
    x=i*delta
    deriv=0
    for j in range(n):
        deriv+=math.cos((2*j+1)*x)

    deriv=scaleh*deriv
    angle=math.atan(deriv)
    length=delta/math.cos(angle)
    tu.left(180*angle/math.pi)
    tu.forward(scale*length)
    tu.penup()
    tu.left(-180*angle/math.pi)
    tu.pendown()

tu.done() 