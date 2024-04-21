from turtle import Turtle,Screen
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("De burst Snake Game")
screen.listen()
# Directions
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0

class Snake:
    pos1= [0,0]
    segments = []
    def __init__(self):
        for i in range(3):
            snake = Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            #snake.shapesize(1,1)
            snake.goto(self.pos1)
            self.pos1[0]-=20
            print(snake.shapesize())
            self.segments.append(snake)
        
        self.head = self.segments[0]

    def animate(self):
        self.segmentsOldPos = []
        for i in range(0,len(self.segments)):
            if self.head.distance( self.segments[i])<10 and not i == 0:
                game_is_on =False
                scoreboard.game_over()
            print(i)
            snake = self.segments[i]
            self.segmentsOldPos.append(snake.position())
            if snake == self.segments[0]:
                snake.forward(20)
            else:
                #print(segments[i-1].position())
                self.segments[i].goto(self.segmentsOldPos[i-1])
                #print(segments[i].position())
    def turnLeft(self):
        self.segments[0].left(90)

    def turnRight(self):
        self.segments[0].right(90)
    
    def up(self):
        if (not self.head.heading() == DOWN):
            self.head.setheading(UP)

    def down(self):
        if (not self.head.heading() == UP):
            self.head.setheading(DOWN)

    def left(self):
        if (not self.head.heading() == RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (not self.head.heading() == LEFT):
            self.head.setheading(RIGHT)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segmentsOldPos[-1])
        self.segments.append(new_segment)
        
    def add_segment(self):
        self.extend()


screen.tracer(0)
snake=Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on =True
j = 0
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

score = 0
while game_is_on ==True:
    #writeStr = f"Score {score}"
    #snake.head.write(writeStr,move = True,align = "center")
    snake.animate()

    #screen.onkey(snake.turnRight,"d")
    #screen.onkey(snake.turnLeft,"a")
    j+=1
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) <15:
        print("nom ")

        food.refresh()
        scoreboard.update_score()
        score+=1
        snake.add_segment()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()