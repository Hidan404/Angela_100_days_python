from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from pprint import pprint

def api_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id= os.getenv("MTM_ID"),
        client_secret= os.getenv("MTM_SECRET"),
        redirect_uri="http://127.0.0.1:8888/callback",  # ou http://localhost:8888/callback
        scope="playlist-modify-private"
    ))

    usuario = sp.current_user()
    return usuario, sp

api_spotify()    

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
        titulos_musicas = []
        for i, titulo in enumerate(titulos[:100], 1):
            nome = titulo.get_text(strip=True)
            titulos_musicas.append(f"{i:02d}. {nome}")
        
        return titulos_musicas, data_usuario  
    else:
        print(f"Erro ao acessar o site: {resposta.status_code}")


def criar_playlist():
    urls= []
    lista_musicas, data_completa = raspar_titulos_musicas()
    usuario, sp = api_spotify()
    ano = data_completa.split("-")[0]
    
    for musica in lista_musicas:
        try:
            resultado = sp.search(q=f"faixa:{musica} ano: {ano}", type="track")
            faixas = resultado["tracks"]["items"]

            if faixas:
                url = faixas[0]["uri"]
                urls.append(url)
                print(f"{musica} Url encontrada {url}")
            else:
                print(f"{musica} não encontrada no Spotify")   
        except Exception as e:
            print(f"Erro ao buscar a musica {e}")    

    print("\nLista de musicas encontradas")
    pprint(urls)             






criar_playlist()    





