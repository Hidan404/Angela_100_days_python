from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.nivel = 1
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.nivel}", align="left", font=FONT)

    def increase_level(self):
        self.nivel += 1
        self.update_scoreboard()    
    def fim_de_jogo(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=FONT)

    def resetar(self):
        self.nivel = 1