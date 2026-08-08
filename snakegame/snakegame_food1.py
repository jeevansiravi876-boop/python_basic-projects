from turtle import Turtle
import random
food_size = [(0.5,0.5),(0.7,0.7),(0.9,0.9),(1.1,1.1),(1.3,1.3)]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(*random.choice(food_size))
        self.refresh()
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        self.shapesize(*random.choice(food_size))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)