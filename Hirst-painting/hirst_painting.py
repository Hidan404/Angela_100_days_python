import random
import colorgram as c
from turtle import Turtle, Screen, colormode

cores = c.extract("Hirst-painting/198991.png", 10)

cores_rgb = [tuple(cor.rgb) for cor in cores]
print(cores_rgb)

t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()


t.goto(-200, 200)

colormode(255)

for linha in range(10):
    for coluna in range(10):
        t.dot(20, random.choice(cores_rgb))
        t.forward(50)
    t.backward(500)
    t.right(90)
    t.forward(30) 
    t.left(90)    


tela = Screen()
tela.exitonclick()     

