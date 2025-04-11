import pandas as pd
from turtle import Turtle, Screen
from tkinter import messagebox



tela = Screen()
tela.title("U.S. States Game")

tela.addshape("day-25-us-states-game-start/blank_states_img.gif")
Turtle().shape("day-25-us-states-game-start/blank_states_img.gif")

estados = pd.read_csv("day-25-us-states-game-start/50_states.csv")
estados_list = estados.state.to_list()
estados_acertados = []

while len(estados_acertados) < 50:
    perguntar_estado = messagebox.askquestion("U.S. Jogo dos Estados", "Você quer jogar o jogo dos Estados Unidos?")
    if perguntar_estado == "no":
        break
    estado = tela.textinput(title=f"{len(estados_acertados)}/50 Estados Corretos", prompt="qual o nome desse estado?").strip()
    estado = estado.title()
    if estado == "Exit":
        estados_acertados = estados_acertados
        salvar_estados_restantes = [estado for estado in estados_list if estado not in estados_acertados]
        estados_restantes = pd.DataFrame(salvar_estados_restantes)
        estados_restantes.to_csv("day-25-us-states-game-start/estados_restantes.csv", index=False)
        break
    if estado in estados_list and estado not in estados_acertados:
        estados_acertados.append(estado)
        estado_dados = estados[estados["state"] == estado]
        x = int(estado_dados["x"])
        y = int(estado_dados["y"])
        estado_turtle = Turtle()
        estado_turtle.hideturtle()
        estado_turtle.penup()
        estado_turtle.goto(x, y)
        estado_turtle.write(estado, align="center", font=("Arial", 8, "normal"))
    elif estado in estados_acertados:
        messagebox.showinfo("U.S. States Game", "Você já acertou esse estado.")
    else:
        messagebox.showinfo("U.S. States Game", "Esse estado não existe.")    

    

    
    












tela.exitonclick()