from rich.console import Console
from rich.text import Text
import pyperclip


def menu():
    console = Console()
    texto_menu = Text('''
        1. Encrypt
        2. Decrypt
        3. Exit
            ''')
            
    console.print(texto_menu, style="bold yellow", emoji= True)

def validar_range_numero(numero):
    try:
        numero = int(numero)
        if numero < 0 or numero > 33:
            raise ValueError
        return numero
    except ValueError:
        print("Por favor, insira um número entre 0 e 33.")
        return None

def encrypt(texto, deslocamento):
    texto_criptografado = ""
    for l in texto:
        if l.isalpha():
            base = ord('A') if l.isupper() else ord('a')
            l = chr((ord(l) - base + deslocamento) % 26 + base)
        texto_criptografado+= l

    pyperclip.copy(texto_criptografado)
    return texto_criptografado 

def decrypt(texto, deslocamento):
    texto_descriptografado = ""   
    for l in texto:
        if l.isalpha():
            base = ord('A') if l.isupper() else ord('a')
            l = chr((ord(l) - base - deslocamento))
        texto_descriptografado+= l

    pyperclip.copy(texto_descriptografado)
    return texto_descriptografado    

def cifra_cesar():
   

    while True:
        menu()
        escolha = input("Digite uma das opções: ").strip()
        if len(escolha) > 1:
            print("Escolha inválida. Por favor, selecione uma das opções.")
            continue

        if escolha == '1':
            texto = input("Digite o texto para criptografar: ")
            deslocamento = int(input("Digite o deslocamento: "))
            if validar_range_numero(deslocamento):
                print(f"Texto criptografado: {encrypt(texto, deslocamento)}")
        elif escolha == '2':
            texto = input("Digite o texto para descriptografar: ")
            deslocamento = int(input("Digite o deslocamento: "))
            if validar_range_numero(deslocamento):
                print(f"Texto descriptografado: {decrypt(texto, deslocamento)}")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, selecione uma das opções.")




if __name__ == "__main__":
    
    cifra_cesar()