import flet as ft
import time


def main(page: ft.Page):
    page.title = "Flet Controls"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def botao_clicado(e):
        page.add(ft.Text("Botão clicado!"))
        page.update()


    botao = ft.ElevatedButton(text="Clique kkk", on_click=botao_clicado)

    page.add(botao)    


ft.app(target=main)
