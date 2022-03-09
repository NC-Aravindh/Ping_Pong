from turtle import Turtle

def Draw_divider():
    divider = Turtle()
    divider.hideturtle()
    divider.penup()
    divider.goto(0, 310)
    divider.right(90)
    divider.width(5)
    for i in range(30):
        divider.forward(10)
        divider.up()
        divider.forward(10)
        divider.down()
