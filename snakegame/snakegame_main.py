from turtle import Turtle,Screen
from snakegame_snake2 import Snake
from snakegame_food1 import Food
from snakegame_score1 import Score
import time

tim= Turtle()
tim.hideturtle()
tim.penup()
tim.color("white")

tim.goto(0, 0)

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake(screen)
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.125)
    snake.move()

    #dectecting collision
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.score_increase()

    #collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        tim.goto(0, 0)
        tim.write("GAME OVER!", align="center", font=("Arial",24,"normal"))
        screen.update()
        game_is_on = False

    #collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            tim.goto(0, 0)
            tim.write("GAME OVER!", align="center", font=("Arial",24,"normal"))
            screen.update()
            game_is_on = False


screen.exitonclick()