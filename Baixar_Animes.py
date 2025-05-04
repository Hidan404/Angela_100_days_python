import requests
from tqdm import tqdm

# URL do arquivo
url = "https://darkmahou.mimas.usbx.me/filebrowser/api/public/dl/mCDQ4ibq/"

# Nome do arquivo de saída
output_file = "arquivo_baixado.zip"

# Fazendo o download com barra de progresso
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Erro se a resposta não for OK

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(output_file, 'wb') as f, tqdm(
        desc=output_file,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=block_size):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))

    print(f"\nDownload concluído com sucesso: {output_file}")

except requests.exceptions.RequestException as e:
    print(f"Erro no download: {e}")
