import random

lista_palavras = ["abacaxi", "banana", "cereja", "damasco", "elefante", "figo", "goiaba", "hortela", "iguana", "jabuticaba"]
random.seed() 
palavra_selecionada = random.choice(lista_palavras)
mostrar = ["_" for _ in palavra_selecionada]


def jogar():
    print("Jogar Forca")
    tentativas = len(palavra_selecionada)

    while tentativas > 0 and  "_" in mostrar:
        print("".join(mostrar))

        tentativa = input("Digite uma letra: ").strip().lower()
        if len(tentativa) > 1:
            print("Somente uma letra pode ser digitada")
            continue

        if tentativa.isdigit():
            print("Digite apenas letras, não números")
            continue

        if tentativa in palavra_selecionada:
            for indice, letra in enumerate(palavra_selecionada):
                if tentativa == letra:
                    mostrar[indice] = tentativa
                
        else:
            tentativas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")
    
    if "_" not in mostrar:
        print(f"vc ganhou o jogo {"".join(mostrar)}")
    else:
        print(f"Você perdeu! A palavra era {palavra_selecionada}")    


if __name__ == "__main__":
    jogar()        