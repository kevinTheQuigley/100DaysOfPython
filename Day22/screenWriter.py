from turtle import Turtle

class ScreenWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.pensize(5)

    def screenWalk(self,screen_height):
        self.goto(0,-screen_height)
        self.setheading(90)
        for i in range(int(screen_height/20)+1):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)

