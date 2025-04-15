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
entrada = tk.Entry(root, width=30, font=("Arial", 22))
entrada.pack(pady=10)

def botao_clicado():
    texto = entrada.get()
    print(type(texto))
    rotulo.config(text=texto)
    palavras = texto.split()
    num_palavras = len(palavras)
    rotulo.config(text=f"Número de palavras: {num_palavras}")


def botao_clicado2():
    texto = entrada.get()
    
    palavras = texto.split()
    rotulo.config(text=palavras[0])
   

botão = tk.Button(root, text="Contar Palavras", font=("Arial", 22), bg="black", fg="white", command=botao_clicado)
botão.pack(side=tk.LEFT, pady=10)


botao2 = tk.Button(root, text="Novo Texto", font=("Arial", 22), bg="black", fg="white", command=botao_clicado2)
botao2.pack(side=tk.RIGHT, pady=10)


spinbox = tk.Spinbox(root, from_=0, to=10, width=5, font=("Arial", 22))
spinbox.pack(pady=10)


escala = tk.Scale(root, from_=0, to=100, orient=tk.VERTICAL, length=100, font=("Arial", 22))
escala.pack(pady=10)

checkbox = tk.RADIOBUTTON(root, text="Opção 1", value=1, font=("Arial", 22), bg="black", fg="white")
checkbox.pack(pady=10)
checkbox2 = tk.RADIOBUTTON(root, text="Opção 2", value=2, font=("Arial", 22), bg="black", fg="white")
checkbox2.pack(pady=10)


lista = tk.Listbox(root, font=("Arial", 22), bg="black", fg="white")
lista.pack(pady=10)
lista.insert(1, "Item 1")
lista.insert(2, "Item 2")
lista.insert(3, "Item 3")
root.mainloop()
     