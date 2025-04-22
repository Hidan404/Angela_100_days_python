import requests
import flet as ft

def main(page: ft.Page):
    page.title = "Kanye Quotes"
    page.bgcolor = "#1e1e1e"  # Cor de fundo escura
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Texto da citação
    quote_text = ft.Text(
        value="Clique no botão para ver uma frase do Kanye!",
        size=22,
        text_align=ft.TextAlign.CENTER,
        color="white",
        weight=ft.FontWeight.BOLD
    )

    # Imagem de topo
    img = ft.Image(
        src="https://img.freepik.com/fotos-gratis/figura-triangular-geometrica-legal-em-uma-luz-de-laser-neon-otima-para-fundos-e-papeis-de-parede_181624-9331.jpg?t=st=1745330164~exp=1745333764~hmac=c748c8dfc18f41849a268dc204a063848b2a8b96c59f20e7f6d898af1d355c94&w=900",
        width=700,
        height=180,
        fit=ft.ImageFit.COVER,
        border_radius=10
    )

    # Função que faz a requisição da frase
    def requisicao(e):
        try:
            url = "https://api.kanye.rest/"
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                quote_text.value = f'"{dados["quote"]}"'
                page.update()
        except Exception as erro:
            quote_text.value = f"Erro: {erro}"
            page.update()

    # Botão estilizado
    get_quote_button = ft.ElevatedButton(
        text="Nova Frase",
        on_click=requisicao,
        bgcolor="#ffcc00",
        color="black",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.symmetric(horizontal=30, vertical=15)
        )
    )

    # Container principal
    container = ft.Container(
        content=ft.Column(
            [
                img,
                ft.Divider(height=30, color="transparent"),
                quote_text,
                ft.Divider(height=20, color="transparent"),
                get_quote_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25
        ),
        padding=30,
        border_radius=20,
        bgcolor="#2a2a2a",
        shadow=ft.BoxShadow(
            blur_radius=30,
            color=ft.colors.BLACK54,
            offset=ft.Offset(0, 20),
            spread_radius=1
        )
    )

    page.add(container)

ft.app(target=main)
