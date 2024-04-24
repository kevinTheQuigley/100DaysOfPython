STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
    
    def moveUp(self):
        self.forward(MOVE_DISTANCE)

    def detectFinish(self,scoreboard):
        if self.ycor() >FINISH_LINE_Y:
            print("we go to the end")
            self.goto(STARTING_POSITION)
            scoreboard.update_score()
    
    def detectCollision(self,carManager,scoreboard):
        for car in carManager.car_list:
            if (car.xcor() +30) >self.xcor() and (car.xcor()-30)<self.xcor():
                if (car.ycor() +20) > self.ycor() and car.ycor() -20 < self.ycor():
                    print("Collision detected")
                    self.goto(STARTING_POSITION)
                    scoreboard.game_over()
                    return False
        return True

