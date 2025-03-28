from turtle import Turtle, Screen

class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 2
        self.y_move = 2

    def move(self):
        nova_x = self.xcor() + self.x_move
        nova_y = self.ycor() + self.y_move
        self.goto(nova_x, nova_y)

    def ricochete(self):
        self.y_move *= -1     
