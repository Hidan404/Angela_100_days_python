from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opcoes_chrome)
driver.get("https://www.amazon.com.br/animal-social-Elliot-Aronson/dp/8576576007")

preco_real = driver.find_element(By.CSS_SELECTOR,"span.a-price.aok-align-center span.a-offscreen")
# Espera até que o elemento esteja presente
print(preco_real.text)


print(preco_real.text)
