from turtle import Screen, Turtle
from raquete import Raquete 
from bola import Bola
import time
from placar import Placar

tela = Screen()
tela.bgcolor("midnight blue")
tela.setup(1200, 900)
tela.title("🔥 Pong Game 🔥")

linha_central = Turtle()
linha_central.color("white")
linha_central.penup()
linha_central.goto(0, 450)
linha_central.setheading(270)  # Aponta para baixo
linha_central.pendown()
linha_central.pensize(2)

for _ in range(23):
    linha_central.forward(20)
    linha_central.penup()
    linha_central.forward(20)
    linha_central.pendown()
linha_central.hideturtle()


tela.listen()
r = Raquete(tela,(580, 0),"Up", "Down")
l = Raquete(tela, (-580, 0),"w","s")

bola = Bola()
placar_jogo = Placar()


def colisao_com_raquete(bola, raquete):
    # Verifica se a bola está na mesma altura da raquete (eixo Y)
    if (bola.ycor() < raquete.ycor() + 60) and (bola.ycor() > raquete.ycor() - 60):
        # Verifica proximidade no eixo X (ajuste 20px para margem de erro)
        if raquete.xcor() > 0:  # Raquete direita
            return bola.xcor() > 540  # Ajuste conforme tamanho da tela
        else:  # Raquete esquerda
            return bola.xcor() < -540
    return False


while True:
    tela.update()
    time.sleep(0.01)
    bola.move()

    if bola.ycor() > 450 or bola.ycor() < -450:
        bola.ricochete_y()
        


    if colisao_com_raquete(bola, r) or colisao_com_raquete(bola, l):
        bola.ricochete_x()
        
       
    # Detectar se a bola passou da tela direita e resetar a bola e marcar ponto
    if bola.xcor() > 600:
        placar_jogo.ponto_esquerda()
        if placar_jogo.vencedor_dez_pontos():
            break

        bola.resetar_posicao()
        
      

    # Detectar se a bola passou da tela esquerda e resetar a bola e marcar ponto
    if bola.xcor() < -600:
        placar_jogo.ponto_direita()
        if placar_jogo.vencedor_dez_pontos():
            break
        bola.resetar_posicao()
        


tela.mainloop()
