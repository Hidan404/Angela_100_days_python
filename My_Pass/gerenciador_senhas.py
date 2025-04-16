import flet as ft
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
import asyncio



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

    def salvar_senha_csv(senha, site):
        if senha and site:
            with open("My_Pass/senhas.csv", "a") as f:
                f.write(f"{site}, {senha}\n")

               
    def criptograr_arquivo_csv(e):
        chave = get_random_bytes(16)
        cipher = AES.new(chave, AES.MODE_CBC)
        with open("My_Pass/senhas.csv", "rb") as f:
            dados = f.read()
            dados_criptografados = cipher.encrypt(pad(dados, AES.block_size))
        with open("My_Pass/senhas_criptografadas.bin", "wb") as f:
            f.write(cipher.iv + dados_criptografados)
            os.remove("My_Pass/senhas.csv")
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
        with open("My_Pass/senhas.csv", "wb") as f:
            f.write(dados_descriptografados)
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
            salvar_senha_csv(senha, site)
            campo_senha.value = ""
            campo_site.value = ""
            campo_senha.focus()
            campo_senha.update()
            campo_site.update()

    async def limpar_msg_apos_delay():
        await asyncio.sleep(5)
        msg_texto.value = ""
        page.update()

    botoes1 = ft.Row([
        botao_gerar,
        ft.ElevatedButton(text="Adicionar Senha", on_click=adicionar_senha)
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )    
    layout = ft.Column([
        ft.Text("Gerenciador de Senhas", size=30, weight=ft.FontWeight.BOLD),
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
    page.add(layout)
    page.add(botoes1)
    page.add(botoes2)
    page.update()


ft.app(target=main)        
    