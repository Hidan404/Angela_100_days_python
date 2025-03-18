import turtle

tartarua = turtle.Turtle()

tartarua.shape("turtle")
tartarua.color("blue")

tela = turtle.Screen()
tela.bgcolor("black")

tela.title("Tartaruga")
tela.setup(width=800, height=600)
tartarua.forward(100)
tartarua.right(90)
tartarua.forward(150)
tela.exitonclick()