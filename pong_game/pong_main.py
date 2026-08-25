from turtle import Screen, Turtle
from pong_paddle import Paddle
from pong_ball import Ball
from pong_scoreboard import Scoreboard
import time

tim = Turtle()
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("pong game!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball((0,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"o")
screen.onkey(r_paddle.go_down, "k")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls up and down
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with r_paddle
    elif ball.distance(r_paddle) < 30 and ball.xcor() > 310:
        ball.bounce_x()
        scoreboard.r_point()

    # detect collision with l_paddle
    elif ball.distance(l_paddle) < 30 and ball.xcor() < -310:
        ball.bounce_x()
        scoreboard.l_point()

    elif ball.xcor() >= 400: 
        ball.reset_position()
        scoreboard.l_point()
        
    elif ball.xcor() <= -400:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()