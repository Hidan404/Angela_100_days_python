from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=opcoes_chrome)


navegador.get("https://creapa.org.br/quero-me-registrar/")
entrada = navegador.find_element(By.NAME, 's')
entrada.send_keys("Python")
entrada.send_keys(Keys.ENTER)