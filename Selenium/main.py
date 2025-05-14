from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opcoes_chrome = webdriver.ChromeOptions()
opcoes_chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opcoes_chrome)
driver.get("https://www.amazon.com.br/animal-social-Elliot-Aronson/dp/8576576007")

preco_real = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'a-price-whole'))
)
preco_inteiro =preco_real.text

print(preco_inteiro)
