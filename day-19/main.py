from turtle import Turtle, Screen, colormode
import random as rd


turtle = Turtle()

def mover_forward():
    turtle.shape("turtle")
    turtle.color("red")
    turtle.forward(10)
def mover_backward():
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.backward(10)
tela = Screen()
tela.listen()


tela.onkey(mover_forward, "w")
tela.onkey(mover_backward, "q")
tela.exitonclick()