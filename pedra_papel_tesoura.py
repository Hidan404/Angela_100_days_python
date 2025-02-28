import random as rd

class Jokenpo():

    def __init__(self):
        self.opcoes = ["pedra", "papel", "tesoura"]

    def gerar_imagens_ascii(self):
        imagens = {
            "pedra": '''
    _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
            ''',
                        "papel": '''
                _______
            ---'    ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            ''',
                        "tesoura": '''
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
            '''
        }
        return imagens    
    
    def jogar(self, usuario_escolha):
        escolha_computador = rd.choice(self.opcoes)
        escolha_usuario = usuario_escolha
        imagens = self.gerar_imagens_ascii()
        
        print(f"Vc escolheu:\n {imagens[escolha_usuario]}")
        print(f"Computador escolheu:\n {imagens[escolha_computador]}")

        if escolha_usuario == escolha_computador:
            return "Empate"
        elif escolha_usuario == "pedra":
            if escolha_computador == "papel":
                return "Vc perdeu"
            else:
                return "Vc ganhou"
        elif escolha_usuario == "papel":
            if escolha_computador == "tesoura":
                return "Vc perdeu"
            else:
                return "Vc ganhou"
        elif escolha_usuario == "tesoura":
            if escolha_computador == "pedra":
                return "Vc perdeu"
            else:
                return "Vc ganhou"

    def ui(self):
        print("Bem vindo ao jogo\n***JOKENPO***")    

        while True:
            
            jogada_usuario = input(f"Escolha uma das opções {self.opcoes}").lower().strip()    
            contador = 0

            jogo = self.jogar(jogada_usuario)   

            if jogada_usuario not in self.opcoes:
                print("Opção inválida. Tente novamente.")
                continue

            
            if "Vc ganhou" in jogo:
                contador += 1
                print(f"Você ganhou {contador} vezes.")
            elif "Vc perdeu" in jogo:
                print(f"Você perdeu. Total de vitórias: {contador}.")
            else:
                print(f"Empate. Total de vitórias: {contador}.")      


            sair_continuar = input("Deseja continuar jogando? (s/n): ").lower().strip()
            if sair_continuar != 's':
                print("Obrigado por jogar!")
                break    
        
        
game = Jokenpo()
game.ui()        

