import random

class AdivinheONumero():
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
    
    def __str__(self):
        print('''
          ________                               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/            \/    \/     \/      ''')
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

                if escolha == self.numero_secreto:
                    print(f"Parabéns! Você acertou o número secreto {self.numero_secreto} em {self.tentativas} tentativas.")
                    break
                elif escolha > self.numero_secreto:
                    print("numero muito alto")
                else:
                    print("numero muito baixo")   

                self.tentativas -= 1
                print(f"Você ainda tem {self.tentativas} tentativas.\n")
            except ValueError:
                print("Digite um número inteiro.")
                continue        


if __name__ == "__main__":
    jogo = AdivinheONumero()
    jogo.jogar()            