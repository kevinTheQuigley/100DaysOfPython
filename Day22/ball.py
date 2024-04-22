from turtle import Turtle
import random as rd

DETECTIONDISTANCE  =20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        #self.shapesize(5)
        self.goto(0,0)
        self.setheading(rd.randint(135,225))
        #self.setheading(80)

    def animate(self):
        self.forward(10)


    
    def wallCollision(self,screen_height):
        if self.ycor() > (screen_height -10)/2:
            if self.heading() <90:
                self.setheading(360 - self.heading())
            elif self.heading()> 90 :
                self.setheading(360 - self.heading())

        if self.ycor() < -(screen_height - 10)/2:
            if self.heading() <270:
                self.setheading(360 - self.heading())
            elif self.heading()> 270 :
                self.setheading(360 - self.heading())
    
    def paddleCollision(self,pieceList):
        for piece in pieceList:
            if self.distance(piece) <DETECTIONDISTANCE:
                if self.heading() >180:
                    self.setheading(540 - self.heading())
                if self.heading() <180:
                    self.setheading(180 - self.heading())

    def detectRightGoal(self,screen_width):
        if self.xcor() > (screen_width -10)/2:
            self.goto(0,0)
            self.setheading(rd.randint(135,225))
            return True

    def detectLeftGoal(self,screen_width):
        if self.xcor() < -(screen_width -10)/2:
            self.goto(0,0)
            self.setheading(rd.randint(0,45))
            return True



