import tkinter as tk

# Crie a janela principal do aplicativo
root = tk.Tk()
root.title("Contador de Palavras")

root.minsize(300, 200)

rotulo = tk.Label(root, text="Digite o texto:", font=("Arial", 22))
rotulo.pack(side=tk.TOP, pady=10)

rotulo["bg"] = "black"
rotulo.config(text="Novo texto")
rotulo["fg"] = "white"

# Crie uma caixa de texto para entrada do usuário
entrada = tk.Text(root, height=5, width=30, font=("Arial", 14))
entrada.pack(pady=10)

def botao_clicado():
    texto = entrada.get("1.0", tk.END)
    palavras = texto.split()
    num_palavras = len(palavras)
    rotulo.config(text=f"Número de palavras: {num_palavras}")


def botao_clicado2():
    rotulo.config(text="hidan")
   

botão = tk.Button(root, text="Contar Palavras", font=("Arial", 22), bg="black", fg="white", command=botao_clicado)
botão.pack(side=tk.LEFT, pady=10)


botao2 = tk.Button(root, text="Novo Texto", font=("Arial", 22), bg="black", fg="white", command=botao_clicado2)
botao2.pack(side=tk.RIGHT, pady=10)
root.mainloop()
     