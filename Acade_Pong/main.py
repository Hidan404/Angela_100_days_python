from turtle import Screen
from raquete import Raquete 
from bola import Bola
import time


tela = Screen()
tela.bgcolor("black")
tela.setup(1200, 900)
tela.title("Pong")


tela.listen()
r = Raquete(tela,(580, 0),"Up", "Down")
l = Raquete(tela, (-580, 0),"w","s")

bola = Bola()


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
    bola.move()

    if bola.ycor() > 450 or bola.ycor() < -450:
        bola.ricochete_y()


    if colisao_com_raquete(bola, r) or colisao_com_raquete(bola, l):
        bola.ricochete_x()
    #if (bola.xcor() > 560 and bola.distance(r) < 50) or (bola.xcor() < -560 and bola.distance(l) < 50):
        #bola.ricochete_x()

    # Detectar se a bola passou da tela direita e resetar a bola e marcar ponto
    if bola.xcor() > 600:
        #bola.resetar_posicao()
        ...
        
      

    # Detectar se a bola passou da tela esquerda e resetar a bola e marcar ponto
    if bola.xcor() < -600:
        #bola.resetar_posicao()
        ...
        


tela.mainloop()
