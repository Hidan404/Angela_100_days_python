from turtle import Screen, Turtle,colormode
import random

tela = Screen()
tela.title("Jogo da Cobra")
tela.bgcolor("black")
tela.setup(width=1200, height=900)



def corpo_cobra():
    cobra = []
    for i in range(3):
        cobra.append(Turtle())
        cobra[i].shape("turtle")
        cobra[i].color("white")
        cobra[i].penup()
        cobra[i].goto(-20 * i, 0)
    return cobra




















tela.exitonclick()