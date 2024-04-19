#Turtle OOP
import random as rd
from turtle import Turtle
from turtle import Screen

from colorgram import extract

tim = Turtle()
tim.shape("turtle")
tim.color("green")

#for i in range(2,14):
#    if i <8:
#        tup = (0.5-(i/7-0.5),0.5+(i/7-0.5),0)
#    else:
#        tup = (0, 0.5-(i/14-0.5), 0.5+(i/14-0.5))
#    tim.pencolor(tup)
#
#
#    for j in range(i):
#        tim.forward(100)
#        tim.left(360/i)


#for i in range (500):
#    rdInt = rd.randint(0,3)
#    tim.pensize(15)
#    tim.speed("fastest")
#    tup = (rd.randint(0,100)/100,rd.randint(0,100)/100,rd.randint(0,100)/100)
#    tim.pencolor(tup)
#    tim.forward(20)
#    tim.left(360*rdInt/4)



#for i in range(50):
#    rdInt = rd.randint(0,3)
#    tim.pensize(2)
#    tim.speed("fastest")
#    tup = (rd.randint(0,100)/100,rd.randint(0,100)/100,rd.randint(0,100)/100)
#    tim.pencolor(tup)
#    tim.left(360/50)
#    tim.circle(100)


#extract("image.jpg",20)
screen = Screen()
colors = extract("C:/Users/kevin/OneDrive/Desktop/100DaysOfPython/Day18/image.jpg",10)
screen.colormode(255)
cList = []
for color in colors:
    r = int(color.rgb.r)
    g = int(color.rgb.g)
    b = int(color.rgb.b)
    cList.append((r,g,b))
print(cList)

tim.speed("fastest")
for i in range(20):   
    for i in range(20):
        tup = rd.choice(cList)
        tim.pencolor(tup)
        tim.dot(10)
        tim.penup()
        tim.forward(20)
        tim.pendown()
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(400)
    tim.left(180)







print(colors[0].rgb)
screen.exitonclick()