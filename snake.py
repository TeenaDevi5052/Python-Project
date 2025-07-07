from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for pos in POSITIONS:
            self.add_seg(pos)
    def move(self):
        for segnum in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segnum - 1].xcor()
            new_y = self.segment[segnum - 1].ycor()
            self.segment[segnum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def extend(self):
        self.add_seg(self.segment[-1].position())
    def add_seg(self,pos):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.segment.append(new_turtle)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
