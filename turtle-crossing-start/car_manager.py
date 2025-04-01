import random
from turtle import Turtle, Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.todos_carros = []
        self.velocidade = STARTING_MOVE_DISTANCE

    def carros_aleatorios(self):
         #dificil fazer jogo meu deus 
         if random.randint(1, 8) == 1: 
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250)) 
            new_car.setheading(180)  
            
            self.todos_carros.append(new_car)

    def mover_carro(self):
        for carros in self.todos_carros:
            carros.forward(self.velocidade) 

    def aumentar_velocidade(self):
        self.velocidade+= MOVE_INCREMENT     

    def resetar(self):
        self.todos_carros.clear()
        self.velocidade = STARTING_MOVE_DISTANCE