from turtle import Turtle


class Score(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x,y)

    def display(self):
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 40, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 40, "normal"))
