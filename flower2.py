import turtle
def draw_square(few_turtle):
    for i in range(4):
        few_turtle.forward(200)
        few_turtle.right(90)
def draw_mosaique_art():
    window =turtle.Screen()
    window.bgcolor("black")

    mosaique=turtle.Turtle()
    mosaique.shape('circle')
    mosaique.speed('fastest')
    mosaique.shapesize(0.5,0.5)
    mosaique.color("red","purple")
    mosaique.begin_fill()

    for i in range (72):
        draw_square(mosaique)
        mosaique.right(5)
    mosaique.end_fill
    mosaique.forward(330)
    window.exitonclick()

draw_mosaique_art()
