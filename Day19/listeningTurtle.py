from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Welcome to turtle racing 2024.What's your bet? Enter a color: ")
print(user_bet)

colors = ["red","purple","orange","yellow","green","blue"]

startingPosition = [-180,-125]
turtleList = []



for color in  colors:
    newTurtle = Turtle()
    newTurtle.color(color)
    newTurtle.shape("turtle")
    newTurtle.penup()
    newTurtle.goto(x = startingPosition[0],y = startingPosition[1])
    startingPosition[1] = startingPosition[1]+50
    turtleList.append(newTurtle)

gameOn = True

while gameOn:
    for turtle in turtleList:
        turtle.forward(randint(10,20))
        if turtle.position()[0]>150:
            gameOn = False
            winColor = turtle.color()

if winColor == user_bet:
    print("You won")
else:
    print("You loose")
         
    

    





screen.exitonclick()