import time
from turtle import Turtle, Screen
from turtle_player import Player
from turtle_car_manager import CarManager
from turtle_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Turtle()
tim.hideturtle()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            
            tim.write("GAME OVER!", align="center", font=("Arial",24,"normal"))
            screen.update()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score_inc()

screen.exitonclick()