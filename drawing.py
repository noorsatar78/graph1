import turtle


ob = turtle.Turtle()
ob.speed(10)


def drawArt(d,angle):
    for i in range(1,100):
        ob.forward(d)
        ob.left(angle)
        d = d - 5
drawArt(200,140)


turtle.done()
