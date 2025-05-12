import requests
from bs4 import BeautifulSoup


url = "https://appbrewery.github.io/instant_pot/"
resposta = requests.get(url= url).text

soup = BeautifulSoup(resposta, "html.parser")

precos_div = soup.find_all("span", class_="a-price")
precos = []

for preco in precos_div:
    try:
        inteiro = preco.find("span", class_="a-price-whole").get_text(strip=True)
        fracao = preco.find("span", class_="a-price-fraction").get_text(strip=True)
        valor = f"{inteiro}.{fracao}"
        precos.append(valor)
    except AttributeError:
        continue  # Se não encontrar uma parte, ignora esse bloco

preco_selecionado = float(precos[0].replace("..","."))

