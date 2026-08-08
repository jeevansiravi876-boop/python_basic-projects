from turtle import Screen, Turtle
COORDINATES = [(-60,0), (-40,0), (-20,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.screen = Screen()
        self.screen.listen()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")
        self.screen.onkey(self.left, "a")
        self.screen.onkey(self.right, "d")


    def create_snake(self):
        for index, position in enumerate(COORDINATES):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

            color = "red" if index == 0 else "green"
            new_segment.color(color)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def run(self):
        self.screen.mainloop()

