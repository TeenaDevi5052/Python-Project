from turtle import Turtle
STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    def at_finish(self):
        if self.ycor()>280:
            return True
        else:
            return False
    def start(self):
        self.goto(STARTING_POSITION)