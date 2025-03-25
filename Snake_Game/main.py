from turtle import Screen, Turtle, colormode
import random

tela = Screen()
tela.title("Jogo da Cobra")
tela.bgcolor("black")
tela.setup(width=1200, height=900)

def corpo_cobra():
    cobra = []
    for i in range(3):
        cobra.append(Turtle())
        cobra[i].shape("square")
        cobra[i].color("white")
        cobra[i].penup()
        cobra[i].goto(-20 * i, 0)
    return cobra

cobra = corpo_cobra()

def mover_cobra():
    for i in range(len(cobra) - 1, 0, -1):
        new_x = cobra[i - 1].xcor()
        new_y = cobra[i - 1].ycor()
        cobra[i].goto(new_x, new_y)
    cobra[0].forward(20)
    tela.update()
    tela.ontimer(mover_cobra, 100)

mover_cobra()

tela.listen()
tela.exitonclick()