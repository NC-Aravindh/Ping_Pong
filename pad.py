from turtle import Turtle


class Pad(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("Black")
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)


    def up(self):

        self.goto(self.xcor(),self.ycor()+10)

    def down(self):

        self.goto(self.xcor(), self.ycor() - 10)
