from turtle import *
import random
#or import turtle as t so now we can use it as t (example:t.Turtle())
tinny=Turtle()
tinny.shape("turtle")#changes to turtle shape
colors=['red','blue','green','yellow','aqua','pink','black','wheat']
def draw_shape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tinny.forward(100)
        tinny.right(angle)
for shape in range(3,11):
    tinny.color(random.choice(colors))
    draw_shape(shape)
screen=Screen()
screen.exitonclick()
