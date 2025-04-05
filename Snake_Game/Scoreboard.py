import turtle

class Score_board:
    def __init__(self):
        self.score = 0
        self.escrita = turtle.Turtle()
        self.escrita.penup()
        self.escrita.hideturtle()
        self.escrita.color("white")
        self.escrita.goto(-230, 260)
        self.high_score = 0
        self.atualizar_pontuacao()
        self.mostrar_maior_score()
        

    def atualizar_pontuacao(self):
        self.escrita.clear()
        self.escrita.write(f"Pontuação: {self.score} ", align="center", font=("Arial", 16, "normal"))

    def mostrar_maior_score(self):
        with open("Snake_Game/score_historico.txt", "r") as file:
            self.high_score = int(file.read().strip())
            self.escrita.goto(-50, 260)
            self.escrita.write(f"Maior Pontuação: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def aumentar_pontuacao(self):
        self.score += 1
        self.atualizar_pontuacao()

    def salvar_historico_maior_txt(self):
        try:
            with open("Snake_Game/score_historico.txt", "r") as file:
                high_score = int(file.read().strip())
        except FileNotFoundError:
            high_score = 0
        except ValueError:
            high_score = 0

        if self.score > high_score:
            try:
                with open("Snake_Game/score_historico.txt", "w") as file:
                    file.write(f"{self.score}")
            except Exception as e:
                print(f"Erro ao salvar o histórico: {e}")