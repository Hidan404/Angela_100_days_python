import os
from colorama import Fore, Style, init

class apresentacao():

    def apresentacao_calculadora(self):
        init(autoreset=True)
        print(Fore.CYAN + Style.BRIGHT + "===============================")
        print(Fore.YELLOW + Style.BRIGHT + "   Bem-vindo à Calculadora!    ")
        print(Fore.CYAN + Style.BRIGHT + "===============================")
        print(Fore.GREEN + "Desenvolvido por Hidan")
        print(Fore.MAGENTA + "Vamos começar a calcular!\n")



class calculadora():

    def __init__(self):
        self.numeros = []

    

    def subtrair(self, *args):
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado
    
    def somar(self, *args):
        resultado = args[0]
        for num in args[1:]:
            resultado += num
        return resultado    
    
    def dividir(self, *args):
        resultado = args[0]
        for num in args[1:]:
            if num != 0:
                resultado /= num
            else:
                raise ValueError("Divisão por zero não é permitida")
        return resultado   

    def multiplicar(self, *args):
        resultado = args[0]
        for num in args[1:]:
            resultado *= num
        return resultado   


def ui():
    while True:
        menu = apresentacao()  
        menu.apresentacao_calculadora()    


        lista_operacoes = ["somar", "subtrair", "multiplicar", "dividir"]
        escolha_operaçao = input(f"Escolha uma das operaçoes {lista_operacoes} ou [S] para sair: ").strip().lower()

        if escolha_operaçao == "s":
            print(Fore.LIGHTRED_EX + "Saindo do progrma...")
            break
        if escolha_operaçao in lista_operacoes:
           valores = input("Digite os numeros seprados por virgula: ").split(",")
           numeros = [float(n) for n in valores]

           calc = calculadora()

           if escolha_operaçao == "somar":
               print(Fore.MAGENTA + f"{calc.somar(*numeros)}")



if __name__ == "__main__":
    ui()    

               
