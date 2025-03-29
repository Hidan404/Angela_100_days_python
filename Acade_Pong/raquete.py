from turtle import Turtle

class Raquete(Turtle):
    def __init__(self, tela, posicao, tecla_baixo, tecla_cima):
        super().__init__()
        self.shape("square")
        self.color("#00FF00")
        self.penup()
        self.goto(posicao)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.tela = tela  # Referência à tela passada pelo arquivo principal

        # Configura a escuta de eventos para mover a raquete
        self.tela.listen()
        self.tela.onkey(self.cima, tecla_cima)
        self.tela.onkey(self.baixo, tecla_baixo)

    def cima(self):
        nova_y = self.ycor() + 30
        self.goto(self.xcor(), nova_y)

    def baixo(self):
        nova_y = self.ycor() - 30
        self.goto(self.xcor(), nova_y)
