import turtle as tu

wn=tu.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball")

tu.color("white")
tu.speed(0)
tu.penup()
tu.goto(-200,-20)
tu.pendown()
tu.forward(400)
tu.hideturtle()

ball=tu.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0,300)
ball.dy=-2
ball.dx=5
gravity=0.4
dfactor=1

while True:
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    if ball.ycor()<0:
        ball.dy*=-dfactor
    if ball.xcor()>200:
        ball.dx*=-1
    if ball.xcor()<-200:
        ball.dx*=-1        
    ball.dy-=gravity    
    
    if ball.ycor()<-10:
        break
    
wn.mainloop()