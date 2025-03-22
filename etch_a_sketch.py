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

def mover_left():
    turtle.shape("turtle")
    turtle.color("green")
    turtle.left(10)

def mover_right():
    turtle.shape("turtle")
    turtle.color("yellow")
    turtle.right(10)

def limpar():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

tela = Screen()
tela.listen()   
tela.onkey(mover_forward, "w")
tela.onkey(mover_backward, "q")
tela.onkey(mover_left, "a")
tela.onkey(mover_right, "d")
tela.onkey(limpar, "c")


tela.exitonclick()