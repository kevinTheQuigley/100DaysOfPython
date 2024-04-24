import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import math as ma
#global
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_DISTANCE = 20.0
UPKEY = "w"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()


car_manager = CarManager()
car_manager.initialize_cars(SCREEN_HEIGHT,SCREEN_WIDTH)

player = Player()
scoreboard = Scoreboard()

game_is_on = True
leveler = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    print(MOVEMENT_DISTANCE)
    car_manager.move_cars(MOVEMENT_DISTANCE*leveler)
    screen.onkeypress(player.moveUp,UPKEY)
    player.detectFinish(scoreboard)
    car_manager.restart_y_position(SCREEN_WIDTH)
    scoreboard.setPosition(SCREEN_HEIGHT)
    leveler = scoreboard.display_score()
    game_is_on = player.detectCollision(car_manager,scoreboard)

screen.exitonclick()
