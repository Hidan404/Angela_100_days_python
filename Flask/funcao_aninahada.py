def fora(funcao):
    print("Estou fora da função")
    def dentro():
        funcao()
        print("Estou dentro da função")

    return dentro

@fora
def bom_dia():
    print("Bom dia!")
    


bom_dia()