from selenium import webdriver
from selenium.webdriver.common.by import By
import json


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=opcoes_chrome)
navegador.get("https://www.python.org/")

datas = navegador.find_elements(By.CSS_SELECTOR,".event-widget li time")
valores = navegador.find_elements(By.CSS_SELECTOR,".event-widget li a")


eventos = {}
for i in range(len(datas)):
    eventos[i] = {
        "data": datas[i].text,
        "evento": valores[i].text,
        "link": valores[i].get_attribute("href")
    }

with open("Selenium/eventos.json", "w") as arquivo_json:
    json.dump(eventos, arquivo_json, indent=4)
    print("Arquivo JSON criado com sucesso!")      