from turtle import Turtle

class Raquete(Turtle):
    def __init__(self, tela):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(410, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.tela = tela  # Referência à tela passada pelo arquivo principal

        # Configura a escuta de eventos para mover a raquete
        self.tela.listen()
        self.tela.onkey(self.cima, "Up")

    def cima(self):
        nova_y = self.ycor() + 20
        self.goto(self.xcor(), nova_y)
