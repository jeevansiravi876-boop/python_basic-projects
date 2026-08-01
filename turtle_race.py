from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "make ur bet!!!" ,prompt="which turtle will win the race? Enter your color: ").lower()
print(user_bet)
color_set = ["Red", "Blue", "Green", "Purple", "black"]
y_positions = [-60, -30, 0, 30, 60]

all_turtle = []


for turtle_index in range(len(color_set)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_set[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"you lost the winner is {winning_color} turtle")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
