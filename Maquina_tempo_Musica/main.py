from datetime import datetime
from bs4 import BeautifulSoup
import requests

cabeçalho = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

def obter_data():
    data_input = input("Digite uma data no formato YYYY-MM-DD: ")
    # Corrigido o formato para bater com o input
    data_formatada = datetime.strptime(data_input, "%Y-%m-%d").date()
    return data_formatada

def raspar_titulos_musicas():
    data_usuario = str(obter_data())
    print(f"Data formatada: {data_usuario}")

    url = f"https://www.billboard.com/charts/hot-100/{data_usuario}"
    resposta = requests.get(url, headers=cabeçalho)

    if resposta.status_code == 200:
        print("Conexão bem-sucedida!")
        soup = BeautifulSoup(resposta.text, "html.parser")
        titulos = soup.select("li ul li h3")
        titulos_filmes = []
        for i, titulo in enumerate(titulos[:100], 1):
            nome = titulo.get_text(strip=True)
            titulos_filmes.append(f"{i:02d}. {nome}")

        return titulos_filmes    
    else:
        print(f"Erro ao acessar o site: {resposta.status_code}")

raspar_titulos_musicas()





