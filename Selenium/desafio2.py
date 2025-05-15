from selenium import webdriver
from selenium.webdriver.common.by import By


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=opcoes_chrome)
navegador.get("https://en.wikipedia.org/wiki/Main_Page")

numero = navegador.find_element(By.XPATH, "//*[@id='articlecount']/ul/li[2]/a[1]")
numero.click()