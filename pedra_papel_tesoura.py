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
    
    def 