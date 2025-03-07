import random
from rich.console import Console
from rich.text import Text

class  hangman():
    def __init__(self):
        self.lista_palavras = ["abacaxi", "banana", "cereja", "damasco", "elefante", "figo", "goiaba", "hortela", "iguana", "jabuticaba"]
        random.seed() 
        self.palavra_selecionada = random.choice(self.lista_palavras)
        self.mostrar = ["_" for _ in self.palavra_selecionada]
        



    def menu_jogo_ascii(self):
        console = Console()
        hangman_text = Text(r"""
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

    def boneco_enforcado_etapas(self, tentativas):
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

        index = max(0, min(tentativas, len(estagios) - 1))
        console = Console()
        console.print(Text(estagios[index], style="bold red"))

    def jogar(self):
        self.menu_jogo_ascii()
        print("Jogar Forca")
        tentativas = len(self.palavra_selecionada)
        

        while tentativas > 0 and "_" in self.mostrar:
            print("".join(self.mostrar))
            tentativa = input("Digite uma letra: ").strip().lower()

            if tentativa.isdigit():
                print("Digite apenas letras, não números")
                continue

            if len(tentativa) > 1:
                print("Somente uma letra pode ser digitada")
                continue

            if tentativa in self.palavra_selecionada:
                for indice, letra in enumerate(self.palavra_selecionada):
                    if tentativa == letra:
                        self.mostrar[indice] = tentativa
            else:
                tentativas -= 1
                self.boneco_enforcado_etapas(tentativas)
                print(f"Letra incorreta! Tentativas restantes: {tentativas}")
        
        if "_" not in self.mostrar:
            print(f"Você ganhou o jogo! A palavra era: {"".join(self.mostrar)}")
        else:
            print(f"Você perdeu! A palavra era: {self.palavra_selecionada}")

    def jogar_novamente(self):
        while True:
            self.__init__()
            console = Console()
            texto_inicio_jogo = Text(r"""
            Bem-vindo ao Jogo da Forca!
            Tente adivinhar a palavra antes que o boneco seja enforcado.
            Você tem várias tentativas, mas cuidado, cada erro te aproxima do fim!
            Boa sorte e divirta-se!
            """, style="bold green")


            console.print(texto_inicio_jogo)
            self.jogar()
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
            if jogar_novamente != 's':
                print("Obrigado por jogar! Até a próxima!")
                break

      


jogo = hangman()
if __name__ == "__main__":
    jogo.jogar_novamente()     