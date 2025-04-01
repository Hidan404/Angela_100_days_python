import turtle
import random

# Configuração da tela
screen = turtle.Screen()
screen.title("Jogo da Cobra")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Desativa a atualização automática da tela para melhor desempenho

# Criando a cobra
cobra = []
for i in range(3):
    segmento = turtle.Turtle()
    segmento.shape("square")
    segmento.color("white")
    segmento.speed("normal")
    segmento.penup()
    segmento.goto(-20 * i, 0)
    cobra.append(segmento)

# Criando a comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(random.randint(-250, 250), random.randint(-250, 250))

# Variáveis de controle
direcao = "direita"
velocidade = 0.1

# Função para mover a cobra
def mover_cobra():
    for i in range(len(cobra)-1, 0, -1):
        x = cobra[i-1].xcor()
        y = cobra[i-1].ycor()
        cobra[i].goto(x, y)
    
    if direcao == "cima":
        cobra[0].setheading(90)
    elif direcao == "baixo":
        cobra[0].setheading(270)
    elif direcao == "esquerda":
        cobra[0].setheading(180)
    elif direcao == "direita":
        cobra[0].setheading(0)
    
    cobra[0].forward(20)
    verificar_colisao_borda()
    verificar_comida()
    colisao_cauda()

    screen.update()
    turtle.ontimer(mover_cobra, int(velocidade * 1500))

# Função para verificar colisão com a borda
def verificar_colisao_borda():
    if cobra[0].xcor() > 300 or cobra[0].xcor() < -300 or cobra[0].ycor() > 300 or cobra[0].ycor() < -300:
        game_over()

# Função para verificar se a cobra comeu a comida
def verificar_comida():
    if cobra[0].distance(comida) < 15:
        comida.goto(random.randint(-250, 250), random.randint(-250, 250))  # Reposiciona a comida
        adicionar_segmento()

# Função para adicionar um segmento à cobra
def adicionar_segmento():
    segmento = turtle.Turtle()
    segmento.shape("square")
    segmento.color("white")
    segmento.penup()
    cobra.append(segmento)

def colisao_cauda():
    for segmento in cobra[1:]:
        if cobra[0].distance(segmento) < 10:
            game_over()

# Função de game over
def game_over():
    global direcao
    direcao = None
    print("Game Over")
    screen.bye()

# Funções para controlar a direção da cobra
def cima():
    global direcao
    if direcao != "baixo":
        direcao = "cima"

def baixo():
    global direcao
    if direcao != "cima":
        direcao = "baixo"

def esquerda():
    global direcao
    if direcao != "direita":
        direcao = "esquerda"

def direita():
    global direcao
    if direcao != "esquerda":
        direcao = "direita"

# Configuração dos controles do teclado
screen.listen()
screen.onkey(cima, "Up")
screen.onkey(baixo, "Down")
screen.onkey(esquerda, "Left")
screen.onkey(direita, "Right")

# Começando o jogo
mover_cobra()

screen.mainloop()
