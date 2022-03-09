from turtle import Turtle, Screen
from score import Score
from pad import Pad
from Divider import Draw_divider
from ball import Ball
import time

# Judge of the game
judge = Turtle()
judge.hideturtle()

# Setting up the screen of the game
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer()


# Creating the ping pong ball
ball = Ball(0, 0)

# Score is written on the canvas
score1 = Score(-50, 250)
score1.display()


score2 = Score(50, 250)
score2.display()


# Creating the 2 pads
pad1 = Pad(-360, 0)
pad2 = Pad(360, 0)

# Drawing the divider line
Draw_divider()

# Player movements
screen.listen()
screen.onkeypress(pad1.up, "w")
screen.onkeypress(pad1.down, "s")

screen.onkeypress(pad2.up, "Up")
screen.onkeypress(pad2.down, "Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #  If the ball is near the pad check if it hits the pad
    if ball.xcor() >320 or ball.xcor() < -320:
        # if (abs(ball.xcor() - pad2.xcor()) < 3 and abs(ball.ycor() - pad2.ycor()) < 3) or (abs(ball.xcor() - pad1.xcor()) < 3 and abs(ball.ycor() - pad1.ycor()) < 3):
        if ball.distance(pad2) < 50 and 360 >= ball.xcor() > 340 or ball.distance(pad1) < 50 and -360 >= ball.xcor() < -340:
            ball.bounce_x()

    # Movement of the ball in the game on hitting the top and bottom boundaries of screen
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()



    if ball.xcor() > 390:
        score1.update_score()
        ball.next_round()

    if ball.xcor() < -390:
        score2.update_score()
        ball.next_round()

    if score1.score - score2.score > 0 and score1.score >=3:
        judge.write("Player 1 wins", move=False, align="center", font=("Arial", 40, "normal"))
        game_on = False
    elif score1.score - score2.score < 0 and score2.score >= 3:
        judge.write("Player 2 wins", move=False, align="center", font=("Arial", 40, "normal"))
        game_on = False

screen.exitonclick()
