from turtle import Screen
import time
from scoreboard_cross import Scoreboard
from car_manager import CarManager
from player import Player
screen=Screen()
screen.setup(600,600)
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()
screen.listen()
screen.onkey(player.go_up,"Up")
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_car:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_on=False
    if player.at_finish():
        player.start()
        car_manager.level_up()
        scoreboard.increase()

screen.exitonclick()