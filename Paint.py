from turtle import Turtle,Screen
tim=Turtle()

screen=Screen()
def move_forward():
    tim.forward(20)
def move_backward():
    tim.backward(20)
def right():
    tim.right(10)
def left():
    tim.left(10)
def clear():
    screen.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(move_forward,"f")
screen.onkey(move_backward,"b")
screen.onkey(left,"l")
screen.onkey(right,"r")
screen.onkey(clear,"c")

screen.exitonclick()
