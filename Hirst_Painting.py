import colorgram
import turtle as t
import random
#rgb_colors=[]
#colors=colorgram.extract("image.jpg.png",48)
#for color in colors:
   # r=color.rgb.r
   # g=color.rgb.g
   # b=color.rgb.b
  #  new_color=(r,g,b)
 #   rgb_colors.append(new_color)
#print(rgb_colors)
color_list=[(254, 253, 251), (253, 250, 252), (98, 181, 238), (248, 37, 59), (201, 236, 248), (41, 83, 190), (207, 70, 6), (244, 222, 102), (246, 252, 248), (36, 47, 172), (243, 124, 166), (207, 15, 36), (115, 233, 181), (68, 23, 4), (28, 146, 29), (191, 20, 15), (243, 114, 3), (16, 61, 25), (80, 169, 47), (249, 61, 9), (184, 32, 106), (10, 172, 206), (253, 206, 0), (235, 131, 52), (13, 90, 17), (244, 12, 28), (139, 174, 133), (111, 213, 245), (153, 185, 235), (253, 5, 3), (230, 166, 181), (82, 116, 184), (236, 171, 158), (91, 25, 28), (103, 77, 13)]
tim=t.Turtle()
tim.hideturtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()
tim.color("pink")
tim.shape("turtle")
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dot=100
for dot_count in range(1,num_of_dot+1):
    tim.dot(20,random.choice(color_list))

    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen=t.Screen()
screen.exitonclick()