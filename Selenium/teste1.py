from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=opcoes_chrome)
navegador.get("https://www.amazon.com.br/animal-social-Elliot-Aronson/dp/8576576007")

preco_inteiro = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
)
preco_decimal = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))
)

# Agora imprime corretamente
print(preco_inteiro.text + "," + preco_decimal.text)