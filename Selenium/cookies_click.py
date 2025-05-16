import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

# Cria o navegador disfarçado (bypass Cloudflare)
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("--disable-blink-features=AutomationControlled")

# Inicializa o navegador com undetected_chromedriver
driver = uc.Chrome(options=options)

# Acessa o Cookie Clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Aguarda o carregamento inicial
time.sleep(10)  # espere o idioma aparecer (pode ajustar se o PC for lento)

# Tenta clicar no botão de idioma PT-BR
try:
    idioma = driver.find_element(By.ID, "langSelect-PT-BR")
    idioma.click()
    print("✅ Idioma selecionado: Português.")
except Exception as e:
    print("⚠️ Não foi possível selecionar o idioma. Continuando...")

# Aguarda o carregamento do jogo principal
time.sleep(15)

# Encontra o cookie gigante
cookie = driver.find_element(By.ID, "bigCookie")

# Loop de cliques infinitos
print("🍪 Começando os cliques no cookie...")
while True:
    cookie.click()
    

