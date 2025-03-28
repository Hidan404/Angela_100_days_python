from turtle import Screen
from raquete import Raquete 
from bola import Bola


tela = Screen()
tela.bgcolor("black")
tela.setup(1200, 900)
tela.title("Pong")


tela.listen()
r = Raquete(tela,(580, 0),"Up", "Down")
l = Raquete(tela, (-580, 0),"w","s")

bola = Bola()

while True:
    tela.update()
    bola.move()

    if bola.ycor() > 450 or bola.ycor() < -450:
        bola.y_move*= -1

    if (bola.xcor() > 560 and bola.distance(r) < 50) or (bola.xcor() < -560 and bola.distance(l) < 50):
        bola.x_move *= -1



tela.mainloop()
