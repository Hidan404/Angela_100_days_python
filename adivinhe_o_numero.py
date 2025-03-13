import random

class AdivinheONumero():
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
    
    def __str__(self):
        return """
      ____                     _   _                 _               
     / ___|_   _  ___  ___ ___| \ | | ___  _ __ ___ | |__   ___ _ __ 
    | |  _| | | |/ _ \/ __/ __|  \| |/ _ \| '_ ` _ \| '_ \ / _ \ '__|
    | |_| | |_| |  __/\__ \__ \ |\  | (_) | | | | | | |_) |  __/ |   
     \____|\__,_|\___||___/___/_| \_|\___/|_| |_| |_|_.__/ \___|_|   
                                     
    """

    def jogar_novamente(self):
        jogar_novamente = input("Deseja jogar novamente [S] ou [N]: ").lower().strip()
        if jogar_novamente == "s":
            self.tentativas = 0
            self.numero_secreto = random.randint(1, 100)
            self.jogar()
        else:
            print("Obrigado por jogar!")



    def jogar(self):
        print(self.__str__())
        nivel_jogo = input("Escolha um nível de jogo: [Fácil] [Médio] [Difícil] ").lower().strip()

        if nivel_jogo == "fácil":
            self.tentativas = 20
        elif nivel_jogo == "médio":
            self.tentativas = 10
        else:
            self.tentativas = 5

        while self.tentativas > 0:
            try:
                escolha = int(input("Escolha um número entre 1 e 100: "))
                contador = 0
                if escolha == self.numero_secreto:
                    print(f"Parabéns! Você acertou o número secreto {self.numero_secreto} em {self.tentativas - contador} tentativas.")
                    self.jogar_novamente()
                    break
                elif escolha > self.numero_secreto:
                    print("numero muito alto")
                else:
                    print("numero muito baixo")   
                contador += 1
                self.tentativas -= 1
                print(f"Você ainda tem {self.tentativas} tentativas.\n")

                if self.tentativas == 0:
                    print(f"Você perdeu! O número secreto era {self.numero_secreto}.")
                    self.jogar_novamente()

            except ValueError:
                print("Digite um número inteiro.")
                continue        


if __name__ == "__main__":
    jogo = AdivinheONumero()
    jogo.jogar()            