from turtle import Turtle,Screen
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5)
        self.shapesize(stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        rx = rd.randint(-28,28)*10
        ry = rd.randint(-28,28)*10
        self.goto(rx,ry)

    def refresh(self):
        rx = rd.randint(-28,28)*10
        ry = rd.randint(-28,28)*10
        self.goto(rx,ry)

