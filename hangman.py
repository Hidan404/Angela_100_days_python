import random
from rich.console import Console
from rich.text import Text

lista_palavras = ["abacaxi", "banana", "cereja", "damasco", "elefante", "figo", "goiaba", "hortela", "iguana", "jabuticaba"]
random.seed() 
palavra_selecionada = random.choice(lista_palavras)
mostrar = ["_" for _ in palavra_selecionada]

def menu_jogo_ascii():
    console = Console()
    hangman_text = Text("""
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    """, style="bold blue")
    console.print(hangman_text)

def boneco_enforcado_etapas(tentativas):
    estagios = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    console = Console()
    console.print(Text(estagios[tentativas], style="bold red"))

def jogar():
    menu_jogo_ascii()
    print("Jogar Forca")
    tentativas = len(palavra_selecionada)

    while tentativas > 0 and "_" in mostrar:
        print("".join(mostrar))
        tentativa = input("Digite uma letra: ").strip().lower()

        if not tentativa.isalpha():
            print("Digite apenas letras, não números")
            continue

        if len(tentativa) > 1:
            print("Somente uma letra pode ser digitada")
            continue

        if tentativa in palavra_selecionada:
            for indice, letra in enumerate(palavra_selecionada):
                if tentativa == letra:
                    mostrar[indice] = tentativa
        else:
            tentativas -= 1
            boneco_enforcado_etapas(tentativas)
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")
    
    if "_" not in mostrar:
        print(f"Você ganhou o jogo! A palavra era: {"".join(mostrar)}")
    else:
        print(f"Você perdeu! A palavra era: {palavra_selecionada}")


if __name__ == "__main__":
    jogar()        