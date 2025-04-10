from turtle import Turtle
import random

class Comida(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))    
