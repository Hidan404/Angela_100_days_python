from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=opcoes_chrome)
navegador.get("https://www.amazon.com.br/animal-social-Elliot-Aronson/dp/8576576007")

preco = navegador.find_element(By.CSS_SELECTOR,".a-price-whole")
preco_inteiro = navegador.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')

print(preco_inteiro.text)