import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
carros = CarManager()

score = Scoreboard()
jogador = Player()
screen.listen()
screen.onkey(jogador.cima, "Up")

def jogar():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        carros.carros_aleatorios()
        carros.mover_carro()

        for carro in carros.todos_carros:
            if carro.distance(jogador) < 20:
                score.fim_de_jogo()
                game_is_on = False
            

        if jogador.linha_chegada():
            jogador.linha_de_partida()
            carros.aumentar_velocidade()
            score.increase_level()

jogar()

screen.exitonclick()   
