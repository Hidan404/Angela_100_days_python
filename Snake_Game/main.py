import turtle
import time
from Snake import Snake
from comida import Comida
from Scoreboard import Score_board

# Tela principal
screen = turtle.Screen()
screen.title("Jogo da Cobra")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Instanciando objetos
snake = Snake()
comida = Comida()
placar = Score_board()

# Funções de controle
screen.listen()
screen.onkey(lambda: snake.set_direcao("cima"), "Up")
screen.onkey(lambda: snake.set_direcao("baixo"), "Down")
screen.onkey(lambda: snake.set_direcao("esquerda"), "Left")
screen.onkey(lambda: snake.set_direcao("direita"), "Right")

# Loop principal do jogo

jogo_ativo  = False

#Todo: terminar implementação do metodo e testar mudança na variavel global 
def confirmar_reinicio():
    continuar = input("deseja continuar [S/N]?").strip().lower()
    if continuar == "s":
        return jogo()
       
    return jogo_ativo


def jogo():
    #Todo: implementar variavel global de controle
    global jogo_ativo = True
    while jogo_ativo:
        screen.update()
        time.sleep(0.1)
        snake.mover_cobra()

        # Verifica colisão com a comida
        if snake.cobra[0].distance(comida) < 15:
            comida.refresh()
            snake.adicionar_segmento()
            placar.aumentar_pontuacao()

        # Verifica colisão com a borda
        if snake.verificar_colisao_borda(600, 600):
            placar.salvar_historico_maior_txt()
            jogo_ativo = False

        # Verifica colisão com a cauda
        if snake.colisao_cauda():
            placar.salvar_historico_maior_txt()
            e

jogo()

# Mensagem de Game Over
game_over = turtle.Turtle()
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
