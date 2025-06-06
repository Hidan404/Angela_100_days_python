from bs4 import BeautifulSoup
import requests

resposta = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page = resposta.text

soup = BeautifulSoup(web_page, "html.parser")

articles = soup.find_all("a", class_="storylink")

artigos_textos = []
artigos_links = []

for tags in articles:
    textos = tags.text
    artigos_textos.append(textos)

    links = tags.get("href")
    artigos_links.append(links)

votos = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]



voto_maior = max(votos)
indice_voto_maior = votos.index(voto_maior)

texto_formatado = f"Maior numero: {voto_maior}, Indice: {indice_voto_maior}"
print(texto_formatado)
for v in votos:
    print(v)