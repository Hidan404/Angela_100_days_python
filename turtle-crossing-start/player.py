from turtle import Turtle , Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
        
        

    def cima(self):
        #new_y = self.ycor() + MOVE_DISTANCE
        #self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)


