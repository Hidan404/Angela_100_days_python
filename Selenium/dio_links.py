from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do navegador
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"  # Altere se estiver diferente
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://web.dio.me/track/wex-end-end-engineering/course/introducao-a-experiencia-wex-integrated-engineer/learning/2ad6a9b2-0896-4b0e-a146-01a8e4fc18b8"
driver.get(url)
time.sleep(10)

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    href = link.get_attribute("href")
    if href and ("youtube.com" in href or "youtu.be" in href):
        print(href)

driver.quit()
