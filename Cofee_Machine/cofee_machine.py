from menu import MENU
from recursos import recursos



def relatrio():
    print(f"Agua {recursos['água']}ml")
    print(f"Leite {recursos['leite']}ml")
    print(f"Café {recursos['café']}g")
    print(f"Dinheiro ${recursos['dinheiro']}")
    print("\n")

def verificar_recursos(ingredientes):
    for item in ingredientes:
        if recursos[item] < ingredientes[item]:
            print(f"Desculpe, não há {item} suficiente para fazer o café.")
            return False
    return True


def processar_moeda():
    print("Por favor, insira moedas.")
    try:
        total = int(input("Quantas moedas de 1 centavo? ")) * 0.01
        total += int(input("Quantas moedas de 5 centavos? ")) * 0.05
        total += int(input("Quantas moedas de 10 centavos? ")) * 0.10
        total += int(input("Quantas moedas de 25 centavos? ")) * 0.25
        print(f"Total inserido: R$ {total:.2f}")  # Exibir o total inserido
        return total
    except ValueError:
        print("Erro! Certifique-se de inserir apenas números inteiros.")
        return 0


def verificar_pagamento(valor_cafe, dinheiro):
    if dinheiro >= valor_cafe:
        troco = round(dinheiro - valor_cafe, 2)
        print(f"Aqui está seu troco: R$ {troco:.2f}")
        recursos["dinheiro"] += valor_cafe
        return True
    else:
        faltando = round(valor_cafe - dinheiro, 2)
        print(f"Desculpe, o valor inserido não é suficiente. Faltam R$ {faltando:.2f}. Dinheiro reembolsado.")
        return False

def fazer_cafe(cafe, ingredientes):
    for item in ingredientes:
        recursos[item] -= ingredientes[item]
    print(f"Aqui está seu {cafe} ☕. Aproveite!")


def main():
    condicao = True

    while condicao:
        try:
            escolha = input("Qual café você gostaria? (espresso/latte/cappuccino): ").lower()  
            if escolha == "off":
                condicao = False
            elif escolha == "relatorio":
                relatrio()   
            else:
                cafe = MENU[escolha]
                if verificar_recursos(cafe["ingredientes"]):
                    pagamento = processar_moeda()
                    if verificar_pagamento(cafe["preço"], pagamento):
                        fazer_cafe(escolha, cafe["ingredientes"])  
        except KeyError:
            print("Desculpe, escolha inválida. Tente novamente.")
        except ValueError:
            print("Desculpe, escolha inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\n\nObrigado por usar a máquina de café. Até a próxima!")
            condicao = False                

main()


