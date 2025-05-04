from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configurar o Selenium (modo headless)
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# URL com os links
URL = "https://ranmatanma.blogspot.com/p/manga.html"

# Acessar a página
driver.get(URL)
time.sleep(5)  # Espera o JS carregar (ajuste se necessário)

# Capturar o HTML renderizado
html = driver.page_source
driver.quit()

# Fazer parsing com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
links = []

for a in soup.find_all('a', href=True):
    href = a['href']
    if "mediafire.com/download" in href:
        links.append(href)

# Remover duplicados (se houver)
links = list(set(links))

# Mostrar todos os links
print(f"\n🔗 {len(links)} links encontrados:")
for link in links:
    print(link)
