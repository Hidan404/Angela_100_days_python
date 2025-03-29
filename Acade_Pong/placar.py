from turtle import Turtle

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.pontos_direita = 0
        self.pontos_esquerda = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.atualizar_placar()

    def atualizar_placar(self):
        """Limpa e redesenha o placar atualizado."""
        self.clear()
        self.goto(-100, 400)
        self.write(self.pontos_esquerda, align="center", font=("Courier", 24, "italic"))
        self.goto(100, 400)
        self.write(self.pontos_direita, align="center", font=("Courier", 24, "italic"))

    def ponto_esquerda(self):
        """Adiciona um ponto ao jogador da esquerda e atualiza o placar."""
        self.pontos_esquerda += 1
        self.atualizar_placar()

    def ponto_direita(self):
        """Adiciona um ponto ao jogador da direita e atualiza o placar."""
        self.pontos_direita += 1
        self.atualizar_placar()

    def vencedor_dez_pontos(self):
        """Exibe o vencedor no centro da tela se algum jogador atingir 10 pontos."""
        if self.pontos_esquerda >= 10 or self.pontos_direita >= 10:
            self.clear()
            if self.pontos_esquerda > self.pontos_direita:
                vencedor_texto = "Jogador da Esquerda Venceu!"
                
            else:
                vencedor_texto = "Jogador da Direita Venceu!"
            self.goto(0, 0)
            self.write(vencedor_texto, align="center", font=("Courier", 36, "bold"))

            return True
   
       