from bs4 import BeautifulSoup


with open("Day-45/filmes.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    
filmes = soup.find_all("div", class_="filme")
for f in filmes:
    titulo = f.find("div", class_ = "titulo").text
    print(titulo)
    ano = f.find(name="div", class_="ano").text
    print(ano)
    genero = f.find("div", class_="genero").text
    print(genero)



url = soup.select_one("p a")  
print(url.attrs)  