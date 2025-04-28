import requests
import json

NOME_ACAO = "TSLA"
NOME_EMPRESA = "Tesla Inc"

ENDPOINT_ACAO = "https://www.alphavantage.co/query"
ENDPOINT_NOTICIAS = "https://newsapi.org/v2/everything"

API_ACAO = "3HC28N54DTWIPXDF"
CHAVE_API_NOTICIAS = "71c5258c2dc547c196ebc0e51815fd7e"

## ETAPA 1: Use https://www.alphavantage.co/documentation/#daily
# Quando o preço da ação aumenta/diminui 5% entre ontem e anteontem, então print("Obter Notícias").

# TODO 1. - Obtenha o preço de fechamento da ação de ontem. Dica: Você pode realizar compreensões de lista em dicionários Python. Exemplo: [novo_valor for (chave, valor) in dicionario.items()]
parametros_acao = {
    "function": "TIME_SERIES_DAILY",
    "symbol": NOME_ACAO,
    "apikey": API_ACAO,
}
resposta = requests.get(ENDPOINT_ACAO, params=parametros_acao)
dados = resposta.json()["Time Series (Daily)"]
lista_dados = [valor for (chave, valor) in dados.items()]
dados_ontem = lista_dados[0]
preco_fechamento_ontem = dados_ontem["4. close"]

print(preco_fechamento_ontem)
# TODO 2. - Obtenha o preço de fechamento da ação de anteontem.
dados_anteontem = lista_dados[1]
preco_fechamento_anteontem = dados_anteontem["4. close"]
print(preco_fechamento_anteontem)
# TODO 3. - Encontre a diferença positiva entre 1 e 2. Exemplo: 40 - 20 = -20, mas a diferença positiva é 20. Dica: https://www.w3schools.com/python/ref_func_abs.asp
diferenca = round(float(preco_fechamento_ontem) - float(preco_fechamento_anteontem), 2)
print(diferenca)
# TODO 4. - Calcule a diferença percentual no preço entre o fechamento de ontem e o fechamento de anteontem.
diferenca_percentual = (float(diferenca) / float(preco_fechamento_ontem)) * 100
print(diferenca_percentual)
# TODO 5. - Se a porcentagem do TODO4 for maior que 5, então print("Obter Notícias").
if diferenca_percentual > 5:
    print("Obter Notícias")
    ## ETAPA 2: https://newsapi.org/ 
    # Em vez de imprimir ("Obter Notícias"), realmente obtenha as 3 primeiras notícias para o NOME_EMPRESA.

# TODO 6. - Em vez de imprimir ("Obter Notícias"), use a API de Notícias para obter artigos relacionados ao NOME_EMPRESA.
if diferenca_percentual > 1:
    parametros_novos = {
        "apikey": CHAVE_API_NOTICIAS,
        "qIntitle": NOME_EMPRESA,
    }
    nova_resposta = requests.get(ENDPOINT_NOTICIAS, parametros_novos)
    with open("stock-news-normal-start/news_data.json", "w") as f:
        f.write(json.dumps(nova_resposta.json(), ensure_ascii=False, indent=4))

    with open("stock-news-normal-start/news_data.json", "r") as t:
        dados_noticias = json.load(t)["articles"]
        tres_artigos = dados_noticias[:3]
        print(tres_artigos)
        
# TODO 7. - Use o operador de fatia do Python para criar uma lista que contenha os 3 primeiros artigos. Dica: https://stackoverflow.com/questions/509211/understanding-slice-notation


## ETAPA 3: Use twilio.com/docs/sms/quickstart/python
# para enviar uma mensagem separada com o título e a descrição de cada artigo para o seu número de telefone.

# TODO 8. - Crie uma nova lista com o título e a descrição dos 3 primeiros artigos usando compreensão de lista.
titulo_descricao = [f"headers: {dados_noticias["title"]}. \nApresentacao: {dados_noticias["description"]}" for dados_noticias in tres_artigos]
print(titulo_descricao)
# TODO 9. - Envie cada artigo como uma mensagem separada via Twilio.

# TODO Opcional: Formate a mensagem assim: 
# Formatar e enviar as mensagens
simbolo_variacao = "🔺" if diferenca > 0 else "🔻"
mensagens = [
    f"{NOME_ACAO}: {simbolo_variacao}{abs(round(diferenca_percentual, 2))}%\n"
    f"Título: {artigo['title']}\n"
    f"Resumo: {artigo['description']}"
    for artigo in tres_artigos
]

for mensagem in mensagens:
    print(mensagem)  # Substitua por lógica de envio via Twilio, se necessário
"""
TSLA: 🔺2%
Título: Os fundos de hedge estavam certos ao investir na Tesla Inc. (TSLA)?.
Resumo: Nós, do Insider Monkey, analisamos mais de 821 registros 13F que os fundos de hedge e investidores proeminentes são obrigados a arquivar na SEC. Os registros 13F mostram as posições de portfólio dos fundos e investidores em 31 de março, próximo ao auge do crash do mercado causado pelo coronavírus.
ou
"TSLA: 🔻5%
Título: Os fundos de hedge estavam certos ao investir na Tesla Inc. (TSLA)?.
Resumo: Nós, do Insider Monkey, analisamos mais de 821 registros 13F que os fundos de hedge e investidores proeminentes são obrigados a arquivar na SEC. Os registros 13F mostram as posições de portfólio dos fundos e investidores em 31 de março, próximo ao auge do crash do mercado causado pelo coronavírus.
"""
