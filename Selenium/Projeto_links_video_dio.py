from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class CapturarLinksVideo():
    def __init__(self):
        self.opcoes = Options()
        self.opcoes.add_argument("--disable-gpu")
        self.opcoes.add_argument("--no-sandbox")
        self.opcoes.add_experimental_option("detach", True)
        self.opcoes.binary_location = "/usr/bin/google-chrome"
        self.navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.opcoes)
        self.navegador.get("https://web.dio.me/track/wex-end-end-engineering/course/introducao-ao-net/learning/9f414c11-f7a9-48d3-beb5-48f970c883e8?autoplay=1")
        time.sleep(5)

    def logar_dio(self, email, senha):
        self.navegador.find_element(By.NAME, "username").send_keys(email)
        self.navegador.find_element(By.NAME, "password").send_keys(senha)
        self.navegador.find_element(By.NAME, "login").click()
        time.sleep(5)



    def capturar_links(self):    
        iframes = self.navegador.find_elements(By.TAG_NAME, "iframe")

        # Coletar todos os links do YouTube
        links_youtube = []
        for i in iframes:
            src = i.get_attribute("src")
            if src and "youtube.com" in src:
                links_youtube.append(src)

        # Abrir os links em nova aba e fechar após análise
        for link in links_youtube:
            print("🎬 Link encontrado:", link)
            self.navegador.execute_script(f"window.open('{link}', '_blank');")
            time.sleep(5)  # tempo para carregar
            self.navegador.switch_to.window(self.navegador.window_handles[-1])
            # Aqui você pode interagir com a aba se quiser
            self.navegador.close()
            self.navegador.switch_to.window(self.navegador.window_handles[0])


if __name__ == "__main__":
    capturar = CapturarLinksVideo()
    capturar.logar_dio("ronaldkurouzo@gmail.com", "Hidan1994@#")  # Substitua pelos seus dados
    capturar.capturar_links()                