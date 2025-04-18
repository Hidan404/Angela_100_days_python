import flet as ft

def main(page: ft.Page):
    page.title = "FlashCard"
   

    palavras_pt = ["cachorro", "gato", "pássaro", "peixe", "cavalo"]
    palavras_en = ["dog", "cat", "bird", "fish", "horse"]

    indice = 0
    mostrar_traducao = False

    texto_card = ft.Text(value=palavras_pt[indice], size=30, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK, selectable=True)

    def atualizar_card():
        if mostrar_traducao:
            texto_card.value = palavras_en[indice]
        else:
            texto_card.value = palavras_pt[indice]
        texto_card.update()

    def proximo_card(e):
        nonlocal indice
        indice = (indice + 1) % len(palavras_pt)
        atualizar_card()

    def mostrar_traducao_card(e):
        nonlocal mostrar_traducao
        mostrar_traducao = not mostrar_traducao
        atualizar_card()    


    containercard = ft.Container(
            content=texto_card,
            alignment=ft.alignment.center,
            padding=30,
            bgcolor=ft.colors.WHITE,
            border_radius=15,
            width=300,
            height=200,
            border=ft.border.all(1, ft.colors.GREY_300),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.GREY_400,
                offset=ft.Offset(2, 2),
                blur_style=ft.ShadowBlurStyle.NORMAL
            )
    )

    page.add(
        ft.Column(
            [
                containercard,
                ft.Row(
                    [
                        ft.IconButton(ft.icons.ARROW_BACK, on_click=proximo_card),
                        ft.IconButton(ft.icons.ARROW_FORWARD, on_click=proximo_card)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.IconButton(ft.icons.INFO, on_click=mostrar_traducao_card),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )



ft.app(target=main)