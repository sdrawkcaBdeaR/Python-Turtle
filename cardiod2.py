import turtle

R=100
r=100
iterations=180
mul=360/iterations

def car(theta,m,n):
    turtle.penup()
    turtle.home()
    turtle.circle(R,theta)
    turtle.left(180)
    turtle.circle(r,(R/r)*theta)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.goto(m,n)
    turtle.pendown()
    return x,y

x=0
y=0
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2)
turtle.bgcolor("black")
turtle.color("white")
turtle.circle(R)

turtle.color("yellow")

for i in range(iterations):
    x,y=car(i*mul+1,x,y)
    turtle.goto(x,y)

turtle.done()