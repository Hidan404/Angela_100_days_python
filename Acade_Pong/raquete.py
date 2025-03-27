from turtle import Turtle

class raquete(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        