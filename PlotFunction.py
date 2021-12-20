import turtle as tu
import math

delta=0.1
scale=30

for i in range(10000):
    x=i*delta
    deriv=math.cos(x)
    angle=math.atan(deriv)
    length=delta/math.cos(angle)
    tu.left(180*angle/math.pi)
    tu.forward(scale*length)
    tu.penup()
    tu.left(-180*angle/math.pi)
    tu.pendown()

tu.done()  
