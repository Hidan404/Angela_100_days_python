import flet as ft
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
import asyncio
import json
import sys

# Função que retorna o caminho absoluto do executável ou do script .py
def obter_caminho_absoluto():
    if getattr(sys, 'frozen', False):  # Se for um executável
        return os.path.dirname(sys.executable)
    else:  # Se estiver rodando o script .py direto
        return os.path.dirname(os.path.abspath(__file__))

# Diretório onde os arquivos serão armazenados
PASTA_SENHAS = os.path.join(obter_caminho_absoluto(), "My_Pass")

# Cria a pasta se não existir
os.makedirs(PASTA_SENHAS, exist_ok=True)

# Caminhos completos para os arquivos usados no app
CAMINHO_JSON = os.path.join(PASTA_SENHAS, "senhas.json")
CAMINHO_BIN = os.path.join(PASTA_SENHAS, "senhas_criptografadas.bin")
CAMINHO_KEY = os.path.join(PASTA_SENHAS, "chave.key")


def main(page: ft.Page):
    page.title = "Gerenciador de Senhas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    campo_senha = ft.TextField(label="Senha gerada", width=300)
    campo_site = ft.TextField(label="Digite o nome do site", width=300)
    msg_texto = ft.Text("")

    def gerar_senha():
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        senha = ''.join(random.choice(caracteres) for i in range(15))
        return senha

    def salvar_senha_json(senha, site):
        try:
            senha_site = {
                "senha": senha,
                "site": site
            }

            # Verifica se o arquivo já existe e carrega o conteúdo
            if os.path.exists(CAMINHO_JSON):
                with open(CAMINHO_JSON, "r") as f:
                    dados = json.load(f)
                if not isinstance(dados, list):
                    dados = [dados]
            else:
                dados = []

            dados.append(senha_site)

            with open(CAMINHO_JSON, "w") as f:
                json.dump(dados, f, indent=4)
        except Exception as e:
            print(f"Erro ao salvar senha: {e}")

    def criptograr_arquivo_csv(e):
        chave = get_random_bytes(16)
        cipher = AES.new(chave, AES.MODE_CBC)
        with open(CAMINHO_JSON, "rb") as f:
            dados = f.read()
            dados_criptografados = cipher.encrypt(pad(dados, AES.block_size))
        with open(CAMINHO_BIN, "wb") as f:
            f.write(cipher.iv + dados_criptografados)
            os.remove(CAMINHO_JSON)
        with open(CAMINHO_KEY, "wb") as f:
            f.write(chave)
        msg_texto.value = "Arquivo criptografado com sucesso!"
        page.add(msg_texto)
        page.update()
        page.run_task(limpar_msg_apos_delay)

    def descriptografar_arquivo_csv(e):
        with open(CAMINHO_KEY, "rb") as f:
            chave = f.read()
        with open(CAMINHO_BIN, "rb") as f:
            iv = f.read(16)
            dados_criptografados = f.read()
        cipher = AES.new(chave, AES.MODE_CBC, iv)
        dados_descriptografados = unpad(cipher.decrypt(dados_criptografados), AES.block_size)
        with open(CAMINHO_JSON, "wb") as f:
            f.write(dados_descriptografados)
        os.remove(CAMINHO_BIN)
        os.remove(CAMINHO_KEY)
        msg_texto.value = "Arquivo descriptografado com sucesso!"
        page.add(msg_texto)
        page.update()
        page.run_task(limpar_msg_apos_delay)

    botao_gerar = ft.ElevatedButton(text="Gerar Senha", on_click=lambda e: (
        campo_senha.__setattr__('value', gerar_senha()),
        campo_site.focus(),
        campo_senha.update(),
        campo_site.update()
    ))

    botao_descriptografar = ft.ElevatedButton(text="Descriptografar Senhas", on_click=descriptografar_arquivo_csv)

    def adicionar_senha(e):
        senha = campo_senha.value
        site = campo_site.value

        if senha and site:
            page.add(ft.Text(f"Senha para {site}:" + f"\t Senha: {senha}"))
            salvar_senha_json(senha, site)
            lista_senhas.controls.append(ft.Text(f"Senha para {site}:" + f"\t Senha: {senha}"))
            lista_senhas.update()
            campo_senha.value = ""
            campo_site.value = ""
            campo_senha.focus()
            campo_senha.update()
            campo_site.update()

    async def limpar_msg_apos_delay():
        await asyncio.sleep(5)
        msg_texto.value = ""
        page.update()

    lista_senhas = ft.Column(
        spacing=5,
        scroll="auto",
        width=400,
        height=200,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    try:
        if os.path.exists(CAMINHO_JSON):
            with open(CAMINHO_JSON, "r") as f:
                dados = json.load(f)
                if isinstance(dados, dict):
                    dados = [dados]
                for item in dados:
                    site = item.get("site")
                    senha = item.get("senha")
                    lista_senhas.controls.append(
                        ft.Text(f"🔒 {site}: {senha}", selectable=True)
                    )
    except Exception as e:
        print(f"Arquivo não encontrado ou inválido. Erro: {e}")

    subtitulo = ft.ListView(
        controls=[
            ft.Text("Gerenciador de Senhas", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.RED_900),
        ],
        width=400,
        height=100,
        spacing=10,
        padding=10,
        auto_scroll=False
    )

    botoes1 = ft.Row([
        botao_gerar,
        ft.ElevatedButton(text="Adicionar Senha", on_click=adicionar_senha)
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    layout = ft.Column([
        campo_site,
        campo_senha,
    ])

    botoes2 = ft.Row([
        ft.ElevatedButton(text="Salvar Senhas", on_click=criptograr_arquivo_csv),
        botao_descriptografar
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    page.add(subtitulo)
    page.add(ft.Container(height=10))
    page.add(layout)
    page.add(ft.Container(height=20))
    page.add(botoes1)
    page.add(ft.Container(height=20))
    page.add(botoes2)
    page.add(lista_senhas)
    page.update()


ft.app(target=main)
