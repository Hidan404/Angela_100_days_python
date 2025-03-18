from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




def maquina_cafe():
    menu = Menu()
    produzir_cafe = CoffeeMaker()
    dinheiro = MoneyMachine()

   
    while True:
        escolha = input(f"Qual café você gostaria? ({menu.get_items()}): ").lower().strip()

        if escolha =="off":
            break
        elif escolha == "relatorio":
            print(produzir_cafe.report())
            print(dinheiro.report())
        else:
            bebida = menu.find_drink(escolha)
            if produzir_cafe.is_resource_sufficient(bebida) and dinheiro.make_payment(bebida.cost):
                produzir_cafe.make_coffee(bebida)




maquina_cafe()