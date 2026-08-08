from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align= ALIGMENT,font=FONT)

    def score_increase(self):
        self.penup()
        self.clear()
        self.goto(0,260)
        self.score += 1
        self.update_score()
        self.getscreen().update()
