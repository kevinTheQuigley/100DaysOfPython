from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_NUMBER = 40
CAR_SPACING_Y = 20
CAR_SPACING_X = 100
PERCENTAGE_CARS_ON_SCREEN = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(rd.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)


class CarManager:
    
    def __init__(self):
        self.car_list = []
        for i in range(CAR_NUMBER):
            new_car = Car()
            self.car_list.append(new_car)

    def initialize_cars(self,screen_height,screen_width):
        for car in self.car_list:
            car_x_initial_position = rd.randint(0,(100/PERCENTAGE_CARS_ON_SCREEN)*screen_width/20)*20
            car_y_initial_position = rd.randint(0,screen_height/20)*18 - screen_height/2 +40
            car.goto(x = car_x_initial_position, y = car_y_initial_position)

    def restart_y_position(self,screen_width):
            for car in self.car_list:
                if car.xcor() < -screen_width/2:
                    car.goto((100/PERCENTAGE_CARS_ON_SCREEN*screen_width),car.ycor())

    
    def move_cars(self,movement_distance):
        for car in self.car_list:
            car.goto(car.xcor()-movement_distance,car.ycor())

