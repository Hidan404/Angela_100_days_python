from turtle import Turtle as t, Screen as s

tartaruga = t()

tartaruga.color("red")
tartaruga.shape("square")


def quadrado(n): 
    for _ in range(n):
        tartaruga.forward(100)
        tartaruga.left(90)


quadrado(4)




ecra = s()
ecra.exitonclick()
 