from turtle import Turtle, Screen, colormode
import random as rd

colormode(255)

tartaruga = Turtle()
tartaruga.speed("fastest")
tartaruga.pensize(10)
def cores():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    cores_escolhidas = (r, g, b)
    return cores_escolhidas

def random_walk(n):
    for _ in range(n):
        tartaruga.color(cores())
        tartaruga.forward(30)
        tartaruga.setheading(rd.choice([0, 90, 180, 270]))
        
random_walk(100)



screen = Screen()
screen.exitonclick()
