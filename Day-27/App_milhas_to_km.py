import tkinter as tk

def converter():
    milhas = float(entrada.get())
    km = milhas * 1.60934
    resultado_texto.set(f"{km:.2f} km")

janela = tk.Tk()
janela.title("Conversor de Milhas para Quilômetros")
janela.config(padx=20, pady=20, bg="white")


for col in range(3):
    janela.grid_columnconfigure(col, weight=1)
for row in range(3):
    janela.grid_rowconfigure(row, weight=1)

# Entrada de texto
entrada = tk.Entry(janela, width=10, font=("Arial", 12))
entrada.grid(column=1, row=0, sticky="ew", padx=10)

# Label "Milhas"
milhas = tk.Label(janela, text="Milhas", font=("Arial", 12), bg="white")
milhas.grid(column=2, row=0, sticky="w", padx=10, pady=10)


texto = tk.Label(janela,text= "e igual a", font=("Arial", 12), bg="white")
texto.grid(column=0, row=1, sticky="e")

resultado_texto = tk.StringVar()
resultado_texto.set("0 km")
resultado = tk.Entry(janela, textvariable=resultado_texto, font=("Arial", 12), state="readonly", width=10)
resultado.grid(column=1, row=1, sticky="w", padx=10, pady=10)

km = tk.Label(janela, text="km", font=("Arial", 12), bg="white")
km.grid(column=2, row=1, sticky="w", padx=10, pady=10)



botao = tk.Button(janela, text="Converter", command=converter, font=("Arial", 12), bg="black", fg="white")
botao.grid(column=1, row=3, sticky="ew", padx=10)




janela.mainloop()
    