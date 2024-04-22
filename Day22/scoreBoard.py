from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 5,stretch_wid = 30)
        self.score = 0 

    def setPosition(self,position,screenHeight):
        self.goto(position,screenHeight/2-30)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.score} ",  align="center", font =("Arial",24,"normal") )


    def update_score(self):
        self.score +=1
        self.display_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",  align="center", font =("Arial",24,"normal"))




        
