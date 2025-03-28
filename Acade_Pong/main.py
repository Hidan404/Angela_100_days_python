from turtle import Screen
from raquete import Raquete 

tela = Screen()
tela.bgcolor("black")
tela.setup(1200, 920)
tela.title("Pong")
tela.tracer(0)

tela.update()
raquete2 = Raquete(tela)



tela.exitonclick()
