import pandas as pd

#TODO 1. Create a dictionary in this format:
dados = pd.read_csv("Nato project Alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv")
dicionario_nato = {linha.letter.lower(): linha.code for index, linha in dados.iterrows()}
#print(dicionario_nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nome_nato_alfabeto():

    nome = input("Digite seu nome? ").strip().lower()
    resultado = [dicionario_nato[letra] for letra in nome if letra in dicionario_nato]
    return resultado
def salvar_txt(funcao):
    
    texto = funcao

    with open("Nato project Alphabet/nato.txt", "w") as f:
        for l in texto:
            f.write(f"{l}\n")

        
alfabeto_nato = nome_nato_alfabeto()
print(alfabeto_nato)

salvar_txt(alfabeto_nato)  
