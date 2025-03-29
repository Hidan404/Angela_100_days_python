from turtle import Turtle, Screen
import time

class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 2
        self.y_move = 2
        self.velocidade_inicial = 2 

    def move(self):
        nova_x = self.xcor() + self.x_move
        nova_y = self.ycor() + self.y_move
        self.goto(nova_x, nova_y)

    def ricochete_y(self):
        self.y_move *= -1  

    def ricochete_x(self):
        self.x_move*= -1    


    def resetar_posicao(self):
        self.goto(0, 0)
        self.x_move = self.velocidade * random.choice([1, -1])  # Direção aleatória
        self.y_move = self.velocidade * random.choice([1, -1])
        time.sleep(0.5)