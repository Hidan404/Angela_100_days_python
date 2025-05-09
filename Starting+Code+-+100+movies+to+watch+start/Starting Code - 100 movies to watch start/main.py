import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

resposta = requests.get(url=URL).text

soup = BeautifulSoup(resposta, "html.parser")

titulos = [t.get_text() for t in soup.find_all(name="h3",class_="title")]
for t in reversed(titulos):
    print(t)



