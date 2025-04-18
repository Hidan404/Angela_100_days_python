import json
import random
from faker import Faker
from pathlib import Path

fake = Faker("pt_BR")
Faker.seed(0)
random.seed(0)

# Função para gerar palavras falsas únicas
def gerar_pares_palavras(qtd):
    palavras_pt = set()
    palavras_en = set()
    pares = []

    while len(pares) < qtd:
        pt = fake.unique.word()
        en = fake.unique.word()
        if pt not in palavras_pt and en not in palavras_en:
            palavras_pt.add(pt)
            palavras_en.add(en)
            pares.append({"pt": pt, "en": en})
    
    return pares

# Gerar 2000 pares únicos
pares_2000 = gerar_pares_palavras(100)

# Salvar como JSON
caminho_arquivo = Path("flashcard capstone app project/palavras_2000.json")
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    json.dump(pares_2000, f, ensure_ascii=False, indent=2)

caminho_arquivo
