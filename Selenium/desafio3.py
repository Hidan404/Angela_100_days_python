from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=opcoes_chrome)


navegador.get("https://secure-retreat-92358.herokuapp.com/")

nome = navegador.find_element(By.NAME, "fName")
nome.send_keys("Ronald")
nome.send_keys(Keys.TAB)


sobrenome = navegador.find_element(By.NAME, "lName")
sobrenome.send_keys("Silva")
sobrenome.send_keys(Keys.TAB)


email = navegador.find_element(By.NAME, "email")
email.send_keys("tatakai@gmail.com")
email.send_keys(Keys.TAB)

botao = navegador.find_element(By.XPATH, '/html/body/form/button')
botao.click()

