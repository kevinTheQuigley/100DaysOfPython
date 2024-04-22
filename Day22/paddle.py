from turtle import Turtle

#globals    
PADDLELENGTH = 10
DOWN = 270
UP = 90
MOVEDISTANCE = 80

class PaddlePiece(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        #self.shapesize(5)
        #self.setheading(rd.randint(135,225))
        #self.setheading(80)


class HumanPaddleBat():

    def __init__(self):
        self.paddleLength = PADDLELENGTH
        self.pieceList = []
        #self.paddleLength = paddleLength
        for i in range(self.paddleLength):
            paddlePiece = PaddlePiece()
            self.pieceList.append(paddlePiece)

        self.head = self.pieceList[0]

    def up(self):
        self.head.setheading(UP)
        self.head.forward(MOVEDISTANCE)
        for i in range(len(self.pieceList[1:])):
            i+=1
            self.pieceList[i].goto(self.pieceList[i-1].xcor(),self.pieceList[i-1].ycor()+20)

    def down(self):
        self.head.setheading(DOWN)
        self.head.forward(MOVEDISTANCE)
        for i in range(len(self.pieceList[1:])):
            i+=1
            self.pieceList[i].goto(self.pieceList[i-1].xcor(),self.pieceList[i-1].ycor()+20)


    def keyInput(self,keys):
        return 0
        #Defines the input keys, the first goes up, and the second goes down
    def startPaddle(self,screen_width):
        # sets initial position
        print("setting initial position")
        for i in range(self.paddleLength):
            if i ==0:
                self.head.goto(screen_width/2,0)
            else:
                self.pieceList[i].goto(self.pieceList[i-1].xcor(),self.pieceList[i-1].ycor()+20)

    def reverseStartPaddle(self,screen_width):
        print("setting initial reverse position")
        # sets initial position on other side of the screen
        for i in range(self.paddleLength):
            if i ==0:
                self.head.goto(-screen_width/2,0)
            else:
                self.pieceList[i].goto(self.pieceList[i-1].xcor(),self.pieceList[i-1].ycor()+20)


