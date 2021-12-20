import turtle as tu

def star(i):
    if i>10:
        for n in range(5):
            tu.forward(i)
            star(i/5)
            tu.right(144)

    return 0

star(300)    
tu.hideturtle()
tu.done()
