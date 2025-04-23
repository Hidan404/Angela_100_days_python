import requests
import json

# Dicionário com categorias disponíveis
CATEGORIAS = {
    9: "Conhecimento Geral",
    10: "Livros",
    11: "Filmes",
    12: "Músicas",
    13: "Musicais & Teatro",
    14: "Televisão",
    15: "Jogos de Vídeo Game",
    16: "Jogos de Tabuleiro",
    17: "Ciência & Natureza",
    18: "Computadores",
    19: "Matemática",
    20: "Mitologia",
    21: "Esportes",
    22: "Geografia",
    23: "História",
    24: "Política",
    25: "Arte",
    26: "Celebridades",
    27: "Animais",
    28: "Veículos",
    29: "Quadrinhos",
    30: "Gadgets",
    31: "Anime & Mangá",
    32: "Desenhos Animados"
}

def exibir_categorias():
    print("Categorias disponíveis:\n")
    for id, nome in CATEGORIAS.items():
        print(f"{id} - {nome}")
    print()

def questoes_interativo():
    exibir_categorias()

    try:
        categoria = int(input("Escolha o ID da categoria: "))
        amount = int(input("Quantas questões deseja (máx 50)? "))
        dificuldade = input("Escolha a dificuldade (easy / medium / hard): ").lower()
        tipo = input("Tipo (multiple / boolean): ").lower()

        url = "https://opentdb.com/api.php"
        parametros = {
            "amount": amount,
            "category": categoria,
            "difficulty": dificuldade,
            "type": tipo
        }

        resposta = requests.get(url, params=parametros)
        resposta.raise_for_status()
        dados = resposta.json()

        if dados["response_code"] != 0:
            print(f"\n❌ Erro: A combinação de filtros não retornou perguntas. Código {dados['response_code']}")
            return

        print(f"\n✅ {len(dados['results'])} perguntas recebidas:\n")
        with open("/home/hidan/Documentos/GitHub/Angela_100_days_python/quiz_project/dados.json", "w") as f:
            f.write(json.dumps(dados,indent= 4))


    except Exception as e:
        print(f"\nErro: {e}")

# Executar
questoes_interativo()
