import os
from colorama import Fore, Style, init

init(autoreset=True)  

def mostrar_titulo():
    """Exibe o título formatado da calculadora"""
    print(Fore.CYAN + Style.BRIGHT + "===============================")
    print(Fore.YELLOW + Style.BRIGHT + "   Bem-vindo à Calculadora!    ")
    print(Fore.CYAN + Style.BRIGHT + "===============================")
    print(Fore.GREEN + "Desenvolvido por Hidan")
    print(Fore.MAGENTA + "Vamos começar a calcular!\n")

class Calculadora:
    """Classe que encapsula as operações matemáticas básicas"""
    
    @staticmethod
    def subtrair(*args):
        if len(args) < 1:
            return 0
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado
    
    @staticmethod
    def somar(*args):
        return sum(args)
    
    @staticmethod
    def dividir(*args):
        if len(args) < 1:
            raise ValueError("Nenhum número fornecido")
            
        resultado = args[0]
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida")
            resultado /= num
        return resultado

    @staticmethod
    def multiplicar(*args):
        if len(args) < 1:
            return 0
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

def obter_numeros():
    """Obtém e valida a entrada de números do usuário"""
    while True:
        entrada = input("Digite os números separados por vírgula: ").replace(" ", "")
        if not entrada:
            print(Fore.RED + "Erro: Por favor, digite pelo menos um número!")
            continue
            
        try:
            numeros = [float(n) for n in entrada.split(",")]
            if len(numeros) < 1:
                raise ValueError
            return numeros
        except ValueError:
            print(Fore.RED + "Erro: Entrada inválida. Use apenas números separados por vírgulas!")

def ui():
    """Interface principal do usuário"""
    operacoes = {
        "somar": Calculadora.somar,
        "subtrair": Calculadora.subtrair,
        "multiplicar": Calculadora.multiplicar,
        "dividir": Calculadora.dividir
    }
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o console
        mostrar_titulo()
        
        escolha = input(f"Operações disponíveis: {list(operacoes.keys())}\n"
                        "Digite a operação desejada ou [S] para sair: ").strip().lower()
        
        if escolha == 's':
            print(Fore.LIGHTRED_EX + "\nSaindo do programa...")
            break
            
        if escolha not in operacoes:
            print(Fore.RED + "\nErro: Operação inválida!\n")
            input("Pressione Enter para continuar...")
            continue
            
        try:
            numeros = obter_numeros()
            resultado = operacoes[escolha](*numeros)
            print(Fore.GREEN + Style.BRIGHT + f"\nResultado: {resultado:.2f}")
        except ZeroDivisionError as e:
            print(Fore.RED + f"\nErro: {e}")
        except Exception as e:
            print(Fore.RED + f"\nErro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    ui()