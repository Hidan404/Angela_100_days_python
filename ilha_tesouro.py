import random

# Definir tamanho da ilha
TAMANHO = 5

# Criar a matriz da ilha (mapa)
ilha = [["." for _ in range(TAMANHO)] for _ in range(TAMANHO)]

# Definir posição inicial do jogador
jogador_posicao = [0, 0]

# Gerar posição aleatória para o tesouro (diferente do início)
while True:
    tesouro_posicao = [random.randint(0, TAMANHO - 1), random.randint(0, TAMANHO - 1)]
    if tesouro_posicao != jogador_posicao:
        break

# Adicionar armadilhas aleatórias no mapa
numero_de_armadilhas = 3
armadilhas = []

while len(armadilhas) < numero_de_armadilhas:
    armadilha = [random.randint(0, TAMANHO - 1), random.randint(0, TAMANHO - 1)]
    if armadilha != jogador_posicao and armadilha != tesouro_posicao and armadilha not in armadilhas:
        armadilhas.append(armadilha)
        ilha[armadilha[0]][armadilha[1]] = "X"  # Marca armadilha

# Função para exibir o mapa
def exibir_mapa():
    print("\nMapa da Ilha:")
    for linha in range(TAMANHO):
        for coluna in range(TAMANHO):
            if [linha, coluna] == jogador_posicao:
                print("P", end=" ")  # Marca o jogador
            else:
                print(".", end=" ")  # Mantém o resto oculto
        print()
    print()

# Loop principal do jogo
while True:
    exibir_mapa()

    print("Movimentos disponíveis: [N] Norte, [S] Sul, [L] Leste, [O] Oeste")
    movimento = input("Para onde deseja se mover? ").strip().upper()

    # Atualizar posição do jogador
    if movimento == "N" and jogador_posicao[0] > 0:
        jogador_posicao[0] -= 1
    elif movimento == "S" and jogador_posicao[0] < TAMANHO - 1:
        jogador_posicao[0] += 1
    elif movimento == "L" and jogador_posicao[1] < TAMANHO - 1:
        jogador_posicao[1] += 1
    elif movimento == "O" and jogador_posicao[1] > 0:
        jogador_posicao[1] -= 1
    else:
        print("Movimento inválido! Tente novamente.")
        continue

    # Verificar se encontrou o tesouro
    if jogador_posicao == tesouro_posicao:
        print("\n🎉 Parabéns! Você encontrou o tesouro! 🎉")
        break

    # Verificar se caiu em uma armadilha
    if jogador_posicao in armadilhas:
        print("\n💀 Você caiu em uma armadilha! Fim de jogo. 💀")
        break
