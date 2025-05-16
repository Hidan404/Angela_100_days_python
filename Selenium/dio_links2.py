from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do Chrome Headless
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"  # ajuste conforme necessário
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL do curso
url = "https://web.dio.me/track/wex-end-end-engineering/course/introducao-a-experiencia-wex-integrated-engineer/learning/2ad6a9b2-0896-4b0e-a146-01a8e4fc18b8"
driver.get(url)
time.sleep(10)

# Procurar por <iframe> com vídeos do YouTube
iframes = driver.find_elements(By.TAG_NAME, "iframe")

print("🎬 Links de vídeo encontrados:")
for iframe in iframes:
    src = iframe.get_attribute("src")
    if src and ("youtube.com" in src or "youtu.be" in src):
        print(src)

driver.quit()
