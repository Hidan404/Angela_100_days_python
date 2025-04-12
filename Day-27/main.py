import tkinter as tk

# Crie a janela principal do aplicativo
root = tk.Tk()
root.title("Contador de Palavras")

root.minsize(300, 200)

rotulo = tk.Label(root, text="Digite o texto:", font=("Arial", 22))
rotulo.pack(side=tk.BOTTOM)
entrada = tk.Text(root, height=10, width=40)
entrada.pack()


root.mainloop()
     