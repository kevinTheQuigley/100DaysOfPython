from turtle import Turtle

FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 5,stretch_wid = 30)
        self.score = 1

    def setPosition(self,screenHeight):
        self.goto(-40,screenHeight/2-10)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level:{self.score} ",  align="center", font =("Arial",24,"normal") )
        return(self.score)


    def update_score(self):
        self.score +=1
        self.display_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",  align="center", font =("Arial",24,"normal"))




        