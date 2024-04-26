from turtle import Turtle


class StateHeader(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 1,stretch_wid = 1)
        self.score = 0 

    def display_state(self,state):
        print(state)
        self.clear()
        self.write(f"{state} ",align = "center", font =("Arial",24,"normal") )

    def setPosition(self,state,xParam,yParam):
        self.display_state(state)
        self.goto(xParam,yParam)
