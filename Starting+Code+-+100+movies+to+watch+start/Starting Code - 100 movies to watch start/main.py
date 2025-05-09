import requests
from bs4 import BeautifulSoup
import json

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

resposta = requests.get(url=URL).text

soup = BeautifulSoup(resposta, "html.parser")

titulos = [t.get_text() for t in soup.find_all(name="h3",class_="title")]

with open("Starting+Code+-+100+movies+to+watch+start/filmes.json", "a") as f:
    for t in reversed(titulos):
        f.write(json.dumps(t, ensure_ascii=False, indent=4) + "\n")



