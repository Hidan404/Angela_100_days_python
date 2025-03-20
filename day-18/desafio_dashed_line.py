from turtle import Turtle, Screen

tartaruga = Turtle()

def dashed(n):
    for _ in range(n):
        tartaruga.forward(10)
        tartaruga.pencolor("green")
        tartaruga.penup()
        tartaruga.forward(10)
        tartaruga.pendown()

dashed(10)

tartaruga.penup()
tartaruga.goto(0, -150)
tartaruga.pendown()
               
def circulo():
    tartaruga.circle(100)
    tartaruga.pencolor("red")


circulo()


def penta():
    for _ in range(5):
        tartaruga.forward(100)
        tartaruga.right(72)
    tartaruga.pencolor("blue")

penta()

tartaruga = Screen()
tartaruga.exitonclick()