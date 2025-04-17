import flet as ft
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
import asyncio
import json



def main(page: ft.Page):
    page.title = "Gerenciador de Senhas" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    campo_senha = ft.TextField(label= "Senha gerada", width=300)
    campo_site = ft.TextField(label="Digite o nome do site", width=300)


    msg_texto = ft.Text("")

    def gerar_senha():
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        senha = ''.join(random.choice(caracteres) for i in range(15))
        return senha
    
    def adicionar_senha(e):
        senha = gerar_senha()
        campo_senha.value = senha
        campo_site.focus()
        campo_senha.update()
        campo_site.update()

    def salvar_senha_json(senha, site):
        try:
            dados = {}

            # Se o arquivo já existir, carrega os dados
            if os.path.exists("My_Pass/senhas.json"):
                with open("My_Pass/senhas.json", "r") as f:
                    try:
                        dados = json.load(f)
                    except json.JSONDecodeError:
                        dados = {}

            # Adiciona ou atualiza a senha para o site
            dados[site] = senha

            # Salva os dados atualizados
            with open("My_Pass/senhas.json", "w") as f:
                json.dump(dados, f, indent=4)

        except Exception as e:
            print(f"Erro ao salvar senha: {e}")



               
    def criptograr_arquivo_csv(e):
        chave = get_random_bytes(16)
        cipher = AES.new(chave, AES.MODE_CBC)
        with open("My_Pass/senhas.json", "rb") as f:
            dados = f.read()
            dados_criptografados = cipher.encrypt(pad(dados, AES.block_size))
        with open("My_Pass/senhas_criptografadas.bin", "wb") as f:
            f.write(cipher.iv + dados_criptografados)
            os.remove("My_Pass/senhas.json")
        with open("My_Pass/chave.key", "wb") as f:  
            f.write(chave)
        msg_texto.value = "Arquivo criptografado com sucesso!"
        page.add(msg_texto)
        page.update()
        page.run_task(limpar_msg_apos_delay)

    def descriptografar_arquivo_csv(e):
        with open("My_Pass/chave.key", "rb") as f:
            chave = f.read()
        with open("My_Pass/senhas_criptografadas.bin", "rb") as f:
            iv = f.read(16)
            dados_criptografados = f.read()
        cipher = AES.new(chave, AES.MODE_CBC, iv)
        dados_descriptografados = unpad(cipher.decrypt(dados_criptografados), AES.block_size)
        with open("My_Pass/senhas.json", "wb") as f:
            f.write(dados_descriptografados)
        os.remove("My_Pass/senhas_criptografadas.bin")
        os.remove("My_Pass/chave.key")
        msg_texto.value = "Arquivo descriptografado com sucesso!"
        page.add(msg_texto)
        page.update()
        page.run_task(limpar_msg_apos_delay)

    botao_gerar = ft.ElevatedButton(text="Gerar Senha", on_click=adicionar_senha)
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
        if os.path.exists("My_Pass/senhas.json"):
            with open("My_Pass/senhas.json", "r") as f:
                dados = json.load(f)
                for site, senha in dados.items():
                    lista_senhas.controls.append(
                        ft.Text(f"🔒 {site.strip()}: {senha.strip()}", selectable=True)
                    )
    except Exception as e:
        print(f"Erro ao carregar senhas: {e}")


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
    