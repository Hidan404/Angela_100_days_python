from bs4 import BeautifulSoup


with open("Day-45/filmes.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    
filmes = soup.find_all("body", class_="filme")
for f in filmes:
    