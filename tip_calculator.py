import random as rd


class Tip_calculator():

    def __init__(self, valor_conta):
        self.pessoas = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivan", "Jack"]
        self.valores_percentuais = [10, 12, 15]
        self.valor_conta = valor_conta

    def escolher_pessoa(self):
        return rd.choice(self.pessoas)  

    def escolher_porcentagem(self):
        return rd.choice(self.valores_percentuais) 
    
    def pagar_conta(self):
        pessoa = self.escolher_pessoa()
        porcentagem = self.escolher_porcentagem()
        valor_tip = self.valor_conta * (porcentagem / 100)
        valor_total = self.valor_conta + valor_tip
        return f"{pessoa} should pay a tip of {porcentagem}% which is {valor_tip:.2f}. Total amount to be paid is {valor_total:.2f}."
    

def Ui():
    valor_da_conta = float(input("Digite o valor da conta: ").strip())
    calculadora_dica = Tip_calculator(valor_da_conta)
    
    while True:
        print("Deseja pagar a conta, digite [S] para sair ou [P] para pagar: ")
        escolha = input("Digite sua opção: ").upper().strip()
        if escolha == "S":
            print("Saindo...")
            break

        print(calculadora_dica.pagar_conta())



if __name__ == "__main__":
    Ui()        