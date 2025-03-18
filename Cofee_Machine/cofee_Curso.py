from menu import MENU
from recursos import recursos


def recursos_suficientes(ingredientes):
    for item in ingredientes:
        if recursos[item] < ingredientes[item]:
            print(f"Desculpe, não há {item} suficiente para fazer o café.")
            return False
    return True

def processa_moedas():
    print("Por favor, insira moedas.")
    total = int(input("Quantas moedas de 1 centavo? ")) * 0.01
    total += int(input("Quantas moedas de 5 centavos? ")) * 0.05
    total += int(input("Quantas moedas de 10 centavos? ")) * 0.10
    total += int(input("Quantas moedas de 25 centavos? ")) * 0.25
    return total

def fazer_cafe(escolha, ingredientes):
    for item in ingredientes:
        recursos[item] -= ingredientes[item]
    print(f"Aqui está seu {escolha}. Aproveite!")

while True:
    escolha = input("Qual café você gostaria? (espresso/latte/cappuccino): ").lower()


    if escolha == "off":
        break
    elif escolha == "relatorio":
        print(f"Água: {recursos['água']}ml")
        print(f"Leite: {recursos['leite']}ml")
        print(f"Café: {recursos['café']}g")
        print(f"Dinheiro: ${recursos['dinheiro']}\n")
    else:
        bebida = MENU[escolha]
        if recursos_suficientes(bebida["ingredientes"]):
            pagamento = processa_moedas()
            if pagamento >= bebida["Preço"]:
                troco = round(pagamento - bebida["Preço"], 2)
                print(f"Aqui está seu troco: ${troco}")
                recursos["dinheiro"] += bebida["Preço"]
                fazer_cafe(escolha, bebida["ingredientes"])
            else:
                print("Desculpe, o dinheiro inserido não é suficiente. Dinheiro reembolsado.")



            
