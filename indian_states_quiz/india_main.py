import pandas
import turtle

screen = turtle.Screen()
screen.title("INdian State Game")
screen.setup(width=650, height=650)

image = "india_blank_map.gif"
screen.addshape(image)
map_turtle = turtle.Turtle()
map_turtle.shape(image)

data = pandas.read_csv("india_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 29:
	answer_state = screen.textinput(title= f"{len(guessed_state)}/29 States are correct",
								  prompt="What's another state").title()
	
	if answer_state == "Exit":
		missing_states = []
		for state in all_states:
			if state not in guessed_state:
				missing_states.append(state)

		print(missing_states)
		break
	if answer_state in all_states:
		guessed_state.append(answer_state)
		state = data[data.state == answer_state].iloc[0]
		writer = turtle.Turtle()
		writer.hideturtle()
		writer.penup()
		writer.goto(state.x * 0.75, state.y * 0.75)
		writer.write(answer_state)
		



screen.exitonclick()
