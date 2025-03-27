from turtle import Turtle, Screen
from raquete import raquete

tela = Screen()
tela.bgcolor("black")
tela.setup(1200,920)
tela.title("Pong")



raquete2 = raquete()
raquete2.goto(350, 0)



tela.exitonclick()