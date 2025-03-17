from menu import MENU
from recursos import recursos



def relatrio():
    print(f"Agua {recursos["água"]}ml")
    print(f"Leite {recursos["leite"]}ml")
    print(f"Café {recursos["café"]}g")
    print(f"Dinheiro ${recursos["dinheiro"]}")
    print("\n")

def verificar_recursos(ingredientes):
    for item in ingredientes:
        if ingredientes[item] >= recursos[item]:
            print(f"Desculpe, não há ingredientes suficientes para fazer o {item}.")

            return False
        print(item)
        print(ingredientes[item])
    return True

def processar_moeda():
    print("Por favor, insira moedas.")
    total = int(input("Quantas moedas de 1 centavo? ")) * 0.01
    total += int(input("Quantas moedas de 5 centavos? ")) * 0.05
    total += int(input("Quantas moedas de 10 centavos? ")) * 0.10
    total += int(input("Quantas moedas de 25 centavos? ")) * 0.25
    return total
