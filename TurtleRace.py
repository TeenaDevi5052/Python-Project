from turtle import Turtle,Screen
import random
race=False
screen=Screen()
screen.setup(width=500,height=400)
turtles=[]
user_bet=screen.textinput(title='Make your Bet',prompt='Which turtle will win the race? (enter a color): ')
colors=['red','blue','green','yellow','pink','purple','orange']
y_positions=[-70,-40,-10,20,50,80]
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=y_positions[i])
    turtles.append(new_turtle)

if user_bet:
    race=True
while race:
    for t in turtles:
        if t.xcor()>230:
            race=False
            win=t.pencolor()
            if win==user_bet:
                print(f"{t.pencolor()} won the game")
            else:
                print(f"You lose! {t.pencolor()} has won the game!")
        speed=random.randint(0,10)
        t.forward(speed)
screen.exitonclick()
