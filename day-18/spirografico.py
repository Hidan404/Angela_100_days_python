from turtle import Turtle, Screen, colormode
import random as rd


def spirografico(turtle, n):
    for _ in range(int(360/n)):
        turtle.circle(100)
        turtle.right(n)
        turtle.pencolor(cores())


colormode(255)

def cores():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    cores_escolhidas = (r, g, b)
    return cores_escolhidas

tartaruga = Turtle()    
tartaruga.speed("fastest")
tartaruga.pensize(4)
spirografico(tartaruga, 36)

screen = Screen()
screen.exitonclick()