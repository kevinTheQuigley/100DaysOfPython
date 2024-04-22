from turtle import Turtle,Screen
import time
from screenWriter import ScreenWriter
from ball import Ball
from paddle import HumanPaddleBat
from scoreBoard import Scoreboard

#Globals

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
GAME_ON = True
HAS_SCORED = False
DOWNKEY = "s"
UPKEY = "w"

ROBOTDOWNKEY = "g"
ROBOTUPKEY = "t"

screen = Screen()
screen.setup(width = SCREEN_WIDTH ,height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.listen()

screen.tracer(0)

screenWriter = ScreenWriter()
screenWriter.screenWalk(SCREEN_HEIGHT)

ball = Ball()

robotPaddleBat =HumanPaddleBat()
robotPaddleBat.reverseStartPaddle(SCREEN_WIDTH)

humanPaddleBat = HumanPaddleBat()
humanPaddleBat.startPaddle(SCREEN_WIDTH)

scoreBoardLeft = Scoreboard()
scoreBoardLeft.setPosition(-30,SCREEN_HEIGHT)

scoreBoardRight = Scoreboard()
scoreBoardRight.setPosition(30,SCREEN_HEIGHT)


while GAME_ON == True:
    HAS_SCORED = False 
    while HAS_SCORED == False:
        time.sleep(0.01)
        screen.update()
        ball.animate()
        ball.wallCollision(SCREEN_HEIGHT)
        ball.paddleCollision(humanPaddleBat.pieceList)
        ball.paddleCollision(robotPaddleBat.pieceList)
        screen.onkeypress(humanPaddleBat.up,UPKEY)
        screen.onkeypress(humanPaddleBat.down,DOWNKEY)
        screen.onkeypress(robotPaddleBat.up,ROBOTUPKEY)
        screen.onkeypress(robotPaddleBat.down,ROBOTDOWNKEY)
        if ball.detectLeftGoal(SCREEN_WIDTH):
            print("LeftGoal!")
            scoreBoardLeft.update_score()
            scoreBoardLeft.display_score()
        if ball.detectRightGoal(SCREEN_WIDTH):
            print("RightGoal!")
            scoreBoardRight.update_score()
            scoreBoardRight.display_score()




screen.exitonclick()



