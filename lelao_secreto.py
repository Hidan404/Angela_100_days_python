import os
from pyfiglet import figlet_format
from termcolor import colored

pessoas_leilao = {}

def inicio_app_desenho():
    texto = figlet_format("Seja bem-vindo ao leilao silencioso", font="slant")
    print(colored(texto, "cyan"))
    print(figlet_format("Feito por Ronald", font="small"))

def verificar_string_comprimento_isalfabetica(texto, comprimento):
    return len(texto) == comprimento and texto.isalpha()

def verificar_maior_valor_dicionario():
    maior_valor = 0
    for nome, lance in pessoas_leilao.items():
        if lance > maior_valor:
            maior_valor = lance
            ganhador = nome

    return maior_valor, ganhador        

def leilao():
    while True:
        try:
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')
            
            inicio_app_desenho()
            participante = input("Deseja participar do leilao [S] ou [N]: ").upper().strip()
            if verificar_string_comprimento_isalfabetica(participante, 1):
                if participante == 'S':
                    nome = input("Digite seu nome: ")
                    lance = float(input("Digite o valor do seu lance: R$"))
                    pessoas_leilao[nome] = lance
                elif participante == 'N':
                    maior_valor, ganhador = verificar_maior_valor_dicionario() 
                    print(f"O ganhador foi {ganhador} com o maior lance de {maior_valor}")
                    break
                else:
                    print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            
        except Exception as erro:
            print(erro)        

        

        
        



if __name__ == "__main__":
    leilao()        
        

