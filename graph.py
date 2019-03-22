import turtle


def draw_art():
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(100)

    for n in range(1, 37):
        draw_square(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(300)

    window.exitonclick()


def draw_square(turtle):
    for i in range(0, 4):
        turtle.forward(100)
        turtle.left((i % 2 + 1) * 90 - 45)


draw_art()
