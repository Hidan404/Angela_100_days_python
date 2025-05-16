from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=opcoes_chrome)


navegador.get("https://orteil.dashnet.org/cookieclicker/")
linguagem = navegador.find_element(By.ID, "langSelect-EN")
if linguagem.is_displayed():
    linguagem.click()
else:
    # Se o botão de linguagem não estiver visível, clique no botão de linguagem
    # que está na tela inicial
    botao_ingles = navegador.find_element(By.ID, "langSelect-EN")
    botao_ingles.click()


botao = navegador.find_element(By.ID, "bigCookie")
botao.click()