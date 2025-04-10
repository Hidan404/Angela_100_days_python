from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.cobra = []
        self.direcao = "direita"
        self.criando_cobra()

    def criando_cobra(self):
        for i in range(3):
            segmento = Turtle("square")
            segmento.color("red")
            segmento.penup()
            segmento.goto(-20 * i, 0)
            self.cobra.append(segmento)

    def mover_cobra(self):
        for i in range(len(self.cobra) - 1, 0, -1):
            x = self.cobra[i - 1].xcor()
            y = self.cobra[i - 1].ycor()
            self.cobra[i].goto(x, y)

        if self.direcao == "cima":
            self.cobra[0].setheading(90)
        elif self.direcao == "baixo":
            self.cobra[0].setheading(270)
        elif self.direcao == "esquerda":
            self.cobra[0].setheading(180)
        elif self.direcao == "direita":
            self.cobra[0].setheading(0)

        self.cobra[0].forward(20)

    def set_direcao(self, nova_direcao):
        direcoes_opostas = {"cima": "baixo", "baixo": "cima", "esquerda": "direita", "direita": "esquerda"}
        if nova_direcao != direcoes_opostas.get(self.direcao):
            self.direcao = nova_direcao

    def verificar_colisao_borda(self, largura, altura):
        cabeca = self.cobra[0]
        x, y = cabeca.xcor(), cabeca.ycor()
        margem = 10  # ou 20, dependendo da precisão desejada

        if x < -largura / 2 + margem or x > largura / 2 - margem or y < -altura / 2 + margem or y > altura / 2 - margem:
            return True
        return False
        

    def adicionar_segmento(self):
        ultimo_segmento = self.cobra[-1]
        novo_segmento = Turtle("square")
        novo_segmento.color("white")
        novo_segmento.penup()
        novo_segmento.goto(ultimo_segmento.xcor(), ultimo_segmento.ycor())
        self.cobra.append(novo_segmento)

    def colisao_cauda(self):
        cabeca = self.cobra[0]
        for segmento in self.cobra[1:]:
            if cabeca.distance(segmento) < 10:
                return True
        return False