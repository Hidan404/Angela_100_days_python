from turtle import Turtle
import time
import random

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
        self.velocidade_atual = self.velocidade_inicial
        

    def move(self):
        nova_x = self.xcor() + self.x_move
        nova_y = self.ycor() + self.y_move
        self.goto(nova_x, nova_y)

    def ricochete_y(self):
        self.y_move *= -1  

    def ricochete_x(self):
        self.x_move *= -1   
        self.aumentar_velocidade() 

    def resetar_posicao(self):
        self.hideturtle()  # Esconde a bola antes de reposicionar
        time.sleep(1)  # Espera 1 segundo antes de recomeçar
        self.goto(0, 0)
        self.showturtle()  # Exibe a bola novamente no centro
        self.velocidade_atual = self.velocidade_inicial
        self.x_move = self.velocidade_inicial * random.choice([1, -1])  
        self.y_move = self.velocidade_inicial * random.choice([1, -1])

    def aumentar_velocidade(self):
        """Aumenta a velocidade da bola gradativamente."""
        self.velocidade_atual *= 1.1  # 🔹 Aumenta a velocidade em 10%
        self.x_move = self.x_move / abs(self.x_move) * self.velocidade_atual
        self.y_move = self.y_move / abs(self.y_move) * self.velocidade_atual