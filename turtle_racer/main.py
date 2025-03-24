from turtle import Turtle, Screen, colormode
from tkinter.messagebox import  showinfo
import random as rd



tela = Screen()
tela.title("Turtle Racer")
tela.setup(width=800, height=600)
tela.bgcolor("black")
cores = ["red", "blue", "green", "yellow", "orange", "purple"]
tartarugas_nomes = ["hidan", "kakuzu", "deidara", "sasori", "itachi", "pain"]
usuario_aposta = tela.textinput("Turtle Racer", f"Escolha uma tartaruga apostar = {", ".join(tartarugas_nomes)} Pressione Enter para começar")

posicoes = [-150, -90, -30, 30, 90, 150]
print(usuario_aposta)

tartarugas = {}

for i in range(6):
    
    tartaruga = Turtle()
    tartaruga.shape("turtle")
    tartaruga.color(cores[i])
    tartaruga.penup()
    tartaruga.goto(-380, posicoes[i])
    tartaruga.pendown()
    tartaruga.speed("normal")

    tartaruga.penup()
    tartaruga.goto(-380, posicoes[i] + 30)  # Ajuste a posição do nome acima da tartaruga
    tartaruga.write(tartarugas_nomes[i], align="center", font=("Arial", 12, "normal"))
    tartaruga.pendown()

    tartarugas[tartarugas_nomes[i]] = tartaruga
print(tartarugas)    

def corrida():
    condicao = True
    while condicao:
        for tartaruga, tartaruga_valores in tartarugas.items():
            
            tartaruga_valores.speed("fastest")
            tartaruga_valores.pendown()
            tartaruga_valores.penup()
            tartaruga_valores.forward(rd.randint(1, 10))
            if tartaruga_valores.xcor() >= 385:
                condicao = False
                if usuario_aposta == tartaruga:
                    showinfo("Turtle Racer", f"O vencedor é a tartaruga {tartaruga}\nParabéns você ganhou")
                    reiniciar()
                else:
                    showinfo("Turtle Racer", f"O vencedor é a tartaruga {tartaruga}\nVocê perdeu")
                    reiniciar()
                return tartaruga_valores.color()

def reiniciar():
    escolha = tela.textinput("Turtle Racer", "Deseja jogar novamente?")
    if escolha == "sim":
        for tartaruga, tartaruga_valores in tartarugas.items():
            tartaruga_valores.goto(-380, posicoes[tartarugas_nomes.index(tartaruga)])
            tartaruga_valores.color(cores[tartarugas_nomes.index(tartaruga)])
        corrida()
    else:
        tela.bye()
    

corrida()


tela.exitonclick()