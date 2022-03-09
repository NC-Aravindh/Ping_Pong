from turtle import Turtle


class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("Black")
        self.penup()
        self.shape("circle")
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.01
        self.goto(x,y)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def next_round(self):
        self.goto(0, 0)
        self.bounce_x()

    def game_stop(self):
        self.goto(50,50)
        self.move_speed(0)
