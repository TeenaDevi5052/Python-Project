from turtle import Screen,Turtle
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
scoreboard=ScoreBoard()
food=Food()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on=False
        scoreboard.game_over()
    for segment in snake.segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()
screen.exitonclick()
