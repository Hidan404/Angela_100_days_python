from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class DioVideoScraper:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.opcoes = Options()
        self.opcoes.add_argument("--headless")
        self.opcoes.add_argument("--disable-gpu")
        self.opcoes.add_argument("--no-sandbox")
        self.opcoes.add_experimental_option("detach", True)
        self.opcoes.binary_location = "/usr/bin/google-chrome"  # ajuste se necessário
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.opcoes)

    def login(self):
        self.driver.get("https://web.dio.me/track/wex-end-end-engineering")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys(self.email)
        self.driver.find_element(By.NAME, "password").send_keys(self.senha)
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Entrar")]').click()
        time.sleep(5)

    def coletar_links_aulas(self, trilha_url):
        self.driver.get(trilha_url)
        time.sleep(5)

        print("🔍 Coletando links das aulas...")
        elementos = self.driver.find_elements(By.TAG_NAME, "a")
        links_aulas = []

        for el in elementos:
            href = el.get_attribute("href")
            if href and "/learning/" in href and href not in links_aulas:
                links_aulas.append(href)

        print(f"✅ Encontrado {len(links_aulas)} aulas.")
        return links_aulas

    def extrair_videos_youtube(self, links_aulas):
        print("\n🎬 Buscando vídeos nas aulas...")
        youtube_links = []

        for idx, aula_url in enumerate(links_aulas, start=1):
            print(f"[{idx}/{len(links_aulas)}] Acessando: {aula_url}")
            self.driver.get(aula_url)
            time.sleep(5)

            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                src = iframe.get_attribute("src")
                if src and "youtube.com" in src and src not in youtube_links:
                    print("   🎯 Vídeo encontrado:", src)
                    youtube_links.append(src)
                    break  # Assume que há um vídeo por aula

        return youtube_links

    def salvar_links(self, links, arquivo="videos_dio.txt"):
        with open(arquivo, "w") as f:
            for link in links:
                f.write(link + "\n")
        print(f"\n✅ Todos os vídeos foram salvos em: {arquivo}")

    def fechar(self):
        self.driver.quit()


if __name__ == "__main__":
    EMAIL = "ronaldkurouzo@gmail.com"
    SENHA = "Hidan1994@#"  # ⚠️ Cuidado com senha hardcoded — ideal usar secrets/env
    URL_TRILHA = "https://web.dio.me/track/wex-end-end-engineering"

    dio = DioVideoScraper(EMAIL, SENHA)
    dio.login()
    aulas = dio.coletar_links_aulas(URL_TRILHA)
    videos = dio.extrair_videos_youtube(aulas)
    dio.salvar_links(videos)
    dio.fechar()
