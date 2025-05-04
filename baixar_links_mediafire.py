import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

# Substitua com a URL real da página HTML que contém os 38 links
URL_PAGINA = "https://ranmatanma.blogspot.com/p/manga.html"

# Criar pasta de destino
DESTINO = "downloads"
os.makedirs(DESTINO, exist_ok=True)

# Função para extrair todos os links MediaFire da página
def extrair_links_mediafire(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if "mediafire.com/download/" in href:
            links.append(href)
    return links

# Função para baixar um arquivo com barra de progresso
def baixar_arquivo(url, destino):
    nome_arquivo = os.path.basename(url)
    caminho = os.path.join(destino, nome_arquivo)

    resposta = requests.get(url, stream=True)
    total = int(resposta.headers.get('content-length', 0))

    with open(caminho, 'wb') as arquivo, tqdm(
        desc=nome_arquivo,
        total=total,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as barra:
        for parte in resposta.iter_content(chunk_size=1024):
            if parte:
                arquivo.write(parte)
                barra.update(len(parte))

# Execução principal
def main():
    print("🔍 Buscando links MediaFire...")
    links = extrair_links_mediafire(URL_PAGINA)
    print(f"✅ {len(links)} links encontrados.")

    for i, link in enumerate(links, 1):
        print(f"\n⬇️ ({i}/{len(links)}) Baixando: {link}")
        try:
            baixar_arquivo(link, DESTINO)
        except Exception as e:
            print(f"❌ Erro ao baixar {link}: {e}")

    print("\n✅ Todos os downloads foram concluídos.")

if __name__ == "__main__":
    main()
