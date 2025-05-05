from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Caminho onde os arquivos serão baixados
download_path = os.path.abspath("RanmaDownloads")
os.makedirs(download_path, exist_ok=True)

# Configurações do navegador
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("prefs", {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
driver.get("https://ranmatanma.blogspot.com/p/manga.html")
time.sleep(5)

# Pega todos os links com 'mediafire' na página
links = driver.find_elements(By.TAG_NAME, "a")
mediafire_links = [link for link in links if "mediafire.com" in link.get_attribute("href")]

print(f"🔗 Encontrados {len(mediafire_links)} links para baixar.")

# Visita cada link, clica no botão de download e volta
for idx, link in enumerate(mediafire_links):
    href = link.get_attribute("href")
    print(f"\n▶️ Acessando link {idx+1}: {href}")
    
    # Abre nova aba
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(href)
    
    try:
        time.sleep(7)  # Espera a página do MediaFire carregar
        # Clica no botão de download
        download_button = driver.find_element(By.CSS_SELECTOR, 'a[href^="https://download"]')
        download_button.click()
        print("✅ Clique no botão de download realizado.")
        
        time.sleep(10)  # Espera o download iniciar (ajuste se necessário)
    except Exception as e:
        print(f"❌ Erro ao clicar no botão de download: {e}")
    
    # Fecha a aba e volta à anterior
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

print("\n✅ Todos os downloads foram iniciados. Verifique a pasta:", download_path)
driver.quit()
