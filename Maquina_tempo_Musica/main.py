from datetime import datetime
from bs4 import BeautifulSoup
import requests

cabeçalho = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
def obter_data():
    data_input = input("Digite uma data no formato YYYY-MM-DD: ")
    data_formatada = datetime.strptime(data_input, "%Y%m%d").date()
    return data_formatada



def raspar_titulos_musicas():
    data_usuario = str(obter_data())
    print(data_usuario)

    url = f"https://www.billboard.com/charts/hot-100/{data_usuario}"
    resposta = requests.get(url=url)

    if resposta.status_code == 200:
        print("ok")
    else:
        print("mal")    


raspar_titulos_musicas()




